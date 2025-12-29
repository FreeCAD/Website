/**
 * canvas.js — Sequence of ordered images as animated canvas.
 * Use canvasAPI to draw animation.
 * Support controls via screen, mouse drag and scroll/wheel, keyboard arrows and spacebar to change frames and play/pause.
 * Support animation speed.
 * Support lazy load and off-screen detection.
 */

document.addEventListener("DOMContentLoaded", () =>
  document.querySelectorAll(".canvas").forEach(initCanvas)
);

/* IntersectionObserver to lazy load and auto-pause off-screen canvas. */
const canvasObserver = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      const wrapper = entry.target;
      const api = wrapper._canvasAPI;
      if (!api) return;

      if (entry.isIntersecting) {
        api._visible = true;
        if (!api._imagesLoaded) api.loadFrames();
      } else {
        api._visible = false;
        api.pause();
      }
    });
  },
  { threshold: 0.1 } // canvas fraction visible in viewport.
);

let hoveredCanvas = null;

window.addEventListener("keydown", e => {
  if (!hoveredCanvas || !hoveredCanvas._canvasAPI) return;
  hoveredCanvas._canvasAPI.onKey(e);
});

function initCanvas(wrapper) {
  const get = s => wrapper.querySelector(s);

  const canvas = get("canvas");
  const context = canvas.getContext("2d");
  const slider = get(".slider");
  const playButton = get(".play");
  const pauseButton = get(".pause");
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const { frames, fps } = JSON.parse(get(".canvas-data").textContent);
  if (!Array.isArray(frames) || frames.length === 0) {
    console.warn("Canvas: no frames found");
    return;
  }

  const COUNT = frames.length;
  const FPS = Number.isFinite(+fps) && +fps > 0 ? +fps : 12;

  let images = new Array(COUNT);
  let frame = 0;
  let playing = false;
  let anim = null;
  let lastFrameTime = 0;
  let loaded = false;

  /* Draw frames. */
  const draw = () => {
    const img = images[frame];
    if (!img) return;

    if (canvas.width !== img.width || canvas.height !== img.height) {
      canvas.width = img.width;
      canvas.height = img.height;
    }

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, 0, 0);
  };

  const setFrame = (n, { loop = false } = {}) => {
    frame = loop ? (n + COUNT) % COUNT : Math.max(0, Math.min(COUNT - 1, n));
    slider.value = frame;
    draw();
  };

  /* Animation. */
  const tick = time => {
    if (!playing) return;
    if (wrapper._canvasAPI._visible === false) {
      pause(); // auto-pause off-screen
      return;
    }

    if (time - lastFrameTime >= 1000 / FPS) {
      setFrame(frame + 1, { loop: true });
      lastFrameTime = time;
    }

    anim = requestAnimationFrame(tick);
  };

  const play = () => {
    if (playing) return;
    if (prefersReducedMotion) return;
    if (wrapper._canvasAPI._visible === false) return; // no auto-play off-screen
    if (!loaded) { loadFrames(); return; }
    playing = true;
    lastFrameTime = performance.now();
    anim = requestAnimationFrame(tick);
    wrapper.classList.add("playing");
  };

  const pause = () => {
    if (!playing) return;
    playing = false;
    if (anim) cancelAnimationFrame(anim);
    anim = null;
    wrapper.classList.remove("playing");
  };

  /* Frames loading. */
  const loadFrames = () => {
    if (loaded) return;
    loaded = true;
    wrapper._canvasAPI._imagesLoaded = true;

    frames.forEach((src, i) => {
      const img = new Image();
      img.decoding = "async";
      img.loading = "eager";
      img.onload = () => {
        images[i] = img;
        if (i === frame) draw();
      };
      img.onerror = () => console.warn("Canvas frame failed to load:", src);
      img.src = src;
    });
  };

  /* Controls. */
  slider.addEventListener("input", () => {
    pause();
    setFrame(+slider.value);
  });

  playButton.onclick = play;
  pauseButton.onclick = pause;

  /* Drag / Touch. */
  let dragging = false;
  let startX = 0;
  let startFrame = 0;
  const DRAG_THRESHOLD = 5;
  const getX = e => e.touches ? e.touches[0].clientX : e.clientX;

  const onDragStart = e => {
    dragging = true;
    startX = getX(e);
    startFrame = frame;
    pause();
    wrapper.classList.add("grabbing");
  };

  const onDragMove = e => {
    if (!dragging) return;
    const dx = getX(e) - startX;
    if (Math.abs(dx) < DRAG_THRESHOLD) return;

    e.preventDefault();
    const delta = Math.round((dx / canvas.getBoundingClientRect().width) * COUNT);
    setFrame(startFrame + delta);
  };

  const onDragEnd = () => {
    dragging = false;
    wrapper.classList.remove("grabbing");
  };

  canvas.addEventListener("mousedown", onDragStart);
  canvas.addEventListener("mousemove", onDragMove);
  canvas.addEventListener("mouseup", onDragEnd);
  canvas.addEventListener("mouseleave", onDragEnd);

  canvas.addEventListener("touchstart", onDragStart, { passive: true });
  canvas.addEventListener("touchmove", onDragMove, { passive: false });
  canvas.addEventListener("touchend", onDragEnd);

  /* Horizontal scroll / Wheel. */
  let wheelAcc = 0;
  let lastDir = 0;
  const WHEEL_SENS = Math.max(1, 500 / COUNT);

  canvas.addEventListener("wheel", e => {
    const { deltaX, deltaY, shiftKey } = e;
    const delta =
      Math.abs(deltaX) > Math.abs(deltaY) ? deltaX :
      shiftKey ? deltaY : 0;

    if (!delta) return;
    e.preventDefault();
    pause();

    const dir = Math.sign(delta);
    if (dir !== lastDir) {
      wheelAcc = 0;
      lastDir = dir;
    }

    wheelAcc += delta;
    const step = Math.trunc(wheelAcc / WHEEL_SENS);
    if (!step) return;

    wheelAcc -= step * WHEEL_SENS;
    setFrame(frame + step);
  }, { passive: false });

  /* Keyboard arrows and spacebar. */
  wrapper.addEventListener("focus", () => { hoveredCanvas = wrapper; });

  document.addEventListener("mouseover", e => {
    hoveredCanvas = e.target.closest(".canvas");
  });
  document.addEventListener("mouseout", e => {
    if (e.target.closest(".canvas")) hoveredCanvas = null;
  });

  wrapper._canvasAPI = {
    _visible: true,
    _imagesLoaded: false,
    loadFrames,
    play,
    pause,
    onKey: e => {
      if (e.key === "ArrowLeft") { e.preventDefault(); pause(); setFrame(frame - 1); }
      if (e.key === "ArrowRight") { e.preventDefault(); pause(); setFrame(frame + 1); }
      if (e.key === " ") { e.preventDefault(); playing ? pause() : play(); }
    }
  };

  canvasObserver.observe(wrapper);

  if (wrapper._canvasAPI._visible) loadFrames();
}
