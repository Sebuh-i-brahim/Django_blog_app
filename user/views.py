from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from .forms import PostsForm, CommentsForm

from .models import Posts, Comments

from django.contrib import messages

from django.contrib.auth.models import User

import json

from .tasks import send_email
# Create your views here.

@login_required(login_url = "login")
def home(request):
	postForm = PostsForm()
	commentForm = CommentsForm()
	allPosts = Posts.objects.all()
	for ps in allPosts:
		print(ps.comments.all())
	return render(request, 'index.html', {
		'postForm' : postForm,
		'commentForm': commentForm,
		'allPosts' : allPosts,
	})
@login_required(login_url="login")
def js_request(request):
	if request.is_ajax():
		if request.method == 'POST':
			data = json.loads(request.body)
			form = PostsForm(data)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				content = form.cleaned_data.get('content')
				q = request.user.posts_set.create(
					title = title,
					content = content,
					)	
				return JsonResponse({'status' : 'OK', 'id': q.id, 'username': request.user.username})
			return JsonResponse({'status' : 'Error', 'errors': form.errors})
	return JsonResponse({'status' : 'BAD'})

@login_required(login_url="login")	
def js_reqCom(request):
	if request.is_ajax():
		if request.method == 'POST':
			data = json.loads(request.body)
			print(data)
			form = CommentsForm(data)
			if form.is_valid():
				com_content = form.cleaned_data.get('comment_content')
				posts = Posts.objects.get(id=data.get('id'))
				new_com = Comments(author_id = request.user.id,comment_content = com_content)
				new_com.post_id = posts
				new_com.save()
				if request.user.id != posts.owner_id.id:
					send_email({
						'header' : request.user.username + " Comment to your posts",
						'body' : com_content,
						'sender' : 'my.django.test.project.from.AZ@gmail.com',
						'recivers' : [posts.owner_id.email,],
						})
					res_data = {
						'username' : request.user.username,
						'date' : new_com.update_date,
					}
				return JsonResponse({'status' : 'OK', 'req_data' : res_data})
			return JsonResponse({'status' : 'Error','errormsg' : form.errors.comment_content})
	return JsonResponse({'status' : 'BAD'})