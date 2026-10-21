---
title: Design Principles
description: Design Principles and UI/UX conventions.
weight: 2
---

The following guiding principles are based on various established UI/UX conventions or _laws_.

- Estética - Não substitui um bom design, mas ajuda a compensar pequenas falhas. Uma estética ruim pode arruinar um fluxo funcional que de outra forma seria bem projetado.\
  ([_Efeito estética-usabilidade_](#aesthetic-usability-effect))

- Evite oferecer várias formas de atingir o mesmo objetivo dentro de uma única bancada. Oferecer métodos alternativos parece um benefício para o usuário, mas exige que ele processe/entenda por que existem dois métodos e como eles podem diferir.\
  "There should be one-- and preferably only one --obvious way to do it."\
  ([The Zen of Python](https://peps.python.org/pep-0020/#the-zen-of-python))

- Ao implementar uma funcionalidade comum a outras bancadas, o desenvolvedor deve fazer todo o esforço para garantir que o comportamento dessas funções permaneça consistente com as implementações existentes.

- Tente tornar as interações do usuário e as respostas do software o mais fluidas e rápidas possível. Idealmente abaixo de 400ms.\
  ([_Limiar de Doherty_](#doherty-threshold))

- Evite tornar os elementos interativos pequenos demais. O tamanho dos elementos deve ser grande o bastante para evitar a maioria dos 'cliques errados'.\
  ([_Lei de Fitts_](#fitts-law))

- A distância de deslocamento entre funções e elementos interativos relacionados deve ser minimizada para reduzir a ocorrência de erros.\
  ([_Lei de Fitts_](#fitts-law))

- Exponha por padrão apenas as configurações ou opções mais comuns/prováveis de que o usuário possa precisar. Controles avançados ou pouco usados devem ficar ocultos, mas facilmente acessíveis. Isso minimiza o tempo necessário para fazer escolhas e aumenta a eficiência.\
  ([_Lei de Hick-Hyman_](#hick-hyman-law))

- Minimize opções supérfluas em troca de padrões amplamente eficazes. As preferências avançadas devem ser acessíveis pelo editor de parâmetros, e não pela caixa de diálogo de preferências.\
  ([_Lei de Hick-Hyman_](#hick-hyman-law))

- Ao implementar recursos ou funções comumente encontrados em outros softwares, deve-se considerar a forma como eles funcionam. Desvios do '_comportamento razoavelmente esperado_' devem ser claramente justificados.\
  ([_Lei de Jakob_](#jakobs-law))

- O comportamento e o uso dos elementos em todo o aplicativo devem permanecer consistentes. Os desvios devem ser claramente justificados.\
  ([_Lei de Jakob_](#jakobs-law))

- Garanta que funções e opções sejam agrupadas logicamente, e não dispersas aleatoriamente.\
  ([_Lei da região comum_](#law-of-common-region))

- A organização adequada de funcionalidades semelhantes próximas umas das outras ajuda os usuários a entender e organizar melhor as informações.\
  Elementos/funções relacionados devem compartilhar simbologia visual semelhante\
  ([_Lei da proximidade_](#law-of-proximity) / [_Lei da conectividade uniforme_](#law-of-uniform-connectedness))

_Entenda que UI/UX está intimamente ligada à psicologia e às tendências humanas_

## Efeito estética-usabilidade

- Um design esteticamente agradável gera uma resposta positiva sobre a usabilidade e faz o design da UI parecer melhor, mesmo na ausência de quaisquer outras diferenças.

  - Este é um ganho fácil para a GUI do FreeCAD, pois os temas padrão apresentados podem ser cuidadosamente selecionados para um efeito visualmente agradável.

- Um design visualmente agradável mascara problemas de usabilidade e impede que eles sejam descobertos.

  - Embora isso seja um benefício do ponto de vista do usuário final, também pode ser um problema ao buscar o retorno dos usuários sobre problemas e soluções propostas.

  - Ao testar melhorias de design de UX, deve-se usar um tema/folha de estilos simplificado e neutro.

- As pessoas são mais tolerantes a problemas de usabilidade quando a estética do design é atraente

- "Durante um teste de usabilidade, uma usuária encontrou muitos problemas ao fazer compras no site da FitBit, desde pequenos incômodos no design de interação até falhas graves na navegação. Ela conseguiu concluir sua tarefa, mas com dificuldade. No entanto, em um questionário pós-tarefa, ela avaliou muito bem a facilidade de uso do site. _"São as cores que eles usaram",_ disse ela. _"Parece o oceano, é calmo. Fotografias muito boas."_ A resposta emocional positiva causada pelo apelo estético do site ajudou a mascarar seus problemas de usabilidade."\
  ([The Aesthetic-Usability Effect](https://www.nngroup.com/articles/aesthetic-usability-effect/))

- **Conclusão:** interfaces esteticamente agradáveis valem o investimento. Designs visuais que agradam aos usuários têm o efeito colateral de fazer o site parecer organizado, bem projetado e profissional. Os usuários tendem a querer experimentar um site visualmente atraente e são mais pacientes com pequenos problemas.

## Limiar de Doherty

- Resume-se a: as interações do usuário e o tempo de resposta do software atingem um estado psicológico 'viciante' quando a resposta é de aproximadamente 400ms ou um pouco menos.

- No caso do FreeCAD, parece ser menos relevante e é incrivelmente difícil de quantificar.

## Lei de Fitts

- O tempo para alcançar um alvo é função da distância até o alvo e do tamanho dele.

  - Quanto maior a distância até o alvo, mais tempo o ponteiro levará para chegar até ele. Em outras palavras, alvos mais próximos são alcançados mais rapidamente.

  - Quanto maior o alvo, menor o tempo de movimento até ele. Em outras palavras, alvos maiores são melhores.

- Complementa os conceitos do "Modelo de dois componentes"

  - Movimento inicial rápido e impreciso

  - Movimento final mais lento, para precisão

- **Takeaways**

  - Size matters, interactive/clickable elements should be large enough to reduce errors/miss-clicks.

  - Minimizing travel distance to relevant targets also reduces the incidence of errors.

## Goal-Gradient Effect

- This effect implies that giving users a sense of progress through visual indicators increases productivity.

- Seems to apply to linear task type applications and is not likely to be applicable to most work done in CAD.

## Hick-Hyman Law

- Hick's Law is a simple idea that says that the more choices you present your users with, the longer it will take them to reach a decision. It's common sense, but often neglected in the rush to cram too much functionality into a site or application.

- "The time it takes to make a decision increases with the number and complexity of choices."

- Minimize choices to decrease and simplify decision making and increase efficiency

- Reducing displayed options increases efficiency and keeps users engaged in their task.

- Avoid Overwhelming Users by highlighting recommended options

- Be careful not to simplify to the point of abstraction

- **Takeaway:** K.I.S.S. - Keep it Simple, Stupid

## Jakob's Law

- Effectively states users spend most of their time using other software (or websites/web apps) This means that users prefer to work within established conventions that they are already used to.

- Closely related to "The Power Law of Learning"

  - Repetition and consistency improve and reduce learning curves

- **Takeaways:**

  - Common functions found in most other software should work generally the same way new users can reasonably expect based on preexisting experiences.

  - Consistency in behavior and element location is paramount to good UI/UX design

  - When making major changes, minimize discontent by empowering users to continue using a familiar version for a limited time.

## Law of Common Region

- UI elements tend to be perceived into groups if they are sharing an area with a clearly defined boundary

- Humans naturally perceive objects as organized patterns.

- Gestalt laws organize based on the following categories:

  - Proximity

  - Similarity

  - Continuidade

  - Closure

  - Connectedness

## Law of Proximity

- Proximity helps to establish a relationship with nearby objects.

- Elements in close proximity are perceived to share similar functionality or traits.

- Proximity helps users understand and organize information faster and more efficiently.

## Law of Pragnanz

- The human eye likes to find simplicity and order in complex shapes because it prevents us from becoming overwhelmed with information.

- Research confirms that people are better able to visually process and remember simple figures than complex figures.

- The human eye simplifies complex shapes by transforming them into a single, unified shape.

- **Takeaway:** Icons should be reviewed with this principle in mind.

## Law of Similarity

- Elements that are visually similar will be perceived as related

- Color, shape, size, orientation and movement can signal that elements belong to the same group and likely share a common meaning or functionality.

- Ensure that links and navigation systems are visually differentiated from normal text elements.

## Law of Uniform Connectedness

- Elements that are visually connected are perceived as more related than elements with no connection

  - Group functions of a similar nature so they are visually connected via colors, lines, frames or other shapes.

  - Use uniform connectedness to show context or to emphasize the relationship between similar items.

  - Use tangible connecting reference (line, arrow, etc) from one element to the next to also create a visual connection

## Lei de Miller

- A pessoa média só consegue manter 7 (+/- 2) itens na memória de trabalho

- Conclusões

  - Não imponha limitações de design desnecessárias só para atingir '7'

  - Organize o conteúdo em blocos menores para ajudar os usuários a processar, entender e memorizar com mais facilidade.

  - A capacidade da memória de curto prazo varia de pessoa para pessoa, com base no conhecimento prévio e na compreensão do contexto

## Navalha de Occam

- Entre hipóteses concorrentes que preveem igualmente bem, deve-se escolher a que tem menos premissas

- **Takeaways:**

  - O melhor método para reduzir a complexidade é evitá-la desde o início

  - Considere algo concluído apenas quando nenhum item adicional puder ser removido

  - Analise cada elemento e remova o máximo possível, sem comprometer a função geral

## Princípio de Pareto

- Para muitos eventos, aproximadamente 80% dos efeitos vêm de 20% das causas.

- Conclusões:

  - Entradas e saídas geralmente não são distribuídas de forma uniforme

  - Um grupo grande pode conter apenas poucos contribuintes significativos para o resultado desejado

  - Concentre a maior parte do esforço nas áreas que trarão os maiores benefícios para a maioria dos usuários.

## Lei de Parkinson

- Toda tarefa se expande até ocupar todo o tempo disponível

- **Takeaways:**

  - Limite o tempo para concluir uma tarefa ao que os usuários poderiam razoavelmente esperar.

  - Reduzir a duração real de uma tarefa em relação à duração esperada melhora a experiência geral do usuário

  - Aproveitar recursos como o preenchimento automático para poupar tempo do usuário permite concluir tarefas rapidamente

## Regra do pico-final

- As pessoas julgam uma experiência em grande parte com base em como se sentiram no seu ponto mais intenso e no seu final, e não pela soma total ou média de cada momento da experiência.

- **Takeaways:**

  - Preste atenção aos pontos mais intensos e aos momentos finais da 'jornada' do usuário

  - Identifique os momentos em que seu produto é mais útil, valioso ou divertido e projete para encantar o usuário final.

  - Lembre-se de que os usuários se lembram das experiências negativas com mais nitidez do que das positivas

## Recursos adicionais:

[Laws of UX](https://lawsofux.com)

[Nielsen Norman Group](https://nngroup.com)

[As 10 heurísticas de UI de Jakob Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/)
