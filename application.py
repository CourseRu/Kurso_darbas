# imports
import sys
from gui import *
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication


class Db(QMainWindow):
    def __init__(self):
        super().__init__()  # Paveldi metodus ir parametrus is kitos klases (siuo ateju is class QMainWindow)
        self.user_interface = MainWindow()
        self.user_interface.setup_ui(self)  # UI instance metodas is gui

        # Susijungimas su DB
        self.data_base = QtSql.QSqlDatabase.addDatabase("QSQLITE")  # Pridedame DB
        self.data_base.setDatabaseName("darbuotojai.db")  # Db pavadinimas

        # Duomenu parinkimas lentelei (kokius duomenis lentele tures)
        self.db_table = QtSql.QSqlTableModel()  # Prideda koreguojama duomenu modeli, vienai duomenu bazes lentelei
        self.db_table.setTable("Darbuotojai")  # Prideda lentele
        self.db_table.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)  # Nustato, kad modelio
        # pakeitimai is karto butu pritaikyti duomenu bazei
        self.db_table.select()  # Ikelia lenteles duomenis i duomenu modeli
        self.db_table.setHeaderData(0, Qt.Orientation.Horizontal, "ID")  # Kad uzrasas lenteleje eitu horizontaliai
        self.db_table.setHeaderData(1, Qt.Orientation.Horizontal, "Vardas")
        self.db_table.setHeaderData(2, Qt.Orientation.Horizontal, "Pavardė")
        self.db_table.setHeaderData(3, Qt.Orientation.Horizontal, "Gimimo metai")
        self.db_table.setHeaderData(4, Qt.Orientation.Horizontal, "Asmens kodas")

        # Duomenu modelio priskirimas lentelei
        self.user_interface.table_widget.setModel(self.db_table)

        # Mygtuku sujungimas su klases metodais
        self.user_interface.button_add.clicked.connect(self.db_add)  # Sujungimas su db_add (kad leistu prideti)
        self.user_interface.button_add.setShortcut("Return")  # "Prideti" mygtuko shortcut klaviaturoje (Enter)
        self.user_interface.button_update.clicked.connect(self.db_update)  # sujungimas su db_update (kad atnaujint)
        self.user_interface.button_update.setShortcut("F5")  # "Atnaujinti" mygtuko shortcut klaviaturoje (F5)
        self.user_interface.button_delete.clicked.connect(self.db_delete)  # sujungimas su db_delete (kad istrint)
        self.user_interface.button_delete.setShortcut("Del")  # "Panaikinti" mygtuko shortcut klaviaturoje (delete)

        self.item = self.db_table.rowCount()  # Skaiciuoja eiluciu skaiciu lenteleje
        print(self.user_interface.table_widget.currentIndex().row())  # Atspausdina kiek eiluciu yra lenteleje
        self.show()  # Iskvieciam, kad rodytu Widgets

    # Metodas, prideti musu ivestus irasus i lentele
    def db_add(self):
        print(self.item)  # Atspausdina viena eile kai pridedam
        self.db_table.insertRows(self.item, 1)  # Uzpildo tuscia laukeli numeriu, kuri eile cia
        self.db_table.setData(self.db_table.index(self.item, 1), self.user_interface.line_edit_name.text())
        self.db_table.setData(self.db_table.index(self.item, 2), self.user_interface.line_edit_surname.text())
        self.db_table.setData(self.db_table.index(self.item, 4), self.user_interface.line_edit_id.text())
        self.db_table.setData(self.db_table.index(self.item, 3), self.user_interface.birth_date.text())
        self.db_table.submitAll()  # Iveda visus duomenis i lentele kuriuos iraseme
        self.item += 1  # Prideda viena, kad zinotume, jog pridejome dar viena eilute
        self.user_interface.line_edit_name.clear()
        self.user_interface.line_edit_surname.clear()
        self.user_interface.line_edit_id.clear()
        self.user_interface.birth_date.setDate(QtCore.QDate(2000, 10, 10))
        self.user_interface.status_bar.showMessage("Darbuotojas sėkmingai įtrauktas į duomenų bazę.")

    # Metodas, atnaujinti musu ivestus irasus lenteleje, pasirinktoje eiluteje
    def db_update(self):
        if self.user_interface.table_widget.currentIndex().row() > -1:  # Jeigu eilutes index nr didesnis -1, leis
            # atnaujint
            data_record = self.db_table.record(self.user_interface.table_widget.currentIndex().row())  # Jei indexas
            # egzistuoja, tuomet leist atnaujinti irasais kuriuos ivesime
            data_record.setValue("Vardas", self.user_interface.line_edit_name.text())
            data_record.setValue("Pavardė", self.user_interface.line_edit_surname.text())
            data_record.setValue("Gimimo metai", self.user_interface.birth_date.text())
            data_record.setValue("Asmens kodas", self.user_interface.line_edit_id.text())
            self.db_table.setRecord(self.user_interface.table_widget.currentIndex().row(), data_record)  # Atnaujina
            # ivestus irasus
            self.user_interface.line_edit_name.clear()
            self.user_interface.line_edit_surname.clear()
            self.user_interface.line_edit_id.clear()
            self.user_interface.birth_date.setDate(QtCore.QDate(2000, 10, 10))
            self.user_interface.status_bar.showMessage("Darbuotojo duomenys, duomenų bazėje, sėkmingai atnaujinti.")
        else:
            self.user_interface.status_bar.showMessage("Nepasirinktas įrašas!")
            # Jeigu lenteleje nepasirenkame jokios eilutes, ismeta langa, kad turime pasirinkti norint atnaujinti
            QMessageBox.question(self, "Nepasirinktas įrašas!", "Pasirinkite įrašą kurį norite atnaujinti!",
                                 QMessageBox.StandardButton.Ok)
            self.show()  # Iskvieciam, kad rodytu widget

    # Metodas, istrinti musu pasirinkta eilute, lenteleje
    def db_delete(self):
        if self.user_interface.table_widget.currentIndex().row() > -1:  # Jeigu eilutes index nr didesnis, leis istrint
            # kitu atveju reiskia irasas neegzistuoja
            self.db_table.removeRow(self.user_interface.table_widget.currentIndex().row())  # Istrina viena eile
            self.item -= 1  # Istrina jos index
            self.db_table.select()
            self.user_interface.line_edit_name.clear()
            self.user_interface.line_edit_surname.clear()
            self.user_interface.line_edit_id.clear()
            self.user_interface.birth_date.setDate(QtCore.QDate(2000, 10, 10))
            self.user_interface.status_bar.showMessage("Darbuotojo duomenys, duomenų bazėje, sėkmingai ištrinti")
        else:
            self.user_interface.status_bar.showMessage("Nepasirinktas įrašas!")
            # Jeigu lenteleje nepasirenkame jokios eilutes, ismeta langa, kad turime pasirinkt norima istrint eilute
            QMessageBox.question(self, "Nepasirinktas įrašas!", "Pasirinkite įrašą kurį norite ištrinti!",
                                 QMessageBox.StandardButton.Ok)
            self.show()


# App paleidimas
if __name__ == "__main__":  # Leidzia executint koda, jeigu jis paleistas tiesiogiai is failo, o ne importuotas.
    course_program = QApplication(sys.argv)
    form = Db()
    sys.exit(course_program.exec())
