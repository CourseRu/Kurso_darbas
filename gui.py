# Imports
from PyQt6 import QtCore, QtGui, QtWidgets
import ctypes  # Leidzia iskviesti funkcijas is kitu programavimo kalbu biblioteku. (Siuo atveju 'C')

# Pridedam savo ikoneliu folderio "resources" path, su pavadinimu "resources". Dabar kelia iki resoures folder galime
# naudoti kaip ('resources:').
# Prefix "addSearchPath", taip pat itraukia ikoneles, kad jos butu rodomos taskbare kai ledziam .exe faila, kuri
# subildinom su pyinstaller.
QtCore.QDir.addSearchPath("resources", "C:/Users/RU/PycharmProjects/kurso_darbas/resources")


class MainWindow(object):
    def __init__(self):
        # Skaitomumo gerinimui, skaitant __init__ norime matyti visus atributus kuriuos turi instance arba kitaip
        # (objektai esantys klaseje: pvz: "def setup_ui")
        self.central_widget = None
        self.group_box = None
        self.label_name = None
        self.line_edit_name = None
        self.label_surname = None
        self.line_edit_surname = None
        self.label_id = None
        self.line_edit_id = None
        self.label_birth_date = None
        self.birth_date = None
        self.calendar_widget = None
        self.table_widget = None
        self.scroll_area = None
        self.scroll_area_widget_contents = None
        self.button_add = None
        self.button_update = None
        self.button_delete = None
        self.status_bar = None

        # UI instance metodas
    def setup_ui(self, main_window):

        # Pagrindinio lango nustatymai
        main_window.setObjectName("main_window")
        main_window.resize(730, 590)  # Programos lango dydis
        main_window.setFont(QtGui.QFont("Calibri"))  # Programos font
        main_window.setWindowIcon(QtGui.QIcon("resources:app_icon.ico"))  # Programos Icon

        # Widgets isdeliojimas
        self.central_widget = QtWidgets.QWidget(main_window)  # Pagrindinis langas
        self.central_widget.setObjectName("central_widget")

        # Group box widget'u grupavimui
        self.group_box = QtWidgets.QGroupBox(self.central_widget)
        self.group_box.setGeometry(QtCore.QRect(0, 0, 721, 261))  # Group box dydis
        self.group_box.setObjectName("group_box")

        # Darbuotojo vardas labelis
        self.label_name = QtWidgets.QLabel(self.group_box)
        self.label_name.setGeometry(QtCore.QRect(10, 20, 241, 16))
        self.label_name.setObjectName("label_name")

        # Darbuotojo vardo ivedimo laukelis
        self.line_edit_name = QtWidgets.QLineEdit(self.group_box)
        self.line_edit_name.setGeometry(QtCore.QRect(10, 40, 411, 20))
        self.line_edit_name.setObjectName("line_edit_name")

        # Darbuotojo pavardes labelis
        self.label_surname = QtWidgets.QLabel(self.group_box)
        self.label_surname.setGeometry(QtCore.QRect(10, 70, 241, 16))
        self.label_surname.setObjectName("label_surname")

        # Darbuotojo pavardes ivedimo laukelis
        self.line_edit_surname = QtWidgets.QLineEdit(self.group_box)
        self.line_edit_surname.setGeometry(QtCore.QRect(10, 90, 411, 20))
        self.line_edit_surname.setObjectName("line_edit_surname")

        # Darbuotojo asmens kodo labelis
        self.label_id = QtWidgets.QLabel(self.group_box)
        self.label_id.setGeometry(QtCore.QRect(10, 120, 261, 16))
        self.label_id.setObjectName("label_id")

        # Darbuotojo asmens kodo ivedimo laukelis
        self.line_edit_id = QtWidgets.QLineEdit(self.group_box)
        self.line_edit_id.setGeometry(QtCore.QRect(10, 140, 411, 20))
        self.line_edit_id.setObjectName("line_edit_id")

        # Darbuotojo gimimo data labelis
        self.label_birth_date = QtWidgets.QLabel(self.group_box)
        self.label_birth_date.setGeometry(QtCore.QRect(10, 180, 241, 16))
        self.label_birth_date.setObjectName("label_birth_date")

        # Darbuotojo gimimo datos pasirinkimo widgetas
        self.birth_date = QtWidgets.QDateEdit(self.group_box)
        self.birth_date.setGeometry(QtCore.QRect(10, 200, 411, 22))
        self.birth_date.setDate(QtCore.QDate(2000, 10, 10))
        self.birth_date.setObjectName("birth_date")

        # Kalendorio widgetas
        self.calendar_widget = QtWidgets.QCalendarWidget(self.group_box)
        self.calendar_widget.setGeometry(QtCore.QRect(430, 30, 281, 191))  # Kalendorio dydis
        self.calendar_widget.setGridVisible(True)  # Kalendorio tinklelis
        self.calendar_widget.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.calendar_widget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat
                                                       .SingleLetterDayNames)
        self.calendar_widget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar_widget.setNavigationBarVisible(True)  # Navigation baras virsuje
        self.calendar_widget.setDateEditEnabled(True)  # Leidzia keisti data
        self.calendar_widget.setObjectName("calendar_widget")

        # Lentele perziureti SQL lenteles duomenis
        self.table_widget = QtWidgets.QTableView(self.central_widget)
        self.table_widget.setGeometry(QtCore.QRect(0, 260, 721, 261))  # Lenteles dydis
        self.table_widget.setObjectName("table_widget")

        # Mygtuku vieta
        self.scroll_area = QtWidgets.QScrollArea(self.central_widget)
        self.scroll_area.setGeometry(QtCore.QRect(0, 520, 721, 41))  # Mygtuku vietos dydis
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        # Mygtuku vietos contentas
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 719, 39))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")

        # Mygtukas prideti
        self.button_add = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_add.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.button_add.setObjectName("button_add")

        # Mygtukas atnaujinti
        self.button_update = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_update.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.button_update.setObjectName("button_update")

        # Mygtukas istrinti
        self.button_delete = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_delete.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.button_delete.setObjectName("button_delete")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        # Widgets centravimas
        main_window.setCentralWidget(self.central_widget)

        # Statuso juosta apacioje
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        # Vercia user interface teksta i kitas kalbas
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # Pasirinktu user interface tekstu vertimas i kitas kalbas
    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Programa"))
        self.group_box.setTitle(_translate("main_window", "Darbuotojai"))
        self.label_name.setText(_translate("main_window", "Darbuotojo vardas:"))
        self.label_surname.setText(_translate("main_window", "Darbuotojo pavardė:"))
        self.label_id.setText(_translate("main_window", "Darbuotojo asmens kodas:"))
        self.label_birth_date.setText(_translate("main_window", "Darbuotojo gimimo data:"))
        self.button_add.setText(_translate("main_window", "Pridėti"))
        self.button_update.setText(_translate("main_window", "Atnaujinti"))
        self.button_delete.setText(_translate("main_window", "Panaikinti"))


# Pasako windowsams, kad cia musu registruota app, del to galesime naudoti savo app icon (Rodys icon taskbare)
my_app = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app)


# # App paleidimas patikrinti ar veikia interface
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     main_window = QtWidgets.QMainWindow()
#     ui = MainWindow()
#     ui.setup_ui(main_window)
#     main_window.show()
#     sys.exit(app.exec())
