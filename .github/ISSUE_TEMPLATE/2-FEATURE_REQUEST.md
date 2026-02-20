---
name: "Feature request"
description: "Feature or improvement idea to help improve the website project."
title: "Feature: <short description>"
labels: Feature
assignees: ""
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this feature request! Please [search](https://github.com/freecad/website/issues) if a similar requested feature already exists. By submitting this issue, you accept the FreeCAD [Code of Conduct](https://github.com/FreeCAD/Website?tab=coc-ov-file#readme).

  - type: textarea
    id: description
    attributes:
      label: Feature description?
      description: Clear and concise description of the feature or improvement idea and how it impacts user experience, workflow or performance. Attach images or files by drag and dropping files in this area.
      placeholder: Describe the feature briefly.
    validations:
      required: true

  - type: textarea
    id: implementation
    attributes:
      label: Feature implemented?
      description: Provide basic info on how the feature can be implemented.
      placeholder: Describe the implementation briefly.
    validations:
      required: true