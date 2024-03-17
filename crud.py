import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView


class DataTableCode(QWidget):

    index = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('crud_box.ui', self)
        self.show()
        self.insert_data_into_table()
        self.saveButton.clicked.connect(self.save)

    
    def save(self):
        name = self.name.text()
        mobile = self.mobile.text()
        email = self.email.text()

        self.data_table.insertRow(self.index)
        self.data_table.setItem(self.index, 0, QTableWidgetItem(f"{self.index}"))
        self.data_table.setItem(self.index, 1, QTableWidgetItem(name))
        self.data_table.setItem(self.index, 2, QTableWidgetItem(mobile))
        self.data_table.setItem(self.index, 3, QTableWidgetItem(email))
        self.data_table.update()

        self.index = self.index + 1
    
    def insert_data_into_table(self):
        self.data_table.verticalHeader().setVisible(False)
        header = self.data_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
    

def run():
    app = QApplication(sys.argv)
    ui_app = DataTableCode()
    sys.exit(app.exec())


run()
