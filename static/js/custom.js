const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['C', 'Python', 'Java', 'Data  Structure', 'Django', 'Machine Learning', "Flask", "Bootstrap"],
        datasets: [{
            label: 'Multiple colors',
            data: [25, 19, 60, 55, 20, 30, 40, 50],
            // borderColor: '#36A2EB',
            borderWidth: 1,
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)',
                'rgb(201, 203, 207)',
                'rgb(201, 203, 207)',
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.4)',
                'rgba(255, 159, 64, 0.4)',
                'rgba(255, 205, 86, 0.4)',
                'rgba(75, 192, 192, 0.4)',
                'rgba(54, 162, 235, 0.4)',
                'rgba(153, 102, 255, 0.4)',
                'rgba(201, 203, 207, 0.4)',
                'rgba(201, 203, 207, 0.4)',
                'rgba(255, 99, 132, 0.4)',
            ],
        }]
    },
    options: {
        responsive: false,
        scales: {
            y: {
                beginAtZero: false,
                title: {
                    display: true,
                    text: "Percentage",
                    fontSize: 50,
                }
            },
            x: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: "Programming Language",
                    fontSize: 50,
                    padding: {
                        top: 20
                    },
                }
            }
        },
        layout: {
            padding: {
                left: 50,
                right: 10,
                top: 10,
                bottom: 0
            },
        },
        plugins: {
            tooltips: {
                enabled: true,
                backgroundColor: "red",
            },

            legend: {
                display: false,
            },
            title: {
                display: true,
                // text: 'Skills',
                fontSize: 50,
                padding: {
                    top: 10,
                    bottom: 20,
                },
            },
        },
        animation: {
            duration: 3500,
            easing: 'easeInOutBounce',
            loop: true,
        },
    },
});