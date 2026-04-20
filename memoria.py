import pele


def buscarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "rt") as _:  # não vou usar Variavel
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "wt+") as _:  # não vou usar Variavel
            pass
    except Exception:
        print(
            "\033[31mErro na criação do arquivo\033[m"
        )  # Se houver erro inexperado ou falta de memoria
    else:
        print(f"\033[32m{nome_arquivo} criado com sucesso!\033[m")


def leiarquivo(nome_arquivo):
    try:
        pacientes = []
        with open(nome_arquivo, "rt") as a:
            for linha in a:
                dado = linha.replace("\n", "").split(";")
                pacientes.append(
                    [dado[0], dado[1]]
                )  # empacota nome e idade em uma mini-lista

        return pacientes

    except Exception:
        pele.msg_erro("Erro ao ler o arquivo")
        return []  # Retorna lista vazia em caso de erro


def cadastrarquivo(
    nome_arquivo, nome="desconhecido", idade=0, sexo="desconhecido", polipo=0
):
    try:
        with open(nome_arquivo, "at") as a:
            try:
                a.write(f"{nome};{str(idade)};{sexo};{str(polipo)}\n")

            except Exception:
                pele.msg_erro("Houve um erro na escrita dos dados")

    except Exception:
        pele.msg_erro("Erro na abertura do banco de dados")


def ordenarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "rt") as a:
            linhas = a.readlines()  # Variavel linhas guarda a lista
            linhas.sort()
        with open(nome_arquivo, "wt") as a:
            a.writelines(linhas)

    except Exception as e:
        pele.msg_erro(f"Erro ao organizar o arquivo: {e}")


def buscarpaciente(nome_arquivo, nome_procurado):
    try:
        with open(nome_arquivo, "rt") as a:
            for linha in a:
                dado = linha.strip().split(";")
                if dado[0].upper() == nome_procurado.upper():
                    return dado

    except Exception:
        pele.msg_erro("Erro ao buscar. Por favor, tente novamente")

    return None  # se o loop acabar sem o dado


def editarquivo(
    nome_arquivo,
    nome_procurado,
    nome_novo="desconhecido",
    idade_nova=0,
    sexo_novo="desconhecido",
    polipo_novo=0,
):
    try:
        with open(nome_arquivo, "rt") as a:  # carrega na memoria
            linhas = a.readlines()

        for i, linha in enumerate(linhas):  # procura quem vai ser editado
            dado = linha.strip().split(";")
            if dado[0].upper() == nome_procurado.upper():
                linhas[i] = f"{nome_novo};{idade_nova};{sexo_novo};{polipo_novo}\n"
                break  # achou/trocou = sai do loop

        with open(nome_arquivo, "wt") as a:  # salva a lista atualizada
            a.writelines(linhas)

    except Exception:
        pele.msg_erro("Erro ao editar cadastro")


def excluicadastro(nome_arquivo, nome_procurado):
    try:
        with open(nome_arquivo, "rt") as a:
            linhas = a.readlines()

        for linha in linhas:
            dado = linha.strip().split(";")
            if dado[0].upper() == nome_procurado.upper():
                linhas.remove(linha)
                break

        with open(nome_arquivo, "wt") as a:
            a.writelines(linhas)

    except Exception:
        pele.msg_erro("Erro ao excluir cadastro")
