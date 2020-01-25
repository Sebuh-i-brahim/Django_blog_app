const share = document.querySelector('#share');

const title = document.querySelector('#title');

const content = document.querySelector('#content');

share.onclick = () => {
	postData('createPost/', {
		'title' : title,
		'content' : content
	}).then((data)=>{
		console.log(data);
	})
};

async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST', 
    mode: 'cors', 
    cache: 'no-cache', 
    credentials: 'same-origin', 
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', 
    referrerPolicy: 'no-referrer', 
    body: JSON.stringify(data)
  });
  return await response.json();
}
