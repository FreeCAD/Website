---
title: Práticas de C++
description: Práticas de C++.
weight: 4
---

A maioria das regras apresentadas aqui cobre os mesmos assuntos das excelentes [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines).
Sempre que algo não estiver coberto ou você tiver dúvidas, não hesite em consultá-las: são uma ótima fonte de informação.

## Evite namespaces anônimos

Namespaces anônimos são muito convenientes, mas tornam o código inacessível para testes
e para outros códigos.
Algum código pode fazer sentido apenas em um determinado contexto, mas se a funcionalidade
for genérica, ela pode ser colocada em uma biblioteca ou algo semelhante.

Use um _namespace nomeado_ para abrigar funções livres, em vez de depender de uma classe ou struct cheia de funções estáticas (ou funções que deveriam ser estáticas).
Essa abordagem garante melhor organização e clareza.

Além disso, funções estáticas privadas não precisam ser declaradas no arquivo de cabeçalho quando movidas para fora de uma classe.
Isso reduz a exposição desnecessária de detalhes de implementação.

## Algoritmos e estruturas de dados

> Algoritmos + Estruturas de dados = Programas
> \--- Niklaus Wirth, 1976

> Os algoritmos da STL dizem o que fazem, ao contrário dos laços for feitos à mão, que apenas mostram como são implementados. Dessa forma, os algoritmos da STL são um meio de elevar o nível de abstração do código, para corresponder ao do ponto de chamada.
> \--- Jonathan Boccara, 2016

> Depurar código é duas vezes mais difícil do que escrever o código. Portanto, se você escrever o código da forma mais engenhosa possível, por definição você não é inteligente o bastante para depurá-lo.
> \--- Brian W. Kernighan

Dados são informações, fatos etc. Um algoritmo é um código que opera sobre dados.

As linguagens de programação, ou suas bibliotecas, incluem algoritmos amplamente testados para lidar com estruturas de dados comuns.

Ao considerar adequadamente algoritmos e estruturas de dados, e manter os dados separados do código, tanto o código quanto os dados ficam mais simples, mais confiáveis, mais flexíveis e mais fáceis de manter para a próxima pessoa.

Laços brutos são aqueles que começam com `for`, `while` etc. Embora haja muitas opções de como escrever um laço, a legibilidade e a manutenibilidade devem ser a prioridade.

```cpp
// Pre-C++11:
for (std::map<KeyType, ValueType>::iterator it = itemsMap.begin(); it != itemsMap.end(); ++it) {
    //...
    doSomething(*it);
    //...
}

for (const auto& item : itemsMap) {
    //...
    doSomething(item);
    //...
}

for (const auto& [name, value] : itemsMap) {
    //...
    doSomething(name, value);
    //...
}
```

Outra forma, que pode ser ainda melhor, é usar a biblioteca STL `<algorithm>`, que oferece uma grande variedade de soluções declarativas comprovadas, p. ex.:

```cpp
// C++17
std::for_each(stuff.begin(), stuff.end(), do_something);
auto result = std::find_if(stuff.begin(), stuff.end(), do_something);

// C++20
std::ranges::for_each(stuff, do_something);
auto result = std::ranges::find_if(stuff, do_something);
```

Observe que a biblioteca STL `<algorithm>` também pode usar lambdas.

## Comentários no código

> Não comente código ruim; reescreva-o.
> \--- Brian W. Kernighan e P. J. Plaugher, 1974

Comentários são uma parte do programa que o computador não executa. Embora a intenção seja ajudar a compreensão, eles tendem a ficar dessincronizados do código real que comentam.

É preferível que o código seja autodocumentado quando possível. Isso pode ser alcançado com boa nomenclatura e estrutura.

Em alguns casos, comentários podem ser necessários para transmitir informações que não podem ser descritas no código. Podem ser links para bugs descritos por uma solução alternativa ou o motivo de casos extremos serem necessários.

## Condicionais

Cada ramificação no código dobra o número de caminhos e torna o código difícil de depurar e manter.

Um `if else` simples pode ser melhor expresso como um ternário `_ : _ ? _`. Muitas vezes há formas de evitar o `else`; quando possível, o código resultante fica melhor sem ele. O ternário, porém, é aceitável.

Mesmo um código modestamente complexo em um ramo `if` ou `else` deve ser
extraído para uma função ou lambda.

Uma sequência de condicionais percorrendo variáveis relacionadas pode indicar
mistura de código e dados.

Também pode se aplicar a instruções `switch`.

Um código `if else` complicado pode se beneficiar da conversão para uma máquina de estados.

### Operador ternário

Você pode reduzir seis linhas:

```cpp
int r; // can’t be const

if (x == 2) {
    r = 2;
} else {
    r = 3;
}
```

para uma, com uma única atribuição, sem chaves, sem repetição e
com a opção const:

```cpp
const int r = x == 2 ? 2 : 3;
```

