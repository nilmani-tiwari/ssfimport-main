// Spinning Actions
    if($.browser.msie && $.browser.version == 9){
        $('.thumb-pad1 .thumbnail .caption a').hover(function(){
            $(this).parent().siblings('figure').find('.sp3').stop().css({'border-color':'transparent transparent #fff transparent'});
            $(this).parent().siblings('figure').find('.sp2').stop().css({'border-color':'transparent transparent #fff transparent'});
            $(this).parent().siblings('figure').find('.sp1').stop().css({'border-color':'transparent transparent #fff transparent'});
            $(this).parent().parent().parent().stop().css({'border-bottom-color':'#fff'});	
            $(this).siblings('p').stop().css({color:'#fff'}); 
                }, function(){
            $(this).parent().siblings('figure').find('.sp3').stop().css({'border-color':'transparent transparent #f4d764 transparent'});
            $(this).parent().siblings('figure').find('.sp2').stop().css({'border-color':'transparent transparent #f4d764 transparent'});	
            $(this).parent().siblings('figure').find('.sp1').stop().css({'border-color':'transparent transparent #f4d764 transparent'});
            $(this).parent().parent().parent().stop().css({'border-bottom-color':'#f4d764'});
            $(this).siblings('p').stop().css({color:'#989a96'}); 					 
        })
        $('.riskBox a').hover(function(){
            $(this).parent().siblings('figure').find('div').stop().css({'background':'#2c2d2b', 'border-color':'#2c2d2b'});
            $(this).parent().siblings('figure').find('div span').stop().css({'color':'#f4d764'});
                }, function(){
            $(this).parent().siblings('figure').find('div').stop().css({'background':'transparent', 'border-color':'#fff'});
            $(this).parent().siblings('figure').find('div span').stop().css({'color':'#fff'});					 
        })
    }else {
       $('.thumb-pad1 .thumbnail .caption a').hover(function(){
            $(this).parent().siblings('figure').find('.sp3').stop().css({'rotate':'315deg', 'border-color':'transparent transparent #fff transparent'});
            $(this).parent().siblings('figure').find('.sp2').stop().css({'rotate':'315deg', 'border-color':'transparent transparent #fff transparent'});
            $(this).parent().siblings('figure').find('.sp1').stop().css({'rotate':'315deg', 'border-color':'transparent transparent #fff transparent'});
            $(this).parent().parent().parent().stop().css({'border-bottom-color':'#fff'});	
            $(this).siblings('p').stop().css({color:'#fff'});  
                }, function(){
            $(this).parent().siblings('figure').find('.sp3').stop().css({'rotate':'-45deg', 'border-color':'transparent transparent #f4d764 transparent'});
            $(this).parent().siblings('figure').find('.sp2').stop().css({'rotate':'-45deg', 'border-color':'transparent transparent #f4d764 transparent'});	
            $(this).parent().siblings('figure').find('.sp1').stop().css({'rotate':'-45deg', 'border-color':'transparent transparent #f4d764 transparent'});
            $(this).parent().parent().parent().stop().css({'border-bottom-color':'#f4d764'});
            $(this).siblings('p').stop().css({color:'#989a96'});					 
        })
        $('.newsBox a').hover(function(){
            $(this).parent().siblings('.col-lg-5').find('.thumb-pad2 .sp3').stop().css({'rotate':'135deg'});
            $(this).parent().siblings('.col-lg-5').find('.thumb-pad2 .sp2').stop().css({'rotate':'135deg'});
            $(this).parent().siblings('.col-lg-5').find('.thumb-pad2 .sp1').stop().css({'rotate':'135deg'});
                }, function(){
            $(this).parent().siblings('.col-lg-5').find('.thumb-pad2 .sp3').stop().css({'rotate':'-45deg'});
            $(this).parent().siblings('.col-lg-5').find('.thumb-pad2 .sp2').stop().css({'rotate':'-45deg'});	
            $(this).parent().siblings('.col-lg-5').find('.thumb-pad2 .sp1').stop().css({'rotate':'-45deg'});					 
        })
        $('.riskBox a').hover(function(){
            $(this).parent().siblings('figure').find('.sp3').stop().css({'rotate':'315deg'});
            $(this).parent().siblings('figure').find('.sp2').stop().css({'rotate':'315deg'});
            $(this).parent().siblings('figure').find('.sp1').stop().css({'rotate':'315deg'});
            $(this).parent().siblings('figure').find('div').stop().css({'background':'#2c2d2b', 'border-color':'#2c2d2b'});
            $(this).parent().siblings('figure').find('div span').stop().css({'color':'#f4d764'});
                }, function(){
            $(this).parent().siblings('figure').find('.sp3').stop().css({'rotate':'-45deg'});
            $(this).parent().siblings('figure').find('.sp2').stop().css({'rotate':'-45deg'});
            $(this).parent().siblings('figure').find('.sp1').stop().css({'rotate':'-45deg'});
            $(this).parent().siblings('figure').find('div').stop().css({'background':'transparent', 'border-color':'#fff'});
            $(this).parent().siblings('figure').find('div span').stop().css({'color':'#fff'});					 
        }) 
    }