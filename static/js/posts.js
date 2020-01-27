class UserPosts {
	addPost(newPost){
		const postList = document.querySelector("#postList");
		let dj = djangoData();
		postList.innerHTML = `
			<div class="col-md-6 col-md-offset-2 col-sm-12 postsStyle">
				<div class="comment-wrapper">
					<div class="panel panel-info">
						<div class="panel-heading">
							<a href="${dj.profilLink}">@You</a><br><p class="ml-2">${newPost.title}</p>
							<p class="ml-2">Kategoriya: ${newPost.category}</p>
							<p class="ml-3 postSubcategory">Subkategoriyaları: ${newPost.subcat.toString()}</p>
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
						</div>
						<br>
						<div class="panel-footer">
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
		const href = document.querySelector('.profil-link').href;
		let comm_retun = `<li class="media">
				<a href="#" class="pull-left" style="float:left">
					<img src="media/user_1.jpg" alt="" class="img-circle">
				</a>
				<div class="media-body">
					<span class="text-muted pull-right mr-3" style="float:right">
						<small class="text-muted">now</small>
					</span>
					<strong class="text-success" ml-2><a href="${href}">@You<a></strong>
					<p class="ml-3">
						${data.comment_content}
					</p>
				</div>
			</li>`;
		return comm_retun;
	}
}