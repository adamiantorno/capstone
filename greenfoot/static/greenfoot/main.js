


console.log('hello');

fetch(`/footprint`)
    .then(response => response.json())
    .then(footprint => {

        console.log(footprint);

        var ctx = document.getElementById('myChart').getContext('2d');
            var chart = new Chart (ctx, {
                type: 'bar',
                data: {
                    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    datasets: [{
                        label: 'g CO2/km',
                        backgroundColor: '#00aa18',
                        borderColor: '#00aa18',
                        data: [
                            footprint.monday,
                            footprint.tuesday,
                            footprint.wednesday,
                            footprint.thursday,
                            footprint.friday,
                            footprint.saturday,
                            footprint.sunday
                        ]
                    }]  
                },

                options: {}

            });

    });


