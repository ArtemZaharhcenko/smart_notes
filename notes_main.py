from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton , QLabel, QHBoxLayout , 
QVBoxLayout , QListWidget ,QTextEdit , QInputDialog )

#затем запрограммируй демо-версию функционала
app = QApplication([])

main_window = QWidget()

main_window.setWindowTitle("Нотатки")
main_window.resize(1000,1000)


dobavyty = QPushButton("добавити замітку")
vidnyty = QPushButton("забрати замітку")
zberehty = QPushButton('ЗБЕРЕГТИ')


pole = QTextEdit()
cpysok = QListWidget()

notes = {}
def add() :
    text,ok = QInputDialog.getText(main_window, "додати замітку", "назва замітки")
    if ok and text != '': 
        cpysok.addItem(text)
        notes[text] = ""


def show_note():
    key = cpysok.selectedItems()[0].text()
    pole.setText(notes[key])

def save_note():
    defolt = cpysok.selectedItems()[0].text()
    notes[defolt] = pole.toPlainText()
    print(notes)




zamitky = QLabel("Замітки")

prylehli = QHBoxLayout()
kolonka2 = QVBoxLayout()
kolonka1 = QVBoxLayout()

cpysok = QListWidget()
pole = QTextEdit()


kolonka1.addWidget(zamitky)
kolonka1.addWidget(pole)

kolonka2.addWidget(dobavyty)
kolonka2.addWidget(vidnyty)
kolonka2.addWidget(zberehty)
kolonka2.addWidget(cpysok)

prylehli.addLayout(kolonka1, stretch=2)
prylehli.addLayout(kolonka2, stretch=1)

main_window.setLayout(prylehli)


dobavyty.clicked.connect(add)
zberehty.clicked.connect(save_note)
cpysok.itemClicked.connect(show_note)

main_window.show()
app.exec_()