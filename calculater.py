import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QDialog, QDialogButtonBox
from PyQt6.QtGui import QFont
from client import check_serial_key  # Import for license check

class SerialKeyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Serial Key Verification')
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()

        self.label = QLabel('Enter your serial key:')
        layout.addWidget(self.label)

        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def get_key(self):
        return self.key_input.text()

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFont(QFont('Arial', 24))
        layout.addWidget(self.display)
        
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]
        
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFont(QFont('Arial', 18))
            button.clicked.connect(self.on_click)
            grid.addWidget(button, row, col)
        
        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        sender = self.sender().text()
        if sender == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    serial_dialog = SerialKeyDialog()
    if serial_dialog.exec() == QDialog.DialogCode.Accepted:
        user_key = serial_dialog.get_key()
        if check_serial_key(user_key):
            calc = Calculator()
            calc.show()
        else:
            QMessageBox.critical(None, 'Invalid Serial Key', 'The entered serial key is invalid or has expired.')
            sys.exit(1)
    else:
        sys.exit(1)

    sys.exit(app.exec())
