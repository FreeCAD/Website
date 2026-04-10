/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Compare before/after images with slider:
- Support click, drag, keyboard arrows and horizontal scroll to move clipping path.
*/


document.addEventListener("DOMContentLoaded", () => {
  const sliders = document.querySelectorAll(".compare");
  if (!sliders.length) return;

  sliders.forEach((container) => {
    const before = container.querySelector(".before");
    const after = container.querySelector(".after");
    const handle = container.querySelector(".handle");
    const divider = container.querySelector(".divider");
    if (!before || !after || !handle || !divider) return;

    let dragging = false;
    let pending = false;
    let percent = 50; // default start at 50%

    const isHovered = () => container.matches(':hover');

    const updateSlider = () => {
      after.style.clipPath = `inset(0 0 0 ${percent}%)`;
      divider.style.left = `${percent}%`;
      handle.style.left = `${percent}%`;
    };

    const moveSlider = (clientX) => {
      if (pending) return;
      pending = true;
      requestAnimationFrame(() => {
        const rect = container.getBoundingClientRect();
        percent = Math.round((Math.max(0, Math.min(clientX - rect.left, rect.width)) / rect.width) * 1000) / 10;
        updateSlider();
        pending = false;
      });
    };

    const adjustSlider = (deltapercent) => {
      percent = Math.max(0, Math.min(100, percent + deltapercent));
      updateSlider();
    };

    const startDrag = (e) => {
      e.preventDefault();
      dragging = true;
      handle.classList.add("active");
      if (e.pointerId) container.setPointerCapture(e.pointerId);
      moveSlider(e.clientX);
    };

    const stopDrag = (e) => {
      if (!dragging) return;
      dragging = false;
      handle.classList.remove("active");
      if (e.pointerId) container.releasePointerCapture(e.pointerId);
    };

    const onDrag = (e) => {
      if (!dragging) return;
      moveSlider(e.clientX);
    };

    [handle, divider, container].forEach((el) => {
      el.addEventListener("pointerdown", startDrag);
      el.addEventListener("pointermove", onDrag);
      el.addEventListener("pointerup", stopDrag);
      el.addEventListener("pointercancel", stopDrag);
      el.addEventListener("pointerleave", stopDrag);
    });

    container.addEventListener("click", (e) => moveSlider(e.clientX));

    container.addEventListener("wheel", (e) => {
      e.preventDefault();
      const delta = e.deltaY || e.deltaX;
      adjustSlider(delta > 0 ? 2 : -2);
    }, { passive: false });

    container.setAttribute("tabindex", "0");
    document.addEventListener("keydown", (e) => {
      if (!isHovered()) return;
      if (e.key === "ArrowLeft") adjustSlider(-2);
      if (e.key === "ArrowRight") adjustSlider(2);
    });

    updateSlider();
  });
});