Isso funciona especialmente bem para simplificar instruções return.

Se você tiver mais de um ternário, pode valer a pena extrair uma função que encapsule a lógica condicional:

```
auto someConditionalLogic = []() {
    if (condition1) {
        return 1;
    } else if (condition2) {
        return 2;
    } else {
        return 3;
    }
}

const int r = someConditionalLogic();
```

## Correção de const

> const em tudo.
> \--- Jason Turner, 2021

`const` é uma declaração de intenção de que algo deve ser imutável
(não pode mudar). A imutabilidade ajuda a confiabilidade e é feita usando `constexpr`

Isso fornece avaliação em tempo de compilação. Pode aumentar o tempo de compilação, mas acelera a execução. Mais erros são detectados em tempo de compilação.

`constexpr` é preferível para tudo o que puder ser representado assim.

## Reduzindo dependências

> Qualquer dependência de código-fonte, não importa onde esteja, pode ser invertida
> \--- Robert C. (Uncle Bob) Martin

Dependências rígidas deixam a base de código mais emaranhada, dificultam as alterações e tornam os testes unitários muito difíceis.

Três exemplos de dependências se infiltrando:

```cpp
Application::getSomething(); // ou qualquer outro singleton
SomeDistantClass thing;
void method(AnotherDistantClass values){}
```

Isso não se opõe à reutilização de código, mas exige cuidado ao projetar como o código acessa os dados.

Uma função com dependências rígidas não pode funcionar, ser entendida, editada ou testada sem o contexto de suas dependências. Vale a pena se esforçar para evitar esses tipos de dependência sem duplicar código.

Diz-se que o código e suas dependências estão _acoplados._ Quando diferentes partes do código _têm a mesma_ dependência, elas, por sua vez, ficam acopladas entre si.

As informações necessárias podem ser injetadas por parâmetros do construtor ou do método.

Se for necessário introduzir código externo (por exemplo, um objeto de serviço), faça isso passando uma interface, uma função auxiliar ou algo semelhante, para evitar o acoplamento.

Mesmo em casos complexos em que singletons são usados, podemos evitar o acoplamento rígido e tornar os testes unitários muito fáceis.
Exemplo:

```cpp
// Neste exemplo, a implementação está incluída na definição da classe
// para simplificar o exemplo.
class Example {
public:
    using DependencyHelper std::function<std::unique_ptr<Dependency>()>;
    Example(
        //...
        DependencyHelper provide_helper_ = {}
    ) : provide_helper_(std::move(provide_helper))
    {
        if (!provide_helper_) {
            provide_helper_ = my_namespace::defaultDependencyHelper();
        }
    };
private:
    DependencyHelper provide_helper_;
}
```

Idealmente, todas as dependências podem ser evitadas; quais dependências manter depende da situação.

Se o seu código precisa de dados externos que não estavam disponíveis ao chamar este
código, provavelmente existe um design geral melhor que pode ser usado.

**Código sem dependências rígidas tem um único propósito, é reutilizável, alterável e testável. Tudo fica mais simples!**

## Design de código

> Qualquer tolo consegue escrever código que um computador entenda. Bons programadores escrevem código que humanos conseguem entender
> \--- Martin Fowler

Algo bem projetado é _instantaneamente_ compreensível e um prazer de trabalhar
com ele. Os princípios de programação desenvolvidos nos últimos 50 anos garantem que
o código bem projetado não apenas funcione bem, mas também seja compreensível por humanos.

O código bem projetado é adaptável, flexível e facilmente alterado para se adequar a novas
circunstâncias.

O código bem projetado é totalmente livre de dados fixos no código.

Código compreensível pode ter sua correção avaliada com mais facilidade.

Para um programador iniciante, muitos desses conceitos provavelmente são bastante estranhos, mas com um pouco de estudo, ajuda da comunidade e revisões de código, um código melhor virá.

## Enumeradores

Usados corretamente, os enums são inestimáveis.

Usar enums:

- ...especificamente `enum class`, permite criar enumerações fortemente tipadas e com escopo.
- ...em vez de booleanos para argumentos de função, facilita entender o que o argumento significa sem consultar a documentação ou pelo menos a assinatura do método.
- ...em vez de inteiros ao expressar qualquer coisa que não sejam números.

Using enums to codify data values is strongly discouraged, as enums are best suited for representing fixed, intrinsic states rather than variable data. Instead, use `std::unordered_map<>` or other data structures that better represent dynamic or data-driven values, offering flexibility and improving maintainability.

## Minimize getters and setters

In object-oriented design, a class should encapsulate behavior, not just data. **Frequent use of getters and setters can limit a class’s ability to fully encapsulate its responsibilities** and may suggest that the data could be handled differently.

Consider:

- Using a struct for simple data containers with public fields.
- Focusing on methods that represent meaningful actions rather than exposing raw data.

