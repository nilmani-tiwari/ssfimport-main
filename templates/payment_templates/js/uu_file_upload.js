var upload_range = 1;
var total_upload_size;
var get_status_speed;
var get_status_url;
var get_data_loop = true;
var seconds = 0;
var minutes = 0;
var hours = 0;
var info_width = 0;
var info_bytes = 0;
var info_time_width = 400;
var info_time_bytes = 15;
var cedric_hold = true;

// alert(window.location.host);


function checkFileNameFormat(){
	if(check_file_name_format == false){ return false; }

	for(var i = 0; i < upload_range; i++){
  		if(document.form_upload.elements['upfile_' + i].value != ""){
  			var string = document.form_upload.elements['upfile_' + i].value;
			var num_of_last_slash = string.lastIndexOf("\\");

			if(num_of_last_slash < 1){ num_of_last_slash = string.lastIndexOf("/"); }

			var file_name = string.slice(num_of_last_slash + 1, string.length);
			var re = /^[\w][\w\s\.\-',]{1,32}$/i;

			if(!re.test(file_name)){
  				alert("Sorry, uploading files in this format is not allowed. Please ensure your file names follow this format. \n\n1. Entire file cannot exceed 32 characters\n2. Format should be filename.extension or filename\n3. Legal characters are 1-9, a-z, A-Z, '_', '-'\n");
  				return true;
  			}
  		}
  	}
	return false;
}

function checkDisallowFileExtensions(){
	if(check_disallow_extensions == false){ return false; }

  	for(var i = 0; i < upload_range; i++){
  		if(document.form_upload.elements['upfile_' + i].value != ""){
  			if(document.form_upload.elements['upfile_' + i].value.match(disallow_extensions)){
  				var string = document.form_upload.elements['upfile_' + i].value;
				var num_of_last_slash = string.lastIndexOf("\\");

				if(num_of_last_slash < 1){ num_of_last_slash = string.lastIndexOf("/"); }

				var file_name = string.slice(num_of_last_slash + 1, string.length);
				var file_extension = file_name.slice(file_name.indexOf(".")).toLowerCase();

  				alert('Sorry, uploading a file with the extension "' + file_extension + '" is not allowed.');
  				return true;
  			}
  		}
  	}
	return false;
}

function checkAllowFileExtensions(){
	if(check_allow_extensions == false){ return false; }

  	for(var i = 0; i < upload_range; i++){
  		if(document.form_upload.elements['upfile_' + i].value != ""){
  			if(!document.form_upload.elements['upfile_' + i].value.match(allow_extensions)){
  				var string = document.form_upload.elements['upfile_' + i].value;
				var num_of_last_slash = string.lastIndexOf("\\");

				if(num_of_last_slash < 1){ num_of_last_slash = string.lastIndexOf("/"); }

				var file_name = string.slice(num_of_last_slash + 1, string.length);
				var file_extension = file_name.slice(file_name.indexOf(".")).toLowerCase();

  				alert('Sorry, uploading a file with the extension "' + file_extension + '" is not allowed.');
  				return true;
  			}
  		}
  	}
	return false;
}

function checkNullFileCount(){
  	if(check_null_file_count == false){ return false; }

  	var null_file_count = 0;

  	for(var i = 0; i < upload_range; i++){
  		if(document.form_upload.elements['upfile_' + i].value == ""){ null_file_count++; }
  	}

  	if(null_file_count == upload_range){
		alert("Please Choose A File To Upload.");
		return true;
  	}
  	else{ return false; }
}

function checkDuplicateFileCount(){
	if(check_duplicate_file_count == false){ return false; }

	var duplicate_flag = false;
	var file_count = 0;
	var duplicate_msg = "Duplicate Upload Files Detected.\n\n";
	var file_name_array = new Array();

	for(var i = 0; i < upload_range; i++){
		if(document.form_upload.elements['upfile_' + i].value != ""){
  			var string = document.form_upload.elements['upfile_' + i].value;
			var num_of_last_slash = string.lastIndexOf("\\");

			if(num_of_last_slash < 1){ num_of_last_slash = string.lastIndexOf("/"); }

			var file_name = string.slice(num_of_last_slash + 1, string.length);

			file_name_array[i] = file_name;
  		}
  	}

  	var num_files = file_name_array.length;

	for(var i = 0; i < num_files; i++){
		for(var j = 0; j < num_files; j++){
			if(file_name_array[i] == file_name_array[j] && file_name_array[i] != null){ file_count++; }
		}
		if(file_count > 1){
			duplicate_msg += 'Duplicate file "' + file_name_array[i] + '" detected in slot ' + (i + 1) + ".\n";
			duplicate_flag = true;
		}
		file_count = 0;
	}

	if(duplicate_flag){
		alert(duplicate_msg);
		return true;
	}
	else{ return false; }
}

function uploadFiles(){
	if(checkFileNameFormat()){ return false; }
	if(checkDisallowFileExtensions()){ return false; }
	if(checkAllowFileExtensions()){ return false; }
	if(checkNullFileCount()){ return false; }
	if(checkDuplicateFileCount()){ return false; }

	var total_uploads = 0;

	for(var i = 0; i < upload_range; i++){
		if(document.form_upload.elements['upfile_' + i].value != ""){ total_uploads++; }
	}

	document.getElementById('total_uploads').innerHTML = total_uploads;
	document.form_upload.upload_range.value = upload_range;
	document.form_upload.submit();
	document.getElementById('upload_button').disabled = true;


	iniProgressRequest();
	getElapsedTime();

	for(var i = 0; i < upload_range; i++){ document.form_upload.elements['upfile_' + i].disabled = true; }
/*
	setTimeout(iniProgressRequest, 2000);
	setTimeout(getElapsedTime, 2500);

	setTimeout( function() { for(var i = 0; i < upload_range; i++){ document.form_upload.elements['upfile_' + i].disabled = true; }	}, 2750);
*/
}

function resetForm(){ top.location.href = self.location; }

function iniFilePage() {
	try {
		for(var i = 0; i < upload_range; i++){
			document.form_upload.elements['upfile_' + i].disabled = false;
			document.form_upload.elements['upfile_' + i].value = "";
		}

		document.getElementById('progress_info').innerHTML = "";
		document.getElementById('upload_button').disabled = false;
		document.getElementById('progress_bar').style.display = "none";
		document.form_upload.reset();
	} catch (e) {};
}


function stopUpload(){
	try{ window.stop(); }
	catch(e){
		try{ document.execCommand('Stop'); }
		catch(e){}
	}
}

function addUploadSlot(num){
	if(upload_range < max_upload_slots){
		if(num == upload_range){
			var up = document.getElementById('upload_slots');
			var dv = document.createElement("div");

			dv.innerHTML = '<input type="file" name="upfile_' + upload_range + '" size="90" onchange="addUploadSlot('+(upload_range + 1)+')">';
			up.appendChild(dv);
			upload_range++;
			document.form_upload.upload_range.value = upload_range;
		}
	}
}

function smoothCedricStatus(){
	if(info_width < progress_bar_width && !cedric_hold){
		info_width = info_width + 1;
		document.getElementById('upload_status').style.width = info_width + 'px';
	}

	if(get_data_loop){ self.setTimeout("smoothCedricStatus()", info_time_width); }
}

function smoothCedricBytes(){
	if(info_bytes < total_upload_size && !cedric_hold){
		info_bytes = info_bytes + 1;
		document.getElementById('current').innerHTML = info_bytes;
	}

	if(get_data_loop){ self.setTimeout("smoothCedricBytes()", info_time_bytes); }
}

function updateCedricStatus(stats, bytes){
	// var deviant_stat = stats + 20; //Add 5% deviation

	// if(deviant_stat < info_width){ cedric_hold = true; }
	// else{
	// 	cedric_hold = false;
	//	info_width = stats;
	//	info_bytes = bytes;
	// }

	cedric_hold = false;
	info_width = stats;
	info_bytes = bytes;
}

function getProgressStatus(){
	var jsel = document.createElement('SCRIPT');

	jsel.type = 'text/javascript';
	jsel.src = get_status_url + "&rnd_id=" + Math.random();

	document.body.appendChild(jsel);

	if(get_data_loop){ self.setTimeout("getProgressStatus()", get_status_speed); }
}

function getElapsedTime(){
	seconds += 1;

    	if(seconds == 60){
    		seconds = 0;
    		minutes += 1;
    	}

    	if(minutes == 60){
    		minutes = 0;
    		hours += 1;
    	}

    	var hr = "" + ((hours < 10) ? "0" : "") + hours;
    	var min = "" + ((minutes < 10) ? "0" : "") + minutes;
    	var sec = "" + ((seconds < 10) ? "0" : "") + seconds;

    	document.getElementById('time').innerHTML = hr + ":" + min + ":" + sec;

    	if(get_data_loop){ self.setTimeout("getElapsedTime()", 1000); }
}

function createRequestObject(){
	var req = false;

	if(window.XMLHttpRequest){
		req = new XMLHttpRequest();

		if(req.overrideMimeType){ req.overrideMimeType('text/xml'); }
	}
	else if(window.ActiveXObject){
		try{ req = new ActiveXObject("Msxml2.XMLHTTP"); }
		catch(e){
			try{ req = new ActiveXObject("Microsoft.XMLHTTP"); }
			catch(e){}
		}
	}

	if(!req){
		document.getElementById('progress_info').innerHTML = "Error: Your browser does not support AJAX";
		return false;
	}
	else{ return req; }
}

function iniProgressRequest() {
	var req = false;
	req = createRequestObject();

	if(req) {
		document.getElementById('progress_info').innerHTML = "Initializing Progress Bar ...";
		req.open("GET", path_to_ini_status_script + "&rnd_id=" + Math.random(), true);
		req.onreadystatechange = function(){ iniProgressResponse(req); };
		req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		req.send(null);
	}
}

function iniProgressResponse(req){
	if(req.readyState == 4) {
/*
		if(req.status == 200) {
*/
			var xml = req.responseXML;

/*
			if(xml.getElementsByTagName('error_status').item(0).firstChild.nodeValue == 1){
				document.getElementById('progress_info').innerHTML = xml.getElementsByTagName('error_msg').item(0).firstChild.nodeValue;

				if(xml.getElementsByTagName('stop_upload').item(0).firstChild.nodeValue == 1){ stopUpload(); }
			}
			else{
*/
				get_status_speed = xml.getElementsByTagName('get_data_speed').item(0).firstChild.nodeValue;
				get_status_url = "http://" + window.location.host + "/uu_get_status.php?temp_dir_sid=" + xml.getElementsByTagName('temp_dir').item(0).firstChild.nodeValue + tmp_sid + "&start_time=" + xml.getElementsByTagName('start_time').item(0).firstChild.nodeValue + "&total_upload_size=" + xml.getElementsByTagName('total_bytes').item(0).firstChild.nodeValue + "&cedric_progress_bar=" + xml.getElementsByTagName('cedric_progress_bar').item(0).firstChild.nodeValue;

				document.getElementById('progress_bar').style.display = "";
				document.getElementById('total_kbytes').innerHTML = Math.round(Number(xml.getElementsByTagName('total_bytes').item(0).firstChild.nodeValue / 1024)) + " ";
        			document.getElementById('progress_info').innerHTML = "Upload In Progress";

				getProgressStatus();

				if(xml.getElementsByTagName('cedric_progress_bar').item(0).firstChild.nodeValue == 1){
					total_upload_size = xml.getElementsByTagName('total_bytes').item(0).firstChild.nodeValue;
	  				smoothCedricBytes();
	  				smoothCedricStatus();
				}
/*
      			}
*/
/*
    		} else {
    			document.getElementById('progress_info').innerHTML = "Error: returned status code " + req.status + " " + req.statusText;
				stopUpload();
    		}
*/
  	}
}
