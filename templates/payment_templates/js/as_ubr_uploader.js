var upload_max_filesize = 1024 * 1024 * 500;
var bytes_total = 0;
var intervalRefresh = 1000;
var uplrun = 0;

jQuery(function(){
	//console.debug('--- START --');
	jQuery("#ifr2").hide();
	jQuery("#uploadbtn").click(function(){
		jQuery("#uploadbtn").attr('disabled', true);
		jQuery("#fupload").submit();
	});
	jQuery("#fupload").submit(function(){
		//console.debug('--- requestInfo --');
		uplrun=1;
		requestInfo();
		checkIframe();
		//jQuery("#fupload,#upl_elements").hide();
		jQuery("#fuploadstop, #upl_elements").show();
	});
	jQuery("#fuploadstop input[type='button']").click(function(){
		stopUpload(1);
	});
	jQuery("#resetbtn").click(function(){
		jQuery("#fupload").find("input").val('');
		stopUpload(1);
	});
});

function requestInfo(){
	//console.debug('--- requestInfo --');
	jQuery.ajax({
		url:"/uploadprogress/info.php?ID="+ id + "&" + new Date(),
		success: function(data){

			if(data != "null" && data != null && data.length > 2  && uplrun == 1){
				data = eval('(' + data + ')');
				data.bytes_total = parseInt(data.bytes_total);
				upload_max_filesize = parseInt(upload_max_filesize);
				if(data.error == 1 && data.error_msg.length > 0){
					setError(data.error_msg);
					stopUpload(0);
				}else if(data.bytes_total > upload_max_filesize){
					setError("The file is too large. More then "+ (upload_max_filesize/1024/1024).toFixed() +" MBytes");
					stopUpload(0);
				}
				bytes_total = data.bytes_total;
				setPosition(data);
				jQuery("#fupload").find("input[type='file']").attr('disabled', true);
			}
			//console.debug(data);
		},
		error: function(jqXHR, textStatus, errorThrown){
			//console.debug("--------- error ---------");
			//console.debug(textStatus);
			//console.debug(jqXHR);
		}
	});
	if(uplrun == 1){
		setTimeout("requestInfo()",intervalRefresh);
	}
}

function stopUpload(reloaddoc){
	uplrun=0;
	jQuery("#fupload").show();
	jQuery("#fuploadstop").hide();
	jQuery("#progressbar").progressbar({value:0}).hide();
	jQuery("#upl_elements").hide().find("span").html('');
	jQuery("#fupload").find("input[type='file']").val('').attr('disabled', false);
	jQuery("#uploadbtn").attr('disabled', false);
	if(reloaddoc){
		//document.location.reload();
		document.location = document.location.toString();
	}
}

function setPosition(data){
	$("#progressbar").progressbar({
		value: (data.bytes_uploaded / data.bytes_total + 0.01) * 100
	});
	if(typeof(data.speed_average) != 'undefined' && data.speed_average > 0){
		jQuery("#upl_est_speed").html(Math.floor(data.speed_average/1024) + ' KB/s.');
	}
	if(typeof(data.est_sec) != 'undefined' ){
		jQuery("#upl_est_time_left").html(timePreFormat(data.est_sec));
	}
	if(typeof(data.bytes_uploaded) != 'undefined' && data.bytes_uploaded > 1){
		jQuery("#upl_percent_complete").html( Math.round(data.bytes_uploaded/data.bytes_total*100) + '%');
		jQuery("#upl_current_position").html(Math.floor(data.bytes_uploaded/1024) +' / '+ Math.floor(data.bytes_total/1024) + ' KBytes');
	}
	if(typeof(data.time_last) != 'undefined'){
		jQuery("#upl_elapsed_time").html( timePreFormat(data.time_last - data.time_start));
	}
}

function timePreFormat(date){
	h = Math.floor(date/3600);
	m = Math.floor((date - h * 3600) / 60);
	s = Math.floor(date - h * 3600 - m * 60);
	if(h < 1){h="00";}
	else if(h < 10){h="0"+h;}
	if(m < 1){m="00";}
	else if(m < 10){m="0"+m;}
	if(s < 1){s="00";}
	else if(s < 10){s="0"+s;}
	return h+":"+m+":"+s;
}

function checkIframe(){
	contresult = jQuery("#ifr2").contents().find('body').html();
	if(contresult.length > 1){
		uplrun=0;
		setPosition({"speed_average":0,"est_sec":0,"bytes_uploaded":bytes_total,"bytes_total":bytes_total});
		result = eval('(' + contresult + ')');
		if(result.result == 1){
			jQuery("#savefupload").find("input[name='fileuploaded']").val(result.newfilename[0]);
			jQuery("#savefupload").submit();
		}
	}else if(uplrun==1){
		setTimeout("checkIframe()",intervalRefresh);
	}
}

function setError(text){
	jQuery("#errormessage").html(jQuery("#errormessage").html() + text+"<br/>");
}



