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
