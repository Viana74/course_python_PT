"""
Documentação
Introdução a tratamento de excessão
"""

# isnumeric, isdigit e isdecimal

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# Verifica se a string tem só numeros inteiro e estes são positivos
#print(num1.isnumeric())
#print(num2.isnumeric())


"""
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 * num2)
else:
    print('Não pude converter os numeros e gerar o resultado')
#print(int(num1) + int(num2))
"""

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1+num2)
except:
    print('ERROR')