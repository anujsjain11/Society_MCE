# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1202, 653)
        self.mainLayout = QHBoxLayout(Widget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.sidebarLayout = QVBoxLayout()
        self.sidebarLayout.setSpacing(7)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.btnInventory = QPushButton(Widget)
        self.btnInventory.setObjectName(u"btnInventory")

        self.sidebarLayout.addWidget(self.btnInventory)

        self.btnStock = QPushButton(Widget)
        self.btnStock.setObjectName(u"btnStock")

        self.sidebarLayout.addWidget(self.btnStock)

        self.btnBilling = QPushButton(Widget)
        self.btnBilling.setObjectName(u"btnBilling")

        self.sidebarLayout.addWidget(self.btnBilling)

        self.btnUpload = QPushButton(Widget)
        self.btnUpload.setObjectName(u"btnUpload")

        self.sidebarLayout.addWidget(self.btnUpload)

        self.btnCreate = QPushButton(Widget)
        self.btnCreate.setObjectName(u"btnCreate")

        self.sidebarLayout.addWidget(self.btnCreate)

        self.btnShop = QPushButton(Widget)
        self.btnShop.setObjectName(u"btnShop")

        self.sidebarLayout.addWidget(self.btnShop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.verticalSpacer)


        self.mainLayout.addLayout(self.sidebarLayout)

        self.stackedPages = QStackedWidget(Widget)
        self.stackedPages.setObjectName(u"stackedPages")
        self.pageInventory = QWidget()
        self.pageInventory.setObjectName(u"pageInventory")
        self.inventoryLayout = QHBoxLayout(self.pageInventory)
        self.inventoryLayout.setObjectName(u"inventoryLayout")
        self.inventoryTable = QTableWidget(self.pageInventory)
        if (self.inventoryTable.columnCount() < 3):
            self.inventoryTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.inventoryTable.setObjectName(u"inventoryTable")

        self.inventoryLayout.addWidget(self.inventoryTable)

        self.formLayout = QVBoxLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.pageInventory)
        self.label.setObjectName(u"label")

        self.formLayout.addWidget(self.label)

        self.itemName = QLineEdit(self.pageInventory)
        self.itemName.setObjectName(u"itemName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemName.sizePolicy().hasHeightForWidth())
        self.itemName.setSizePolicy(sizePolicy)

        self.formLayout.addWidget(self.itemName)

        self.label_2 = QLabel(self.pageInventory)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.addWidget(self.label_2)

        self.itemQty = QLineEdit(self.pageInventory)
        self.itemQty.setObjectName(u"itemQty")
        sizePolicy.setHeightForWidth(self.itemQty.sizePolicy().hasHeightForWidth())
        self.itemQty.setSizePolicy(sizePolicy)

        self.formLayout.addWidget(self.itemQty)

        self.label_3 = QLabel(self.pageInventory)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.addWidget(self.label_3)

        self.itemPrice = QLineEdit(self.pageInventory)
        self.itemPrice.setObjectName(u"itemPrice")
        sizePolicy.setHeightForWidth(self.itemPrice.sizePolicy().hasHeightForWidth())
        self.itemPrice.setSizePolicy(sizePolicy)

        self.formLayout.addWidget(self.itemPrice)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.addItem(self.verticalSpacer_2)

        self.btnAdd = QPushButton(self.pageInventory)
        self.btnAdd.setObjectName(u"btnAdd")

        self.formLayout.addWidget(self.btnAdd)


        self.inventoryLayout.addLayout(self.formLayout)

        self.stackedPages.addWidget(self.pageInventory)
        self.pageStock = QWidget()
        self.pageStock.setObjectName(u"pageStock")
        self.stockLayout = QVBoxLayout(self.pageStock)
        self.stockLayout.setObjectName(u"stockLayout")
        self.labelStock = QLabel(self.pageStock)
        self.labelStock.setObjectName(u"labelStock")

        self.stockLayout.addWidget(self.labelStock)

        self.stackedPages.addWidget(self.pageStock)
        self.pageBilling = QWidget()
        self.pageBilling.setObjectName(u"pageBilling")
        self.billingLayout = QVBoxLayout(self.pageBilling)
        self.billingLayout.setObjectName(u"billingLayout")
        self.labelBilling = QLabel(self.pageBilling)
        self.labelBilling.setObjectName(u"labelBilling")

        self.billingLayout.addWidget(self.labelBilling)

        self.stackedPages.addWidget(self.pageBilling)
        self.pageUpload = QWidget()
        self.pageUpload.setObjectName(u"pageUpload")
        self.uploadLayout = QVBoxLayout(self.pageUpload)
        self.uploadLayout.setObjectName(u"uploadLayout")
        self.labelUpload = QLabel(self.pageUpload)
        self.labelUpload.setObjectName(u"labelUpload")

        self.uploadLayout.addWidget(self.labelUpload)

        self.stackedPages.addWidget(self.pageUpload)
        self.pageCreate = QWidget()
        self.pageCreate.setObjectName(u"pageCreate")
        self.createLayout = QVBoxLayout(self.pageCreate)
        self.createLayout.setObjectName(u"createLayout")
        self.labelCreate = QLabel(self.pageCreate)
        self.labelCreate.setObjectName(u"labelCreate")

        self.createLayout.addWidget(self.labelCreate)

        self.stackedPages.addWidget(self.pageCreate)
        self.pageShop = QWidget()
        self.pageShop.setObjectName(u"pageShop")
        self.shopLayout = QVBoxLayout(self.pageShop)
        self.shopLayout.setObjectName(u"shopLayout")
        self.labelShop = QLabel(self.pageShop)
        self.labelShop.setObjectName(u"labelShop")

        self.shopLayout.addWidget(self.labelShop)

        self.shopTable = QTableWidget(self.pageShop)
        if (self.shopTable.columnCount() < 1):
            self.shopTable.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.shopTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.shopTable.setObjectName(u"shopTable")

        self.shopLayout.addWidget(self.shopTable)

        self.btnBuy = QPushButton(self.pageShop)
        self.btnBuy.setObjectName(u"btnBuy")

        self.shopLayout.addWidget(self.btnBuy)

        self.stackedPages.addWidget(self.pageShop)

        self.mainLayout.addWidget(self.stackedPages)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"College Society System", None))
        self.btnInventory.setText(QCoreApplication.translate("Widget", u"Inventory", None))
        self.btnStock.setText(QCoreApplication.translate("Widget", u"Stock", None))
        self.btnBilling.setText(QCoreApplication.translate("Widget", u"Billing", None))
        self.btnUpload.setText(QCoreApplication.translate("Widget", u"Upload Invoice", None))
        self.btnCreate.setText(QCoreApplication.translate("Widget", u"Create Invoice", None))
        self.btnShop.setText(QCoreApplication.translate("Widget", u"Shop", None))
        ___qtablewidgetitem = self.inventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Item", None));
        ___qtablewidgetitem1 = self.inventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Quantity", None));
        ___qtablewidgetitem2 = self.inventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Price", None));
        self.label.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.itemName.setPlaceholderText(QCoreApplication.translate("Widget", u"Item Name", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.itemQty.setPlaceholderText(QCoreApplication.translate("Widget", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.itemPrice.setPlaceholderText(QCoreApplication.translate("Widget", u"Price", None))
        self.btnAdd.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.labelStock.setText(QCoreApplication.translate("Widget", u"Stock Module", None))
        self.labelBilling.setText(QCoreApplication.translate("Widget", u"Billing Module", None))
        self.labelUpload.setText(QCoreApplication.translate("Widget", u"Upload Invoice Module", None))
        self.labelCreate.setText(QCoreApplication.translate("Widget", u"Create Invoice Module", None))
        self.labelShop.setText(QCoreApplication.translate("Widget", u"College Society Shop", None))
        ___qtablewidgetitem3 = self.shopTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Items for Sale", None));
        self.btnBuy.setText(QCoreApplication.translate("Widget", u"Buy", None))
    # retranslateUi