A well-designed class manages its own state and provides behavior, not just access.

## Appropriate typing

Using strings for everything can make code harder to understand and maintain. Use appropriate types to add clarity and structure.

### The use of `auto`

The use of `auto` has not yet been discussed in the C++ Core Guidelines (see
the to-do
list).
Below follow general guidelines with examples:

#### The use of `auto` is ok if the right-hand side makes clear which type it is

```cpp
auto* xyz = new Xyz(); // OK: type is clear from calling the constructor
```

```cpp
auto xyz = <whatever>_cast<Xyz>(...); // OK: o tipo fica claro pelo cast
```

```cpp
auto xyz = getAnything<Xyz>(...); // OK: o tipo fica claro pelo contexto e pelo parâmetro de tipo
```

```cpp
auto value = randomThing.weirdProperty->getValue(); // ruim: tipo não óbvio
```

```cpp
auto doStuff() { ... } // ruim: auto como tipo de retorno
```

```cpp
auto xyz = 1; // ruim: não fica claro qual tipo de inteiro
```

#### O uso de `auto` é aceitável se o tipo for longo ou verboso

```cpp
auto it = foo.begin(); // OK: iterador
```

```cpp
auto lambda = [](){...}; // OK: tipo função
```

#### O uso de `auto` é aceitável se evitar redundância

```cpp
std::unordered_map<std::string, int> map;
for (const auto& [key, value] : map) { ... } // OK: a declaração do map contém o tipo
```

## Caminho principal do código e indentação

> Se você passou de três níveis de indentação, basicamente está ferrado.
> Hora de reescrever.
> \--- Linus Torvalds, 1995

Código indentado pode ser difícil de entender e frágil.

O caminho principal de execução deve ser o menos indentado, ou seja, as condições devem cobrir casos específicos. A saída antecipada deve ser preferida para podar rapidamente ramos de execução indesejados.

Exemplo:

```cpp
if (something) {
    doSomething();
    if (somethingElse) {
        doSomethingElse()
        if (somethingElseAgain) {
            doThing();
        } else {
            doDifferent();
        }
    } else {
        doTheOther();
    }
} else {
    doNothing();
}
```

Pode ser alterado para:

```cpp
if (!something) {
    doNothing();
    return;
}
doSomething();
if (!somethingElse) {
    doTheOther();
    return;
}
doSomethingElse();
if (!somethingElseAgain) {
    doDifferent();
    return;
}
doThing();
```

## Inicialização

**Inicialize todos os objetos e, se possível, use const ou, melhor ainda, constexpr.**

Evite construtores padrão. Se ainda não há um valor para um objeto, não há necessidade de criá-lo. Declare as variáveis perto de onde são usadas (não é necessário declarar as variáveis no início do bloco como em ansi-c). Unir declaração e inicialização permite usar const:

```cpp
AType thing; // mutável. Ele tem um construtor padrão?
const AType thing3 { calcVal() }; // imutável
```

Usar variáveis de tipo POD não inicializadas é comportamento indefinido.

_É_ aceitável declarar variáveis dentro de um laço.

Prefira a inicialização uniforme `{ }` (também chamada de inicialização com chaves), pois ela impede o estreitamento.

Deixa claro que não é uma atribuição (=) nem uma chamada de função (()).

Inicialize as variáveis membro da classe na declaração, não nos construtores:

- Simplifica os construtores
- Evita repetição
- Estabelece o estado padrão

Membros estáticos podem ser definidos no arquivo de cabeçalho, sem necessidade de separá-los no arquivo-fonte:

```cpp
struct Something {
    static const int _value_ = 2; // desde o C++98 para int
    static inline std::string _something_ {"str"}; // desde o C++17
}
```

Lambdas podem criar e inicializar variáveis na captura, eliminando a
necessidade de ter o parâmetro no escopo ao redor. Mas não se esqueça do
mutable se quiser atualizar o valor dela. A variável existe durante todo o tempo de vida
do lambda (pense em static, só que melhor).

## Lambdas

> Um dos recursos mais populares do C++ moderno.
> \--- Jonathan Boccara, 2021

Um lambda (desde o `C++11`) é como uma função que pode receber um nome e ser passada para
e a partir de funções. Eles aceitam parâmetros, podem ser genéricos (desde o `C++14`), fazem uma
ótima dedução de tipo (auto) e podem ser constexpr (desde o `C++17`).

Lambdas podem capturar dados dos escopos envolventes e impor o encapsulamento, simplificando os escopos ao redor.

Lambdas são indispensáveis ao dividir código complexo em responsabilidades
individuais, talvez como etapa anterior à passagem para funções. O mesmo vale
ao remover repetições.

Embora os lambdas funcionem bem com parâmetros auto simples, é melhor não
omitir const ou & quando apropriado. Types may be required to help the IDE.

Consider the following code:

