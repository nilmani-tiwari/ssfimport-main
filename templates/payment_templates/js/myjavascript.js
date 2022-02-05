
// !!!!!!! RATING PROCESS

function fxRate(vkey,rate,idToHide,idToShow,vid){
	cp.call('/ajax/myajaxphp.php','process_data',return_data,rate,vid);
//	hideMe(idToHide);
//	showMe(idToShow);
}

function return_data(restul){

	// Collect the number of BLUE star
	var cnt=restul.getElementsByTagName('trate').item(0).firstChild.data;
	// alert(cnt);
    // hideMe('idViewVoteResult');
	if(cnt!='exist')
	{
		/**
		 * var x1=getElementsByClassName('floatmenu', 'div', document.getElementById('voteProcess').parentNode)[0].innerHTML="<FONT COLOR=#7CC1FA>Thanks for rating!</FONT>";
		 * # Show the vote
		 * var x=getElementsByClassName('info', 'span', getElementsByClassName('startratebox2', 'div' , document)[0])[0];
		 * x.innerHTML = x.innerHTML.replace(/[0-9]+/, restul.getElementsByTagName('tvote').item(0).firstChild.data);
		 */
		var x1=getElementsByClassName('floatmenu')[0];
		x1.innerHTML="<FONT COLOR=#7CC1FA>Thanks for rating!</FONT>";
		// # Show the vote
		var x=getElementsByClassName('info', 'span', getElementsByClassName('startratebox2', 'div' , document)[0])[0];
		x.innerHTML = x.innerHTML.replace(/[0-9]+/, restul.getElementsByTagName('tvote').item(0).firstChild.data);


		if(cnt>6)
		{
			cnt=6;
		}
		else if (cnt<0)
		{
			cnt=0;
		}

		blank_star=6-cnt;

		var x=getElementsByClassName('title', 'span', getElementsByClassName('startratebox2', 'div' , document)[0])[0];
        var x2=document.getElementById('voteProcess');
        
		x.innerHTML = '';
		x2.innerHTML = '<span class="title">';
		
		for (i=0;i<cnt;i++ )
		{
			x.innerHTML += '<img width="11" src='+imgurl+'/tpl_icon_star_full.gif>';
			x2.innerHTML += '<img width="11" style="padding: 0px 2px;" src='+imgurl+'/tpl_icon_star_full.gif>';
		}

		for (j=cnt;j<5;j++ )
		{
			x.innerHTML += '<img width="11" src=' + imgurl+'/tpl_icon_star_empty.gif>';
			x2.innerHTML += '<img width="11" style="padding: 0px 2px;" src=' + imgurl+'/tpl_icon_star_empty.gif>';
		}
		x2.innerHTML = x2.innerHTML + '</span>';
	}
	else
	{
		var x=getElementsByClassName('floatmenu', 'div', document.getElementById('voteProcess').parentNode)[0].innerHTML="<FONT COLOR=#FF0000>You already rated this video.</FONT>";
		var x2=document.getElementById('voteProcess');
		// x2.innerHTML = '';
		var x3 = document.getElementById('hidden_current_rate').innerHTML;
		// alert(x3);
		x2.innerHTML = x3;
	}

	return false;
}
// RATING PROCESS END


// !!!!!!! My voting process

