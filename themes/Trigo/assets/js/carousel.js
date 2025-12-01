/**
 * carousel.js — Carousel between image slides.
 * Support arrows, bullets, scroll or drag to display previous or next slides.
 * Support automatic mode option with duration.
 */

document.addEventListener('DOMContentLoaded', () => {

  const carousels = document.querySelectorAll('.carousel');

  carousels.forEach(carousel => {

    const item = carousel.querySelector('ul');
    const slides = Array.from(carousel.querySelectorAll('ul > li'));
    const bullets = Array.from(carousel.querySelectorAll('ol > li'));
    const nextArrow = carousel.querySelector('.next');
    const prevArrow = carousel.querySelector('.prev');

    const mode = carousel.dataset.mode || "fixed";
    const duration = carousel.dataset.duration || "5000";

    if (slides.length === 0) return;

    let isDragging = false;
    let startX = 0;
    let startScrollLeft = 0;
    let interacted = false;
    let autoTimer = null;

    bullets[0]?.classList.add('selected');
    slides[0]?.classList.add('selected');

    const goToSlide = (n) => {
      const target = slides[n];
      if (target) item.scrollLeft = target.offsetLeft;
    };

    const getCurrentIndex = () => {
      const diff = slides[1].offsetLeft - slides[0].offsetLeft;
      return Math.round(item.scrollLeft / diff);
    };

    const updateSelected = () => {
      const index = getCurrentIndex();

      bullets.forEach(b => b.classList.remove('selected'));
      slides.forEach(s => s.classList.remove('selected'));

      bullets[index]?.classList.add('selected');
      slides[index]?.classList.add('selected');

      const titleBox = carousel.parentElement.parentElement.querySelector('.dynamictitle');
      if (titleBox) {
        const title = slides[index].querySelector('img')?.getAttribute('title');
        if (title) titleBox.textContent = title;
      }
    };

    const nextSlide = () => {
      const index = getCurrentIndex();
      goToSlide(index + 1 < slides.length ? index + 1 : 0);
    };

    const prevSlide = () => {
      const index = getCurrentIndex();
      goToSlide(index > 0 ? index - 1 : slides.length - 1);
    };

    const markInteracted = () => { interacted = true; };

    item.addEventListener("scroll", debounce(updateSelected));

    item.addEventListener("mousedown", (e) => {
      isDragging = true;
      markInteracted();
      item.classList.add('grabbing');
      startX = e.pageX - item.offsetLeft;
      startScrollLeft = item.scrollLeft;
    });

    item.addEventListener("mouseup", () => {
      isDragging = false;
      item.classList.remove('grabbing');
      updateSelected();
    });

    item.addEventListener("mouseleave", () => {
      isDragging = false;
      item.classList.remove('grabbing');
      updateSelected();
    });

    item.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.pageX - item.offsetLeft;
      const walk = (x - startX) * 3;
      item.scrollLeft = startScrollLeft - walk;
    });

    item.addEventListener("touchstart", markInteracted);
    item.addEventListener("keydown", e => {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') markInteracted();
    });

    nextArrow.addEventListener("click", () => { markInteracted(); nextSlide(); });
    prevArrow.addEventListener("click", () => { markInteracted(); prevSlide(); });

    bullets.forEach((bullet, index) => {
      bullet.addEventListener("click", e => {
        e.preventDefault();
        markInteracted();
        goToSlide(index);
      });
    });

    // Auto-play only if "auto"
    if (mode === "auto" && duration > 0) {
      autoTimer = setInterval(() => {
        if (!interacted && item !== document.querySelector(".carousel:hover ul")) {
          nextSlide();
        }
      }, duration);
    }
  });

});


/**
* Debounce functions for better performance
* (c) 2021 Chris Ferdinandi, MIT License, https://gomakethings.com
* @param  {Function} fn The function to debounce
*/

function debounce(fn) {
  let timeout;
  return function (...args) {
    if (timeout) cancelAnimationFrame(timeout);
    timeout = requestAnimationFrame(() => fn.apply(this, args));
  };
}
