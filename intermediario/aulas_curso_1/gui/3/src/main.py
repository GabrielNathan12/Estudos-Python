import sys
from main_window import MainWindow
from info import Info
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from display import Display
from styles import setupTheme
from buttons import Button,ButtonsGrid

from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
    
    #Colocando icon no janela
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    
    info = Info()
    window.addWidgetToVLayout(info)
    
    display = Display()
    #display.setStyleSheet('background: #1E90FF; font-size: 30px;')
    display.setPlaceholderText('0')
    window.addWidgetToVLayout(display)

    #Layout dos botoes
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    
    window.show()
    app.exec()

"""
pyinstaller --name="Calculadora" --noconfirm --noconsole --onefile --add-data='../file/;file' --icon='../file/icon.png' --clean --log-level=WARN --distpath="__localcode/dist" --workpath="__localcode/build" --specpath="__localcode/" .\main.py
"""