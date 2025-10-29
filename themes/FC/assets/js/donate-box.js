document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("donation-form");
  const customInput = document.getElementById("custom-amount");
  const currencySelect = document.getElementById("currency-toggle");
  const donateButton = document.getElementById("donate-checkbox");
  const customLabel = form.querySelector('label[for="custom-amount"]');

  const tierGroups = {
    "once": document.querySelector(".tiers.once"),
    "monthly": document.querySelector(".tiers.monthly")
  };

  const getType = () =>
    form.querySelector('input[name="donation-type"]:checked')?.value || "once";

  const getTier = () =>
    tierGroups[getType()].querySelector('input[name="amount"]:checked');

  const getAmount = () => {
    const tier = getTier();
    if (tier) return Number(tier.value);

    if (getType() === "once") {
      const val = customInput.value.trim();
      const amount = Number(val);
      if (val && Number.isInteger(amount) && amount >= 1) return amount;
    }

    return null;
  };

  const updateDonateButton = () => {
    const isOnce = getType() === "once";
    const isValid = customInput.checkValidity();
    const hasValidAmount = getAmount() !== null;

    donateButton.disabled = (isOnce && !isValid) || !hasValidAmount;
  };

  const handleTierChange = () => {
    if (getType() === "once") {
      const selected = getTier();
      customInput.value = selected ? selected.value : "";
      customInput.focus();
      document.getElementById("custom-amount-box").classList.remove("active");
    }
    updateDonateButton();
  };

  const syncCustomToTier = () => {
    if (getType() !== "once") return false;

    const val = Number(customInput.value.trim());
    const tiers = tierGroups["once"].querySelectorAll('input[name="amount"]');

    let matched = false;

    Array.from(tiers).forEach(radio => {
      const tierValue = Number(radio.value);
      const isMatch = Number.isInteger(val) && val === tierValue;
      radio.checked = isMatch;
      if (isMatch) matched = true;
    });

    updateDonateButton();

    return !matched;
  };

  const handleCustomChange = () => {
    const isCustom = syncCustomToTier();
    document.getElementById("custom-amount-box").classList.toggle("active", isCustom);
    updateDonateButton();
  };

  const updateCurrency = () => {
    const symbol = currencySelect.value === "USD" ? "$" : "€";
    Object.values(tierGroups).forEach(group => {
      group.querySelectorAll("label").forEach(label => {
        label.textContent = label.textContent.replace(/^[€$]/, symbol);
      })
    });
    customLabel.textContent = symbol;
  };

  const handleTypeChange = () => {
    const newType = getType()
    const previousType = newType === "once" ? "monthly" : "once";
    const previousAmount = tierGroups[previousType].querySelector('input[name="amount"]:checked')?.value;

    // Reset amount selection
    form.querySelectorAll('input[name="amount"]').forEach(radio => (radio.checked = false));

    // Match tier in new selected donation type
    const match = previousAmount && tierGroups[newType].querySelector(`input[value="${previousAmount}"]`);
    const fallback = tierGroups[newType].querySelector('input[name="amount"][checked]');
    (match || fallback)?.click();

    // Sync or reset custom amount
    if (newType === "once") {
      const tier = getTier();
      customInput.value = tier ? tier.value : "";
      syncCustomToTier();
    } else {
      customInput.value = "";
    }

    // Reset donate checkbox
    donateButton.checked = false;

    updateCurrency();
    updateDonateButton();
  };

  // Function to build URLs for each platform
  const setPaymentUrl = (button, platform, type, amount, currency) => {
    let url = button.getAttribute("formaction");

    if (!url || !amount || !currency || !type) {
      console.error("Missing required parameters for payment platform URL.");
      return null;
    }

    const encodedAmount = encodeURIComponent(amount);
    const encodedCurrency = encodeURIComponent(currency);
    const encodedType = encodeURIComponent(type);

    switch (platform.toLowerCase()) {
      case "stripe":
        url += ``;
        break;

      case "opencollective":
        url += `?interval=${encodedType}&amount=${encodedAmount}`;
        break;

      case "github":
        let githubType = type === "once" ? "one-time" : type;
        url += `?frequency=${encodeURIComponent(githubType)}&amount=${encodedAmount}`;
        break;

      case "paypal":
        url += ``;
        break;

      default:
        console.warn(`No specific URL found for payment platform: ${platform}`);
        break;
    }

    return url;
  };

  // Intercept payment button clicks
  form.querySelectorAll('#donation-payment button[type="submit"]').forEach(button => {
    button.addEventListener("click", e => {
      if (!window.hasOwnProperty("fetch")) {
        return;
      }

      e.preventDefault();

      if (!donateButton.checked) {
        alert("Please check 'Donate' to proceed.");
        return;
      }

      const type = getType();
      const amount = getAmount();
      const currency = currencySelect.value;
      const platform = button.id.replace(/^payment-/, '');

      const url = setPaymentUrl(button, platform, type, amount, currency);
      if (!url) return;

      window.open(url, "_blank");
    });
  });

  // Event Listeners
  customInput.addEventListener("input", handleCustomChange);
  customInput.addEventListener("change", handleCustomChange);

  currencySelect.addEventListener("change", () => {
    updateCurrency();
    updateDonateButton();
  });

  form.querySelectorAll('input[name="donation-type"]').forEach(input => {
    input.addEventListener("change", () => {
      handleTypeChange();
    });
  });

  form.querySelectorAll('input[name="amount"]').forEach(radio => {
    radio.addEventListener("change", () => {
      handleTierChange();
    });
  });

  // Init on load
  handleTypeChange();
  updateCurrency();
  updateDonateButton();
});
