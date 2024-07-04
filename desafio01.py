# print("Seu nome contém " + str(len(input('Digite seu Nome:'))) + " caracteres")

# num1 = input("Digite o primeiro número:")
# num2 = input("Digite o segundo número:")

# soma = int(num1) +  int(num2)
# print(soma)

CONSTANTE_BONUS = 1000

Nome_usuario = input('Digite seu Nome:')

salario_usuario = float(input("Digite seu sálario:"))

bonus_usuario = float(input("Digite seu bonus:"))

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario 

print(f"O nome do usuário é: {Nome_usuario} com um salário de  {salario_usuario} tendo um direito ao bonus de {valor_do_bonus}")