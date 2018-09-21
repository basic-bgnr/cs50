document.addEventListener('DOMContentLoaded', () => {
	alert('content loaded');
        document.querySelector('#item_form').onsubmit= onSubmitListener;
}
);


function onSubmitListener(){
	const li = document.createElement('li');
	li.innerHTML = document.querySelector('#item_name').value;
	document.querySelector('#item_list').append(li);
	return false;
}




