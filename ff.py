from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QListWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle("Розумні замітки")
window.resize(900,600)
window.move(600,300)


text = QTextEdit()
text.setText ("Додаток")
notes1 = QLabel("Список заміток")
notes2 = QLabel("Список тегів")

but1 = QPushButton("Створити замітку")
but1.setStyleSheet("background-color:skyblue; font-size:15px; color:green; border: 1px solid yellow;")
but2 = QPushButton("Вдалити замітку")
but3 = QPushButton("Зберегти замітку")
but4 = QPushButton("Додати до замітки")
but5 = QPushButton("Відкріпити від замітки")
but6 = QPushButton("Шукати замітки по тегу")

items1 = QListWidget()
items2 = QListWidget()
line = QLineEdit()
line = QLineEdit()
line.setPlaceholderText("Введіть тег...")

line_main = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()

lineV1.addWidget(text)
lineH1.addWidget(but1)
lineH1.addWidget(but2)
lineH2.addWidget(but4)
lineH2.addWidget(but5)

lineV2.addWidget(notes1)
lineV2.addWidget(items1)
lineV2.addLayout(lineH1)
lineV2.addWidget(but3)
lineV2.addWidget(notes2)
lineV2.addWidget(items2)
lineV2.addWidget(line)
lineV2.addLayout(lineH2)
lineV2.addWidget(but6)

line_main.addLayout(lineV1, stretch=2)
line_main.addLayout(lineV2, stretch=1)
window.setLayout(line_main)
window.show()
app.exec_()
