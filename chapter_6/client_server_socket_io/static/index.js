document.addEventListener('DOMContentLoaded', function(){
	let key = 'vote'
	let buttons = Array.from(document.getElementsByTagName('button'));
	buttons.forEach((button)=> {
		button.addEventListener('click', ()=>{
		       let message =button.dataset.content;	
		       post_message(key, message);
		})
	});
	}
);


function post_message(key, message){
	const request = new XMLHttpRequest();
	request.open('post', '/submit');
	
	const form = new FormData();
	form.append(key, message);
	

	request.send(form);
	request.onload = function(){
		alert(request.responseText);
		window.location.reload();
	}

}

