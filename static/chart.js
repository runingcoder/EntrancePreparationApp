

    var endpoint = '/api/progress/'
    var defaultData = []
    var labels = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels = value.labels
            defaultData = value.data
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Physics',
                        data: defaultData,
                        color: "blue",
                        backgroundColor: "rgba(255,99,132,0.2)",
                        borderColor: "rgba(255,99,132,1)",
                        borderWidth: 2
                    }]
                },
                options: {
                    plugins: { // 'legend' now within object 'plugins {}'
                        legend: {
                            labels: {
                                color: "blue", // not 'fontColor:' anymore
                                // fontSize: 18  // not 'fontSize:' anymore
                                font: {
                                    size: 18 // 'size' now within object 'font {}'
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
        },
        error: function(error_data) {
            console.log("error")
            console.log(error_data)
        }





    })


    var defaultData1 = []
    var labels1 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels1 = value.labels1
            defaultData1 = value.data1
            var ctx = document.getElementById('myChart2').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels1,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Chemistry!',
                        data: defaultData1,
                        color: "blue",
                        backgroundColor: "rgba(255,99,132,0.2)",
                        borderColor: "rgba(255,99,132,1)",
                        borderWidth: 2
                    }]
                },
                options: {
                    plugins: { // 'legend' now within object 'plugins {}'
                        legend: {
                            labels: {
                                color: "blue", // not 'fontColor:' anymore
                                // fontSize: 18  // not 'fontSize:' anymore
                                font: {
                                    size: 18 // 'size' now within object 'font {}'
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
        },
        error: function(error_data) {
            console.log("error")
            console.log(error_data)
        }





    })





    var defaultData2 = []
    var labels2 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels2 = value.labels2
            defaultData2 = value.data2
            var ctx = document.getElementById('myChart3').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels2,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Mathematics',
                        data: defaultData2,
                        color: "blue",
                        backgroundColor: "rgba(55,199,32,0.2)",
                        borderColor: "rgba(25,99,192,1)",
                        borderWidth: 2
                    }]
                },
                options: {
                    plugins: { // 'legend' now within object 'plugins {}'
                        legend: {
                            labels: {
                                color: "blue", // not 'fontColor:' anymore
                                // fontSize: 18  // not 'fontSize:' anymore
                                font: {
                                    size: 18 // 'size' now within object 'font {}'
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
        },
        error: function(error_data) {
            console.log("error")
            console.log(error_data)
        }





    })


