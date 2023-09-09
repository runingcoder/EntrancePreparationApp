var endpointGK = '/api/progress/GK';

// Reusable function to create a chart
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

// Function to fetch data and create charts
function fetchDataAndCreateCharts() {
    $.ajax({
        method: "GET",
        url: endpointGK,
        success: function (value) {
            createChart('myChart9', value.labels9, value.data9, 'General Knowledge', "rgba(25, 19, 13, 0.2)", "rgba(25, 29, 12, 1)");
            createChart('myChart10', value.labels10, value.data10, 'Books', "rgba(55, 199, 32, 0.2)", "rgba(25, 99, 192, 1)");
            createChart('myChart11', value.labels11, value.data11, 'Science And Nature', "rgba(255, 199, 232, 0.7)", "rgba(255, 99, 132, 1)");
            createChart('myChart12', value.labels12, value.data12, 'Geography', "rgba(13, 180, 185, 0.4)", "rgba(0, 230, 12, 1)");
        },
        error: function (error_data) {
            console.log("error");
            console.log(error_data);
        }
    });
}

// Call the function to fetch data and create charts
fetchDataAndCreateCharts();
