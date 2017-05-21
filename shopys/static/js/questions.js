/**
 * Created by Administrator on 2017/4/25.
 */
$(function(){
    /*公共*/
    var $priceNumber =  $(".change-number");
    var total = $('.question-show').length;
    var i = 1;
    /*默认事件*/
    function change(now) {
        $('.question-show').eq(now).show().find("h2").animate({
            'margin-top':'1.693333rem',
            'opacity': '1'
        },600);
        $priceNumber.html(now+1);
    }
    change(0);

    $(".total-number").html(total);


    /*点击下一个按钮*/
    $(".question-show .next").click(function(){
        i++;
        $(this).parents(".question-show:not(total)").fadeOut(500,
            function() {
                $(this).next().fadeIn();
            });
        $priceNumber.html(i);
    });

    /*点击上一个按钮*/
     $(".question-show .prev").click(function(){
         i--;
         $(this).parents('.question-show').fadeOut(500,
         function() {
            $(this).prev().fadeIn(500);
         });
         $priceNumber.html(i);
     });

    $("input[type='submit']").click(function(){
        window.location.href='results-show.html';
    });

    /*获取宽高度*/
    function getViewportSize () {
        return {
            width: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
            height: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
        };
    }

    $(".wrapper.results-shows").css("height",getViewportSize().height);
    $(".shadow").css("height",getViewportSize().height);

    //判断手机横竖屏状态：
    window.addEventListener("onorientationchange" in window ? "orientationchange" : "resize", function() {
        if (window.orientation === 180 || window.orientation === 0) {
          /* alert('竖屏状态！');*/

        }
        if (window.orientation === 90 || window.orientation === -90 ){
            /*alert('横屏状态！');*/

        }
    }, false);

    /*点击答题历史列表*/
    $(".results-lists-ul").find("li").on("click",function(e){
         $(".shadow").css("display","block");
         $(document).on('touchmove',function (e){
            e.preventDefault();
         });

    });

    /*点击关闭按钮*/
    $(".shadow-close").on("click",function(){
       $(".shadow").css("display","none");
       $(document).on('touchend',function (e){
             $(document).unbind("touchmove");
       });
    });



});