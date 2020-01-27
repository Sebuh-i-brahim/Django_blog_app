from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from .forms import PostsForm, CommentsForm

from .models import Posts, Comments, Categorie, SubCategory

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
	Categories = Categorie.objects.all()
	return render(request, 'index.html', {
		'postForm' : postForm,
		'commentForm': commentForm,
		'allPosts' : allPosts,
		'Categories' : Categories,
	})
@login_required(login_url="login")
def js_request(request):
	if request.is_ajax():
		if request.method == 'POST':
			data = json.loads(request.body)
			print(data)
			form = PostsForm(data)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				content = form.cleaned_data.get('content')
				category = Categorie.objects.get(id=data.get('category'))
				sublist = []
				for id in data.get('sub_category'):
					sublist.append(SubCategory.objects.get(id=id).name)
				p = Posts(title=title,content=content,subcategory=json.dumps(sublist))
				p.owner_id = request.user
				p.category = category
				p.save()	
				return JsonResponse({
					'status' : 'OK',
					'id': p.id,
					'username': request.user.username,
					'category': category.categorie_name,
					'subCat' : sublist,
					})
			return JsonResponse({'status' : 'Error', 'errors': form.errors})
	return JsonResponse({'status' : 'BAD'})

@login_required(login_url="login")	
def js_reqCom(request):
	if request.is_ajax():
		if request.method == 'POST':
			data = json.loads(request.body)
			form = CommentsForm(data)
			if form.is_valid():
				com_content = form.cleaned_data.get('comment_content')
				posts = Posts.objects.get(id=data.get('id'))
				new_com = Comments(comment_content = com_content)
				new_com.post_id = posts
				new_com.author_id = request.user
				new_com.save()
				res_data = {}
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

@login_required(login_url="login")
def profil(request):
	all_posts = request.user.posts.all()
	return render(request, "profil.html", {'posts': all_posts})

@login_required(login_url="login")
def info(request, id = None, username = None):
	user = {}
	if id:
		user = get_object_or_404(User, id = id)
	if username:
		user = get_object_or_404(User, username = username)
	if user:
		all_posts = user.posts.all()
		return render(request, "info.html", {'posts' : all_posts, 'username' : user.username})
	return HttpResponse('Page Not Found', status=404)

@login_required(login_url="login")
def category(request, id):
	cat = get_object_or_404(Categorie, id=id)
	subcat = cat.category.all()
	data = []
	for sub in subcat:
		data.append({'id': sub.id, 'name': sub.name}) 
	return JsonResponse({'status': 'OK', 'data' : data})

@login_required(login_url="login")
def refresh(request):
	allPosts = Posts.objects.all()
	data = []
	url = ''
	urlText = ''
	for post in allPosts:
		if request.user.id == post.owner_id.id:
			url = 'profil/'
			urlText = '@You'
		else:
			url = 'info/'+str(post.owner_id.id)+'/'
			urlText = '@'+post.owner_id.username
		title = post.title
		post_date = post.created_date.isoformat()
		post_category = post.category.categorie_name
		post_subcat = post.subcategory
		content = post.content
		comments = []
		for comment in post.comments.all():
			com_url = ''
			com_urlText = ''
			if comment.author_id.id == request.user.id:
				com_url = 'profil/'
				com_urlText = '@You'
			else:
				com_url = 'info/' + str(comment.author_id.id) + '/'
				com_urlText = '@' + comment.author_id.username
			com_date = comment.comment_date.isoformat()
			com_content = comment.comment_content
			comments.append({
				'url' : com_url,
				'urlText': com_urlText,
				'date': com_date,
				'content' : com_content, 
				})
		data.append({
			'url': url,
			'urlText': urlText,
			'title' : title,
			'date' : post_date,
			'category' : post_category,
			'subcat' : post_subcat,
			'content' : content,
			'comments' : comments,
			'id' : post.id,
			})
	return JsonResponse({'status': 'OK', 'data' : data})