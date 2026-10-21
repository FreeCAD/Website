---
title: Introdução ao design
description: Introdução ao design no FreeCAD.
weight: 1
---

O FreeCAD é um software de projeto altamente modular e complexo, desenvolvido há mais de [20 anos](https://wiki.freecad.org/History) por colaboradores voluntários de todo o mundo. Devido a esse crescimento orgânico, as pessoas incorporaram suas próprias ideias e implementações sem seguir uma linguagem de design uniforme sobre como o aplicativo deveria se apresentar aos usuários e como seus muitos recursos deveriam fluir. Como resultado, o retorno dos usuários sobre estética e usabilidade costumava ser ruim, apesar de um conjunto robusto de recursos.

Este _Guia de Design_ tem como objetivo apresentar aos desenvolvedores/designers uma série de conceitos e diretrizes com os quais possam expandir, estender e melhorar o FreeCAD por meio de interações aprimoradas com o usuário e de consistência geral de aparência, estrutura e comportamento. Como tal, este deve ser considerado um documento vivo, que pode mudar para atender às necessidades de desenvolvedores, designers e usuários. Ele também pode ajudar quem escreve documentação a usar uma terminologia consistente.

Este guia é o produto de um Grupo de Trabalho de Design formado por membros da comunidade, garantindo que as decisões sobre a interface e a experiência do usuário sejam consistentes com as necessidades das pessoas que de fato usam o FreeCAD, tanto em ambientes profissionais quanto amadores. Este grupo de trabalho também participará da revisão das alterações do FreeCAD relacionadas à interface/experiência, para orientar desenvolvedores e mantenedores sobre os méritos e a consistência de recursos que possam afetar a interação e/ou os fluxos de trabalho.

_As palavras-chave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" e "OPTIONAL" neste documento devem ser interpretadas como descrito na [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt)._

### Como usar este guia:

Este guia está organizado em vários documentos, conforme descrito acima, para ajudar os desenvolvedores a encontrar conteúdo relevante sem excesso de informação. Quem está começando no FreeCAD e neste Guia de Design deve se familiarizar com os princípios e premissas usados como base para estas diretrizes antes de passar para conteúdos mais específicos. As demais seções estão organizadas em uma hierarquia lógica de conceitos e diretrizes, começando por assuntos mais conceituais e avançando para níveis maiores de detalhe.

### Premissas:

A interface é ajustada para uma resolução padrão de 1920 x 1080.

De acordo com a [_pesquisa mensal de hardware do Steam_](https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam), mais de 90% de todos os monitores de computador usam resolução de 1920x1080 ou superior. A interface do usuário do FreeCAD deve ser otimizada para essa resolução recomendada com escala de 100%. Esta será a "resolução de referência" no restante deste guia de design.

**Observação:** para elementos específicos do sistema operacional, o Windows é considerado o padrão devido à participação de mercado (70% em 2023). Todo esforço deve ser feito para manter uma aparência uniforme entre as plataformas.

**Observação:** desvios das diretrizes prescritivas deste documento de design exigem justificativa com argumentos sólidos e exigem uma revisão de design que confirme que tais desvios (um ou mais) são justificados e atendem às necessidades do usuário sem degradar a consistência geral da experiência do usuário.

### TODO

- Controles interativos (ainda em desenvolvimento)

- Cores e acessibilidade (ainda em desenvolvimento)

- Tema/estilo (ainda em desenvolvimento)

- Ícones/arte (ainda em desenvolvimento)