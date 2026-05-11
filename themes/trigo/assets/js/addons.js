/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Sort Addons script:
- Toggle Addons sorting order by Title, Date, and Downloads number.
*/


(() => {
  const container = document.querySelector(".cards");
  const buttons = document.querySelectorAll(".addons-sort button");

  if (!container || !buttons.length) return;

  const numericFields = new Set(["date", "downloads"]);

  const activeButton =
    [...buttons].find(pressed => pressed.getAttribute("aria-pressed") === "true")
    || buttons[0];

  let currentSort = {
    key: activeButton.dataset.sort,
    order: activeButton.dataset.order,
  };

  const getValue = (element, key) => {
    const value = element.dataset[key] ?? "";

    return numericFields.has(key)
      ? Number(value) || 0
      : value.toLowerCase();
  };

  const sortCards = ({ key, order }) => {
    const direction = order === "asc" ? 1 : -1;

    [...container.children]
      .sort((a, b) => {
        const A = getValue(a, key);
        const B = getValue(b, key);

        if (A < B) return -1 * direction;
        if (A > B) return 1 * direction;
        return 0;
      })
      .forEach(card => container.append(card));
  };

  const updateButtons = (activeKey, activeOrder) => {
    buttons.forEach(button => {
      const isActive = button.dataset.sort === activeKey;

      button.classList.toggle("active", isActive);
      button.setAttribute("aria-pressed", isActive);

      if (isActive) {
        button.dataset.order = activeOrder;
      }
    });
  };

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const key = button.dataset.sort;

      currentSort = {
        key,
        order:
          currentSort.key === key && currentSort.order === "asc"
            ? "desc"
            : "asc",
      };

      sortCards(currentSort);
      updateButtons(currentSort.key, currentSort.order);
    });
  });

  sortCards(currentSort);
  updateButtons(currentSort.key, currentSort.order);
})();