function draw_ip_state(categories, series, container){
    _draw_state(categories, series, container, '(ms)');
}

function draw_domain_state(categories, series, container) {
    _draw_state(categories, series, container, '(ms)');
}

function draw_url_state(categories, series, container){
    _draw_state(categories, series, container, '(kb/s)');
}

function _draw_state(categories, series, container, y_text){
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
                categories:categories,
                labels: {
                    rotation: -45,
                    align: 'right',
                    style: {
                        font: 'normal 13px Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: y_text
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
