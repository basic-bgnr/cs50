document.addEventListener('DOMContentLoaded', ()=>{
	document.querySelector('#user_input').onsubmit = () => {
		vote = document.getElementbyID('votes').value;
		alert(votes);
		
});


