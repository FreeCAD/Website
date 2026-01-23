(() => {
  const container = document.querySelector(".cards");
  if (!container) return;

  const buttons = Array.from(document.querySelectorAll(".catalog-sort button"));
  if (!buttons.length) return;

  const activeButton =
    [...buttons].find(pressed => pressed.getAttribute("aria-pressed") === "true")
    || buttons[0];

  let currentSort = {
    key: activeButton.dataset.sort,
    order: activeButton.dataset.order,
  };

  const numericKeys = new Set(["date", "downloads"]);

  const compare = (a, b, key, order) => {
    let A = a.dataset[key] ?? "";
    let B = b.dataset[key] ?? "";

    // Numbers (date and downloads)
    if (numericKeys.has(key)) {
      A = Number(A) || 0;
      B = Number(B) || 0;
      return order === "asc" ? A - B : B - A;
    }

    // Strings (titles)
    if (A === B) return 0;
    return order === "asc"
      ? (A < B ? -1 : 1)
      : (A > B ? -1 : 1);
  };

  const sortCards = (key, order) => {
    const cards = [...container.children];
    cards.sort((a, b) => compare(a, b, key, order));
    cards.forEach(card => container.appendChild(card));
  };

  const updateButtons = (active, order) => {
    buttons.forEach(button => {
      button.classList.remove("active");
      button.setAttribute("aria-pressed", "false");
    });

    active.classList.add("active");
    active.setAttribute("aria-pressed", "true");
    active.dataset.order = order;
  };

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const key = button.dataset.sort;
      let order = button.dataset.order;

      if (currentSort.key === key) {
        order = order === "asc" ? "desc" : "asc";
      }

      currentSort = { key, order };
      button.dataset.order = order;
      sortCards(key, order);
      updateButtons(button, order);
    });
  });

  sortCards(currentSort.key, currentSort.order);
  updateButtons(activeButton, currentSort.order);
})();