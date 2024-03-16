import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QGridLayout, QMainWindow

@Slot()
def slot_example(status_bar):
    status_bar.showMessage('Mostre a mensagem')
@Slot()
def outro_sloot(checked):
    print('Está marcado', checked)
@Slot()
def terceiro_sloot(action):
    def inner():
        outro_sloot(action.isChecked())
    return inner


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Esse é um título')

botao = QPushButton('Botão 1')
botao.setStyleSheet('font-size: 40px; color: red')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px; color: blue')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px; color: black')

central_widget = QWidget()
window.setCentralWidget(central_widget)

layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(botao,1,1,1,1)
layout.addWidget(botao2,1,2,1,1)
layout.addWidget(botao3,3,1,1,2)

status_bar = window.statusBar()
status_bar.showMessage('Uma mensagem')

menu = window.menuBar()
prineiro_menu = menu.addMenu('Primeiro Menu')

primeira_acao = prineiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

segunda_acao = prineiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_sloot)
segunda_acao.hovered.connect(terceiro_sloot(segunda_acao))
botao.clicked.connect(terceiro_sloot(segunda_acao))

window.show()
app.exec()