function fxVote(voteId)
{
	voteAnswer=document.getElementById('opAns').value;

	if(voteAnswer=='')
	{
		alert('Select any one');
	}
	else
	{
		cp.call(baseurl+'/ajax/myajaxphp.php','process_Vote',return_vote_result,voteId,voteAnswer);
	}
}
function return_vote_result(result)
{
	var xx=result.getElementsByTagName('result').item(0).firstChild.data;
	if (xx=='1'){
		count=result.getElementsByTagName('count').item(0).firstChild.data;
		for (var  ii=0; ii<count  ; ii++ ){

			var vv='A1'+ii;
			var pp='P1'+ii;

			vv=result.getElementsByTagName(vv).item(0).firstChild.data;
			pp=result.getElementsByTagName(pp).item(0).firstChild.data;

			// # Generate Voring table
			var tt=document.getElementById('tblVoteResult').insertRow(0);
			var y=tt.insertCell(0);
			var z=tt.insertCell(1);
			y.innerHTML=vv;
			z.innerHTML=pp +'%';

			if(vv==""){
				break;
			}
		}
		insertInToTable('tblPResult', 0,0,'Vote result');
		// # Hide the previous tale
		hideMe('divviewvresult');
		hideMe('tblVote');

	}
	else if(xx>1)
	{
		insertInToTable('tblPResult', 0,0,'<font color=#FF0000><B>Sorry you already voted..</B></FONT>');
		viewVote(xx);
		// # Hide the previous table
		//showMe('divviewvresult');
		hideMe('tblVote');
	}
}


// END

// VIEW VOTE
function viewVote(pollId)
{
	cp.call(baseurl+'/ajax/myajaxphp.php','view_vote',return_view_vote,pollId);
}
function return_view_vote(result){
	var xx;
	if (1){
		count=result.getElementsByTagName('count').item(0).firstChild.data;
		for (var  ii=0; ii<count  ; ii++ ){

			var vv='A1'+ii;
			var pp='P1'+ii;

			vv=result.getElementsByTagName(vv).item(0).firstChild.data;
			pp=result.getElementsByTagName(pp).item(0).firstChild.data;

			// # Generate Voring table
			var tt=document.getElementById('tblViewVoteResult').insertRow(0);
			var y=tt.insertCell(0);
			var z=tt.insertCell(1);
			y.innerHTML=vv;
			z.innerHTML=pp +'%';

			if(vv==""){
				break;
			}
		}
		insertInToTable('tblViewVote', 0,0,'Current vote status');
	}

}



// !!!!!!!! SEND COMMENT PROCESS

function fxSendComments(idToHide,commentId,uid,vid){
	comment_value=document.getElementById(commentId).value;
	if(uid == '') {
		uid = 0;
	}
	if(comment_value==''){
		alert(' Comment box is empty !!');
	}
	else{
		hideMe(idToHide);
		cp.call(baseurl+'/ajax/myajaxphp.php','process_comments',return_comment_response,comment_value,uid,vid);
	}

}

function return_comment_response(restul){

	if(restul.getElementsByTagName('a').item(0).firstChild.data==0){
		showMe('divComResult2');
	}
	else{
		showMe('divComResult1');
	}
}
// END

// RECENT VIEW PROCESS
var current_position=4;
function recentview(amount,flag){

	gflag="viewrecent";
	if(flag=='next')
	{
		var start=current_position
		current_position=current_position+amount;
		var end=current_position;
		if(dbreport!='1'){

		}

		sql="SELECT VID, title, viewtime, vkey from video where viewtime<>'0000-00-00 00:00:00' order by viewtime desc limit "+start + " , " +end;
		executeDB(sql);
		//alert(sql);
		if(dbreport<0)
		{
			end=current_position;
			current_position=current_position-amount;
			start=current_position;
			alert("End");

		}
	}

	if(flag=='prev')
	{
		var end=current_position;
		current_position=current_position-amount;
		var start=current_position;

		if(start<0){
			start=amount;
			end=start+amount;
			alert("End");
		}

		sql="SELECT VID, title, viewtime, vkey from video where viewtime<>'0000-00-00 00:00:00' order by viewtime desc limit "+start + " , " +end;
		executeDB(sql);
	}
}
//END


function pollAnsBox(myID){
	Me=document.getElementById(myID);
	if(Me.value==""){
		Me.style.background="#3366FF";

	}
	else{

		Me.style.background="#FFFFFF";
		xy=Me.value;
		for (i=0;i<Me.value;i++ ){
			var x=document.getElementById('tblViweAnsBox').insertRow(0);
			var y=x.insertCell(0);
			var z=x.insertCell(1);
			y.innerHTML='Answer ' + (xy-i);
			z.innerHTML='<INPUT TYPE=text SIZE=40 NAME=voteAnsBox'+i+' ID=voteAnsBox'+i+' onBlur=txtBoxValidation(voteAnsBox'+i+', #EAEAEA,#FF0033) >';
		}
	}

}

