from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

def setupTheme(app):
    app.setStyleSheet(f"""
        MainWindow {{
            background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(173, 216, 230, 1), stop:1 rgba(10, 10, 10, 1));
        }}
        QPushButton[cssClass="specialButton"] {{
            color: #fff;
            background: {PRIMARY_COLOR};
        }}
        QPushButton[cssClass="specialButton"]:hover{{
            color: #fff;
            background: {DARKER_PRIMARY_COLOR};
        }}
        QPushButton[cssClass="specialButton"]:pressed {{
            color: #fff;
            background: {DARKEST_PRIMARY_COLOR};
        }}
    """
    )