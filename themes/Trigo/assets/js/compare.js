/**
 * compare.js — Compare before/after images.
 * Support click or drag to move clipping path.
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

    const move = (clientX) => {
      const rect = container.getBoundingClientRect();
      let x = clientX - rect.left;
      x = Math.max(0, Math.min(x, rect.width));

      let pct = (x / rect.width) * 100;
      pct = Math.round(pct * 10) / 10;

      after.style.clipPath = `inset(0 0 0 ${pct}%)`;
      divider.style.left = `${pct}%`;
      handle.style.left = `${pct}%`;
    };

    const startDrag = (e) => {
      e.preventDefault();
      dragging = true;
      handle.classList.add("active");
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      move(clientX);
    };

    const stopDrag = () => {
      dragging = false;
      handle.classList.remove("active");
    };

    const onDrag = (e) => {
      if (!dragging) return;
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      move(clientX);
    };

    [handle, divider, container].forEach((el) => {
      el.addEventListener("mousedown", startDrag);
      el.addEventListener("touchstart", startDrag, { passive: true });
    });

    window.addEventListener("mousemove", onDrag);
    window.addEventListener("mouseup", stopDrag);

    window.addEventListener("touchmove", onDrag, { passive: true });
    window.addEventListener("touchend", stopDrag);

    const onClick = (e) => {
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      move(clientX);
    };
    container.addEventListener("click", onClick);
    container.addEventListener("touchstart", onClick, { passive: true });
  });
});
