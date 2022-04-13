
$(window).scroll(function(){
    if($(this).scrollTop()>50) 
    {
      $(".backtotop").fadeIn()
    }
    else
    {
      $(".backtotop").fadeOut()
    }

  });


 