let currentIndex = 0;

const images = document.querySelectorAll('.carousel-item');
const totalImages = images.length;

document.getElementById('nextBtn').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalImages; // Move to the next image
    updateCarousel();
});

document.getElementById('prevBtn').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalImages) % totalImages; // Move to the previous image
    updateCarousel();
});

function updateCarousel() {
    const offset = -currentIndex * 100; // Calculate the offset for sliding images
    document.querySelector('.carousel-container').style.transform = `translateX(${offset}%)`;
}
