# Lesson 2: How to Repeat

## Using Procedures

+ Para usar um procedimento, nós precisamos do nome do procedimento seguido de uma lista entradas. Essas entradas são, algumas vezes, chamadas de operandos ou argumentos.
+ `string.find('sub')` find é um pouco diferente dos procedimentos que vamos criar. Em primeiro lugar, find é pré-definido, em segundo é que em vez de ter apenas `find` nós temos `string.find`

````python
def rest_of_string(s) :
	return s[1:]
```

+ Para usar o procedimento acima podemos fazer o seguinte: `print rest_of_string("audacity")`
+ Quando chamamos um procedimento, ele desvia para executar o código que está dentro do procedimento. E ele vai atribuir aos parâmetros os valores  que são passados como entrada
+ `return` significa que vamos voltar para onde o procedimento foi chamado, retornando um valor
+ Tudo o que vamos fazer no resto do curso e quase tudo que todo mundo faz em programação de computadores tem a ver com definir e usar procedimentos
+ Podemos pensar em nossos procedimentos em termos de mapeamento de entradas em saídas
+ Temos entradas vindo por meio dos nossos olhos, por meio da boca e até pelo nosso nariz
+ Python usa o valor especial None para indicar que não há nenhum valor
+ Se passarmos variáveis como argumento, isso não muda os valores dessa variáveis
+ os parâmetros e variáveis de um procedimento são acessíveis somente dentro do procedimento
