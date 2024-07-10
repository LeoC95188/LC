# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(751, 368)
        MainWindow.setStyleSheet(u"*{\n"
"	font-family: NSimSun;\n"
"}\n"
"QMainWindow{\n"
"	background-color: #eee;\n"
"}\n"
"QRadioButton{\n"
"	height: 100px;\n"
"	width: 200px;\n"
"	font-size: 48px;\n"
"}\n"
"QPushButton{\n"
"	font-size: 36px;\n"
"	background-color: #ddd;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_0_intro = QWidget()
        self.page_0_intro.setObjectName(u"page_0_intro")
        font = QFont()
        font.setFamilies([u"NSimSun"])
        font.setPointSize(48)
        self.page_0_intro.setFont(font)
        self.gridLayout_9 = QGridLayout(self.page_0_intro)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_0 = QLabel(self.page_0_intro)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setFont(font)

        self.gridLayout_9.addWidget(self.label_0, 0, 0, 1, 1)

        self.label_0_prompt = QLabel(self.page_0_intro)
        self.label_0_prompt.setObjectName(u"label_0_prompt")
        font1 = QFont()
        font1.setFamilies([u"NSimSun"])
        font1.setPointSize(28)
        self.label_0_prompt.setFont(font1)
        self.label_0_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_0_prompt.setAlignment(Qt.AlignCenter)
        self.label_0_prompt.setWordWrap(True)

        self.gridLayout_9.addWidget(self.label_0_prompt, 1, 1, 1, 2)

        self.label_0_detail = QLabel(self.page_0_intro)
        self.label_0_detail.setObjectName(u"label_0_detail")
        font2 = QFont()
        font2.setFamilies([u"NSimSun"])
        font2.setPointSize(18)
        self.label_0_detail.setFont(font2)
        self.label_0_detail.setAlignment(Qt.AlignCenter)
        self.label_0_detail.setWordWrap(True)

        self.gridLayout_9.addWidget(self.label_0_detail, 2, 1, 1, 2)

        self.button_next_page_0 = QPushButton(self.page_0_intro)
        self.button_next_page_0.setObjectName(u"button_next_page_0")

        self.gridLayout_9.addWidget(self.button_next_page_0, 3, 2, 1, 1)

        self.gridLayout_9.setRowStretch(1, 1)
        self.gridLayout_9.setRowStretch(2, 1)
        self.gridLayout_9.setRowStretch(3, 1)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_0_intro)
        self.page_1_size = QWidget()
        self.page_1_size.setObjectName(u"page_1_size")
        self.page_1_size.setFont(font)
        self.gridLayout = QGridLayout(self.page_1_size)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_next_page_1 = QPushButton(self.page_1_size)
        self.button_next_page_1.setObjectName(u"button_next_page_1")

        self.gridLayout.addWidget(self.button_next_page_1, 3, 2, 1, 1)

        self.radioButton_1_no = QRadioButton(self.page_1_size)
        self.radioButton_1_no.setObjectName(u"radioButton_1_no")

        self.gridLayout.addWidget(self.radioButton_1_no, 2, 2, 1, 1)

        self.radioButton_1_yes = QRadioButton(self.page_1_size)
        self.radioButton_1_yes.setObjectName(u"radioButton_1_yes")

        self.gridLayout.addWidget(self.radioButton_1_yes, 2, 1, 1, 1)

        self.label_1_prompt = QLabel(self.page_1_size)
        self.label_1_prompt.setObjectName(u"label_1_prompt")
        self.label_1_prompt.setFont(font1)
        self.label_1_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_1_prompt.setAlignment(Qt.AlignCenter)
        self.label_1_prompt.setWordWrap(True)

        self.gridLayout.addWidget(self.label_1_prompt, 1, 1, 1, 2)

        self.label_1 = QLabel(self.page_1_size)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font)

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.button_prev_page_1 = QPushButton(self.page_1_size)
        self.button_prev_page_1.setObjectName(u"button_prev_page_1")
        self.button_prev_page_1.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout.addWidget(self.button_prev_page_1, 3, 1, 1, 1)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_1_size)
        self.page_2_allergy = QWidget()
        self.page_2_allergy.setObjectName(u"page_2_allergy")
        self.gridLayout_3 = QGridLayout(self.page_2_allergy)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.page_2_allergy)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_2_prompt = QLabel(self.page_2_allergy)
        self.label_2_prompt.setObjectName(u"label_2_prompt")
        self.label_2_prompt.setFont(font1)
        self.label_2_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_2_prompt.setAlignment(Qt.AlignCenter)
        self.label_2_prompt.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_2_prompt, 1, 1, 1, 2)

        self.radioButton_2_yes = QRadioButton(self.page_2_allergy)
        self.radioButton_2_yes.setObjectName(u"radioButton_2_yes")

        self.gridLayout_3.addWidget(self.radioButton_2_yes, 2, 1, 1, 1)

        self.radioButton_2_no = QRadioButton(self.page_2_allergy)
        self.radioButton_2_no.setObjectName(u"radioButton_2_no")

        self.gridLayout_3.addWidget(self.radioButton_2_no, 2, 2, 1, 1)

        self.button_prev_page_2 = QPushButton(self.page_2_allergy)
        self.button_prev_page_2.setObjectName(u"button_prev_page_2")
        font3 = QFont()
        font3.setFamilies([u"NSimSun"])
        self.button_prev_page_2.setFont(font3)

        self.gridLayout_3.addWidget(self.button_prev_page_2, 3, 1, 1, 1)

        self.button_next_page_2 = QPushButton(self.page_2_allergy)
        self.button_next_page_2.setObjectName(u"button_next_page_2")
        self.button_next_page_2.setFont(font3)

        self.gridLayout_3.addWidget(self.button_next_page_2, 3, 2, 1, 1)

        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_2_allergy)
        self.page_3_others = QWidget()
        self.page_3_others.setObjectName(u"page_3_others")
        self.gridLayout_4 = QGridLayout(self.page_3_others)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.page_3_others)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.radioButton_3_yes = QRadioButton(self.page_3_others)
        self.radioButton_3_yes.setObjectName(u"radioButton_3_yes")

        self.gridLayout_4.addWidget(self.radioButton_3_yes, 2, 1, 1, 1)

        self.radioButton_3_no = QRadioButton(self.page_3_others)
        self.radioButton_3_no.setObjectName(u"radioButton_3_no")

        self.gridLayout_4.addWidget(self.radioButton_3_no, 2, 2, 1, 1)

        self.label_3_prompt = QLabel(self.page_3_others)
        self.label_3_prompt.setObjectName(u"label_3_prompt")
        self.label_3_prompt.setFont(font1)
        self.label_3_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_3_prompt.setAlignment(Qt.AlignCenter)
        self.label_3_prompt.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_3_prompt, 1, 1, 1, 2)

        self.button_prev_page_3 = QPushButton(self.page_3_others)
        self.button_prev_page_3.setObjectName(u"button_prev_page_3")
        self.button_prev_page_3.setFont(font3)

        self.gridLayout_4.addWidget(self.button_prev_page_3, 3, 1, 1, 1)

        self.button_next_page_3 = QPushButton(self.page_3_others)
        self.button_next_page_3.setObjectName(u"button_next_page_3")
        self.button_next_page_3.setFont(font3)

        self.gridLayout_4.addWidget(self.button_next_page_3, 3, 2, 1, 1)

        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_3_others)
        self.page_4_fur = QWidget()
        self.page_4_fur.setObjectName(u"page_4_fur")
        self.gridLayout_5 = QGridLayout(self.page_4_fur)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.page_4_fur)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.radioButton_4_yes = QRadioButton(self.page_4_fur)
        self.radioButton_4_yes.setObjectName(u"radioButton_4_yes")

        self.gridLayout_5.addWidget(self.radioButton_4_yes, 2, 1, 1, 1)

        self.radioButton_4_no = QRadioButton(self.page_4_fur)
        self.radioButton_4_no.setObjectName(u"radioButton_4_no")

        self.gridLayout_5.addWidget(self.radioButton_4_no, 2, 2, 1, 1)

        self.label_4_prompt = QLabel(self.page_4_fur)
        self.label_4_prompt.setObjectName(u"label_4_prompt")
        self.label_4_prompt.setFont(font1)
        self.label_4_prompt.setAutoFillBackground(False)
        self.label_4_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_4_prompt.setAlignment(Qt.AlignCenter)
        self.label_4_prompt.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_4_prompt, 1, 1, 1, 2)

        self.button_prev_page_4 = QPushButton(self.page_4_fur)
        self.button_prev_page_4.setObjectName(u"button_prev_page_4")

        self.gridLayout_5.addWidget(self.button_prev_page_4, 3, 1, 1, 1)

        self.button_next_page_4 = QPushButton(self.page_4_fur)
        self.button_next_page_4.setObjectName(u"button_next_page_4")

        self.gridLayout_5.addWidget(self.button_next_page_4, 3, 2, 1, 1)

        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setRowStretch(3, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_4_fur)
        self.page_5_working = QWidget()
        self.page_5_working.setObjectName(u"page_5_working")
        self.gridLayout_6 = QGridLayout(self.page_5_working)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.page_5_working)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.radioButton_5_no = QRadioButton(self.page_5_working)
        self.radioButton_5_no.setObjectName(u"radioButton_5_no")

        self.gridLayout_6.addWidget(self.radioButton_5_no, 2, 2, 1, 1)

        self.radioButton_5_yes = QRadioButton(self.page_5_working)
        self.radioButton_5_yes.setObjectName(u"radioButton_5_yes")

        self.gridLayout_6.addWidget(self.radioButton_5_yes, 2, 1, 1, 1)

        self.label_5_prompt = QLabel(self.page_5_working)
        self.label_5_prompt.setObjectName(u"label_5_prompt")
        self.label_5_prompt.setFont(font1)
        self.label_5_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_5_prompt.setAlignment(Qt.AlignCenter)
        self.label_5_prompt.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_5_prompt, 1, 1, 1, 2)

        self.button_prev_page_5 = QPushButton(self.page_5_working)
        self.button_prev_page_5.setObjectName(u"button_prev_page_5")
        self.button_prev_page_5.setFont(font3)

        self.gridLayout_6.addWidget(self.button_prev_page_5, 3, 1, 1, 1)

        self.button_next_page_5 = QPushButton(self.page_5_working)
        self.button_next_page_5.setObjectName(u"button_next_page_5")
        self.button_next_page_5.setFont(font3)

        self.gridLayout_6.addWidget(self.button_next_page_5, 3, 2, 1, 1)

        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_6.setRowStretch(2, 1)
        self.gridLayout_6.setRowStretch(3, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_5_working)
        self.page_6_temperment = QWidget()
        self.page_6_temperment.setObjectName(u"page_6_temperment")
        self.gridLayout_8 = QGridLayout(self.page_6_temperment)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.radioButton_6_no = QRadioButton(self.page_6_temperment)
        self.radioButton_6_no.setObjectName(u"radioButton_6_no")

        self.gridLayout_8.addWidget(self.radioButton_6_no, 2, 2, 1, 1)

        self.label_6_prompt = QLabel(self.page_6_temperment)
        self.label_6_prompt.setObjectName(u"label_6_prompt")
        self.label_6_prompt.setFont(font1)
        self.label_6_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_6_prompt.setAlignment(Qt.AlignCenter)
        self.label_6_prompt.setWordWrap(True)

        self.gridLayout_8.addWidget(self.label_6_prompt, 1, 1, 1, 2)

        self.label_6 = QLabel(self.page_6_temperment)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.radioButton_6_yes = QRadioButton(self.page_6_temperment)
        self.radioButton_6_yes.setObjectName(u"radioButton_6_yes")

        self.gridLayout_8.addWidget(self.radioButton_6_yes, 2, 1, 1, 1)

        self.button_next_page_6 = QPushButton(self.page_6_temperment)
        self.button_next_page_6.setObjectName(u"button_next_page_6")

        self.gridLayout_8.addWidget(self.button_next_page_6, 3, 2, 1, 1)

        self.button_prev_page_6 = QPushButton(self.page_6_temperment)
        self.button_prev_page_6.setObjectName(u"button_prev_page_6")

        self.gridLayout_8.addWidget(self.button_prev_page_6, 3, 1, 1, 1)

        self.gridLayout_8.setRowStretch(1, 1)
        self.gridLayout_8.setRowStretch(2, 1)
        self.gridLayout_8.setRowStretch(3, 1)
        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_6_temperment)
        self.page_7_conclusion = QWidget()
        self.page_7_conclusion.setObjectName(u"page_7_conclusion")
        self.gridLayout_10 = QGridLayout(self.page_7_conclusion)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_7_detail = QLabel(self.page_7_conclusion)
        self.label_7_detail.setObjectName(u"label_7_detail")
        font4 = QFont()
        font4.setFamilies([u"NSimSun"])
        font4.setPointSize(48)
        font4.setBold(True)
        self.label_7_detail.setFont(font4)
        self.label_7_detail.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_7_detail, 2, 1, 1, 2)

        self.label_7 = QLabel(self.page_7_conclusion)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)

        self.button_prev_page_7 = QPushButton(self.page_7_conclusion)
        self.button_prev_page_7.setObjectName(u"button_prev_page_7")

        self.gridLayout_10.addWidget(self.button_prev_page_7, 3, 1, 1, 1)

        self.label_7_prompt = QLabel(self.page_7_conclusion)
        self.label_7_prompt.setObjectName(u"label_7_prompt")
        self.label_7_prompt.setFont(font1)
        self.label_7_prompt.setStyleSheet(u"background-color: #e8e8e8;")
        self.label_7_prompt.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_7_prompt, 1, 1, 1, 2)

        self.button_restart = QPushButton(self.page_7_conclusion)
        self.button_restart.setObjectName(u"button_restart")

        self.gridLayout_10.addWidget(self.button_restart, 3, 2, 1, 1)

        self.gridLayout_10.setRowStretch(1, 1)
        self.gridLayout_10.setRowStretch(2, 1)
        self.gridLayout_10.setRowStretch(3, 1)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_10.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page_7_conclusion)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_0.setText(QCoreApplication.translate("MainWindow", u"\u200e ", None))
        self.label_0_prompt.setText(QCoreApplication.translate("MainWindow", u"Welcome, this test will help you decide which dog breed suits your personal needs best.", None))
        self.label_0_detail.setText(QCoreApplication.translate("MainWindow", u" Please answer questions with the yes or no button and click next to move on.", None))
        self.button_next_page_0.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_next_page_1.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.radioButton_1_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.radioButton_1_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label_1_prompt.setText(QCoreApplication.translate("MainWindow", u"Do you like a large dog more than a small dog?", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_prev_page_1.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_2_prompt.setText(QCoreApplication.translate("MainWindow", u"Does this dog need to be hypoallergenic?", None))
        self.radioButton_2_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_2_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.button_prev_page_2.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.button_next_page_2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_3_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_3_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_3_prompt.setText(QCoreApplication.translate("MainWindow", u"Do you have any other pets?", None))
        self.button_prev_page_3.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.button_next_page_3.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.radioButton_4_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_4_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_4_prompt.setText(QCoreApplication.translate("MainWindow", u"Would you prefer a fluffy dog over a short-haired one?", None))
        self.button_prev_page_4.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.button_next_page_4.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.radioButton_5_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.radioButton_5_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label_5_prompt.setText(QCoreApplication.translate("MainWindow", u"Does this dog need to work on a farm/around the house for you?", None))
        self.button_prev_page_5.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.button_next_page_5.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.radioButton_6_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_6_prompt.setText(QCoreApplication.translate("MainWindow", u"Does this dogs temperment need to be protective rather than friendly?", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.radioButton_6_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.button_next_page_6.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_prev_page_6.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.label_7_detail.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u200e ", None))
        self.button_prev_page_7.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.label_7_prompt.setText(QCoreApplication.translate("MainWindow", u"Your recommended dog is the...", None))
        self.button_restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
    # retranslateUi

