const share = document.querySelector('#share');

const title = document.querySelector('#title');

const content = document.querySelector('#content');

const csrftoken = getCookie('csrftoken');

const postList = document.querySelector('#postList');

share.onclick = () => {
	titul = title.value;
	cont = content.value;
	postData('createPost/', {
		title: title.value,
		content: content.value,
	}, new Headers({
      'X-Requested-With' : 'XMLHttpRequest',
      'X-CSRFToken' : csrftoken,
      "Accept": "application/json",
      'Content-Type': 'application/json;charset=utf-8',
    })).then((data)=>{
		console.log(data);
		switch (data.status) {
			case "OK":
				const newPost = new UserPosts();
				newPost.addPost({
					title: title.value,
					content: content.value,
					id: data.id,
					username : data.username
				});
				break;
			case "Error":
				alert(data.form.errors.title + "\n" + data.form.errors.content);
			case "BAD":
				alert("You don't have any permission to do that!");
			default:
				// statements_def
				break;
		}
	})
};

postList.onclick = (e)=>{
	if (e.target.classList == "btn btn-info pull-right btn-sm addbtn") {
		let com_content = e.target.parentElement.querySelector(".CommentForm").value;
		console.log(com_content);
		console.log(e.target.value);
		postData('createComment/',{
			comment_content: com_content,
			id: e.target.value,
		}, new Headers({
	      'X-Requested-With' : 'XMLHttpRequest',
	      'X-CSRFToken' : csrftoken,
	      "Accept": "application/json",
	      'Content-Type': 'application/json;charset=utf-8',
	    })).then((data)=>{
				console.log(data);
				switch (data.status) {
					case "OK":
						const newContent = new UserPosts();
						newContent.addComment({
							element: e.target.parentElement.parentElement.querySelector(".media-list"),
							comment_content : com_content,
							username : data.req_data.username,
							date : data.req_data.date,
						});
						break;
					case "Error":
						alert(data.errormsg);
					case "BAD":
						alert("You don't have any permission to do that!");
					default:
						// statements_def
						break;
			}
		});
	}
	// console.log(e.target.tagName);
	if (e.target.tagName == 'A') {
		window.location.href = e.target.href;
	}
	e.preventDefault();
}