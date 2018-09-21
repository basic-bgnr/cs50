let counter = 0;
function hello(){
	document.querySelector('h1').innerHTML = 'good bye ! world';
	document.querySelector('#greeting').innerHTML = 'fuck off';
	document.querySelector('#counter').innerHTML = counter++;
	if (counter % 10 === 0){
		alert(`counter reached ${counter}`);
		counter = 0;
	}
}

