const share = document.querySelector('#share');

const title = document.querySelector('#title');

const content = document.querySelector('#content');

const csrftoken = getCookie('csrftoken');

const postList = document.querySelector('#postList');

const category = document.querySelector('#category');

const subCategory = document.querySelector('#subCategory')

share.onclick = () => {
	postData('createPost/', {
		title: title.value,
		content: content.value,
		category: category.value,
		sub_category: multiSelect(subCategory),
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
					username : data.username,
					category : data.category,
					subcat : data.subCat,
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
		const el = e.target.parentElement.parentElement.parentElement.querySelector(".media-list");
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
						let html = newContent.addComment({
							comment_content : com_content,
							username : data.req_data.username,
							date : data.req_data.date,
						});
						el.innerHTML = html + el.innerHTML;
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

category.onchange = () => {
	if (isNaN(category.value)) {
		subCategory.innerHTML = `<option selected>İlk öncə kategorianı seçin</option>`;
	}
	else {
		fetch('category/'+ category.value+"/").then((res) => {
			return res.json();
		}).then((resp)=>{
			if (resp.status === 'OK') {
				let inner = '';
				resp.data.forEach((item) =>{
					inner += `<option value="${item.id}">${item.name}</option>`;
				});
				subCategory.innerHTML = inner;
			}	
		});
	}
};