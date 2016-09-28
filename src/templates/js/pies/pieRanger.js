
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

            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                style: {
            color: '#000',
            font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
                },
                text: ' <h1>Thanks for Signing Up!</h1><br><h2>Check out the projects standings!</h2>'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true
                    },
                    showInLegend: false
                }
            },
            series: [{
                    name: "sign ups",
                    colorByPoint: true,
                    data: [{
                        name: "Squiggles",
                        y: squiggles_sign                 
                    }, {
                        name: "Herbs",
                        y: herbs_sign 
                    }, {
                        name: "Friends",
                        y: friends_sign
                    }, {
                        name: "Fitness",
                        y: fitness_sign
                    }, {
                        name: "Good News",
                        y: goodNews_sign
                    }, {
                        name: "Ranger",
                        y: ranger_sign,
                        sliced: true,
                        selected: true
                    }]

            }]
        });
    });
    });


    