<script>
    $(function () {

    $(document).ready(function () {
        all_sign = parseInt("{{ all_sign }}") 
        squiggles_sign = parseInt("{{ squiggles_sign }}")
        herbs_sign = parseInt("{{ herbs_sign }}")
        friends_sign = parseInt("{{ friends_sign }}")
        fitness_sign = parseInt("{{ fitness_sign }}")
        goodNews_sign = parseInt("{{ goodNews_sign }}")
        ranger_sign = parseInt("{{ ranger_sign }}")

            
        // Build the chart
        
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
                text: 'Signed Forms'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
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
                }, {
                    name: "Ranger",
                    y: ranger_sign
                }, {
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
                text: 'Projects Interest Percentage'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
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
                }, {
                    name: "Good News",
                    y: goodNews_sign
                }, {
                    name: "Ranger",
                    y: ranger_sign
                }]
            }]

        });
    });
    });
    </script>