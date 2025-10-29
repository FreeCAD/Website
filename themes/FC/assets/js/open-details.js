document.addEventListener('DOMContentLoaded', () => {
  const openDetailsById = (id) => {
    const element = document.getElementById(id);
    if (element?.tagName.toLowerCase() === 'details') {
      element.open = true;
    }
  };

  if (window.location.hash) {
    openDetailsById(window.location.hash.slice(1));
  }

  document.querySelectorAll('a[data-details-link]').forEach((link) => {
    link.addEventListener('click', () => {
      const id = link.getAttribute('href').slice(1);
      openDetailsById(id);
    });
  });
});