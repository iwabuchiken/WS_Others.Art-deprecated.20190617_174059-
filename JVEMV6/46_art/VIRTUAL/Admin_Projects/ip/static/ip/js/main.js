//alert("main.js");

function show_Message(msg) {
	
	alert(msg);
	
}//function show_Message(msg) {

function im_Action(_param) {
	
	alert("!!param is => '" + _param + "'");
	
	/*
	 * test
	 */
	$('div#index_Message_Area').html(_param);
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/im/im_actions";
//	var _url = "http://127.0.0.1:8000/im/actions";
	
	var _data = {action : _param};
		
	$.ajax({
		
	    url: _url,
	    type: "GET",
	    //REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
	    data: _data,
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {
		
		alert(data);
		
		$('div#index_Area__Result').html(data);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});

}//function im_Action(param) {