```cpp
doSomething()
if (somethingWentWrong()) {
    // Clean up this
    // ...
    // Clean up that
    return;
}
doSomethingElse();
if (somethingElseWentWrong()) {
    // Clean up this
    // ...
    // Clean up that
    return;
}
doSomeOtherThing();
// Clean up this
// ...
// Clean up that
```

Using lambdas we can remove code duplication to create the following:

```cpp
auto cleanup = [](){
    // Clean up this
    // ...
    // Clean up that
};

doSomething()
if (somethingWentWrong()) {
    cleanup();
    return;
}
doSomethingElse();
if (somethingElseWentWrong()) {
    cleanup();
    return;
}
doSomeOtherThing();
cleanup();
```

## Avoid macros

While macros was needed back in the days, today with modern C++, that's usually not the case anymore.

Macros are global, can be lead to unpredicted side effects and are difficult to debug. Consider replacing with a function. For conditional compilation in templates consider constexpr if.

## Avoid magic literals

“Magic” literals placed directly in code offer no clue as to what exactly
is being specified or its origin, and no clue if the same data is used
elsewhere. Comprehension and maintenance burden.

To document what the magic literal is, use a suitable named constant.

Instead of this:

```cpp
displayLines(80);
```

Do the following instead:

```cpp
constexpr unsigned standardScreenLength {80};
displayLines(standardScreenLength);
```

## Good naming

**Clear, concise, naming makes code understandable**.

For an object whose purpose is to _do_ something (service object), prefer a verb. E.g. `renderer`.

For an object that _is_ something (value object), prefer a noun. E.g. `drawing`.

Something difficult to name concisely likely does not have a single purpose and needs refactoring.

Use names that are specific. E.g. `SaveLogToDisk`, not `ProcessLog`. `Process` could be anything.

A variable named after its data value defeats the whole point of a variable:

```cpp
struct Dog {
    std::string color {};
};
Dog redDog {"blue"}; // BAD
// 200 lines later, -_obviously_\- redDog is red! He’s blue? WTF?
Dog dog {"pink"}; // OK
constexpr auto redDogColor {"red"}; // OK
```

Veja também conjuntos de variáveis.

## Parâmetros de saída

Parâmetros de saída são parâmetros de função _não const, por referência ou por ponteiro_. Eles são conhecidos por causar bugs difíceis de encontrar.

Não é óbvio se os valores são atualizados pela função.

**Sempre que possível, torne os parâmetros da função `const` ou `const&` e retorne um valor, ou retorne um contêiner para retornar vários valores**.

A otimização de valor de retorno (RVO) simplifica o retorno e geralmente elimina cópias.

```cpp
auto func = [](const auto& str, const auto num) {
    return { str, num };
};
```

O structured binding (desde o C++17) simplifica a leitura do resultado no ponto de chamada:

```cpp
auto [name, value] = func("qty", 2);
```

Para métodos que retornam vários valores, dependendo do contexto, pode ser melhor fornecer uma struct dedicada para o resultado.

## Repetição de código

> Uma das coisas que venho tentando fazer é procurar regras mais simples que sustentam o bom ou o mau design. Acho que uma das regras mais valiosas é evitar a duplicação
> \--- Martin Fowler

> A duplicação de código é de longe um dos piores antipadrões da engenharia
> de software, levando a sistemas cheios de bugs e impossíveis de manter.
> \--- Magnus Stuhr, 2020

Reduzir a duplicação de código e códigos semelhantes também reduz os diferentes caminhos que um programa pode seguir durante a execução. Isso, por sua vez, facilita depurar e testar a base de código.

Uma alteração exige encontrar cada uso (difícil) e replicar a alteração (propenso a erros). Deixar passar uma única ocorrência cria um bug desagradável que pode permanecer sem ser descoberto por muito tempo. A compreensão exige estudar cada item. Pequenas diferenças são notoriamente difíceis de perceber.

**A repetição é totalmente evitável.**

A parte variável (o trecho que difere entre os usos) do código repetido costuma ser apenas um ou dois itens em uma longa cadeia de instruções.
As partes variáveis podem ser extraídas e passadas como parâmetros para uma função ou lambda que executa o corpo comum. Uma sequência de código repetido provavelmente indica que os dados subjacentes são na verdade um conjunto e, portanto, devem ser definidos em um contêiner e tratados de acordo.

## Estática

Geralmente é melhor evitar. Para variáveis `const`, considere `constexpr` ou
a inicialização na captura do lambda.

Pode _ser_ melhor mover funções `static` para fora da classe, para um namespace nomeado ou alguma biblioteca/arquivo utilitário.

## Testes automatizados

> Nada torna um sistema mais flexível do que um conjunto de testes. Nada. Boa arquitetura e bom design são importantes, mas o efeito de um conjunto robusto de testes é uma ordem de grandeza maior. É muito maior porque esses testes permitem melhorar o design.
> \--- Uncle Bob

