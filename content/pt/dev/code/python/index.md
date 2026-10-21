---
title: Práticas de Python
description: Práticas de Python.
weight: 5
---

## Convenções de nomenclatura - PEP8

Usar convenções bem conhecidas facilita que outros desenvolvedores entendam seu código e o mantenham no futuro.

- [PEP 8 – Guia de estilo para código Python](https://peps.python.org/pep-0008/)

## Namespaces

Use namespaces adequados para evitar conflitos com pacotes existentes. É preferível colocar qualquer código do FreeCAD em um submódulo do namespace base `freecad`.

- [Documentação de módulos do Python](https://docs.python.org/3/tutorial/modules.html#packages)
- [Guia de pacotes de namespace do Python Packaging](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)

## Ferramentas

### Formatação de código e linting

- **Ruff**: (moderno e rápido)

  [Documentação do Ruff](https://docs.astral.sh/ruff/)

- **Black**

  [Documentação do Black](https://black.readthedocs.io/en/stable/)

  O repositório principal do FreeCAD usa `black` com `--linelength=100` no hook de pre-commit; portanto, se você estiver enviando código para o main, leve isso em conta.

### Gerenciamento de projetos

A ferramenta moderna para Python é o `uv`; ele substitui o `pip` e gerencia dependências, metadados do projeto, ambientes virtuais etc... e é 10x mais rápido que o pip.

[Documentação do uv](https://docs.astral.sh/uv/)

## Tipagem

As dicas de tipo tornam o código mais seguro e mais fácil de manter e refatorar.

- [resumo de tipagem](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

Existem muitos verificadores de tipo estáticos:

- [mypy](https://mypy-lang.org/) (talvez o mais comum)
- [pyright](https://github.com/microsoft/pyright) (Microsoft)
- [ty](https://github.com/astral-sh/ty) (novo e rápido)

## Versões do Python

As versões do Python atualmente suportadas no FreeCAD são 3.10+, mas alguns complementos podem não funcionar com as versões mais recentes do Python.
