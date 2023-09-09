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
            createChart('myChart5', value.labels5, value.data5, 'Physics', "rgba(255,99,132,0.2)", "rgba(255,99,132,1)");
            createChart('myChart6', value.labels6, value.data6, 'Chemistry!', "rgba(25,19,13,0.2)", "rgba(25,29,12,1)");
            createChart('myChart7', value.labels7, value.data7, 'Botany', "rgba(55,199,32,0.2)", "rgba(25,99,192,1)");
            createChart('myChart8', value.labels8, value.data8, 'Zoology!', "rgba(255,199,232,0.7)", "rgba(255,99,132,1)");

        },
        error: function (error_data) {
            console.log("error");
            console.log(error_data);
        }
    });
}

var endpoint = '/api/progress/IOM';
fetchDataAndCreateChart(endpoint);
// Fetch and create charts for different subjects
