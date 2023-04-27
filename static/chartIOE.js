

    var endpoint = '/api/progress/IOE'
    var defaultData = []
    var labels = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            console.log(value)
            labels = value.labels
            defaultData = value.data
            var ctx = document.getElementById('myChart1').getContext('2d');
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
                        backgroundColor: "rgba(25,19,13,0.2)",
                        borderColor: "rgba(25,29,12,1)",
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

    var defaultData3 = []
    var labels3 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels3 = value.labels3
            defaultData3 = value.data3
            var ctx = document.getElementById('myChart4').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels3,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'English!',
                        data: defaultData1,
                        color: "blue",
                        backgroundColor: "rgba(255,199,232,0.7)",
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
    var defaultData4 = []
    var labels4= []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels4 = value.labels4
            defaultData4 = value.data4
            var ctx = document.getElementById('myChart5').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels4,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Aptitude!',
                        data: defaultData1,
                        color: "blue",
                        backgroundColor: "rgba(13, 180, 185, 0.4)",
                        borderColor: "rgba(0,230,12,1)",
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




