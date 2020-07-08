# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget, QComboBox, QGroupBox, QPushButton, QMainWindow, QTextEdit, QLineEdit, QLayout, QGridLayout, QLabel, QSpinBox
from PySide2.QtCore import QObject, SIGNAL
# sfrom PySide2.QtGui import *

orderNumber  = 1;
priceVec     = [0,0,0,0,0,0,0,0]
TOTAL        = 0
tradicionals = ['Calabresa', 'Frango', 'Margerita', 'Mista', 'Mussarela']
specials     = ['Frango com catupiry', 'Portuguesa']
premiums     = ['Pepperoni']

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Widget object
        self.mainWidget = QWidget()
        # Layout object
        self.mainLayout = QGridLayout(self.mainWidget)

        self.infoGroup  = QGroupBox("Dados")
        self.comboGroup = QGroupBox("Pedido")
        self.endGroup   = QGroupBox("Resumo")

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

        self.editClient.textChanged.connect(self.checkMinimumData)
        self.editPhone.textChanged.connect(self.checkMinimumData)
        self.editAddr.textChanged.connect(self.checkMinimumData)
        self.editBurgh.textChanged.connect(self.checkMinimumData)

#        self.editObs.setFixedHeight(40)

        self.combo = [1,2,3,4,5,6,7,8]
        self.labelPriceU = [1,2,3,4,5,6,7,8]
        self.labelPriceT = [1,2,3,4,5,6,7,8]
        self.editQtd = [1,2,3,4,5,6,7,8]
        self.list = ['','Calabresa','Frango','Frango com catupiry','Margerita','Mista','Mussarela','Pepperoni', 'Portuguesa']
        for i in range (0,8):
            self.combo[i] = QComboBox()
            self.labelPriceU[i] = QLabel("R$ 0,00")
            self.labelPriceT[i] = QLabel("R$ 0,00")
            self.editQtd[i] = QSpinBox()
            self.editQtd[i].setMaximumWidth(50);

        self.labelQtd = QLabel("Qtd."); self.labelItem = QLabel("Item"); self.labelPriceUStr = QLabel("Preço uni."); self.labelPriceTStr = QLabel("Preço total")

        self.combo[0].insertItems(0, self.list); self.combo[0].currentIndexChanged.connect(lambda: self.price(0))
        self.combo[1].insertItems(0, self.list); self.combo[1].currentIndexChanged.connect(lambda: self.price(1))
        self.combo[2].insertItems(0, self.list); self.combo[2].currentIndexChanged.connect(lambda: self.price(2))
        self.combo[3].insertItems(0, self.list); self.combo[3].currentIndexChanged.connect(lambda: self.price(3))
        self.combo[4].insertItems(0, self.list); self.combo[4].currentIndexChanged.connect(lambda: self.price(4))
        self.combo[5].insertItems(0, self.list); self.combo[5].currentIndexChanged.connect(lambda: self.price(5))
        self.combo[6].insertItems(0, self.list); self.combo[6].currentIndexChanged.connect(lambda: self.price(6))
        self.combo[7].insertItems(0, self.list); self.combo[7].currentIndexChanged.connect(lambda: self.price(7))

        self.editQtd[0].valueChanged.connect(lambda: self.price(0))
        self.editQtd[1].valueChanged.connect(lambda: self.price(1))
        self.editQtd[2].valueChanged.connect(lambda: self.price(2))
        self.editQtd[3].valueChanged.connect(lambda: self.price(3))
        self.editQtd[4].valueChanged.connect(lambda: self.price(4))
        self.editQtd[5].valueChanged.connect(lambda: self.price(5))
        self.editQtd[6].valueChanged.connect(lambda: self.price(6))
        self.editQtd[7].valueChanged.connect(lambda: self.price(7))

        orderStr = "Pedido n#"+str(orderNumber)
        totalStr = "Valor Total = R$ 0,00"
        self.labelDate = QLabel("Data: 07/07/2020"); self.labelOrder = QLabel(orderStr); self.labelTotal = QLabel(totalStr)
        self.buttonConfirm = QPushButton("Confirmar pedido")
        self.buttonConfirm.clicked.connect(self.confirmClick)
        self.buttonConfirm.setEnabled(False)

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
        self.comboLayout.addWidget(self.labelQtd      , 0, 0)
        self.comboLayout.addWidget(self.labelItem     , 0, 1)
        self.comboLayout.addWidget(self.labelPriceUStr, 0, 2)
        self.comboLayout.addWidget(self.labelPriceTStr, 0, 3)
        for i in range(1,8):
            self.comboLayout.addWidget(self.editQtd[i]    , i+1, 0)
            self.comboLayout.addWidget(self.combo[i]      , i+1, 1)
            self.comboLayout.addWidget(self.labelPriceU[i], i+1, 2)
            self.comboLayout.addWidget(self.labelPriceT[i], i+1, 3)

        self.endLayout = QGridLayout(self.endGroup)
        self.endLayout.addWidget(self.labelDate, 0, 0)
        self.endLayout.addWidget(self.labelOrder, 0, 1)
        self.endLayout.addWidget(self.labelTotal, 0, 2)
        self.endLayout.addWidget(self.buttonConfirm, 1, 2)

    def checkMinimumData(self):
        if TOTAL > 0 and self.editClient.text() and self.editAddr.text() and self.editPhone.text() and self.editBurgh.text():
            self.buttonConfirm.setEnabled(True)
        else:
            self.buttonConfirm.setEnabled(False)

    # CLICK: Confirm order
    def price(self,index):
        global priceVec, TOTAL
        qtd = self.editQtd[index].value()
        if self.combo[index].currentText() in tradicionals:
            price = 20
        elif self.combo[index].currentText() in specials:
            price = 25
        elif self.combo[index].currentText() in premiums:
            price = 30
        else:
            price = 0

        priceVec[index] = price*qtd;
        self.labelPriceU[index].setText('R$ '+str(price)+',00')
        self.labelPriceT[index].setText('R$ '+str(priceVec[index])+',00')

        TOTAL = sum(priceVec)
        self.labelTotal.setText('Valor Total = R$ '+str(TOTAL)+',00')
        self.checkMinimumData()


    def confirmClick(self):
        global orderNumber
        orderNumber += 1
        orderStr = "Pedido n#"+str(orderNumber)
        self.labelOrder.setText(orderStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    form = MainWindow()
    form.setWindowTitle('Orçamento: Já chegou!')
    form.setGeometry(100, 100, 500, 500)
    form.show()
    sys.exit(app.exec_())
