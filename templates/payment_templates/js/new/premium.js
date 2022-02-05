var currCid = ldcid;
var currSCid = ldscid;
var instartup = false;

function Set_Cookie( name, value, expires, path, domain, secure ) {
  var today = new Date();
  today.setTime( today.getTime() );
  if ( expires ){
    expires = expires * 1000 * 60 * 60 * 24;
  }
  var expires_date = new Date( today.getTime() + (expires) );
  document.cookie = name + "=" +escape( value ) +
  ( ( expires ) ? ";expires=" + expires_date.toGMTString() : "" ) +
  ( ( path ) ? ";path=" + path : "" ) +
  ( ( domain ) ? ";domain=" + domain : "" ) +
  ( ( secure ) ? ";secure" : "" );
}

jQuery( document ).ready(function( $ ) {
  $('a.catsPanel').click(function() {
    $( '.start' ).remove();
    currCid = $(this).attr('val');
    var $target = $($(this).attr('href')),
        $other = $target.siblings('.active'),
        animIn = function () { $target.addClass('active').show().css({ left: -($target.width()) }).animate({ left: 0 }, 500); };

    if (!$target.hasClass('active') && $other.length > 0) {
        $other.each(function(index, self) { var $this = $(this); $this.removeClass('active').animate({ left: -10000 }, 500, animIn); });
    }
    else if (!$target.hasClass('active')) { animIn(); }
    return false;
  });

  if (currCid) {
    $('.start' ).remove();
    var $target = $("#cat"+currCid),
    $other = $target.siblings('.active'),
    animIn = function () { $target.addClass('active').show().css({ left: -($target.width()) }).animate({ left: 0 }, 500); };
    if (!$target.hasClass('active') && $other.length > 0) {
        $other.each(function(index, self) { var $this = $(this); $this.removeClass('active').animate({ left: -10000 }, 500, animIn); });
    } else if (!$target.hasClass('active')) { animIn(); }

    if (currSCid) { instartup = true; loadSubcat(currSCid); }
  }

  $('a.subcat').click(function () { $('.categories LI').each(function(idx, li) { $(li).removeClass('catActive'); }); $(this).parent().addClass('catActive'); loadSubcat($(this).attr('val')); });

  var inRate = false;
  $('#voteProcess').hover(function() { inRate = true; }, function() { inRate = false; showStars(-1); });

  $('.dorate').hover(function () { showStars($(this).attr('val')); }).click(function () { fxRateVideo($(this).attr('vid'), $(this).attr('val')); });

  $('a.infoTab').click(function() {
    var $target = $('#infoTab'+$(this).attr('val')),
        $other = $target.siblings('.activeInfo'),
        animIn = function () { $target.addClass('activeInfo').show(); };

    if (!$target.hasClass('activeInfo') && $other.length > 0) {
        $other.each(function(index, self) { var $this = $(this); $this.removeClass('activeInfo'); });
    }
    else if (!$target.hasClass('activeInfo')) { animIn(); }
    return false;
  });

  if (currVid && (!isdef || uid)) { $('#aTab2').click(); if (!uid) {$('#aTab1').hide(); } }
  else if (currSCid) { $('#aTab3').click(); $('#aTab1').hide(); if (!uid) {$('#aTab1').hide(); } }
  else $('#aTab1').click();

});

function loadSubcat(subcat) {
  if (subcat == 0) { return false; }
  currSCid = subcat;
  $.ajax({
    url : "/newscript/ajax.php",
    type : "POST",
    data : {action:"subcat",scid:subcat},
    dataType: 'json',
    success: function(res) {
      if (res.error == true) { alert("Error:\n"+res.msg); }
      else {
        var catinfo = res.data.catinfo;
        $('#subcattitle').html(catinfo.name);
        $('#infoTab3').html(catinfo.info != '' ? catinfo.info : 'No Information Available');
        $('#playlist').empty();
        var i=0;
        for (i=0; i<res.data.items.length; i++) {
          var vid = res.data.items[i];
          $('#playlist').append('<li><a class="subcatvid" href="/premium/film/'+vid.id+'/'+currCid+'/'+currSCid+'/'+vid.urltitle+'#videoContainer" ><img src="/thumb/1_'+vid.id+'.jpg"><figcaption>'+vid.title+'</figcaption></a></li>');
//          $('#playlist').append('<li><a class="subcatvid" href="#" onclick="return loadSubCatVideo('+vid.id+')"><img src="/thumb/1_'+vid.id+'.jpg"><figcaption>'+vid.title+'</figcaption></a></li>');
        };
        if (instartup) { instartup = false; }
        else if (!$('#infoTab3').hasClass('activeInfo')) { $('#aTab3').click(); $('#videoContainer').hide(950); }

      }
    },
    error: function() {
      alert('error');
    }
  });
}

