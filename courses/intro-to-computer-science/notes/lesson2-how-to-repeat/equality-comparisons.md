# Lesson 2: How to Repeat

## Equality Comparisons

+ Tudo o que fizemos até agora foi bastante limitado - fizemos as mesmas coisas para todos os dados. Não pudemos fazer nada que realmente dependa do que os dados sejam.
+ Vamos aprender uma maneira de fazer o código se comportar de modo diferente, com base em decisões.
+ A primeira coisa que vamos fazer é como fazer comparações, de modo que tenhamos uma maneira de testar, e decidir o que fazer.
+ Python provê muitos operadores diferentes para fazer comparações.
	+ Existem operadores similares aos que usamos na matemática: `<` `>` `<=` `>=` Que comprara 2 números.
	+ `<number> <operador> <number>` Isso é muito semelhante ao que vimos anteriormente, para expressões aritméticas `+` `-` `*` `/`
	+ O resultado de uma comparação é um `Boolean`
	+ Um `Boolean` pode ser somente um valor de dois possíveis. Ele pode ser o valor `true`, ou o valor `false`
	+ `print 2 < 3` `>>> true`
	+ `print 21 < 3` `>>> false`
	+ `print 7 * 3 < 21` `>>> false`
	+ `print 7 * 3 != 21` `>>> false`
	+ `print 7 * 3 == 21` `>>> true`
