"""JAC_AI.py"""

import requests, json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Configurations import menu_config

# sys.path.insert(0, "core-api\core_api")


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 780)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("Designs/JAC AI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        Dialog.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 371, 221))
        self.label_2.setStyleSheet("border-image: url(Designs/JAC AI.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 240, 371, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.expense = QtWidgets.QWidget()
        self.expense.setObjectName("expense")
        self.comboBox = QtWidgets.QComboBox(self.expense)
        self.comboBox.setGeometry(QtCore.QRect(150, 120, 161, 22))
        self.comboBox.setObjectName("comboBox")
        for item in menu_config.expense_type_menu:
            self.comboBox.addItem(item)
        self.label = QtWidgets.QLabel(self.expense)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 14))
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.expense)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 160, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        for item in menu_config.accounts:
            self.comboBox_2.addItem(item)
        self.label_7 = QtWidgets.QLabel(self.expense)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 55, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.expense)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 80, 161, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.expense)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.expense)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.expense)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 50, 161, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.expense)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.expense)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.expense)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.expense)
        self.dateEdit.setGeometry(QtCore.QRect(150, 210, 161, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.dateEdit.setObjectName("dateEdit")
        self.tabWidget.addTab(self.expense, "")
        self.account = QtWidgets.QWidget()
        self.account.setObjectName("account")
        self.label_8 = QtWidgets.QLabel(self.account)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 81, 14))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.account)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 20, 161, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(self.account)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 55, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.account)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 50, 161, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.account)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.account)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 161, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.account)
        self.textBrowser.setGeometry(QtCore.QRect(20, 140, 331, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.account, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 40, 181, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.settings)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.settings)
        self.label_11.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 80, 181, 22))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.settings)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 55, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 120, 181, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_13 = QtWidgets.QLabel(self.settings)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 55, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_10.setGeometry(QtCore.QRect(130, 160, 181, 22))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.settings)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 200, 181, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.settings, "")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 540, 281, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 570, 371, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 540, 81, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 500, 160, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(self.put_expense)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def show_information(self, message, info_text, title_name):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(message)
        msg.setInformativeText(info_text)
        msg.setWindowTitle(title_name)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def put_expense(self):
        headers = {"content-type": "application/json"}
        data = {
            "account": self.comboBox_2.currentText(),
            "description": self.lineEdit_3.text(),
            "expense_amt": self.lineEdit_2.text(),
            "expense_type": self.comboBox.currentText(),
            "spend_to": self.lineEdit.text(),
            "date": str(self.dateEdit.text()),
        }
        url = "http://127.0.0.1:8000/expenses/"
        response = requests.put(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            self.show_information("Added", "Added Expense details", "Expense Details")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "JAC AI"))
        self.label.setText(_translate("Dialog", "Spend to"))
        self.label_7.setText(_translate("Dialog", "Date"))
        self.label_4.setText(_translate("Dialog", "Description"))
        self.label_6.setText(_translate("Dialog", "Account"))
        self.label_3.setText(_translate("Dialog", "Amount"))
        self.label_5.setText(_translate("Dialog", "Type"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.expense),
            _translate("Dialog", "Expense Tracker"),
        )
        self.label_8.setText(_translate("Dialog", "Balance"))
        self.label_9.setText(_translate("Dialog", "Account"))
        self.pushButton.setText(_translate("Dialog", "Add Account"))
        self.pushButton_2.setText(_translate("Dialog", "Delete Account"))
        self.textBrowser.setPlaceholderText(
            _translate("Dialog", "Connecting Cloud Service ...")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.account),
            _translate("Dialog", "Accounts Settings"),
        )
        self.lineEdit_7.setText(menu_config.server_ip)
        self.label_10.setText(_translate("Dialog", "Server IP"))
        self.label_11.setText(_translate("Dialog", "Port"))
        self.lineEdit_8.setText(menu_config.server_port)
        self.label_12.setText(_translate("Dialog", "User"))
        self.lineEdit_9.setText(_translate("Dialog", "Akhil Jacob"))
        self.label_13.setText(_translate("Dialog", "Status"))
        self.pushButton_4.setText(_translate("Dialog", "Test Connection"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.settings), _translate("Dialog", "Settings")
        )
        self.lineEdit_6.setPlaceholderText(
            _translate("Dialog", "You can ask JAC AI for suggestions here")
        )
        self.pushButton_3.setText(_translate("Dialog", "Go"))
        self.pushButton_5.setText(_translate("Dialog", "Add"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
