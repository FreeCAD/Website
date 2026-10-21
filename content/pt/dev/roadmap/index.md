---
title: Roteiro
description: Objetivos para a direção do desenvolvimento do FreeCAD.
weight: 4
icon: mapa
---

Este documento descreve vários objetivos de alto nível para o projeto FreeCAD.  Em vez de ser uma longa lista de tarefas de desenvolvimento, ele se concentra em um pequeno conjunto de iniciativas estratégicas que, se alcançadas, aproximarão o FreeCAD de um estado futuro ideal.

Este roteiro descreve objetivos estratégicos amplos. As contribuições de código dos desenvolvedores sempre serão avaliadas pelos seus méritos, mas têm mais chances de receber atenção em tempo hábil e de ser integradas com sucesso se forem consistentes com os objetivos declarados neste roteiro.

## Justificativa do roteiro

As pessoas podem, _e provavelmente vão_, discutir sobre _qual_ estado futuro o FreeCAD deve buscar.  Para os fins deste documento, assumimos o seguinte:

1. Queremos que o FreeCAD tenha uma comunidade de desenvolvimento saudável, em que novos recursos sejam adicionados regularmente, bugs sejam resolvidos rapidamente e o desempenho seja mantido.
2. Queremos uma comunidade grande e diversa de pessoas usando o FreeCAD para fazer trabalho real, incluindo atividades comerciais, acadêmicas e de hobby.
3. Queremos que a base de código seja fácil de manter, compreensível e testável.
4. Queremos que a interface do usuário seja bonita, intuitiva e eficiente.
5. Queremos documentação de alta qualidade e relevante.
6. Queremos que o software seja bem projetado para suportar vários casos de uso, incluindo a operação por scripts.
7. Queremos uma API estável e bem projetada, que permita incluir o FreeCAD em outros fluxos de trabalho e ferramentas.

### Por que criar um roteiro?

As discussões técnicas muitas vezes se tornam polêmicas porque as decisões tomadas têm consequências reais.  Pessoas bem-intencionadas podem discordar porque têm prioridades ou objetivos diferentes.

Um roteiro bem elaborado é benéfico porque _primeiro_ se concentra nas prioridades e depois incentiva a tomada de decisões técnicas dentro desse contexto.

Um bom roteiro será útil para muitos tipos diferentes de pessoas:

1. Os desenvolvedores poderão decidir melhor quais recursos devem ser tratados primeiro e quais bugs vale a pena corrigir.
2. Os mantenedores podem priorizar a revisão de código e a integração dos PRs.
3. Novos colaboradores podem ter uma noção de onde e como seus esforços seriam mais úteis.
4. Colaboradores que não são desenvolvedores podem preparar documentação melhor, dar suporte aos usuários de forma mais eficaz e defender mudanças apropriadas.
5. A FPA pode alocar recursos para incentivar esforços-chave de desenvolvimento, planejar eventos e arrecadar fundos. Ela pode incentivar os patrocinadores de forma adequada e recusar patrocinadores com objetivos que não sejam consistentes com os objetivos do projeto.
6. Criadores de conteúdo podem montar currículos, preparar tutoriais e ajudar a ensinar os usuários sobre novos recursos.
7. A Ondsel e outros parceiros comerciais podem planejar suas ofertas de produtos com eficácia.
8. Mentores do GSoC e outros poderão definir projetos consistentes com a direção geral do projeto.
9. Outros projetos de código aberto podem identificar oportunidades de parceria e codesenvolvimento.

### Por que agora?

As versões do FreeCAD nunca seguiram uma rotina previsível.  Em vez disso, o lema não oficial do projeto, “Fica pronto quando estiver pronto”, ditou quando as versões oficiais eram preparadas.  Esse modelo serviu muito bem ao projeto por muitos anos, mas não sem controvérsias e consequências.

Nos últimos dois anos, muitas coisas mudaram no ecossistema do FreeCAD.

A comunidade de usuários cresceu drasticamente.  Ela se espalhou muito além do fórum e inclui muito mais usuários que não são desenvolvedores.

A FPA foi criada para proteger o projeto FreeCAD e incentivar seu crescimento.  A FPA começou a receber doações. Usar bem esses fundos está se tornando um desafio em si.

