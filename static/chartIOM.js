

    var endpoint = '/api/progress/IOM'
    var defaultData5 = []
    var labels5 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            console.log(value)
            labels5 = value.labels5
            defaultData5 = value.data5
            var ctx = document.getElementById('myChart5').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels5,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(5, 12, 12)',
                        tension: 0.1,
                        label: 'Physics',
                        data: defaultData5,
                        color: "blue",
                        backgroundColor: "rgba(25,9,132,0.2)",
                        borderColor: "rgba(25,9,32,1)",
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


    var defaultData6 = []
    var labels6 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels6 = value.labels6
            defaultData6 = value.data6
            var ctx = document.getElementById('myChart6').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels6,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Chemistry!',
                        data: defaultData6,
                        color: "blue",
                        backgroundColor: "rgba(255,99,132,0.2)",
                        borderColor: "rgba(255,9,132,1)",
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


    var defaultData8 = []
    var labels8= []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels8= value.labels8
            defaultData8= value.data8
            var ctx = document.getElementById('myChart8').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels8,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Botany',
                        data: defaultData8,
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



    var defaultData7 = []
    var labels7 = []
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(value) {
            labels7 = value.labels7
            defaultData7 = value.data7
            var ctx = document.getElementById('myChart7').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                color: '#ff0000',
                data: {
                    labels: labels7,
                    datasets: [{
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1,
                        label: 'Zoology',
                        data: defaultData7,
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

    