Existem vários tipos de testes automatizados. Testes de regressão, testes de integração. testes unitários etc. Embora haja semelhanças, a ideia por trás deles é diferente. São ferramentas diferentes na caixa de ferramentas que podemos usar para garantir código de boa qualidade.

- **Testes de regressão**: quando bugs são encontrados, são criados testes para garantir que o bug encontrado seja 1. corrigido e 2. não aconteça novamente.
- **Testes de integração** garantem que vários componentes possam trabalhar juntos para concluir uma tarefa.
- **Testes unitários** visam um único comportamento de uma única unidade de código, com uma única asserção.

Escrever testes em um design acoplado é difícil; portanto, remover dependências rígidas não é apenas um exercício acadêmico, mas uma ótima ferramenta para tornar o código testável.

O desenvolvimento orientado a testes, em que os testes são escritos antes e durante a criação do código, é uma boa prática a seguir para garantir código de boa qualidade. Escrever testes depois pode ser difícil, pois isso não ajuda tanto no design do código enquanto ele é produzido.

O código de interface gráfica costuma ser classificado como não testável porque faltam boas ferramentas para verificar o comportamento quando botões e controles deslizantes são manipulados. E embora o código de interface gráfica não possa ser testado facilmente, a lógica à qual ele está conectado pode. Separar a interface da "lógica de negócio" é uma boa escolha e altamente recomendada.

Assim como bons nomes são importantes para variáveis e funções, também são para os testes. Um bom nome de teste descreve o que foi testado. Assim, quando falhar para outra pessoa, ela poderá ver facilmente o que falhou.

Se o código for difícil de testar unitariamente, considere se ele pode ser extraído do seu contexto, talvez para alguma classe no estilo de biblioteca, onde possa ser testado isoladamente. É possível refatorar para remover dependências fixas no código? Ele está tentando fazer coisas demais? Ele está acoplado demais? Veja também dependências.

## Evite conjuntos de variáveis

Representar dados com código, em que variáveis relacionadas têm nomes fortemente ligados ao seu valor inicial, deve ser evitado para reduzir a repetição e tornar o código mais fácil de entender e manter.

Por exemplo, em vez disto:

```cpp
Item fred { "Fred", 20 };
Item martha { "Martha", 30 };
Item george { "George", 40 };
```

Mova os dados para um contêiner, por exemplo `constexpr std::initializer_list`, e não um vector ou map.

Os elementos do contêiner normalmente são valor, array, pair, tuple ou uma struct definida.
Pair e tuple só devem ser usados para dados de vida muito curta, como neste caso:

```cpp
using Pair = std::pair<std::string_view, size_t>;

constexpr std::initializer_list<Pair> items {
    { "Fred", 20 },
    { "Martha", 30 },
    { "George", 40 }
};
```

Também pode ser usada uma struct, que tem a vantagem de ter elementos nomeados, mas com um pouco mais de sobrecarga.

```cpp
struct Button {
    std::string_view name;
    size_t height;
    size_t width;
};

constexpr std::initializer_list<Button> buttonDefs {
    { "Go", 25, 25 },
    { "Get set", 20, 20 },
    { "On your marks", 15, 15 }
};
```

Na dúvida, use uma struct: é melhor ter bons nomes do que não tê-los.

## Documentação da API

A documentação da API no FreeCAD consiste em dois tipos principais de documentação.  Os **tópicos** explicam os conceitos por trás do código, e as **strings de documentação da API** explicam o próprio código.  Ambos são importantes, mas os tópicos são especialmente valorizados.

Embora não seja estritamente obrigatório, os desenvolvedores são fortemente incentivados a escrever documentação da API quando aplicável.  Observe que **é obrigatório** manter a documentação da API atual em dia com as alterações feitas no código.  Esta seção apresenta um conjunto de diretrizes para essa documentação.

### Diretrizes gerais

- Seja o mais completo possível, com cada item (classes, enums, membros públicos e protegidos) de um arquivo tendo uma string de documentação.
- Minimize o espaço vertical.  Assim, quando possível, use uma única linha com `///` ou `///<` para itens de enum (veja abaixo).
- Em geral, não documente conceitos do C++ como destrutores, friends ou construtores, exceto quando houver argumentos ou se algo especial acontecer.

### Sintaxe

O Doxygen suporta dois tipos diferentes de sintaxe para comandos: os com barra invertida (por exemplo `\brief`) e os com o símbolo `@` (`@brief`).  A versão com prefixo `@` é mais comum no código-fonte do FreeCAD e é o estilo preferido para nova documentação.

Para um comentário de documentação da API de uma única linha, por exemplo comentando uma função, use `/// <seu comentário.` sem usar `@brief` e terminando com ponto final.  Exemplo:

```cpp
    /// Get the transaction ID of this transaction.
    int getID() const;
```

