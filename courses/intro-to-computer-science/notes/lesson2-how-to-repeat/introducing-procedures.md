# Lesson 2: How to Repeat

# Introducing Procedures

+ Um procedimento(procedure) é algo que recebe entradas(inputs) - pode ter mais de uma entrada. Procedimentos trabalham com as entradas(inputs) e produzem saídas(outputs) como resultado
+ A ideia de procedimento é poderosa, ela nos permite usar pouco código para fazer muitas coisas diferentes.
+ O mesmo código pode operar com entradas diferentes. O que for passado como entrada para o procedimento, ele trabalhará em cima dessa entrada
+ Ele pode fazer diferentes coisas dependendo de tais entradas
+ E ele produz saídas que nos dizem o resultado, baseado no que usamos como entradas.
+ Você já viu coisas bem semelhantes a procedimentos, como por exemplo, operadores: `+ - * / %`
+ O operador `+` tem duas entradas(dois números) e produz uma saída(o resultado da soma dos dois números).
	+ A sintaxe que utilizamos pra ele é diferente por ser um operador. Mas, em termos de ser algo que abstratamente opera com diferentes entradas e produz uma saída correspondente, é basicamente a mesma ideia.

+ Vamos fazer nossos próprios procedimentos. **Python** provê um conceito e uma gramática para fazer isso:

´´´ python
def <name>(<parameters>) :
	<block>
´´´

+ `def` (define)
+ `<name>` é um nome como o nome de uma variável
+ `(<parameter>)` Os parâmetros são separados por virgula (parâmetros são opcionais).
+ `:` Define o começo do `block`(uma sequência de instruções)
+ `block` é o código que queremos executar ao chamar o procedimento. Ele é indentado dentro da `def`(define), normalmente é usado 4 espaços, por convenção.