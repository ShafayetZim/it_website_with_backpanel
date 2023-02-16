var swiper =  new Swiper(".slider-main", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 0,
    navigation: {
        nextEl: ".btn-next-main",
        prevEl: ".btn-prev-main",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1280: {
            slidesPerView: 1,
            spaceBetween: 0,
        },
    },
});

var swiper =  new Swiper(".sl-post", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 30,
    navigation: {
        nextEl: ".btn-next-post",
        prevEl: ".btn-prev-post",
    },
});

var swiper =  new Swiper(".slider-project", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 30,
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        750: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        991: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },
    navigation: {
        nextEl: ".next-project",
        prevEl: ".prev-project",
    },
});

var swiper =  new Swiper(".slider-project2", {
    slidesPerView: 1,
    loop: true, 
    spaceBetween: 30,
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        750: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        991: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },
    navigation: {
        nextEl: ".next-project2",
        prevEl: ".prev-project2",
    },
});

var swiper =  new Swiper(".slider-team", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 30,
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        750: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        991: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    },
});

var swiper4 =  new Swiper(".slider-testimonior-thum", {
    freeMode: true,
    watchSlidesProgress: true,
    slidesPerView: 5,
    loop: false, 
    spaceBetween: 0,
    pagination: {
        el: ".testimonior-pagination",
        clickable: true,
    },
    breakpoints: {
        1280: {
            slidesPerView: 5,
            spaceBetween: 0,
        },
    },
});

var swiper =  new Swiper(".slider-testimonior", {
    slidesPerView: 1,
    loop: true, 
    spaceBetween: 50,
    pagination: {
        el: ".testimonior-pagination",
        clickable: true,
    },
    breakpoints: {
        1280: {
            slidesPerView: 1,
            spaceBetween: 50,
        },
    },
    thumbs: {
        swiper: swiper4,
    },
});

var swiper =  new Swiper(".sl-partner", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 90,
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 90,
        },
        450: {
            slidesPerView: 2,
            spaceBetween: 90,
        },
        600: {
            slidesPerView: 2,
            spaceBetween: 90,
        },
        750: {
            slidesPerView: 3,
            spaceBetween: 90,
        },
        991: {
            slidesPerView: 4,
            spaceBetween: 90,
        },
        1280: {
            slidesPerView: 4,
            spaceBetween: 60,
        },
    },
});

var swiper =  new Swiper(".slider-service", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 30,
    pagination: {
        el: ".service-pagination",
        clickable: true,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        750: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        991: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    },
});

var swiper = new Swiper(".swiper-loop", {
    spaceBetween: 30,
    loop: true,
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        500: {
            slidesPerView: 2
        },
        600: {
            slidesPerView: 2
        },
        991: {
            slidesPerView: 3
        },
        1200: {
            slidesPerView: 3
        },
    },
    disableOnInteraction: true
});

var swiper3 = new Swiper(".gallery-thumbs2", {
    spaceBetween: 20,
    grabCursor: true,
    slidesPerView: 3,
    loop: false,
    breakpoints: {
        500: {
            slidesPerView: 3,
        },
        767: {
            slidesPerView: 3,
            direction: "vertical",
            allowTouchMove: true,
            freeMode: true, 
            disableOnInteraction: true
        },
        991: {
            slidesPerView: 4,
            spaceBetween: 20,  
            direction: "vertical",
        },
    },
    allowTouchMove: true,
    freeMode: true, 
    disableOnInteraction: true
  });
  
  var swiper4 = new Swiper(".gallery-slider2", {
    slidesPerView: 1,
    spaceBetween: 50,
    loop: false,
    navigation: {
      nextEl: ".btn-next-customer",
      prevEl: ".btn-prev-customer",
    },
    pagination: {
        el: ".swiper-pagination2",
        clickable: true,
    },
    thumbs: {
        swiper: swiper3,
    },
  });

  var swiper =  new Swiper(".slider-product", {
    slidesPerView: 1,
    loop: false, 
    spaceBetween: 30,
    navigation: {
        nextEl: ".btn-next-product",
        prevEl: ".btn-prev-product",
      },
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        750: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        991: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    },
});
