---
title: Code Formatting Guidelines
description: Guidelines for code formatting in C++ and Python.
weight: 3
---

FreeCAD is written primarily in C++ and Python (with a few files in other languages such as CMake). To smooth the process of merging new contributions it is desirable to minimize formatting changes to existing code, and to use a uniform code formatting style when writing new code. Eventually we expect to standardize the codebase on specific coding styles using Clang Format for C++ and a Python code-formatter (such as Black), but that is a work-in-progress and _should not_ be applied to existing otherwise-untouched code.

## Direitos autorais

Every file in the FreeCAD project should contain [SPDX Annotations][copyright] if possible.

C++ and Python source files are currently also required to have [Copyright Headers][copyright].

## Setting up pre-commit

For the sections of the code that have already been auto-formatted, we use [git pre-commit hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) to enforce that formatting. We use the [pre-commit](https://pre-commit.com/) framework to install and manage our hooks. All developers should install pre-commit following the [instructions here](https://freecad.github.io/DevelopersHandbook/gettingstarted/). When making a new commit, the hooks examine your changed files and ensure that they follow the appropriate formatting for the section of code you are working on. You do not need to manually yourself with your code's formatting as you develop, and may code it as you like (or as your IDE likes...). The hook will ensure that your finished code conforms to project requirements.

Not all of FreeCAD currently uses these hooks: it is up to the Maintainers in charge of a particular Workbench or subdirectory to work with their development team to migrate their code's formatting to the automated tools, and to then enable the hooks on their subdirectory.

Currently the following sections of code are covered by pre-commit: `src/Mod/AddonManager`, `src/Tools`, and `tests/src`.

## C++

FreeCAD's codebase currently includes a [.clang-format](https://github.com/FreeCAD/FreeCAD/blob/master/.clang-format) file. Many IDEs will automatically apply these settings when editing files. To minimize disruption of other developers, only new or significantly-refactored code should have the formatting automatically applied. Code not being worked on should not be automatically formatted at this time.

For naming conventions, please see [Naming Things](../review#naming-things).

## Python

Não há um estilo unificado de código Python acordado para a base de código do FreeCAD: atualmente cada módulo tem seu próprio estilo. Desenvolvedores que trabalham em um módulo existente devem formatar seu código no estilo predominante do módulo em que estão trabalhando.

## Documentação embutida

Você encontrará na base de código uma mistura de diferentes gerações de sistemas de documentação embutida baseados em comentários, dependendo de quando o código foi escrito.  Desde 2024, é preferível escrever documentação em comentários compatível com o [doxygen](https://www.doxygen.nl/manual/docblocks.html).  Para métodos, é altamente recomendável incluir @param e @return conforme apropriado.

[copyright]: ../copyright