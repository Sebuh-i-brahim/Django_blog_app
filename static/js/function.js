async function postData(url = '', data = {}, header) {
    let body = JSON.stringify(data)
    let headers = header;
    const response = await fetch(url, { method: 'POST', credentials: 'include', headers, body});
    return await response.json();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function multiSelect(element){
    options = element.querySelectorAll('option');
    data = [];
    options.forEach((item)=>{
        if (item.selected) {
            data.push(item.value);
        }
    });
    return data;
}

async function updateAll(){
    await fetch('refresh/').then((res) => {
        return res.json();
    }).then((resp)=>{   
        const postlist = document.querySelectorAll('.postsStyle');
        if (resp.status === 'OK') {
            let data = setUpdateData(resp.data);
            postlist.forEach((item, index)=>{
                item.querySelector(".panel-heading").innerHTML = data[index].header;
                item.querySelector(".media-list").innerHTML = data[index].comment;
            });
        }
        window.setTimeout(updateAll, 5000);
    });
}

function setUpdateData(data){
    let elem = [];
    
    data.forEach((item)=>{
        let head = `
                <a href="${item.url}">${item.urlText}</a>
                <br> 
                <p class="ml-2">${item.title}
                    <span class="text-muted pull-right mr-3" style="float:right">
                        <small class="text-muted agoDate" >
                            <input type="hidden" value="${timeAgo(new Date(item.date))}">
                        </small>
                    </span>
                <p>
                <p class="ml-2">Kategoriya: ${item.category}</p>
                <p class="ml-3 postSubcategory">
                    Subkategoriyaları: ${ JSON.parse(item.subcat).toString()} 
                </p> `;
        let comments = '';
        item.comments.forEach((com)=>{
            comments += `<li class="media">
                            <a href="#" class="pull-left" style="float:left">
                                <img src="/media/user_1.jpg" alt="" class="img-circle">
                            </a>
                            <div class="media-body">
                                <span class="text-muted pull-right mr-3" style="float:right">
                                    <small class="text-muted agoDate" >
                                        ${timeAgo(new Date(com.date))}
                                    </small>
                                </span>
                                <strong class="text-success ml-2">
                                <a href="${com.url}">${com.urlText}</a> 
                                </strong>
                                <p class="ml-3">
                                    ${com.content}
                                </p>
                            </div>
                        </li>`;
        });
        elem.push({
            header : head,
            comment : comments,
        });
    });
    return elem;
}
