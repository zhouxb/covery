function draw_ip_state(categories, series, container){
    _draw_state(categories, series, container);
}

function draw_domain_state(categories, series, container) {
    _draw_state(categories, series, container);
}

function draw_url_state(categories, series, container){
    _draw_state(categories, series, container);
}

function _draw_state(categories, series, container){
        var chart;
        chart = new Highcharts.Chart({
            chart: {
                renderTo: container,
                type: 'column'
            },
            title: {
                text: ''
            },
            xAxis: {
                categories:categories
            },
            yAxis: {
                min: 0,
                title: {
                    text: '(s)'
                }
            },
            legend: {
                layout: 'vertical',
                backgroundColor: '#FFFFFF',
                align: 'left',
                verticalAlign: 'top',
                x: 100,
                y: 70,
                floating: true,
                shadow: true
            },
            tooltip: {
                formatter: function() {
                    return ''+ this.y +' s';
                }
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series:series
        });
}
