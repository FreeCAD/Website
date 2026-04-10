/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Carousel of image slides:
- Support arrows, bullets, scroll or drag to display previous or next slides.
- Support automatic mode option with duration.
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
    const duration = parseInt(carousel.dataset.duration, 10) || 5000;

    if (slides.length <= 1) return;

    let isDragging = false;
    let startX = 0;
    let startScrollLeft = 0;
    let interacted = false;
    let autoTimer = null;

    const isHovered = () => carousel.matches(':hover');

    const getCurrentIndex = () => {
      let closest = 0;
      let minDiff = Infinity;

      slides.forEach((slide, i) => {
        const diff = Math.abs(item.scrollLeft - slide.offsetLeft);
        if (diff < minDiff) {
          minDiff = diff;
          closest = i;
        }
      });

      return closest;
    };

    const updateSelected = () => {
      const index = getCurrentIndex();

      bullets.forEach((b, i) => {
        b.classList.toggle('selected', i === index);
        b.toggleAttribute('aria-current', i === index);
      });

      slides.forEach((s, i) => {
        s.classList.toggle('selected', i === index);
      });
    };

    const goToSlide = (index) => {
      if (!slides[index]) return;
      item.scrollTo({ left: slides[index].offsetLeft, behavior: 'smooth' });
    };

    const nextSlide = () => goToSlide((getCurrentIndex() + 1) % slides.length);
    const prevSlide = () => goToSlide((getCurrentIndex() - 1 + slides.length) % slides.length);

    const markInteracted = () => { interacted = true; };

    item.setAttribute('tabindex', '0');

    // Scroll tracking
    item.addEventListener("scroll", debounce(updateSelected), { passive: true });

    // Drag support
    item.addEventListener("mousedown", (e) => {
      e.preventDefault();
      isDragging = true;
      markInteracted();
      item.classList.add('grabbing');
      startX = e.pageX - item.offsetLeft;
      startScrollLeft = item.scrollLeft;
    });

    item.addEventListener("mouseup", () => {
      if (!isDragging) return;
      isDragging = false;
      item.classList.remove('grabbing');
      updateSelected();
    });

    item.addEventListener("mouseleave", () => {
      if (!isDragging) return;
      isDragging = false;
      item.classList.remove('grabbing');
      updateSelected();
    });

    item.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.pageX - item.offsetLeft;
      const walk = (x - startX) * 2;
      item.scrollLeft = startScrollLeft - walk;
    });

    // Interaction tracking
    item.addEventListener("touchstart", markInteracted, { passive: true });
    document.addEventListener("keydown", e => {
      if (!isHovered()) return;

      if (e.key === 'ArrowRight') {
        e.preventDefault();
        markInteracted();
        nextSlide();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        markInteracted();
        prevSlide();
      }
    });

    // Controls
    if (nextArrow) {
      nextArrow.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        markInteracted();
        nextSlide();
      });
    }

    if (prevArrow) {
      prevArrow.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        markInteracted();
        prevSlide();
      });
    }

    bullets.forEach((bullet, index) => {
      bullet.addEventListener("click", (e) => {
        e.preventDefault();
        markInteracted();
        goToSlide(index);
      });
    });

    // Auto-play
    const startAuto = () => {
      if (mode !== "auto" || duration <= 0) return;
      stopAuto();
      autoTimer = setInterval(() => {
        if (!interacted && !isHovered()) nextSlide();
      }, duration);
    };

    const stopAuto = () => {
      if (autoTimer) clearInterval(autoTimer);
    };

    item.addEventListener("mouseenter", stopAuto);
    item.addEventListener("mouseleave", startAuto);

    startAuto();
    updateSelected();
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