// ## Delete row of a Tabile
function delteRow(){
	var x=document.getElementById('tblViweAnsBox').rows.length-1;

	for (var i=x;i>=0;i--){
		document.getElementById('tblViweAnsBox').deleteRow(i);
	}
}


function fxvalidation(){
	var flag=true;
	var x=document.getElementById('tblViweAnsBox').rows.length-1;

	// ## Question text
	flag=txtBoxValidation('txtQtn','#EAEAEA','#FF0033');

	// ## Questin qty
	flag=txtBoxValidation('txtPollAnsQty','#EAEAEA','#FF0033');


	for ( i=x; i>=0; i-- )
	{
		targetID='voteAnsBox'+i;
		if (document.getElementById(targetID).value==""){
			txtBoxValidation(targetID,'#EAEAEA','#FF0033');
			flag=false;
			break;
		}


	}

	return flag;
}


function fxShowAccInfo(a,b){
	showMe(a);
	hideMe(b);
}


function pollAnsBox($num){
	alert($num);
}


/*
	Developed by Robert Nyman, http://www.robertnyman.com
	Code/licensing: http://code.google.com/p/getelementsbyclassname/
*/	
var getElementsByClassName = function (className, tag, elm){
	if (document.getElementsByClassName) {
		getElementsByClassName = function (className, tag, elm) {
			elm = elm || document;
			var elements = elm.getElementsByClassName(className),
				nodeName = (tag)? new RegExp("\\b" + tag + "\\b", "i") : null,
				returnElements = [],
				current;
			for(var i=0, il=elements.length; i<il; i+=1){
				current = elements[i];
				if(!nodeName || nodeName.test(current.nodeName)) {
					returnElements.push(current);
				}
			}
			return returnElements;
		};
	}
	else if (document.evaluate) {
		getElementsByClassName = function (className, tag, elm) {
			tag = tag || "*";
			elm = elm || document;
			var classes = className.split(" "),
				classesToCheck = "",
				xhtmlNamespace = "http://www.w3.org/1999/xhtml",
				namespaceResolver = (document.documentElement.namespaceURI === xhtmlNamespace)? xhtmlNamespace : null,
				returnElements = [],
				elements,
				node;
			for(var j=0, jl=classes.length; j<jl; j+=1){
				classesToCheck += "[contains(concat(' ', @class, ' '), ' " + classes[j] + " ')]";
			}
			try	{
				elements = document.evaluate(".//" + tag + classesToCheck, elm, namespaceResolver, 0, null);
			}
			catch (e) {
				elements = document.evaluate(".//" + tag + classesToCheck, elm, null, 0, null);
			}
			while ((node = elements.iterateNext())) {
				returnElements.push(node);
			}
			return returnElements;
		};
	}
	else {
		getElementsByClassName = function (className, tag, elm) {
			tag = tag || "*";
			elm = elm || document;
			var classes = className.split(" "),
				classesToCheck = [],
				elements = (tag === "*" && elm.all)? elm.all : elm.getElementsByTagName(tag),
				current,
				returnElements = [],
				match;
			for(var k=0, kl=classes.length; k<kl; k+=1){
				classesToCheck.push(new RegExp("(^|\\s)" + classes[k] + "(\\s|$)"));
			}
			for(var l=0, ll=elements.length; l<ll; l+=1){
				current = elements[l];
				match = false;
				for(var m=0, ml=classesToCheck.length; m<ml; m+=1){
					match = classesToCheck[m].test(current.className);
					if (!match) {
						break;
					}
				}
				if (match) {
					returnElements.push(current);
				}
			}
			return returnElements;
		};
	}
	return getElementsByClassName(className, tag, elm);
};