A Ondsel foi criada como uma empresa de benefício público open-core, construída em torno do projeto FreeCAD.  Como empresa comercial, ela tem forte necessidade de previsibilidade no processo de desenvolvimento e nos objetivos do projeto.

O interesse de usuários comerciais em implantar o FreeCAD em ambientes de produção está aumentando.

O FreeCAD está atingindo um nível de completude de recursos que sugere uma versão 1.0. A partir daí, a compatibilidade com versões anteriores e a estabilidade dos documentos se tornarão cada vez mais importantes.

Universidades, escolas técnicas e educadores on-line demonstraram interesse em ensinar o FreeCAD e oferecer alguma forma de certificação.

### Quem pode escrevê-lo/alterá-lo?

The roadmap is, in a sense, a living document.  It should be frequently reviewed and revised. The FPA is the steward of the document itself and takes the lead on drafting and revising its content, but it should reflect the will of the whole FreeCAD community.  The FPA actively seeks input from the community members and other stakeholders, partners and industry experts.

## The "Next" Release

These objectives described here are very broad. Some of them are very ambitious and will take a long time to achieve.  Others will never be fully achieved or 'done'.  For that reason, it's helpful to pick a specific set of goals to focus on for the next release.  [This page](next) broadly describes the major goals for the next release.

Releasing an official 1.0 release is a major milestone as well as a psychologically important event for the project. It is a signal to the world that FreeCAD is ready for production use, and that it is a mature, stable, and reliable tool for the job.

The criteria for when FreeCAD would be ready for 1.0 status has been debated for a long time. In general, the consensus has been that the software should be both feature complete and stable.  Feature completeness means that it has the major features a user would expect from a mature CAD application, not that it has ALL the features we desire or can imagine.

Stability means that the software does not crash routinely and that user models are not corrupted by normal use.  It does not mean that the software is bug free, or that it is perfect.  It does mean that the software is reliable enough to be used in production, and that it is not likely to cause data loss or other major problems.

At this time, we are setting four major goals to be completed for version 1.0.  When 1.0 is released, it will likely contain many more features and improvements than these four but we will not release 1.0 until these four are achieved.

- Mitigating the topological naming problem
- An integrated assembly workbench
- A unified Material system
- Improved initial user experience

### Topological Naming Problem

The toponaming problem has been widely discussed and work is proceeding to resolve it.

**Reference**:

