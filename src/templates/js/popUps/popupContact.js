{% load staticfiles %}
    $(function () {

    $(document).ready(function () { 
        squiggles_sign = parseInt("{{ squiggles_sign }}")
        herbs_sign = parseInt("{{ herbs_sign }}")
        friends_sign = parseInt("{{ friends_sign }}")
        fitness_sign = parseInt("{{ fitness_sign }}")
        goodNews_sign = parseInt("{{ goodNews_sign }}")
        ranger_sign = parseInt("{{ ranger_sign }}")
          
        //  Chart      
        $('#containerSignUp').highcharts({

            credits: {
                enabled: false
            },
            title: {
                style: {
            color: '#000',
            font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
                },
                text: ' <br><br><br><h1>Thanks for getting in contact with Us!</h1><br><br><br><br><h2>Someone will respond to your message shortly.</h2>'
            },
            
            
        });
    });
    });


    
    