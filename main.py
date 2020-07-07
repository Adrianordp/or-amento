# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget, QComboBox, QGroupBox, QPushButton, QMainWindow, QTextEdit, QLineEdit, QLayout, QGridLayout, QLabel, QSpinBox
from PySide2.QtCore import QObject, SIGNAL
# sfrom PySide2.QtGui import *

orderNumber  = 1;
tradicionals = ['Calabresa', 'Frango', 'Margerita', 'Mista', 'Mussarela']
specials     = ['Frango com catupiry', 'Portuguesa', '']
premiums     = ['Pepperoni']

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Widget object
        self.mainWidget = QWidget()
        # Layout object
        self.mainLayout = QGridLayout(self.mainWidget)

        self.infoGroup  = QGroupBox()
        self.comboGroup = QGroupBox()
        self.endGroup   = QGroupBox()

        self.mainLayout.addWidget(self.infoGroup, 0, 0)
        self.mainLayout.addWidget(self.comboGroup, 1, 0)
        self.mainLayout.addWidget(self.endGroup, 2, 0)

        self.setCentralWidget(self.mainWidget)

#        # Creating button objects
        self.labelClient  = QLabel("Cliente:") ; self.editClient   = QLineEdit()
        self.labelPhone   = QLabel("Telefone:"); self.editPhone    = QLineEdit()
        self.labelAddr    = QLabel("Endereço:"); self.editAddr     = QLineEdit()
        self.labelBurgh   = QLabel("Bairro:")  ; self.editBurgh    = QLineEdit()
        self.labelAllergy = QLabel("Alergia")  ; self.editAllergy  = QLineEdit()
        self.labelObs     = QLabel("Obs.:")    ; self.editObs      = QLineEdit()

#        self.editObs.setFixedHeight(40)

        self.labelQtd = QLabel("Qtd."); self.labelItem = QLabel("Item"); self.labelPriceU  = QLabel("Preço u."); self.labelPriceT  = QLabel("Preço t.")
        self.editQtd1 = QSpinBox()    ; self.combo1    = QComboBox()   ; self.labelPriceU1 = QLabel("R$ 0,00") ; self.labelPriceT1 = QLabel("R$ 0,00")
        self.editQtd2 = QSpinBox()    ; self.combo2    = QComboBox()   ; self.labelPriceU2 = QLabel("R$ 0,00") ; self.labelPriceT2 = QLabel("R$ 0,00")
        self.editQtd3 = QSpinBox()    ; self.combo3    = QComboBox()   ; self.labelPriceU3 = QLabel("R$ 0,00") ; self.labelPriceT3 = QLabel("R$ 0,00")
        self.editQtd4 = QSpinBox()    ; self.combo4    = QComboBox()   ; self.labelPriceU4 = QLabel("R$ 0,00") ; self.labelPriceT4 = QLabel("R$ 0,00")
        self.editQtd5 = QSpinBox()    ; self.combo5    = QComboBox()   ; self.labelPriceU5 = QLabel("R$ 0,00") ; self.labelPriceT5 = QLabel("R$ 0,00")
        self.editQtd6 = QSpinBox()    ; self.combo6    = QComboBox()   ; self.labelPriceU6 = QLabel("R$ 0,00") ; self.labelPriceT6 = QLabel("R$ 0,00")
        self.editQtd7 = QSpinBox()    ; self.combo7    = QComboBox()   ; self.labelPriceU7 = QLabel("R$ 0,00") ; self.labelPriceT7 = QLabel("R$ 0,00")
        self.editQtd8 = QSpinBox()    ; self.combo8    = QComboBox()   ; self.labelPriceU8 = QLabel("R$ 0,00") ; self.labelPriceT8 = QLabel("R$ 0,00")

        self.list = ['','Calabresa','Frango','Frango com catupiry','Margerita','Mista','Mussarela','Pepperoni', 'Portuguesa']
        self.combo1.insertItems(0, self.list); self.combo1.currentIndexChanged.connect(self.price1)
        self.combo2.insertItems(1, self.list)
        self.combo3.insertItems(2, self.list)
        self.combo4.insertItems(3, self.list)
        self.combo5.insertItems(4, self.list)
        self.combo6.insertItems(5, self.list)
        self.combo7.insertItems(6, self.list)
        self.combo8.insertItems(7, self.list)

        self.editQtd1.setMaximumWidth(50);
        self.editQtd2.setMaximumWidth(50);
        self.editQtd3.setMaximumWidth(50);
        self.editQtd4.setMaximumWidth(50);
        self.editQtd5.setMaximumWidth(50);
        self.editQtd6.setMaximumWidth(50);
        self.editQtd7.setMaximumWidth(50);
        self.editQtd8.setMaximumWidth(50);

        orderStr = "Pedido n#"+str(orderNumber)
        totalStr = "Valor Total = R$ 0,00"
        self.labelDate = QLabel("Data: 07/07/2020"); self.labelOrder = QLabel(orderStr); self.labelTotal = QLabel(totalStr)
        self.buttonConfirm = QPushButton("Confirmar pedido")
        self.buttonConfirm.clicked.connect(self.confirmClick)
