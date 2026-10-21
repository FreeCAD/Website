---
title: Direitos autorais
description: Direitos autorais.
weight: 6
---

## Anotações SPDX

As anotações SPDX declaram metadados sobre o arquivo em que são colocadas, como a licença do conteúdo nele contido, os detentores dos direitos autorais ou a origem do conteúdo.

Em geral, todo arquivo cujo formato permita adicionar comentários deve conter anotações SPDX.

### Posicionamento

As anotações SPDX devem ser colocadas em comentários de linha no topo do arquivo.

```C++
// SPDX-License-Identifier: LGPL-2.1-or-later
```

Alguns formatos ou conteúdos de arquivo podem impedir isso; por exemplo, declarações shebang podem já ocupar a primeira linha de um arquivo de script. Nesse caso, basta adicionar as anotações nas linhas seguintes.

```sh
#!/usr/bin/env bash
# SPDX-License-Identifier: LGPL-2.1-or-later
```

### Licença

Para declarar sob qual licença um arquivo está, especifique o [License Id] apropriado da seguinte forma:

```
SPDX-License-Identifier: ‹Id da licença›
```

#### C++

```C++
// SPDX-License-Identifier: ‹Id da licença›
```

#### Python

```Python
# SPDX-License-Identifier: ‹Id da licença›
```

### Direitos autorais

Para declarar quem detém os direitos autorais de um arquivo, adicione uma anotação para cada pessoa / organização:

```
SPDX-FileCopyrightText: ‹Ano› ‹Entidade›
```

`‹Ano›` é o ano em que o código foi publicado.

`‹Entidade›` é uma pessoa ou uma organização.

#### Pessoa

```
SPDX-FileCopyrightText: 1999 Robert Robertson
```

#### Organização

```
SPDX-FileCopyrightText: 2000 Crazy CAD Technologies
```

### Exemplos

#### 1. Arquivo-fonte C++ interno

Você acabou de escrever um novo arquivo `.cpp` do zero e quer licenciá-lo sob a licença padrão usada pelo FreeCAD ( `LGPL-2.1-or-later` )

```c++
// SPDX-License-Identifier: LGPL-2.1-or-later
// SPDX-FileCopyrightText: 2026 Mike Mc Mickers
// SPDX-FileNotice: Part of the FreeCAD project.

...
```

#### 2. Arquivo-fonte C++ externo

Você quer incluir algum código preexistente licenciado sob uma licença compatível, mas diferente da que o FreeCAD usa por padrão.

```c++
// SPDX-License-Identifier: MIT
// SPDX-FileCopyrightText: 1939 The Wizard of Oz
// SPDX-FileNotice: Part of the FreeCAD project.

...
```

#### 3. Licenciamento misto em Python

Você tem algum código existente licenciado sob uma licença, mas também quer adicionar código sob uma licença diferente.

```Python
# SPDX-License-Identifier: LGPL-2.1-or-later AND MIT
# SPDX-FileCopyrightText: 2010 Technology Inc
# SPDX-FileCopyrightText: 2026 Jane Jay Jensen
# SPDX-FileNotice: Part of the FreeCAD project.

...
```

#### 4. Script Python executável

Você tem um script Python com uma declaração shebang.

```Python
#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: 2011 Nyan Cat
# SPDX-FileNotice: Part of the FreeCAD project.

...
```

### Ícones

Os ícones devem ter a licença que o autor pretendeu, por exemplo `CC-BY-SA-4.0`.

Em arquivos `svg`, isso é declarado por metadados, não como um comentário SPDX.

### Documentação

Além da wiki, atualmente não licenciamos a documentação; no entanto, você pode considerar colocá-la sob a `Unlicense` ou a `CC-BY-SA-4.0`.

## Cabeçalhos de direitos autorais

Os cabeçalhos de direitos autorais são um artefato de softwares antigos; atualmente ainda são mantidos nos arquivos existentes que os têm e são adicionados a novos arquivos-fonte `C++` & `Python`.

### Condições

Cabeçalhos de direitos autorais devem ser adicionados a novos arquivos se **TODAS** as condições a seguir se aplicarem:

1. O arquivo é código-fonte `C++` ou `Python`.

2. O arquivo é código totalmente original.

3. O código foi escrito para o projeto FreeCAD.

4. O código é licenciado sob `LGPL-2.1-or-later`.

### Declarações

As declarações de direitos autorais devem ser feitas por meio de anotações SPDX.

### Texto da licença

```
FreeCAD is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 2.1
of the License, or (at your option) any later version.

FreeCAD is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with FreeCAD. If not, see https://www.gnu.org/licenses
```

## Trechos de direitos autorais

Abaixo você encontra alguns trechos das anotações SPDX / cabeçalhos de direitos autorais mais usados.

### C++

```C++
// SPDX-License-Identifier: LGPL-2.1-or-later
// SPDX-FileCopyrightText: ‹Ano› ‹Entidade›
// SPDX-FileNotice: Part of the FreeCAD project.

/******************************************************************************
 *                                                                            *
 *   FreeCAD is free software: you can redistribute it and/or modify          *
 *   it under the terms of the GNU Lesser General Public License as           *
 *   published by the Free Software Foundation, either version 2.1            *
 *   of the License, or (at your option) any later version.                   *
 *                                                                            *
 *   FreeCAD is distributed in the hope that it will be useful,               *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty              *
 *   of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  *
 *   See the GNU Lesser General Public License for more details.              *
 *                                                                            *
 *   You should have received a copy of the GNU Lesser General Public         *
 *   License along with FreeCAD. If not, see https://www.gnu.org/licenses     *
 *                                                                            *
 ******************************************************************************/
```

### Python

```Python
# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: ‹Ano› ‹Entidade›
# SPDX-FileNotice: Part of the FreeCAD project.

################################################################################
#                                                                              #
#   FreeCAD is free software: you can redistribute it and/or modify            #
#   it under the terms of the GNU Lesser General Public License as             #
#   published by the Free Software Foundation, either version 2.1              #
#   of the License, or (at your option) any later version.                     #
#                                                                              #
#   FreeCAD is distributed in the hope that it will be useful,                 #
#   but WITHOUT ANY WARRANTY; without even the implied warranty                #
#   of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    #
#   See the GNU Lesser General Public License for more details.                #
#                                                                              #
#   You should have received a copy of the GNU Lesser General Public           #
#   License along with FreeCAD. If not, see https://www.gnu.org/licenses       #
#                                                                              #
################################################################################
```

### Outros

_Lembrete: outros tipos de arquivo exigem apenas anotações SPDX, não cabeçalhos de direitos autorais._

```C++
// SPDX-License-Identifier: LGPL-2.1-or-later
// SPDX-FileCopyrightText: ‹Ano› ‹Entidade›
// SPDX-FileNotice: Part of the FreeCAD project.
```

---

```Python
# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: ‹Ano› ‹Entidade›
# SPDX-FileNotice: Part of the FreeCAD project.
```

---

```CSS
/* SPDX-License-Identifier: LGPL-2.1-or-later */
/* SPDX-FileCopyrightText: ‹Ano› ‹Entidade› */
/* SPDX-FileNotice: Part of the FreeCAD project. */
```

---

```Bat
@REM SPDX-License-Identifier: LGPL-2.1-or-later
@REM SPDX-FileCopyrightText: ‹Ano› ‹Entidade›
@REM SPDX-FileNotice: Part of the FreeCAD project.
```

[License Id]: https://spdx.org/licenses/
