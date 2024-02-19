from abc import ABC, abstractclassmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractclassmethod
    def enviar(self) -> bool:
        ...


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS enviado: ', self.msg)
        return True

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail enviado: ', self.msg)
        return True


def notificar(notificar: Notificacao):
    notificar_enviada = notificar.enviar()

    if notificar_enviada:
        print('FOi enviada')
    else:
        print('Nao enviada')


notificar(NotificacaoEmail('Enviando email'))
notificar(NotificacaoSMS('Enviando SMS'))
