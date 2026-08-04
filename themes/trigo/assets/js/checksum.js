/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Copy checksum to clipboard button for download buttons:
- Add class for subtle interaction styling.
*/


document.querySelectorAll(".checksum-button").forEach(button => {
  button.addEventListener("click", async event => {
    event.preventDefault();

    try {
      await navigator.clipboard.writeText(button.dataset.sha256);
      button.classList.add("copied");

      setTimeout(() => {
        button.classList.remove("copied");
      }, 1500);
    } catch (error) {
      console.warn("Failed to copy checksum:", error);
    }
  });
});