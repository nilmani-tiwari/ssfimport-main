	function hoverTab(tabData){
		tabData.style.backgroundPosition = " 0% -25px";
		tabData.style.lineHeight = "24px";
	}
	
	function outTab(tabData){
		tabData.style.backgroundPosition = " 0% -25px";
	}
	
	function executeTab(tabData){
		tabData.className = "tabactive";
		tabData.style.backgroundPosition = " 0% -0px";
		tabData.onmouseover=function(){};
		tabData.onmouseout=function(){};
	}
	
	function showTabData(idForDisplay){
		var tabFeatured = document.getElementById('tab-featured'); 
		var tabMostview = document.getElementById('tab-mostview');
		
		var featuretab = document.getElementById('featuretab');
		var mostviewedtab = document.getElementById('mostviewedtab');
		
		tabFeatured.style.display = "none";
		tabMostview.style.display = "none";
		 
		featuretab.className = "";
		mostviewedtab.className = "";
		
		featuretab.style.backgroundPosition = " 0% -25px";
		mostviewedtab.style.backgroundPosition = " 0% -25px";
		
		featuretab.onmouseover=function(){hoverTab(this);}
		mostviewedtab.onmouseover=function(){hoverTab(this);}
		
		featuretab.onmouseout=function(){outTab(this);}
		mostviewedtab.onmouseout=function(){outTab(this);}
		
		if (idForDisplay == "featured"){	
			tabFeatured.style.display = "block";
			executeTab(featuretab);
		}			
		else if(idForDisplay == "mostview"){
			tabMostview.style.display = "block";
			executeTab(mostviewedtab);
		}
		
 	}