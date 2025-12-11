const openTargetDetails = () => {
  if (!location.hash) return;

  const el = document.getElementById(location.hash.slice(1));
  if (el instanceof HTMLDetailsElement) el.open = true;
};

document.addEventListener("DOMContentLoaded", openTargetDetails);
window.addEventListener("hashchange", openTargetDetails);
