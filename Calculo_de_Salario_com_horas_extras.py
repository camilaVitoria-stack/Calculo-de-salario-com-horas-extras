#trabalho  Cálculo de Salário com Horas Extras
#horas normais hnor
#horas extras = hex
#percentual = he
#valor da hora = vh
#nm = nome 
# entradas de dados
linha = "-"*50
cor = '\033[1;32;41m'
fim = '\033[0m'
tit = "DADOS FORNECIDOS"
tit2 = "CALCULO"
tit3 = "AVISO"
print(linha)
print(f'{cor}{tit3:^50}{fim}')
print(linha)
print("Até 160 horas/mês são consideradas normais.")
print("160 horas/mês = 8 horas por dia (na escala 5x2)")
print("Horas acima de 160 são calculadas como extras (+50%).")
print(linha)
nm = input("Digite o seu nome: ")
hnor = float(input("Digite as horas trabalhadas no mês: "))
vh = float(input("Digite o valor da hora: "))
he = 50
import os
# processamento
if hnor > 160:
    hex = hnor - 160
    hnor_normais = 160
else:
    hex = 0
    hnor_normais = hnor
# cálculos
salsem = hnor_normais * vh
valor_hora_extra = vh * (1 + (he/100))
valorex = hex * valor_hora_extra
salcom = salsem + valorex
os.system('cls' if os.name == 'nt' else 'clear')
# saída de dados
print(linha)
print (f'{cor}{tit:^50}{fim}')
print(linha)
print("Horas trabalhadas:", hnor)
print(linha)
print(f'{cor}{tit2:^50}{fim}')
print(linha)
print("Nome do funcionário:", nm)
print("Total de horas normais:", hnor_normais)
print("Total de horas extras:", hex)
print("Salário bruto final: R$", round(salcom, 2))
print(linha)
input("\nPressione ENTER para finalizar...")