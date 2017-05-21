/**
 * Created by User on 2017/4/7.
 */

$(function(){

    /*topBar Search*/
    $(".search-btn").on("click",function(){
        if( $(".topBar-search-block").hasClass("topBar-search-visible") ){
            $(".topBar-search-block").slideUp();
            $(".topBar-search-block").removeClass("topBar-search-visible");
        }else {
            $(".topBar-search-block").slideDown();
            $(".topBar-search-block").addClass("topBar-search-visible");
        }
    });

    /*topBar search close*/
    $(".search-close").on("click",function(){
        $(".topBar-search-block").slideUp();
        $(".topBar-search-block").removeClass("topBar-search-visible");
    });


    /*返回顶部*/
    $(window).scroll(function(){
        if( $(window).scrollTop() > 100 ){
            $(".to-top").show();
            $(".header-fixed .header-static").addClass("header-fixed-shrink");
        }else {
             $(".to-top").hide();
            $(".header-fixed .header-static").removeClass("header-fixed-shrink");
        }
    });

    $("#to-top").click(function(){
         $('html,body').animate({scrollTop : 0},800);
    });

    /*下一项目*/
    $(".next-btns").on("click",function(){
        $(this).css("display","none");
        $(".display-hidden").show();
    });

    /*获取时间*/
    var $date = new Date();
    var $year = $date.getFullYear();
    var $month = $date.getMonth()+1;
    var $day = $date.getDate();

    $(".topBar-time").html($year+"年" + $month + "月" + $day + "日");

})