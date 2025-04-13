// Добавляем класс .scrolled к заголовку при прокрутке страницы
window.onscroll = function() {
    let header = document.querySelector('.sticky-header');
    if (window.scrollY > 50) { // Когда скролл на 50px и более
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
};

// Добавление эффекта при наведении на заголовок
const header = document.querySelector('.sticky-header');

header.addEventListener('mousemove', () => {
    header.classList.add('scrolled');
});

header.addEventListener('mouseleave', () => {
    if (window.scrollY < 50) {
        header.classList.remove('scrolled');
    }
});
