# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(n1, n2, n3):
	if n1 > n2 and n1 > n3:
    	return n1
  	else:
    	if n2 > n1 and n2 > n3:
      		return n2
    	else:
      		return n3

print biggest(3, 6, 9)

# def bigger(a, b):
# 	if a > b:
# 		return a	
#	else:
#		return b
#
# def biggest(a, b, c):
# 	return bigger(bigger(a, b), c)

# procedimento pré-definido
# print max(9,32,16)
# >>> 32

# Para todo procedimento pré-definido em Python, nós poderiamos defini-los nós mesmo.
# Tudo que pode ser computado mecanicamente por uma máquina, pode ser descrito por um programa
# que usa apenas coisas como procedimentos, aritmética simples, comparações e comandos if.
# Isso é uma coisa muito impressionante! Porque com poucas operações muito simples,
# você pode simular qualquer outra operação.
# Você já viu neste curso operações aritméticas, comparações, definição e chamada de procedimentos
# como usar comandos if para tomada de decisão
# Isso é o suficiente para fazer qualquer computação(cálculo)


#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9