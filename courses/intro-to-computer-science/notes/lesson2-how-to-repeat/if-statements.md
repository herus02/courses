# Lesson 2: How to Repeat

## If Statements

+ Já sabemos algumas maneiras de fazer comparações, agora vamos usá-las para tomar decisões, para o nosso código fazer coisas diferentes, dependendo do resultado de uma comparação.
+ A maneira de fazer isso é usando um comando `if`
+ A estrutura desse comando é, a palavra reservada `ìf` seguida de uma declaração - que chamamos de  expressão condicional - seguido de `:`

``` python
if <test Expression> :
	<block>
```
+ Dentro do `if` temos um bloco de comandos, esse bloco de comandos será executado caso a expressão condicional seja verdadeira
+ Se a expressão não avalia como true, então o bloco não é executado
+ Sabemos o final do `if` porque usamos indentação
+ Todos os comandos dentro do bloco são executados apenas quando a expressão condicional é `true`. O próximo comando que não é indentado é executado independente da expressão ser `true` ou não

``` python
def absolute(x) :
	if x < 0 :
		x = -x
	return x
```

``` python
def bigger(a, b):
	if a > b:
		return a
	else:
		return b
```

``` python
def bigger(a, b):
	if a > b:
		result = a
	if b > a:
		result = b
	return result
```