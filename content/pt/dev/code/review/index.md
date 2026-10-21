---
title: Guia de revisão de código
description: Guia de revisão de código.
weight: 2
---

Este documento visa fornecer um conjunto de boas práticas que devem ser úteis tanto para desenvolvedores quanto para revisores de código. Elas devem ser tratadas como receitas culinárias: você pode brincar com elas e alterá-las, mas toda mudança deve ser pensada e intencional.

Assim como as práticas de C++, este documento é **muito** inspirado nas [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines).
Você sempre pode consultá-las para aprender mais coisas úteis.

Embora os pontos deste guia possam não ser seguidos de forma consistente em toda a base de código existente, é possível verificar se o código novo os segue, e a longo prazo isso deve nos ajudar imensamente.

> [!NOTE]
> Lembre-se de que a revisão de código é uma discussão colaborativa. Não hesite em pedir esclarecimentos ou ajuda quando necessário. Revisores também podem errar; o objetivo é trabalhar juntos para refinar o código até que todos fiquem satisfeitos.

Neste documento, o texto em **negrito** indicará a importância de cada sugestão.

- **deve** será usado para coisas fundamentais, que não devem gerar controvérsia e que você realmente precisa seguir
- **deveria** será usado para detalhes importantes que se aplicam à grande maioria dos casos; no entanto, pode haver motivos válidos para ignorá-los dependendo do contexto
- **poderia**/**pode** será usado para boas práticas, coisas que você deveria tentar seguir, mas não segui-las não é um erro em si

## Regras comuns

1. A consistência **deve** ser preferida em vez de seguir regras estritamente. Se, por exemplo, em um determinado contexto o código usa um esquema de nomenclatura diferente, ele deve ser seguido em vez do descrito neste documento.
2. O objetivo da revisão de código **não é** encontrar erros no código, mas garantir a qualidade do código.
3. Não há revisores dedicados: todos **podem** ajudar nesse esforço!
4. Os revisores **deveriam** comentar principalmente o código adicionado e discutir o código existente apenas se alterá-lo ajudar o novo trecho.
5. **Poderiam** ser feitos comentários sobre o código existente apenas para observar que outras soluções (potencialmente melhores) estão disponíveis e deveriam ser usadas ao escrever código novo.
6. O revisor **pode** sugerir mais alterações no código existente para melhorar a solução proposta (por exemplo, refatorar outra classe para que possa ser usada).
7. O código **deve** seguir a Regra do Escoteiro - https://biratkirat.medium.com/step-8-the-boy-scout-rule-robert-c-martin-uncle-bob-9ac839778385 - ou seja, deixar o código em melhor estado do que o encontrou.
8. Se possível, a limpeza de código feita durante o trabalho no recurso deveria ser separada em commits distintos ou, melhor ainda, em um PR separado.
9. PRs **não devem** conter restos de código de desenvolvimento, como instruções de depuração além dos logs reais.
10. Código novo **não deve** introduzir novos avisos do linter
11. O desenvolvedor **deveria** ter o `pre-commit` instalado e funcionando. Commits do `pre-commit-ci` deveriam ser evitados.

## PRs e commits

1. A mensagem de commit **deveria** incluir um prefixo com o nome do módulo, por exemplo `Part: `
2. A mensagem de commit **deveria** usar o modo imperativo, assim como o git faz, por exemplo `Part: Add fillet feature`

{{< details summary="Mensagem do commit" open="falso" >}}

Uma linha de assunto de commit Git bem formada deveria sempre poder completar a seguinte frase em inglês:

If applied, this commit will **your commit message**,

por exemplo, If applied, this commit will add fillet feature.

{{< /details >}}

3. Se o conjunto de alterações for grande e abranger vários módulos, ele **deveria** ser dividido em um commit por módulo.
4. Cada commit do PR **deve** compilar e executar corretamente. O fluxo de trabalho do `git bisect` não funciona se alguns commits não puderem ser compilados.
5. A mensagem de commit **pode** conter informações adicionais após uma linha em branco.
6. Todo PR **deveria** ter uma descrição, mesmo que pareça óbvio.

## Regras básicas de código

1. (Somente C++) O código novo **deve** ser formatado com a ferramenta clang-format ou de forma compatível com o resultado do clang-format, se o arquivo estiver excluído da formatação automática.
2. (Somente Python) O código **deve** seguir o padrão PEP 8 e ser formatado com o Black.
3. O caminho principal de execução **deveria** ser o menos indentado, ou seja, as condições deveriam cobrir casos específicos.
4. A saída antecipada **deveria** ser preferida para podar rapidamente ramos de execução indesejados.
5. O estado global (variáveis globais, campos estáticos, singletons) **deveria ser** evitado.
6. (Somente C++) `enum class` **deveria** ser preferido em vez do enum normal sempre que possível.
7. (Somente C++) Bibliotecas/estruturas de C++ **deveriam** ser preferidas em vez das de C. i.e. `std::array/vector` should be used instead of C array.
8. (C++ only) C++ standard library **should** be utilized if possible, especially the `<algorithms>` one.

{{< details summary="Example" open="falso" >}}

Consider the following code:

```c++
    std::vector<int> vertices;

    std::set<int> vertexSet;
    for (auto &s : face.getSubShapes(TopAbs_VERTEX)) {
        int idx = shape.findShape(s) - 1;
        if (idx >= 0 && vertexSet.insert(idx).second) {
            vertices.push_back(idx);
        }
    }
```

You can rewrite it in a following way:

```c++
    std::vector<int> vertices;

    std::set<int> vertexSet;
    for (auto &vertex : face.getSubShapes(TopAbs_VERTEX)) {
        int vertexId = shape.findShape(vertex);

        if (vertexId > 0) {
            vertexSet.insert(vertexId);
        }
    }


    std::copy(vertexSet.begin(), vertexSet.end(), std::back_inserter(vertices));
```

This way you split the responsibility of computing unique set with result preparation.

{{< /details >}}

11. (C++ only) Return values **should** be preferred over out arguments.
    a. For methods that can fail `std::optional` should be used
    b. For methods that return multiple values it may be better to either provide dedicated struct for result or use `std::tuple` with expression binding.
12. (C++ only) If dealing with pointers `auto` **must** be suffixed with `*`: `auto*`.
13. (C++ only) If dealing with references `auto` **must** be suffixed with `&`: `auto&`
14. (C++ only) `auto` **should** be used if:
    a. the right-hand side makes clear which type it is, e.g. with `static_cast`, or `new`
    b. the type is long or verbose (iterators, ranges, ...)
    c. reduz a redundância no código (tipo repetido)
15. (Somente C++) `auto` **não deveria** ser usado se:
    a. lidar com tipos primitivos (o tipo nem sempre é claro, int vs unsigned etc)
    b. o tipo não for claro pelo contexto, nome do método ou argumentos de template
16. Se a expressão não for óbvia, ela **deveria** receber um nome por meio de uma variável.
17. (Somente C++) O código **não deveria** ser colocado em namespace anônimo.
18. Todos os membros **devem** ser inicializados.

{{< details summary="Justificativa" open="falso" >}}

Membros não inicializados podem facilmente causar comportamentos indefinidos muito difíceis de encontrar.

{{< /details >}}

19. Se possível, funções / métodos **não deveriam** usar mais de 3 níveis de indentação.

{{< details summary="Justificativa" open="falso" >}}

O caminho principal do código deveria ser o menos indentado; os casos excepcionais deveriam ser tratados como
instruções if de saída antecipada. Código muito indentado é mais difícil de processar e frequentemente
tem grande carga cognitiva; se algo não puder ser escrito em até 3 níveis
de indentação, é um bom sinal de que talvez precise ser dividido em métodos menores.

{{< /details >}}

20. (Somente C++) casts dedicados deveriam ser preferidos em vez de `dynamic_cast` por questão de desempenho
    a. QObjects deveriam usar `qobject_cast`
    b. Tipos do FreeCAD (derivados de `BaseClass`) deveriam usar `freecad_cast`

## Design / Arquitetura

1. Cada classe / método / função **deveria** fazer apenas uma coisa e fazê-la bem.
2. Classes que fornecem lógica de negócio **deveriam** ser sem estado. Isso ajuda na reutilização.
3. Funções / métodos **deveriam** ser puros, ou seja, o resultado deveria depender apenas dos argumentos (e do estado do objeto, no caso de método). Isso ajuda na reutilização, na previsibilidade e nos testes.
4. Dados imutáveis **deveriam** ser usados sempre que possível, (Em C++ use `const`)

{{< details summary="Justificativa" open="falso" >}}

É muito mais fácil raciocinar sobre código que lida com dados que não mudam.

Usar o modificador const garante que o objeto permanecerá inalterado, e o compilador se certificará disso.

{{< /details >}}

5. (Somente C++) Se possível, `constexpr` **deveria** ser usado para armazenar dados constantes.
6. Métodos longos **deveriam** ser divididos em métodos menores e mais bem descritos.
7. (Somente C++) A definição de novas macros **deve** ser evitada, a menos que seja absolutamente necessária.
8. Inteiros **não devem** ser usados para expressar nada além de números. Para enumerações, **devem** ser usados enums.
9. O código **deveria** ser escrito de forma a expressar a intenção, ou seja, o que deve ser feito, e não apenas como é feito.

{{< details summary="Example" open="falso" >}}

Considere este código:

```c++
    void setOverlayMode(OverlayMode mode)
    {
        // ... some code ...

        QDockWidget *dock = nullptr;

        for (auto w = qApp->widgetAt(QCursor::pos()); w; w = w->parentWidget()) {
            dock = qobject_cast<QDockWidget*>(w);
            if (dock) {
                break;
            }
            auto tabWidget = qobject_cast<OverlayTabWidget*>(w);
            if (tabWidget) {
                dock = tabWidget->currentDockWidget();
                if (dock) {
                    break;
                }
            }
        }

        if (!dock) {
            for (auto w = qApp->focusWidget(); w; w = w->parentWidget()) {
                dock = qobject_cast<QDockWidget*>(w);
                if (dock) {
                    break;
                }
            }
        }

        // some more code ...

        toggleOverlay(dock, m);
    }
```

É difícil entender qual é a função do laço for dentro da instrução `if (!dock)`.
Podemos refatorá-lo para um novo método `QWidget* findClosestDockWidget()`, de modo que fique assim:

```c++
    void setOverlayMode(OverlayMode mode)
    {
        // ... some code ...

        QDockWidget *dock = findClosestDockWidget();

        // ... some more code ...

        toggleOverlay(dock, m);
    }
```

O findClosestDockWidget() pode ser implementado como um método privado ou como uma função interna usando lambdas.

```c++
auto findClosestDockWidget = []() { ... }
```

Assim, ao ler o código de `setOverlayMode`, não precisamos nos preocupar com os detalhes de encontrar o dock widget mais próximo.

{{< /details >}}

10. Argumentos booleanos **devem** ser evitados. Use enumerações em vez disso; um enum com 2 valores é perfeitamente aceitável.
    Em Python, argumentos booleanos são aceitáveis, mas **devem** ser obrigatoriamente argumentos nomeados.

{{< details summary="Example" open="falso" >}}

Consider the following code:

```c++
mapper.populate(false, it.key(), it.value());
```

É impossível entender o que false significa sem consultar a documentação ou pelo menos a assinatura do método.

Em vez disso, deveria ser usado o enum:

```c++
mapper.populate(mappingstatus::modified, it.key(), it.value());
```

Agora a intenção está clara.

{{< /details >}}

11. (Somente C++) O código **deveria** preferir a inicialização uniforme `{ }` (também chamada de inicialização com chaves). Prevents narrowing.
12. (C++ only) Class member variables **should** be initialized at declaration, not in constructors
13. Magic numbers or other literals **must** be avoided.

## Naming Things

Naming described in that section of the document refers mostly to newer parts of code. Some modules use different naming conventions,
while checking the code Reviewer should take into account surrounding code and first of all ensure consistency within the closest scope.

1. Code symbols (classes, structs, methods, functions, variables...) **must** have names that are meaningful and grammatically correct.
2. Variables **should not** be named using abbreviations and/or 1 letter names. Iterator variables or math related ones like `i` or `u` are obviously not covered by this rule.
3. Names **must not** use the hungarian notation.
4. (C++ only) Classes/Structs/Enums **must** be written in `PascalCase`, underscores are allowed but should be avoided.
5. (C++ only) Class/Struct members **should** be written in `camelCase`, underscores are allowed but should be avoided.
6. (C++ only) Global functions **should** be written in `camelCase`, underscores are allowed but should be avoided.
7. (C++ only) Enum cases **should** use `PascalCase`
8. (C++ only) Enums should use singular form (i.e. `enum ObjectState` instead of `enum ObjectStates`)
9. (C++ only) Local variables **should** use `camelCase`

### Naming Conventions

1. Coin nodes **should** be prefixed with `So`, e.g. `SoTransformDragger`. Reimplementation of existing Coin nodes **should** use `SoFC` prefix, e.g. `SoFCTransform`.
2. Features in Part and Part Design workbenches **should** be prefixed with `Feature`, e.g. `FeatureHole`.
3. View Providers corresponding to features / other objects **should** be prefixed `ViewProvider`, e.g. `ViewProviderHole`
4. Task Views (content for task panels) **should** be prefixed with `Task`, e.g. `TaskTransform`
5. Task Dialog for Task View **should** be additionally suffixed with `Dialog`, e.g. `TaskTransformDialog`
6. Preference Pages **should** be prefixed with `DlgSettings`, e.g. `DlgSettingsLights`.
7. Commands **should** be prefixed with `Cmd` and Workbench name e.g. `CmdPartDesignCreateSketch`

## Commenting the code

1. Good naming **must** be preferred over commenting the code.
2. Comments that describe what code does **should** be avoided, instead comments **should** explain intended result.
3. All edge-cases in code **must** be described with comment describing when such edge-case can occur and why it is handled in certain way.
4. All "Hacks" **must** be described with how the hack works, why it is applied and when it no longer will be needed.
5. Commented code **must** be contain additional information on why it was commented out and when it is safe to remove it.
