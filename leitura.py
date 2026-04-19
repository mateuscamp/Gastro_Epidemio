from pele import msg_aviso


def leiaint(numero):
    while True:
        try:
            resposta = int(input(numero))
        except (ValueError, TypeError):
            msg_aviso("Digite apenas números")
            continue
        except KeyboardInterrupt:
            msg_aviso("Finalize o programa corretamente")
            continue
        else:
            return resposta


def leiafloat(numero):
    while True:
        try:
            resposta = float(input(numero))
        except (ValueError, TypeError):
            msg_aviso("Digite apenas números")
            continue
        except KeyboardInterrupt:
            msg_aviso("Finalize o programa corretamente")
            continue
        else:
            return resposta
