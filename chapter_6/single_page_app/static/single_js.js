function page_click(page_no){
	let req = new XMLHttpRequest();
	let address = location.protocol + '//' + location.host + `/page/${page_no}`;
	req.open('GET', address);
	req.onload = () => { 
		let response_text = req.responseText;
		console.log(response_text);	
                let page_id = `#page${page_no}_content`;
		console.log('page_id ' + page_id);
		let elem = document.querySelector(page_id);
		elem.innerHTML = response_text;
	};
	req.send();
	
}

function onContentLoaded(){
	document.querySelector('#page1_href').onclick = () => {
		page_click(1);
		return false;
	};
	document.querySelector('#page2_href').onclick = () => {
		page_click(2);
		return false;
	};
}

		
document.addEventListener('DOMContentLoaded', onContentLoaded);

