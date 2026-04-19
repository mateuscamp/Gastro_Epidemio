import pele


def buscarquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, "wt+")
    except Exception:
        print(
            "\033[31mErro na criação do arquivo\033[m"
        )  # Se houver erro inexperado ou falta de memoria
    else:
        print(f"\033[32m{nome_arquivo} criado com sucesso!\033[m")
        a.close()


def leiarquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, "rt")
    except Exception:
        pele.msg_erro("Erro ao ler PESSOAS CADASTRADAS")
    else:
        for linha in a:
            dado = linha.replace("\n", "")
            dado = dado.split(";")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        a.close()


def cadastrarquivo(nome_arquivo, nome="desconhecido", idade="0", polipo="0"):
    try:
        a = open(nome_arquivo, "at")
    except Exception:
        pele.msg_erro("Houve um erro na abertura do banco de dados")
    else:
        try:
            a.write(f"{nome};{idade};{polipo}\n")
        except Exception:
            pele.msg_erro("Houve um erro na escrita dos dados")
        else:
            a.close()


def editarquivo(nome_arquivo, nome, idade, polipo):
    try:
        a = open(nome_arquivo, 'wt+')
