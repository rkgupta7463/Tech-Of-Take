$('.owl-carousel').owlCarousel({
    loop: true,
    Infinity: true,
    margin: 10,
    nav: false,
    // autoplay: true,
    autoplayTimeOut: 1000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 4
        }
    }
})