#        self.buttonConfirm.setEnabled(False)

        self.infoLayout = QGridLayout(self.infoGroup)
        self.infoLayout.addWidget(self.labelClient , 0, 0)
        self.infoLayout.addWidget(self.editClient  , 0, 1)
        self.infoLayout.addWidget(self.labelPhone  , 1, 0)
        self.infoLayout.addWidget(self.editPhone   , 1, 1)
        self.infoLayout.addWidget(self.labelAddr   , 2, 0)
        self.infoLayout.addWidget(self.editAddr    , 2, 1)
        self.infoLayout.addWidget(self.labelBurgh  , 3, 0)
        self.infoLayout.addWidget(self.editBurgh   , 3, 1)
        self.infoLayout.addWidget(self.labelAllergy, 4, 0)
        self.infoLayout.addWidget(self.editAllergy , 4, 1)
        self.infoLayout.addWidget(self.labelObs    , 5, 0)
        self.infoLayout.addWidget(self.editObs     , 5, 1)

        self.comboLayout = QGridLayout(self.comboGroup)
        self.comboLayout.setColumnStretch(1, 1)
        self.comboLayout.addWidget(self.labelQtd    , 0, 0)
        self.comboLayout.addWidget(self.labelItem   , 0, 1)
        self.comboLayout.addWidget(self.labelPriceU , 0, 2)
        self.comboLayout.addWidget(self.labelPriceT , 0, 3)
        self.comboLayout.addWidget(self.editQtd1    , 1, 0)
        self.comboLayout.addWidget(self.combo1      , 1, 1)
        self.comboLayout.addWidget(self.labelPriceU1, 1, 2)
        self.comboLayout.addWidget(self.labelPriceT1, 1, 3)
        self.comboLayout.addWidget(self.editQtd2    , 2, 0)
        self.comboLayout.addWidget(self.combo2      , 2, 1)
        self.comboLayout.addWidget(self.labelPriceU2, 2, 2)
        self.comboLayout.addWidget(self.labelPriceT2, 2, 3)
        self.comboLayout.addWidget(self.editQtd3    , 3, 0)
        self.comboLayout.addWidget(self.combo3      , 3, 1)
        self.comboLayout.addWidget(self.labelPriceU3, 3, 2)
        self.comboLayout.addWidget(self.labelPriceT3, 3, 3)
        self.comboLayout.addWidget(self.editQtd4    , 4, 0)
        self.comboLayout.addWidget(self.combo4      , 4, 1)
        self.comboLayout.addWidget(self.labelPriceU4, 4, 2)
        self.comboLayout.addWidget(self.labelPriceT4, 4, 3)
        self.comboLayout.addWidget(self.editQtd5    , 5, 0)
        self.comboLayout.addWidget(self.combo5      , 5, 1)
        self.comboLayout.addWidget(self.labelPriceU5, 5, 2)
        self.comboLayout.addWidget(self.labelPriceT5, 5, 3)
        self.comboLayout.addWidget(self.editQtd6    , 6, 0)
        self.comboLayout.addWidget(self.combo6      , 6, 1)
        self.comboLayout.addWidget(self.labelPriceU6, 6, 2)
        self.comboLayout.addWidget(self.labelPriceT6, 6, 3)
        self.comboLayout.addWidget(self.editQtd7    , 7, 0)
        self.comboLayout.addWidget(self.combo7      , 7, 1)
        self.comboLayout.addWidget(self.labelPriceU7, 7, 2)
        self.comboLayout.addWidget(self.labelPriceT7, 7, 3)
        self.comboLayout.addWidget(self.editQtd8    , 8, 0)
        self.comboLayout.addWidget(self.combo8      , 8, 1)
        self.comboLayout.addWidget(self.labelPriceU8, 8, 2)
        self.comboLayout.addWidget(self.labelPriceT8, 8, 3)

        self.endLayout = QGridLayout(self.endGroup)
        self.endLayout.addWidget(self.labelDate, 0, 0)
        self.endLayout.addWidget(self.labelOrder, 0, 1)
        self.endLayout.addWidget(self.labelTotal, 0, 2)
        self.endLayout.addWidget(self.buttonConfirm, 1, 2)

    # CLICK: Confirm order
    def price1(self):
        global orderNumber
        qtd = self.editQtd1.value()
        if self.combo1.currentText() in tradicionals:
            price = 20
        elif self.combo1.currentText() in specials:
            price = 25
        elif self.combo1.currentText() in premiums:
            price = 30
        else:
            price = 0
        self.labelPriceU1.setText('R$ '+str(price)+',00')
        self.labelPriceT1.setText('R$ '+str(price*qtd)+',00')






    def confirmClick(self):
        global orderNumber
        orderNumber += 1
        orderStr = "Pedido n#"+str(orderNumber)
        self.labelOrder.setText(orderStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    form = MainWindow()
    form.setWindowTitle('Editor de Nuvem de Pontos')
    form.setGeometry(100, 100, 500, 500)
    form.show()
    sys.exit(app.exec_())