Para várias linhas, use `/**` para iniciar a docstring.  A documentação começa na linha seguinte com um comando `@brief` que termina com ponto final e depois uma quebra de linha.  No caso abaixo, há detalhes após os quais os comandos `@param[in]` e `@return` documentam os parâmetros e a instrução de retorno, respectivamente.

```cpp
    /**
     * @brief Check whether the passed name is valid.
     *
     * If a name is null or an empty string it is considered invalid, and valid
     * otherwise.
     *
     * @param[in] name The name to check.
     * @return True if the name is valid, false otherwise.
     */
    static bool isValidName(const char* name);
```

Mantenha o número de linhas adicionadas no mínimo.  Por exemplo, use `///<` para manter os comentários na mesma linha:

```cpp
    /// The status of the transaction object.
    enum Status
    {
        New, ///< A new object is added to the document.
        Del, ///< An object is deleted from the document.
        Chn ///< An object is changed in the document.
    } status {New};
```

Use uma única linha para separar a documentação de funções diferentes, para deixar mais claro a qual função pertence a string de documentação:

```cpp
    /// Generate a new unique transaction ID.
    static int getNewID();

    /// Get the last transaction ID.
    static int getLastID();
```

Para evitar que o Doxygen crie automaticamente um link irrelevante ou indesejado, use o prefixo `%`.  Por exemplo, como existe um namespace `Base` no FreeCAD, use `%Base` como mostrado no exemplo abaixo para evitar que o Doxygen crie aqui um link para o pacote `Base`:

```cpp
/**
 * @brief %Base class of all properties.
 * @ingroup PropertyFramework
 *
 * This is the base class of all properties.  Properties are objects that are
 * ...
 */
```

É possível usar a sintaxe Markdown nos comentários de documentação.  For example, a Markdown list:

```cpp
    /**
     * @brief A multi index container for holding the property spec.
     *
     * The multi index has the following index:
     * - a sequence, to preserve creation order
     * - hash index on property name
     * - hash index on property pointer offset
     */
    mutable bmi::multi_index_container<
        PropertySpec,
        bmi::indexed_by<
		...
    > propertyData;
```

### Placing API documentation

The main page of the API documentation is in `src/Doc/mainpage.dox.in`.  The most important function of this page is the "Organization of the API Documentation" section allowing readers to quickly browse important topics.

Topics should be defined in dedicated `.dox` files in the main directory of a package.  For example, `src/App/core-app.dox` defines a group `APP` that is in group `CORE` (defined in the main page) and then it defines several topics in `APP`, such as `DocumentGroup` (for the concept of a Document in FreeCAD), `DocumentObjectGroup` (for the concept of a document object), etc.  Below are two excerpts from that file to give an indication:

```cpp
/**
 * @defgroup APP App
 * @ingroup CORE
 * @brief The part of FreeCAD that works without GUI (console or server mode).
 *
 * It contains the App namespace and defines core concepts such as
 * @ref DocumentGroup "Document", @ref DocumentObjectGroup "Document Object",
 * @ref PropertyFramework "Property Framework", @ref ExpressionFramework
 * "Expression Framework", and the @ref ExtensionFramework "Extension
 * Framework".
 *
 * The largest difference between the functionality in @ref BASE "Base"
 * compared to %App is that %App introduces the notion of properties, both used
 * ...
 */
```

```cpp
/**
 * @defgroup DocumentGroup Document
 * @ingroup APP
 * @brief The class that represents a FreeCAD document
 *
 * This (besides the App::Application class) is the most important class in FreeCAD.
 * It contains all the data of the opened, saved, or newly created FreeCAD Document.
 * The App::Document manages the Undo and Redo mechanism and the linking of documents.
 * ...
 */
```

Given such a topic, you can include the most important classes into this topic, for example in `App/Document.h` class `App::Document` is included in `DocumentGroup`.

```cpp
/**
 * @brief A class that represents a FreeCAD document.
 *
 * A document is a container for all objects that are part of a FreeCAD
 * project.  Besides managing the objects, it also maintains properties itself.
 * As such, it is also a PropertyContainer.
 *
 * @ingroup DocumentGroup
 * For a more high-level discussion see the topic @ref DocumentGroup "Document".
 */
class AppExport Document: public PropertyContainer
{
...
```

Documentation strings can be added to classes, enums, and public and protected members of a class.  This is especially important if a class is at the top of a hierarchy and its methods are reused in many other subclasses.  The documentation should be added in the header file and not in the C++ file.

### Specific guidelines

This section contains guidelines for specific types of documentation.

#### Namespaces

Como as instruções de namespace geralmente aparecem em muitos arquivos, é difícil determinar onde colocar as strings de documentação.  Na maioria dos casos, a melhor prática é adicioná-las ao arquivo `.dox` do módulo respectivo.  Por exemplo, em `src/App/core-app.dox`:

