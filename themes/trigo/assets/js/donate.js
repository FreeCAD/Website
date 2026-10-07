document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('donation-form');

  if (!form) return;

  const custom = form.querySelector('#custom-input');
  const currency = form.querySelector('#currency-toggle');
  const symbols = form.querySelectorAll('.currency-symbol');
  const types = form.querySelectorAll('#donation-type input');
  const tiers = form.querySelectorAll('.tiers input[type="radio"]');

  if (!custom) return;

  const getAmount = () => {
    if (!custom.value || !custom.checkValidity()) return null;

    const amount = Number(custom.value);

    return Number.isSafeInteger(amount) ? amount : null;
  };

  const updateTiers = () => {
    const amount = getAmount();
    const valid = amount !== null;
    const isMonthly = form.querySelector('#monthly:checked') !== null;
    const active = isMonthly ? '.tiers.monthly input[type="radio"]' : '.tiers.once input[type="radio"]';

    form.classList.toggle('custom-valid', valid);

    form.querySelectorAll(active).forEach(input => {
      const min = Number(input.dataset.min);
      const max = Number(input.dataset.max);
      const selected = valid && (isMonthly ? amount >= min && amount <= max : amount === min);

      input.checked = selected;
      input.closest('label')?.classList.toggle('selected', selected);
    });
  };

  tiers.forEach(input => {
    input.addEventListener('change', () => {
      custom.value = input.value;
      updateTiers();
    });
  });

  custom.addEventListener('input', updateTiers);

  types.forEach(input => {
    input.addEventListener('change', () => {
      tiers.forEach(tier => {
        tier.checked = false;
        tier.closest('label')?.classList.remove('selected');
      });

      custom.value = '';
      updateTiers();
    });
  });

  form.addEventListener('submit', event => {
    const amount = getAmount();
    const button = event.submitter;
    const parameter = button?.dataset.amountParam;

    if (!amount || !parameter) return;

    const url = new URL(button.formAction, location.href);
    url.searchParams.set(parameter, amount);
    button.formAction = url;
  });

  currency?.addEventListener('change', () => {
    const symbol = currency.selectedOptions[0]?.dataset.symbol;

    if (!symbol) return;

    symbols.forEach(element => {
      element.textContent = symbol;
    });
  });

  updateTiers();
});
