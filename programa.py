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
        dados_paciente = memoria.leiarquivo(arquivo_bd)  # pede os dadps para a memoria

        if dados_paciente:  # Verifica se a lista não está vazia
            pele.listar(dados_paciente)
        else:
            pele.msg_aviso("Ainda não há pacientes cadastrados")

    elif opçao == 2:
        pele.cabeçalho("NOVO CADASTRO")
        nome = input("Nome: ").strip().upper()
        idade = leiaint("Idade: ")
        while True:
            sexo = input("Sexo [M/F]: ").strip().upper()[0]
            if sexo in "M/F":
                break
            else:
                pele.msg_aviso("Favor preencher com um parâmetro válido.")
        polipo = leiaint("Polipo(s): ")
        memoria.cadastrarquivo(arquivo_bd, nome, idade, sexo, polipo)
        memoria.ordenarquivo(arquivo_bd)
        pele.msg_sucesso("Cadastro concuído com sucesso!")

    elif opçao == 3:
        pele.cabeçalho("EDITAR CADASTRO")
        nome_busca = input(
            "Nome completo do paciente que deseja \033[33mEDITAR\033[m: "
        )
        resultado = memoria.buscarpaciente(arquivo_bd, nome_busca)
        if resultado:  # não precisa coloca ==True (se retornar None entao é ==False)
            pele.msg_sucesso(
                f"Cadastro encontrado: {resultado[0]}, {resultado[1]} anos, Sexo: {resultado[2]}, {resultado[3]} polipo(s)"
            )
            pele.msg_aviso("Digite os novos dados")
            nome_novo = input("Nome: ").strip().upper()
            idade_nova = leiaint("Idade: ")
            sexo_novo = input("Sexo [M/F]: ").strip().upper()[0]
            polipo_novo = leiaint("Polipo(s): ")
            memoria.editarquivo(
                arquivo_bd, nome_busca, nome_novo, idade_nova, polipo_novo
            )
            pele.msg_sucesso("Cadastro alterado com sucesso!")
        else:
            pele.msg_aviso("Cadastro não encontrado")

    elif opçao == 4:
        pele.cabeçalho("EXCLUIR CADASTRO")
        nome_busca = input(
            "Nome completo do cadastro que deseja \033[1;31mEXCLUIR\033[m: "
        )
        resultado = memoria.buscarpaciente(arquivo_bd, nome_busca)
        if resultado:
            pele.msg_sucesso(
                f"Cadastro encontrado: {resultado[0]}, {resultado[1]} anos, {resultado[2]} polipo(s)"
            )
            pele.submenu()
            sub_opcao = leiaint("Sua opção: ")
            if sub_opcao == 1:
                memoria.excluicadastro(arquivo_bd, nome_busca)
                pele.msg_sucesso("Cadastro excluído com sucesso")
            elif sub_opcao == 2:
                continue

    elif opçao == 5:
        pele.msg_sucesso("Obrigado por usar o programa. Até logo!")
        break

    else:
        pele.msg_erro("Digite uma opção válida!")

    sleep(1.5)