- [original issue](https://github.com/freecad/freecad/issues/8432)
- [Github Project](https://github.com/orgs/freecad/projects/2)

### Assembly Workbench

Building multi-part assemblies is something users expect a modern CAD system to do.  FreeCAD has multiple add-on options but lacks an integrated Assembly workbench.  Version 1.0 will address this deficiency.  The integrated workbench delivered in 1.0 will be minimally viable.  It will provide the core functionality users need but will likely be less capable than the addon options currently available.  Goals for this release are modest and include

- An intuitive and user-friendly user interface
- An integrated solver to resolve assembly constraints
- A standard API for assemblies that external workbench authors can use to be compatible with both that workbench and each other.

**Reference**:

- [Ondsel Blog Series](https://ondsel.com/blog/default-assembly-workbench-1/)
- [Github Project](https://github.com/orgs/freecad/projects/7)

### Material System

The existing material capability is limited and does not meet the needs of many users.  Version 1.0 will start the process of improving the material system. A new material system will address needs in many different workbenches include FEM, Arch, Path, and Render.  Like the assembly workbench, goals for 1.0 are modest. We will provide minimum viable functionality with a solid foundation for future improvment.

**Reference**:

- [original issue](https://github.com/freecad/freecad/issues/10174)
- [Projeto no GitHub](https://github.com/orgs/freecad/projects/17)
- [Post no blog da Ondsel](https://ondsel.com/blog/freecad-needs-a-better-materials-system)
- [Tópico no fórum](https://forum.freecad.org/viewtopic.php?style=4&t=78242)

### Experiência inicial do usuário

O FreeCAD é frequentemente criticado por ser difícil de aprender.  Isso é compreensível, porque é um aplicativo complexo com muitos recursos.  No entanto, podemos fazer melhor, especialmente para usuários iniciantes que têm dificuldade para começar.

Os objetivos para a 1.0 são

- Um assistente de primeira execução
- Página inicial aprimorada
- Melhorias de UI / UX para aumentar a descoberta de recursos e a usabilidade.

**Reference**:

- [Projeto no GitHub para a limpeza de personalização e preferências](https://github.com/orgs/freecad/projects/1/views/1)
- [Projeto no GitHub para a estabilidade e modernização das barras de ferramentas](https://github.com/orgs/freecad/projects/15/views/1)
- [Projeto no GitHub para a limpeza do seletor de bancadas](https://github.com/orgs/freecad/projects/16/views/1)

## Objetivo: estabilidade dos modelos

Modelos robustos e estáveis são um pré-requisito necessário para a adoção ampla do FreeCAD.  Alguns tipos de quebra são o resultado inevitável de más práticas de projeto por parte do usuário, mas o FreeCAD deve se comprometer a reduzir ou eliminar o maior número possível de causas de quebra. As áreas de foco incluem:

1. Resolução e otimização da nomeação topológica
2. Redução dos erros do solucionador do Sketcher
3. Recursos de UI/UX que promovam melhores práticas de modelagem e evitem fragilidade:
   1. Facilitar as boas práticas
   2. Remover / substituir ferramentas que permitem resultados instáveis
4. Maior estabilidade em documentos vinculados

## Objetivo: montagem

A montagem é um recurso essencial dos sistemas CAD modernos.  Sem uma capacidade de montagem integrada, os usuários são obrigados a usar uma das várias opções de complementos.  Com alternativas concorrentes disponíveis, a colaboração e a interoperabilidade são prejudicadas.  A adoção de uma bancada de montagem deve considerar, no mínimo, um conjunto básico de recursos, incluindo

1. Um formato de dados de montagem.  Um padrão de dados para a representação das informações de montagem no documento do FreeCAD.  O padrão deve ser bem pensado e utilizável tanto pela solução integrada quanto pelas opções de complementos.
2. Um solucionador com licença compatível ou a opção de incluir um solucionador posteriormente
3. Um conjunto mínimo de recursos para atender a mais de 80% dos requisitos dos usuários típicos

## Objetivo: suavizar a curva de aprendizado

CAD é difícil.  São ferramentas complicadas e poderosas, e espera-se que o usuário invista o tempo adequado para aprender a usá-las bem.  No entanto, a inconsistência de UI/UX torna o processo de aprendizado mais difícil do que precisa ser.  A comunidade do FreeCAD deve adotar um programa de normalização da UI para facilitar o aprendizado do FreeCAD.

O primeiro passo nesse processo é parar de piorar as coisas aceitando contribuições de UI mal projetadas ou mal implementadas.  Áreas de foco:

1. Criação de um ‘guia de estilo’ de UI/UX.  Seria um guia para os desenvolvedores seguirem ao criar funcionalidades do núcleo e de complementos.  O guia de estilo também seria útil para avaliar novas contribuições que afetem a experiência do usuário.  Com o tempo, os padrões do guia de estilo podem ser usados para ‘pontuar’ as bancadas existentes e identificar oportunidades de melhoria.
2. Um assistente de ‘primeira execução’ para familiarizar o usuário com as personalizações e os recursos essenciais.
3. Reduzir elementos de UI confusos:
   1. Eliminar ferramentas redundantes
   2. Ocultar bancadas pouco usadas
   3. Consolidate settings, preferences, and other customization tools
   4. Make toolbar placement more predictable and stable
4. Toolbar placement consistency
5. Make tasks fail safe.  Tasks should always be in transactions and ‘undo’ cleanly. Red errors in the console are unacceptable for normal workflow.
6. Normalize the use of terminology both within FreeCAD and, when possible, with external standards.
7. Improve support for materials and implement consistently across all workbenches

## Objective:  Seamless Extensibility

FreeCAD has an addon manager to allow the user to add niche features.  This provides two important functions.  First, it allows the core application to remain leaner and avoid bloat. Second, it allows for competing solutions early on.  Our approach to addons, however, has been somewhat undisciplined.  As a result, the quality of addons is very uneven.  Some are excellent and behave like native parts of the application.  Others feel and behave inconsistently.  Still others are completely broken or unmaintained.  If we want the addon capability to serve both purposes, additional development is needed.  As áreas de foco incluem:

1. Improve the Addon Manager workbench to make it easier for users to find good well-maintained addons.  Maybe a ‘Featured’ section if addon workbench has a responsive maintainer, minimum open bugs.   Maybe a user review?  Without some status, we could end up with lots of cruft polluting the the manager.
2. Establish standards for addons to meet to achieve a ‘recommended’ or ‘featured’ status. Featured Addons should:
   1. Have an engaged maintainer
   2. Have minimal high priority open issues tickets
   3. Comply with published style book
   4. Support translation
   5. Support unit schema
   6. Install and function cleanly with only the addon manager.
3. Improve Scriptability:
   1. Improved editor / support external editor
   2. Native debugger
   3. Improved API

## Objective:  Have the best documentation possible

Documentation has become as important as the FreeCAD application itself. Good documentation can offer a bridge to new users and smooth the learning curve. It can make all the difference between an application that is hard to use and one that is easy to learn.

The FreeCAD documentation is generally in a very good state already. But it could, and should, go much further.  Focus areas include

1. Low-friction to revision through the browser
2. Git-trackable
3. Versions of the documentation that match software versions
4. Good translation support
5. Support for off-line readers
6. Natural integration of Developer / API documentation

## Objective: UI modernization and beautification

We want the FreeCAD application to be both efficient and attractive.  Queremos que ele se integre bem ao restante da experiência do desktop, seja responsivo e agradável de usar. As áreas de foco incluem:

1. Personalização pelo usuário:
   1. temas
2. Conceitos modernos de UI:
   1. Ex.: “menu circular”
   2. Menus de contexto
   3. Barra de faixa de opções
3. Uso eficiente da área da tela:
   1. Transparência
   2. Suporte a várias telas
4. Visualização aprimorada:
   1. Sombras
   2. Ray tracing e renderização simplificados

## Objetivo: fluxo de trabalho simplificado

Realizar tarefas comuns e repetitivas deve exigir o menor esforço possível.  Os desenvolvedores do FreeCAD devem se comprometer a construir fluxos de trabalho eficientes em todo o aplicativo.  Isso significa minimizar cliques e diálogos desnecessários.  Significa adicionar ferramentas dedicadas para funções rotineiras, em vez de depender de ferramentas genéricas que podem exigir mais etapas. Significa antecipar e dar ao usuário acesso eficiente às informações quando e onde ele precisar.  As áreas de foco incluem:

1. Ferramentas de medição melhores e consistentes
2. Melhorar o Sketcher :
   1. Ferramentas ausentes :
      1. Ferramenta de deslocamento.
      2. Padrão circular
      3. Matriz retangular utilizável.
      4. Restringir de acordo com o contexto.
3. Copiar e colar geometrias/esboços sem dificuldades
4. Modos de seleção uniformes
5. Abordagem uniforme para parâmetros do usuário
6. Acesso simplificado aos dados mais necessários
   1. Volume
   2. Massa
   3. Momento
   4. Centro de Gravidade
   5. Área de superfície
7. Ferramenta de alinhamento de texto

## Objetivo: reduzir as barreiras de entrada

O FreeCAD tem um número enorme de funções e, para um novo usuário, não há uma forma óbvia de usar apenas um subconjunto orientado a tarefas.  Deveria ser possível que novos usuários acessem um subconjunto das funcionalidades do FreeCAD, por exemplo no nível de um TinkerCAD.  À medida que ganham experiência, podem usar funções adicionais.

O FreeCAD tem um grande problema de terminologia para novos usuários.  Temos uma bancada Part que não cria Parts e uma bancada Part Design que não é usada para projetar Parts.  Temos Pads e Extrudes, Pockets e Cuts, Fuses e Unions etc.  Temos um contêiner Part e um contêiner Group(?) mas nenhuma função do núcleo para preencher um contêiner (ex.: uma função de montagem do núcleo)..

Comentário no fórum sobre nomenclatura: [https://forum.freecad.org/viewtopic.php?p=669869#p669869](https://forum.freecad.org/viewtopic.php?p=669869#p669869)

## Objetivo: evitar dar um tiro no próprio pé

O FreeCAD permite que os usuários façam coisas que sabidamente criam modelos frágeis, como construir elementos com base em fundações variáveis (ex.: esboços em faces, cotas baseadas em linhas de desenho).  Temos até ícones e comandos para fazer isso.  O FreeCAD deveria impedir ações "perigosas", convertê-las internamente em ações seguras ou, pelo menos, avisar sobre práticas inseguras.
