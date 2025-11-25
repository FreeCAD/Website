---
title: "♥︎ Donate"
description: "Sustain FreeCAD"
date: 2024-05-22T08:04:23+12:00
authors: FreeCAD
cover:
  image: 3.webp
  caption: "a cover caption"
  alt: "a cover alternative title"
menus:
  main:
    weight: 8
    params:
      style: button
  footer:
    weight: 8
params:
  currencies:
    - currencyCode: "EUR"
      currencySymbol: "€"
      selected: true
    - currencyCode: "USD"
      currencySymbol: "$"
  donateLabel: "Donate"
  onceLabel: "One-time"
  onceDefaultMessage: "Choose a <strong>one-time</strong> donation amount"
  onceChoiceMessage: "Make a <strong>one-time</strong> donation"
  onceErrorMessage: "Please choose a <strong>natural number</strong> amount"
  once:
    - amount: 25
    - amount: 50
      default: false
    - amount: 100
    - amount: 200
  monthlyLabel: "Monthly sponsor"
  monthlyDefaultMessage: "Choose a <strong>monthly sponsorship</strong> level"
  monthly:
    - amount: 5
      message: "Become a sponsor"
    - amount: 25
      message: "Become a <strong>Bronze</strong> sponsor"
      default: false
    - amount: 100
      message: "Become a <strong>Silver</strong> sponsor"
    - amount: 200
      message: "Become a <strong>Gold</strong> sponsor"
  corporateLabel: "Corporate"
  payment:
    - platform: "Paypal"
      weight: 0
      url: "https://www.paypal.com/donate/?hosted_button_id=M3Z8BGW6DB69Q"
    - platform: "Stripe"
      weight: 1
      url: "https://donate.stripe.com/14k3ei9TYgwFclq145"
    - platform: "GitHub"
      weight: 2
      url: "https://github.com/sponsors/FreeCAD"
    - platform: "OpenCollective"
      weight: 3
      url: "https://opencollective.com/freecad/donate"
    - platform: "SEPA"
      weight: 4
      info: "<strong>SEPA Bank transfer</strong><br><br><strong>Beneficiary:</strong> The FreeCAD Project Association<br><strong>IBAN:</strong> BE04 0019 2896 4531<br><strong>BIC/SWIFT:</strong> GEBABEBBXXX<br><strong>Bank agency:</strong> BNP Paribas Fortis<br><strong>Address:</strong> Rue de la Station 64, 1360 Perwez, Belgium"
  grantsLink: https://github.com/FreeCAD/FPA-grant-proposals/issues
  grantsTitle: Funded Grants Projects
---

### Donations Frequently Asked Questions

{{< details summary="Why donate to FreeCAD?" name="faq" >}}
Why donate to FreeCAD?
{{< /details >}}

{{< details summary="How to donate?" name="faq" >}}
How to donate?
{{< /details >}}

{{< details summary="Sponsorship Tiers" name="faq" id="tiers" >}}
Normal Sponsorship info.

Bronze Sponsorship info.

Silver Sponsorship info.

Gold Sponsorship info.
{{< /details >}}

{{< details summary="Corporate Sponsorship" name="faq" id="corporate" >}}
Corporate Sponsorship info.
{{< /details >}}

{{< details summary="Payment options" name="faq" >}}
Payment options info.
{{< /details >}}