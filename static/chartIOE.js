function createChart(chartId, labels, data, labelName, backgroundColor, borderColor) {
    var ctx = document.getElementById(chartId).getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                fill: false,
                borderColor: borderColor,
                tension: 0.1,
                label: labelName,
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 2
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: "blue",
                        font: {
                            size: 18
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function fetchDataAndCreateChart(endpoint) {
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (value) {
            createChart('myChart1', value.labels, value.data, 'Physics', "rgba(255,99,132,0.2)", "rgba(255,99,132,1)");
            createChart('myChart2', value.labels1, value.data1, 'Chemistry!', "rgba(25,19,13,0.2)", "rgba(25,29,12,1)");
            createChart('myChart3', value.labels2, value.data2, 'Mathematics', "rgba(55,199,32,0.2)", "rgba(25,99,192,1)");
            createChart('myChart4', value.labels3, value.data3, 'English!', "rgba(255,199,232,0.7)", "rgba(255,99,132,1)");
            createChart('myChart5', value.labels4, value.data4, 'Aptitude!', "rgba(13, 180, 185, 0.4)", "rgba(0,230,12,1)");

        },
        error: function (error_data) {
            console.log("error");
            console.log(error_data);
        }
    });
}

var endpoint = '/api/progress/IOE';
fetchDataAndCreateChart(endpoint);
    // Fetch and create charts for different subjects
