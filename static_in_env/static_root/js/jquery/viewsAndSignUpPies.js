$(function () {

    $(document).ready(function () {
        all_sign = parseInt("{{ all_sign }}") 
        squiggles_sign = parseInt("{{ squiggles_sign }}")
        herbs_sign = parseInt("{{ herbs_sign }}")
        friends_sign = parseInt("{{ friends_sign }}")
        fitness_sign = parseInt("{{ fitness_sign }}")
        goodNews_sign = parseInt("{{ goodNews_sign }}")

        homeView = parseInt("{{ homeView }}")
        appView = parseInt("{{ appView }}")
        businessView = parseInt("{{ businessView }}")
        contactView = parseInt("{{ contactView }}")
        fitnessView = parseInt("{{ fitnessView }}")
        friendsView = parseInt("{{ friendsView }}")
        gamesView = parseInt("{{ gamesView }}")
        goodnewsView = parseInt("{{ goodnewsView }}")
        herbsView = parseInt("{{ herbsView }}")
        squigglesView = parseInt("{{ squigglesView }}")
        aboutView = parseInt("{{ aboutView }}")
        labView = parseInt("{{ labView }}")


              
        // Build the chart
        $('#container').highcharts({

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
                text: 'Page Views'
            },
            tooltip: {
                //pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
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
                name: "Views",
                colorByPoint: true,
                data: [{
                    name: "Home",
                    y: homeView,
                    sliced: true,
                    selected: true
                },{
                    name: "Business",
                    y: businessView
                }, {
                    name: "Contact",
                    y: contactView
                },{
                    name: "About",
                    y: aboutView
                },{
                    name: "Lab",
                    y: labView
                },{
                    name: "Apps",
                    y: appView                   
                },{
                    name: "Fitness",
                    y: fitnessView
                },{
                    name: "Friends",
                    y: friendsView
                },{
                    name: "Herbs",
                    y: herbsView
                },{
                    name: "Good News",
                    y: goodnewsView
                },{
                    name: "Games",
                    y: gamesView
                },{
                    name: "SquigglesView",
                    y: friendsView
                }]
            }]
            

        });
        $('#containerTwo').highcharts({

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
                text: 'Sign Forms'
            },
            tooltip: {
                //pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
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
                },{
                    name: "All",
                    y: all_sign,
                    sliced: true,
                    selected: true
                }]
            }]


        });
        $('#containerThree').highcharts({

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
                text: 'Projects Interest'
            },
            tooltip: {
                //pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
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
                }]
            }]

        });
    });
    });