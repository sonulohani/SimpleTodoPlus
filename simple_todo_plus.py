import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
)

from PySide2.QtCore import QObject, Qt


class SimpleTodoPlus(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.todo_list_widget = QListWidget(self)

        self.add_todo_btn = QPushButton("Add Todo", self)
        self.add_todo_btn.clicked.connect(self.add_todo_btn_clicked)

        self.remove_todo_btn = QPushButton("Remove Todo", self)
        self.remove_todo_btn.clicked.connect(self.remove_todo_btn_clicked)

        self.clear_todo_btn = QPushButton("Clear Todo", self)
        self.clear_todo_btn.clicked.connect(self.clear_todo_btn_clicked)

        vbox_layout = QVBoxLayout(self)
        vbox_layout.addWidget(self.todo_list_widget)

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.add_todo_btn)
        hbox_layout.addWidget(self.remove_todo_btn)
        hbox_layout.addWidget(self.clear_todo_btn)

        vbox_layout.addLayout(hbox_layout)

    def add_todo_btn_clicked(self):
        item = QListWidgetItem(f"Todo {self.todo_list_widget.count() + 1}")
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEditable)
        item.setCheckState(Qt.Unchecked)
        self.todo_list_widget.addItem(item)

    def remove_todo_btn_clicked(self):
        if self.todo_list_widget.count():
            self.todo_list_widget.takeItem(self.todo_list_widget.currentRow())

    def clear_todo_btn_clicked(self):
        self.todo_list_widget.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = SimpleTodoPlus()
    window.show()
    sys.exit(app.exec_())