```cpp
/**
 * @namespace App
 * @ingroup APP
 * @brief The namespace for the part of FreeCAD that works without GUI.
 *
 * This namespace includes %Application services of FreeCAD that such as:
 *   - The Application class
 *   - The Document class
 *   - The DocumentObject classes
 *   - The Expression classes
 *   - The Property classes
 *
 * For a more high-level discussion see the topic @ref APP "App".
 */
```

#### Classes

Para classes, use uma declaração breve e comentários mais detalhados:

```cpp
/**
 * @brief A class that represents a FreeCAD document.
 *
 * A document is a container for all objects that are part of a FreeCAD
 * project.  Besides managing the objects, it also maintains properties itself.
 * As such, it is also a PropertyContainer.
 *
 * ...
 */
class AppExport Document: public PropertyContainer
{
...
```

#### Funções

Para funções, use uma declaração breve, opcionalmente comentários mais detalhados e, se aplicável e os parâmetros não forem triviais, instruções `@param` indicando a direção `[in]`, `[out]` ou `[in,out]`, um comando `@return` e um comando `@throws`, se aplicável.  Um exemplo:

```cpp
    /**
     * @brief Get the value of the property identified by the path.
     *
     * This function gets the value of the property identified by the path.  It
     * is meant to be overridden for subclasses in which the `path` is
     * typically ignored.  The default implementation makes use of the `path`
     * ObjectIdentifier to get the value of the property.
     *
     * @param[in] path The path to the property.
     * @return The value of the property.
     */
    virtual const boost::any getPathValue(const App::ObjectIdentifier& path) const;
```

#### Enumeradores

Para enumerações, geralmente basta ter uma declaração breve e um comentário curto para cada item:

```cpp
    /// The status of the transaction object.
    enum Status
    {
        New, ///< A new object is added to the document.
        Del, ///< An object is deleted from the document.
        Chn ///< An object is changed in the document.
    } status {New};
```

#### Agrupando

Comentários especiais de documentação podem ser usados para indicar que um grupo de funções, variáveis etc. faz parte de um único agrupamento conceitual. A melhor prática é iniciar um grupo com um bloco de documentação `/**` com um comando `@name` e um comando de agrupamento `@{` na linha seguinte.  O grupo é encerrado com `/// @}`.

Com frequência, os arquivos-fonte do FreeCAD contêm comandos de agrupamento com comentários normais em vez de comentários de documentação, como `// @{` e `// @}`.  Como esses comentários não são comentários de documentação, esse uso é incorreto e pode causar problemas na renderização da documentação. Esse uso deve ser evitado em código novo e corrigido quando encontrado.

```cpp
    /**
	 * @name Properties
     * @{
     */

    /// The long name of the document (utf-8 coded).
    PropertyString Label;

    /// The fully qualified (with path) file name (utf-8 coded).
    PropertyString FileName;

    ...

    /// Whether to use hasher on topological naming.
    PropertyBool UseHasher;
    /// @}
```

#### Templates

Templates podem ser documentados com um comando `@tparam`:

```cpp
    /**
     * @brief Get all objects of a given type.
     *
     * @tparam T The type to search for.
     * @return A vector of objects of the given type.
     */
    template<typename T>
    inline std::vector<T*> getObjectsOfType() const;
```

#### Documentação com muita repetição

A forma preferida de lidar com código com repetição significativa é usar `@copydoc` ou `@copydetails`.

```cpp
    /**
     * @brief Check if this mapped name starts with the search target.
     *
     * If there is a postfix, only the postfix is considered. If not, then only
     * the data is considered. A search string that overlaps the two will not
     * be found.
     *
     * @param[in] searchTarget The search target to match.
     * @param[in] offset An offset to perform the match at.
     *
     * @return True if this MappedName begins with the target bytes.
     */
    bool startsWith(const QByteArray& searchTarget, int offset = 0) const;

    /// @copydoc startsWith(const QByteArray&,int) const
    bool startsWith(const char* searchTarget, int offset = 0) const;

    /// @copydoc startsWith(const QByteArray&,int) const
    bool startsWith(const std::string& searchTarget, int offset = 0) const;
```

Outro exemplo que adiciona um parâmetro:

```cpp
    /**
     * @brief Convert the expression to a string.
     *
     * @param[in] persistent If true, the string representation is persistent
     * and can be saved to a file.
     * @param[in] checkPriority If true, check whether the expression requires
     * parentheses based on operator priority.
     * @param[in] indent The indentation level for pretty-printing.
     *
     * @return The string representation of the expression.
     */
    std::string toString(bool persistent = false, bool checkPriority = false, int indent = 0) const;

    /**
     * @brief Write a string representation of the expression to a stream.
     *
     * @param[in,out] os The output stream to write to.
     * @copydoc Expression::toString(bool, bool, int) const
     */
    void toString(std::ostream &os, bool persistent=false, bool checkPriority=false, int indent=0) const;
```

