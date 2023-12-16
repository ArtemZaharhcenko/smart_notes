from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QTextEdit, QPushButton, QListWidget, QInputDialog, QMessageBox

import json

app = QApplication([])
window = QWidget()

text = QTextEdit()
lineText = QLineEdit()
notes_list = QListWidget()
tags_list = QListWidget()

mainline = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()

create_btn = QPushButton("Create note")
btn_save = QPushButton("Save")
delete_btn = QPushButton("Delete")

window.setStyleSheet('''background-color: #DDA0DD''')
create_btn.setStyleSheet('''background-color: #0000CD''')
btn_save.setStyleSheet('''background-color: #FFFF00''')
delete_btn.setStyleSheet('''background-color: #0000CD''')

create_btn2 = QPushButton("Add tag")
btn_save2 = QPushButton("Delete tag")
delete_btn2 = QPushButton("search")

create_btn2.setStyleSheet('''background-color: #FFFF00''')
btn_save2.setStyleSheet('''background-color: #0000CD''')
delete_btn2.setStyleSheet('''background-color: #FFFF00''')

line1.addWidget(text)
line2.addWidget(notes_list)
line2.addWidget(create_btn)

h_line = QHBoxLayout()

h_line.addWidget(btn_save)
h_line.addWidget(delete_btn)


line2.addLayout(h_line)


line2.addWidget(tags_list)
line2.addWidget(lineText)
line2.addWidget(create_btn)

line2.addWidget(create_btn2)


h_line2 = QHBoxLayout()

h_line2.addWidget(btn_save2)
h_line2.addWidget(delete_btn2)

line2.addLayout(h_line2)

mainline.addLayout(line1, stretch=2)
mainline.addLayout(line2, stretch=1)

window.setLayout(mainline)

def writeFile():
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=True, sort_keys=True, indent=4)


def save_note():
    try:
        note_text = text.toPlainText()
        note_name = notes_list.currentItem().text()

        notes[note_name]['text'] = note_text
        writeFile()
    except:
        msg = QMessageBox(window, text="Виберіть замітку")
        msg.show()

notes = {}

def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова замітка", "Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {
            "text": "",
            "tags": [],
        }
        notes_list.addItem(note_name)

def show_note():
    note_name = notes_list.currentItem().text()
    text.setText(notes[note_name]['text'])

    tags_list.clear()
    tags_list.addItems(notes[note_name]['tags'])

def add_tag():
    note_name = notes_list.currentItem().text()
    tag = lineText.text()

    notes[note_name]["tags"].append(tag)
    tags_list.addItem(tag)
    writeFile() 

create_btn2.clicked.connect(add_tag)

def del_tag():
    try:
        note_name = notes_list.currentItem().text()
        tag_name = tags_list.currentItem().text()

        notes[note_name]["tags"].remove(tag_name)

        tags_list.clear()
        tags_list.addItems(notes[note_name]['tags'])

        writeFile()
    except:
        msg = QMessageBox(window, text="Виберіть тег")
        msg.show()


def del_note():
    try:
        note_name = notes_list.currentItem().text()

        del notes[note_name]

        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes)

        writeFile()
    except:
        msg = QMessageBox(window, text="Виберіть замітку")
        msg.show()



def search_note_bytag():
    tag = lineText.text()

    if(delete_btn2.text()=="Search"):
        filtered = {}
        for key in notes:
            if tag in notes[key]['tags']:
                print(notes[key])
                filtered[key] = notes[key]
        notes_list.clear()
        notes_list.addItems(filtered)
        tags_list.clear()
        lineText.clear()
            
        delete_btn2.setText("Відмінити пошук")
    else:
        delete_btn2.setText("Search")
        notes_list.clear()
        notes_list.addItems(notes)
        tags_list.clear()

delete_btn2.clicked.connect(search_note_bytag)




btn_save2.clicked.connect(del_tag)

delete_btn.clicked.connect(del_note)

notes_list.itemClicked.connect(show_note)
try:
    with open("notes.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    print("File not found")

notes_list.addItems(notes)

create_btn.clicked.connect(add_note)

btn_save.clicked.connect(save_note)

window.show()
app.exec_()