function setQuality(q) {
  Set_Cookie( "quality", q, "", "/", "", "" );
  url = '/premium/film/'+currVid+'/'+currCid+'/'+currSCid+'/'+currttl;
  window.location.assign(url);
  return false;

/*
  var api = flowplayer();
  f = (q==1) ? 'mp4:/encoded/'+currVid+'_1800.mp4' : 'mp4:/encoded/'+currVid+'_1000.mp4';
($('#idVoteView')).html(f);
  api.resume(); api.pause();
  api.load(f, function(event, api, video) { api.pause(); });
*/
}

/* --------------------------------------------------------------------------------------------- */

function fxSendComments(idToHide,commentId,auid,avid) {
	comment_value=$('#'+commentId).val();
	if(comment_value=='') { alert(' Comment box is empty !!'); }
	else{
		$('#'+idToHide).hide();
    $.ajax({
      url : "/newscript/ajax.php",
      type : "POST",
      data : {action:"addcomment",vid:avid,uid:auid,comment:comment_value},
      dataType: 'json',
      success: function(res) {
        if (res.error == true) {
          if (res.msg != '') { $('#commerr').html(res.msg); }
          $('#divComResult2').show();
        }
        else {
          $('#divComResult1').show();
          $('#commentlist').html(res.data);
        }
      },
      error: function() { $('#divComResult2').show(); }
    });
  }
  return false;
}

/* --------------------------------------------------------------------------------------------- */

function fxAddFavorite(toadd,todel,auid,avid) {
  $.ajax({
    url : "/newscript/ajax.php",
    type : "POST",
    data : {action:"addfavorite",vid:avid,uid:auid},
    dataType: 'json',
    success: function(res) {
      if (res.error == true) { }
      else {
        $('#'+toadd).addClass('hidden');
        $('#'+todel).removeClass('hidden');
      }
    },
    error: function() { }
  });
  return false;
}

function fxDelFavorite(toadd,todel,auid,avid) {
  $.ajax({
    url : "/newscript/ajax.php",
    type : "POST",
    data : {action:"delfavorite",vid:avid,uid:auid},
    dataType: 'json',
    success: function(res) {
      if (res.error == true) { }
      else {
        $('#'+todel).addClass('hidden');
        $('#'+toadd).removeClass('hidden');
      }
    },
    error: function() { }
  });
  return false;
}

/* --------------------------------------------------------------------------------------------- */

function showStars(val) {
  val = Math.floor(val/2);
  for (var i=0; i<5; i++)
    $('#rate'+i).addClass(i <= val ? 'fa-star' : 'fa-star-o').removeClass(i > val ? 'fa-star' : 'fa-star-o');
}

function fxRateVideo(avid, arate) {
  $.ajax({
    url : "/newscript/ajax.php",
    type : "POST",
    data : {action:"addrate",vid:avid,rate:arate},
    dataType: 'json',
    success: function(res) {
      if (res.error == true) { }
      else {
        rate  = res.data.rate;
        votes = res.data.votes;
        $('#voteProcess').addClass('hidden');
        $('#idVoteView').removeClass('hidden');
        if (rate) {
          var cl="";
          for (var i=0; i<5; i++) {
            j = i*2;
            cl=((j+0.66) > rate ? 'fa-star-o' : ((j+1.33) > rate ? 'fa-star-half' : 'fa-star'));
            $('#vidRate'+i).removeClass('fa-star-o').removeClass('fa-star-half').removeClass('fa-star').addClass(cl);
          }
        }
        if (votes) { $('#voteCount').html(votes); }
      }
    },
    error: function() { }
  });
  return false;
}

