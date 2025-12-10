from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QColor, QPalette
import sys, random
#modullar lazımi

app = QApplication(sys.argv)

w = QWidget()
w.resize(300, 200)#pəncərə boyu

def change_color():#rəng deyişmə funksiya 
    colors = ["red", "green", "blue", "yellow", "pink", "orange", "gray", "white"]
    c = QColor(random.choice(colors))
    p = w.palette()
    p.setColor(QPalette.Window, c)
    w.setPalette(p)

btn = QPushButton("Rəngi dəyiş")#düyə
btn.clicked.connect(change_color)

layout = QVBoxLayout()
layout.addWidget(btn)#butonu əlavə etmə
w.setLayout(layout)

w.show()
sys.exit(app.exec_())
