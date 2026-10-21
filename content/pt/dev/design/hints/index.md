---
title: Dicas de entrada
description: Input Hints Guidelines.
weight: 8
---

Input Hints is feature that provides user with hints for available actions as part of the status bar.

![Input Hints Preview](input-hints-preview.webp)

Technically the hint consists of the displayed message with placeholders (`%1`, `%2`, ...)
corresponding to each key sequence, and key sequences. One hint can contain one sequence (`[M]
change mode`) or multiple ones (`[U]/[J] increase / decrease number of sides`). Cada sequência pode
consistir em uma ou mais teclas (por exemplo `[shift][M]`). Os marcadores podem ser colocados em qualquer lugar da
mensagem de dica; no entanto, as dicas devem seguir a convenção `[tecla] ação`. As teclas disponíveis são definidas
no enum `Gui::InputHint::UserInput`.

As mensagens de dicas devem respeitar estas regras:

1. Comece com a entrada, depois letra minúscula; a dica não é uma frase, por exemplo `%1 pick radius`.

2. Mantenha as dicas o mais curtas possível, evite redundância se o contexto for claro, por exemplo `%1 pick arc center`
   em vez de `1% pick center of an arc`.

3. Comece apenas com os modificadores (`ctrl`, `alt`, `shift` etc.) se eles afetarem outras entradas; depois as entradas do mouse e, por fim, as teclas normais.

4. Idealmente, dentro dos grupos, as dicas devem ser ordenadas pela frequência de uso (as ações mais comuns devem vir
   primeiro).

5. Tente ser específico: em vez de `change mode`, tente criar uma dica dinâmica com o nome do
   próximo modo.

6. Se as ações forem semelhantes, mas diferirem em detalhes menores, elas podem ser combinadas, por exemplo `%1 / %2 decrease
   / increase side`, `%1, %2 or %3 constrain axis`.

7. Lembre-se de usar a função de tradução!

8. Devido ao espaço limitado, tente manter a lista de ações curta, idealmente com no máximo 6
   dicas. Concentre-se nas ações mais comuns e importantes.

9. Evite adicionar dicas desnecessárias; por exemplo, não mostre comandos de navegação como dicas quando houver ferramentas
   ativas e não mostre dicas que no momento não são possíveis devido a outras ações.

10. Se as dicas mudarem dinamicamente, mantenha as dicas comuns entre os estados da ferramenta usada. Se uma determinada ação
    for removida, isso é um forte indício de que ela não está mais disponível.
