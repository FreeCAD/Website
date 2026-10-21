---
title: Contributors, welcome!
linkTitle: ຍິນດີຕ້ອນຮັບ
description: ຕ້ອງການມີສ່ວນຮ່ວມກັບ FreeCAD ບໍ່? Start here.
weight: 1
icon: directions
welcome:
  - id: short
    label: I have 5 minutes to help
    children:
      - id: donate
        label: Make a donation
        url: donate
      - id: showcase
        label: Show your projects
        url: showcase
      - label: Spread the word
        url: events

  - id: medium
    label: I can spend a few hours
    children:
      - id: docs
        label: Write documentation and translate
        children:
          - id: writing
            label: Write tutorials and the user manual
            url: writing
          - id: localization
            label: Improve translations
            url: localization

      - id: bugs
        label: Report bugs and test new features
        children:
          - id: bug
            label: ລາຍງານບັກ
            url: https://github.com/FreeCAD/FreeCAD/issues
          - id: testing
            label: Provide feedback for new features
            url: https://github.com/FreeCAD/FreeCAD/pulls

      - id: ລະຫັດ
        label: Start coding
        children:
          - id: ການຕັ້ງຄ່າ
            label: Set up your development environment
            url: ການຕັ້ງຄ່າ
          - id: fix
            label: Browse first good issues to fix
            url: https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Good%20first%20issue%22

  - id: long
    label: I want to get deeply involved
    children:
      - id: design
        label: Design and UX
        url: design

      - id: ຊຸມຊົນ
        label: Community and onboarding
        children:
          - id: teams
            label: Join a team
            url: teams
          - id: web
            label: Help with the website
            url: web

      - id: tech
        label: Code and technical development
        children:
          - id: review
            label: Review pull requests
            url: review
          - id: ສ່ວນເສີມ
            label: Develop addons
            url: addon-academy
          - id: infra
            label: Help with infrastructure
            url: infra
  - id: ອື່ນໆ
    label: Not sure? Reach out to the community.
    url: ຊຸມຊົນ
---