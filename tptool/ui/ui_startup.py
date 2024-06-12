# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(260, 220)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.ChipComboBox = QComboBox(Form)
        self.ChipComboBox.addItem("")
        self.ChipComboBox.addItem("")
        self.ChipComboBox.addItem("")
        self.ChipComboBox.addItem("")
        self.ChipComboBox.setObjectName(u"ChipComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ChipComboBox.sizePolicy().hasHeightForWidth())
        self.ChipComboBox.setSizePolicy(sizePolicy1)
        self.ChipComboBox.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        self.ChipComboBox.setFont(font)

        self.gridLayout.addWidget(self.ChipComboBox, 0, 2, 1, 1)

        self.ChipLabel = QLabel(Form)
        self.ChipLabel.setObjectName(u"ChipLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ChipLabel.sizePolicy().hasHeightForWidth())
        self.ChipLabel.setSizePolicy(sizePolicy2)
        self.ChipLabel.setMaximumSize(QSize(100, 30))
        self.ChipLabel.setFont(font)

        self.gridLayout.addWidget(self.ChipLabel, 0, 1, 1, 1)

        self.FunctionLabel = QLabel(Form)
        self.FunctionLabel.setObjectName(u"FunctionLabel")
        sizePolicy2.setHeightForWidth(self.FunctionLabel.sizePolicy().hasHeightForWidth())
        self.FunctionLabel.setSizePolicy(sizePolicy2)
        self.FunctionLabel.setMaximumSize(QSize(100, 30))
        self.FunctionLabel.setFont(font)

        self.gridLayout.addWidget(self.FunctionLabel, 2, 1, 1, 1)

        self.FunctionComboBox = QComboBox(Form)
        self.FunctionComboBox.addItem("")
        self.FunctionComboBox.addItem("")
        self.FunctionComboBox.addItem("")
        self.FunctionComboBox.setObjectName(u"FunctionComboBox")
        sizePolicy1.setHeightForWidth(self.FunctionComboBox.sizePolicy().hasHeightForWidth())
        self.FunctionComboBox.setSizePolicy(sizePolicy1)
        self.FunctionComboBox.setMinimumSize(QSize(0, 30))
        self.FunctionComboBox.setFont(font)

        self.gridLayout.addWidget(self.FunctionComboBox, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.OkPushButton = QPushButton(Form)
        self.OkPushButton.setObjectName(u"OkPushButton")
        sizePolicy1.setHeightForWidth(self.OkPushButton.sizePolicy().hasHeightForWidth())
        self.OkPushButton.setSizePolicy(sizePolicy1)
        self.OkPushButton.setMaximumSize(QSize(160, 35))

        self.horizontalLayout.addWidget(self.OkPushButton)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Startup Selection", None))
        self.ChipComboBox.setItemText(0, QCoreApplication.translate("Form", u"ESP32", None))
        self.ChipComboBox.setItemText(1, QCoreApplication.translate("Form", u"ESP32-S2", None))
        self.ChipComboBox.setItemText(2, QCoreApplication.translate("Form", u"ESP32-S3", None))
        self.ChipComboBox.setItemText(3, QCoreApplication.translate("Form", u"ESP32-P4", None))

        self.ChipLabel.setText(QCoreApplication.translate("Form", u"Chip Type", None))
        self.FunctionLabel.setText(QCoreApplication.translate("Form", u"Function Type", None))
        self.FunctionComboBox.setItemText(0, QCoreApplication.translate("Form", u"Button", None))
        self.FunctionComboBox.setItemText(1, QCoreApplication.translate("Form", u"Proximity", None))
        self.FunctionComboBox.setItemText(2, QCoreApplication.translate("Form", u"Slider", None))

        self.OkPushButton.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

