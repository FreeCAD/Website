---
name: "Bug report"
description: "Report a problem to help improve the website project."
title: "Bug: <short description>"
labels: Bug
assignees: ""
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report! Please [search](https://github.com/freecad/website/issues) if a similar reported bug already exists. By submitting this issue, you accept the FreeCAD [Code of Conduct](https://github.com/FreeCAD/Website?tab=coc-ov-file#readme).

  - type: textarea
    id: description
    attributes:
      label: Bug description?
      description: Clear and concise description of the problem and how it impacts user experience, workflow or performance. Attach images or files by drag and dropping files in this area.
      placeholder: Describe the problem briefly.
    validations:
      required: true

  - type: dropdown
    id: dir
    attributes:
      label: Page collection affected?
      options:
        - Homepage
        - Features
        - Download
        - News
        - Community
        - Documentation
        - Donate
        - Others
    validations:
      required: true

  - type: textarea
    id: reproduce
    attributes:
      label: Steps to reproduce?
      description: Provide a recipe to help reliably reproduce the issue.
      placeholder: |
        Steps to reproduce the behavior:
        1. Go to ...
        2. Click on ...
    validations:
      required: true

  - type: textarea
    id: system
    attributes:
      label: System affected?
      description: Provide basic info on the system affected by the issue.
      placeholder: |
        - Device: e.g. Desktop, Tablet, Smartphone
        - Viewport size: e.g. 1920x1080px, 360x800px
        - Operating system: e.g. Android 16, iOS 26
        - Browser: e.g. Chrome 145.0, Firefox 147.0
        - Hugo Version: e.g. 0.156.0 if applicable
    validations:
      required: true