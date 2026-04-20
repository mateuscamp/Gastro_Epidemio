import pele
import memoria
from leitura import leiaint
from time import sleep

arquivo_bd = "dados.txt"

if not memoria.buscarquivo(arquivo_bd):
    memoria.criarquivo(arquivo_bd)

while True:
    pele.menu()
    opçao = leiaint("Sua opção: ")

    if opçao == 1:
        pele.cabeçalho("PESSOAS CADASTRADAS")
        memoria.leiarquivo(arquivo_bd)

    elif opçao == 2:
        pele.cabeçalho("NOVO CADASTRO")
        nome = input("Nome: ").strip().upper()
        idade = leiaint("Idade: ")
        polipo = leiaint("Polipo: ")
        memoria.cadastrarquivo(arquivo_bd, nome, idade, polipo)
        memoria.ordenarquivo(arquivo_bd)
        pele.msg_sucesso("Cadastro concuído com sucesso!")

    elif opçao == 3:
        pele.cabeçalho("EDITAR CADASTRO")
        nome = input("Nome completo do paciente que deseja editar:")
        memoria.buscarpaciente(arquivo_bd)

    elif opçao == 4:
        pele.cabeçalho("EXCLUIR CADASTRO")

    elif opçao == 5:
        pele.msg_sucesso("Obrigado por usar o programa. Até logo!")
        break

    else:
        pele.msg_erro("Digite uma opção válida!")

    sleep(2)