Um exemplo com `@copydetails`:

```cpp
    /**
     * @brief Register an import filetype given a filter.
     *
     * An example of a filter is: @c "STEP with colors (*.step *.STEP *.stp *.STP)".
     * An example of a module is: @c "Import" or @c "Mesh".
     *
     * @param[in] filter The filter that describes the file type and extensions.
     * @param[in] moduleName The module name that can handle this file type.
     */
    void addImportType(const char* filter, const char* moduleName);

    /**
     * @brief Register an export filetype given a filter.
     *
     * @copydetails addImportType
     */
    void addExportType(const char* filter, const char* moduleName);
```

Outra forma de lidar com documentação com alto grau de repetição é o agrupamento, embora na maioria dos casos a melhor prática seja usar `@copydoc` ou `@copydetails`.

```cpp
  /**
   * @name PropertyData accessors
   *
   * @details These methods are used to access the property data based on:
   * - the offset base,
   * - either:
   *   - a property pointer, or
   *   - a property name.
   * @{
   */
  const char* getName         (OffsetBase offsetBase,const Property* prop) const;
  short       getType         (OffsetBase offsetBase,const Property* prop) const;
  short       getType         (OffsetBase offsetBase,const char* name)     const;
  const char* getGroup        (OffsetBase offsetBase,const char* name)     const;
  const char* getGroup        (OffsetBase offsetBase,const Property* prop) const;
  const char* getDocumentation(OffsetBase offsetBase,const char* name)     const;
  const char* getDocumentation(OffsetBase offsetBase,const Property* prop) const;
  /// @}
```

## Recomendações para concorrência

Nesta seção propomos algumas convenções de código para tornar o código concorrente mais fácil de manter, especialmente para outros desenvolvedores além do autor.

### Marque variáveis agrupadas logicamente

Com frequência, locks ou mutexes protegem variáveis que pertencem logicamente ao mesmo conjunto (se uma muda, é muito provável que outra variável também mude).  Um exemplo é uma estrutura de dados que tem um buffer e precisa manter o número de itens no buffer.  Se a adição à estrutura de dados puder acontecer de forma concorrente, tanto a variável do buffer quanto a variável do número de itens precisam ser protegidas ao mesmo tempo.  Nesses casos, é muito útil marcar explicitamente o que o lock ou mutex está protegendo.

```cpp
std::mutex taskMutex;
// Este mutex protege a fila e a contagem de workers ativos:
// ////////
std::queue<std::function<void()>> tasks;
int active_worker_count = 0;
// ////////
```

Se você operar em uma dessas variáveis controladas pelo lock, precisa garantir que está segurando o lock.  Veja também [CP.50](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rconc-mutex).

### Adote "and" nos nomes de funções para ações atômicas

Código concorrente frequentemente limita a composabilidade.  Isso costuma ficar evidente em estruturas de dados em que cada função pública individual usa locks corretamente.  No entanto, muitas vezes é preciso compor essas funções para uma operação correta, por exemplo:

```cpp
if (!stack.empty()) {
  int v = stack.top();
  stack.pop();
  process(v);
}
```

Embora `empty()`, `top()` e `pop()` usem locks corretamente internamente, a composição dessas funções como no exemplo acima não é necessariamente correta em ambientes concorrentes (e o exemplo acima explicitamente não é).

Por causa desses problemas de composabilidade, um padrão típico é que os nomes das funções concorrentes sejam menos claros do que os nomes das funções sequenciais.  Given functions that perform a particular task and are named properly for these tasks, when making use of these functions for concurrency, often it is necessary to combine multiple of such functions into one larger function to adapt to the locking scheme.  In such cases, often the names of these function do not reflect well what the function does.

In such situations, the recommendation is firstly to minimize the number of things that a function does and secondly adopt the convention to add "and" in the name of functions, akin to the most fundamental concurrency operations such as `testAndSet` and `compareAndSwap`.

This has two benefits: 1) it is easier to find a proper name for what the function does and 2), since this is often regarded bad practice in sequential code, it marks these functions as likely concurrent functions.

As an example, for the code above, a function that composes those operations could be called:

```cpp
checkForEmptyAndProcess()
```

### Name condition variables according to what they wait for

Naming condition variables well can make the code more readable, for example:

```cpp
_recomputeRequestAvailable.wait(lock, [this] {
  ...
}
_recomputeRequestAvailable.notify_all();
```

### Document new concepts introduced for concurrency

If new concepts are introduced for concurrency, document the logic well and try to explain the state that needs to be maintained.  Concurrent code has a tendency to accumulate state with counters, booleans, a touched set, etc.  Each new boolean introduced doubles the state-space and you always want to be able to account for all cases.  In these situations, it is very helpful to explain the state machine, the flow, and invariants that help prune that state-space.
