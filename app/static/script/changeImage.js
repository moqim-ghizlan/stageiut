const images= document.getElementsByClassName("images-slider__main__slider__image__img");

for(let i = 0; i < images.length; i++) {
    images[i].addEventListener('click', function() {
        document.getElementsByClassName('images-slider__main__image__img')[0].classList.add('animation');
        document.getElementsByClassName('images-slider__main__image__img')[0].src = this.src;
    });
}
