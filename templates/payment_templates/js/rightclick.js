// shut the door but don't lock it right-click disable

$(document).ready(function(){
   $('#ssfVideo').bind('contextmenu',function() { return false; });
});