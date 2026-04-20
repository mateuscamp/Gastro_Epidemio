import pele


def buscarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "rt") as _: # não vou usar Variavel
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "wt+") as _: # não vou usar Variavel
            pass
    except Exception:
        print(
            "\033[31mErro na criação do arquivo\033[m"
        )  # Se houver erro inexperado ou falta de memoria
    else:
        print(f"\033[32m{nome_arquivo} criado com sucesso!\033[m")


def leiarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "rt") as a:
            for linha in a:
                dado = linha.replace("\n", "").split(';')
                print(f"{dado[0]:<30}{dado[1]:>3} anos")

    except Exception:
        pele.msg_erro("Erro ao ler o arquivo")


def cadastrarquivo(nome_arquivo, nome="desconhecido", idade="0", polipo="0"):
    try:
        with open(nome_arquivo, "at") as a:
            try:
                a.write(f"{nome};{idade};{polipo}\n")

            except Exception:
                pele.msg_erro("Houve um erro na escrita dos dados")

    except Exception:
        pele.msg_erro("Houve um erro na abertura do banco de dados")


def ordenarquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt') as a:
            linhas = a.readlines() # Variavel linhas guarda a lista
            linhas.sort()
        with open(nome_arquivo, 'wt') as a:
            a.writelines(linhas)

    except Exception as e:
        pele.msg_erro(f'Erro ao organizar o arquivo: {e}')


def buscarpaciente(nome_arquivo, nome_procurado):
    try:
        with open(nome_arquivo, 'rt') as a:
            for linha in a:
                dado = linha.strip().split(';')
                if dado[0].upper() == nome_procurado.upper():
                    return dado
    except Exception:
        pele.msg_erro('Erro ao buscar. Por favor, tente novamente')
    return pele.msg_aviso('Não encontrado') # se o loop acabar sem o dado


def editarquivo(nome_arquivo, nome, idade, polipo):
    try:
        with open(nome_arquivo, 'wt') as a:
        
