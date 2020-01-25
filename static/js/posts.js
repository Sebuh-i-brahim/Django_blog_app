class UserPosts {
	addPost(newPost){
		const postList = document.querySelector("#postList");
		let dj = djangoData();
		postList.innerHTML = `
			<div class="col-md-6 col-md-offset-2 col-sm-12 ml-auto mr-auto postsStyle">
				<div class="comment-wrapper">
					<div class="panel panel-info">
						<div class="panel-heading">
							<a href="${dj.profilLink}">@You</a><br><p class="ml-2">${newPost.title}</p>
						</div>
						<div class="panel-body">
							<p class="ml-3">
								${newPost.content}
							</p>
							<br>
							<div class="clearfix"></div>
							<ul class="media-list">	
							</ul>
							<br>
							<div>
								${dj.commentForm}
								<br>
								<button type="button" class="btn btn-info pull-right btn-sm addbtn" style="float:right" value="${newPost.id}">Əlavə et</button>
							</div>
							<br><br>
						</div>
					</div>
				</div>
			</div>
		` + postList.innerHTML;
	}
	addComment(data){
		const href = document.querySelector('.profilLink').href;
		data.element.innerHTML = `
			<li class="media">
				<a href="#" class="pull-left" style="float:left">
					<img src="media/user_1.jpg" alt="" class="img-circle">
				</a>
				<div class="media-body">
					<span class="text-muted pull-right" style="float:right">
						<small class="text-muted">now</small>
					</span>
					<strong class="text-success" ml-2><a href="${href}">@You<a></strong>
					<p class="ml-3">
						${data.comment_content}
					</p>
				</div>
			</li>
		` + data.element.innerHTML;
	}
}