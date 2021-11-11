# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pr.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1241, 821))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.addemployee = QtWidgets.QPushButton(self.tab_1)
        self.addemployee.setGeometry(QtCore.QRect(0, 10, 131, 61))
        self.addemployee.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.addemployee.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addemployee.setIcon(icon)
        self.addemployee.setIconSize(QtCore.QSize(50, 50))
        self.addemployee.setObjectName("addemployee")
        self.editemployee = QtWidgets.QPushButton(self.tab_1)
        self.editemployee.setGeometry(QtCore.QRect(130, 10, 131, 61))
        self.editemployee.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.editemployee.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editemployee.setIcon(icon1)
        self.editemployee.setIconSize(QtCore.QSize(50, 50))
        self.editemployee.setObjectName("editemployee")
        self.deleteemployee = QtWidgets.QPushButton(self.tab_1)
        self.deleteemployee.setGeometry(QtCore.QRect(260, 10, 131, 61))
        self.deleteemployee.setMouseTracking(False)
        self.deleteemployee.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.deleteemployee.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.deleteemployee.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteemployee.setIcon(icon2)
        self.deleteemployee.setIconSize(QtCore.QSize(50, 50))
        self.deleteemployee.setCheckable(False)
        self.deleteemployee.setFlat(False)
        self.deleteemployee.setObjectName("deleteemployee")
        self.tableemp = QtWidgets.QTableWidget(self.tab_1)
        self.tableemp.setEnabled(True)
        self.tableemp.setGeometry(QtCore.QRect(0, 90, 700, 700))
        self.tableemp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableemp.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableemp.setDragEnabled(False)
        self.tableemp.setDragDropOverwriteMode(False)
        self.tableemp.setAlternatingRowColors(False)
        self.tableemp.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableemp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableemp.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableemp.setShowGrid(False)
        self.tableemp.setGridStyle(QtCore.Qt.NoPen)
        self.tableemp.setWordWrap(False)
        self.tableemp.setCornerButtonEnabled(False)
        self.tableemp.setObjectName("tableemp")
        self.tableemp.setColumnCount(0)
        self.tableemp.setRowCount(0)
        self.picture = QtWidgets.QLabel(self.tab_1)
        self.picture.setGeometry(QtCore.QRect(710, 100, 350, 450))
        self.picture.setMinimumSize(QtCore.QSize(100, 100))
        self.picture.setMaximumSize(QtCore.QSize(1920, 1080))
        self.picture.setSizeIncrement(QtCore.QSize(1920, 1080))
        self.picture.setBaseSize(QtCore.QSize(1920, 1080))
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.layoutWidget = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 0, 311, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.search_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.search_line.setObjectName("search_line")
        self.horizontalLayout.addWidget(self.search_line)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tablegroup = QtWidgets.QTableWidget(self.tab_2)
        self.tablegroup.setGeometry(QtCore.QRect(0, 90, 700, 700))
        self.tablegroup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablegroup.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablegroup.setObjectName("tablegroup")
        self.tablegroup.setColumnCount(0)
        self.tablegroup.setRowCount(0)
        self.addgroup = QtWidgets.QPushButton(self.tab_2)
        self.addgroup.setGeometry(QtCore.QRect(0, 10, 131, 61))
        self.addgroup.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.addgroup.setText("")
        self.addgroup.setIcon(icon)
        self.addgroup.setIconSize(QtCore.QSize(50, 50))
        self.addgroup.setObjectName("addgroup")
        self.editgroup = QtWidgets.QPushButton(self.tab_2)
        self.editgroup.setGeometry(QtCore.QRect(130, 10, 131, 61))
        self.editgroup.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.editgroup.setText("")
        self.editgroup.setIcon(icon1)
        self.editgroup.setIconSize(QtCore.QSize(50, 50))
        self.editgroup.setObjectName("editgroup")
        self.deletegroup = QtWidgets.QPushButton(self.tab_2)
        self.deletegroup.setGeometry(QtCore.QRect(260, 10, 131, 61))
        self.deletegroup.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.deletegroup.setText("")
        self.deletegroup.setIcon(icon2)
        self.deletegroup.setIconSize(QtCore.QSize(50, 50))
        self.deletegroup.setObjectName("deletegroup")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(390, 0, 311, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_32 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_45.addWidget(self.label_32)
        self.search_line_group = QtWidgets.QLineEdit(self.layoutWidget1)
        self.search_line_group.setObjectName("search_line_group")
        self.horizontalLayout_45.addWidget(self.search_line_group)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabledep = QtWidgets.QTableWidget(self.tab_3)
        self.tabledep.setGeometry(QtCore.QRect(0, 90, 700, 700))
        self.tabledep.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabledep.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabledep.setObjectName("tabledep")
        self.tabledep.setColumnCount(0)
        self.tabledep.setRowCount(0)
        self.deletedep = QtWidgets.QPushButton(self.tab_3)
        self.deletedep.setGeometry(QtCore.QRect(260, 10, 131, 61))
        self.deletedep.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.deletedep.setText("")
        self.deletedep.setIcon(icon2)
        self.deletedep.setIconSize(QtCore.QSize(50, 50))
        self.deletedep.setObjectName("deletedep")
        self.adddep = QtWidgets.QPushButton(self.tab_3)
        self.adddep.setGeometry(QtCore.QRect(0, 10, 131, 61))
        self.adddep.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.adddep.setText("")
        self.adddep.setIcon(icon)
        self.adddep.setIconSize(QtCore.QSize(50, 50))
        self.adddep.setObjectName("adddep")
        self.editdep = QtWidgets.QPushButton(self.tab_3)
        self.editdep.setGeometry(QtCore.QRect(130, 10, 131, 61))
        self.editdep.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.editdep.setText("")
        self.editdep.setIcon(icon1)
        self.editdep.setIconSize(QtCore.QSize(50, 50))
        self.editdep.setObjectName("editdep")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(390, 0, 311, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_38 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_54.addWidget(self.label_38)
        self.search_line_dep = QtWidgets.QLineEdit(self.layoutWidget2)
        self.search_line_dep.setObjectName("search_line_dep")
        self.horizontalLayout_54.addWidget(self.search_line_dep)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tablepos = QtWidgets.QTableWidget(self.tab_4)
        self.tablepos.setGeometry(QtCore.QRect(0, 90, 700, 700))
        self.tablepos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablepos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablepos.setObjectName("tablepos")
        self.tablepos.setColumnCount(0)
        self.tablepos.setRowCount(0)
        self.deletepos = QtWidgets.QPushButton(self.tab_4)
        self.deletepos.setGeometry(QtCore.QRect(260, 10, 131, 61))
        self.deletepos.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.deletepos.setText("")
        self.deletepos.setIcon(icon2)
        self.deletepos.setIconSize(QtCore.QSize(50, 50))
        self.deletepos.setObjectName("deletepos")
        self.addpos = QtWidgets.QPushButton(self.tab_4)
        self.addpos.setGeometry(QtCore.QRect(0, 10, 131, 61))
        self.addpos.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.addpos.setText("")
        self.addpos.setIcon(icon)
        self.addpos.setIconSize(QtCore.QSize(50, 50))
        self.addpos.setObjectName("addpos")
        self.editpos = QtWidgets.QPushButton(self.tab_4)
        self.editpos.setGeometry(QtCore.QRect(130, 10, 131, 61))
        self.editpos.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.editpos.setText("")
        self.editpos.setIcon(icon1)
        self.editpos.setIconSize(QtCore.QSize(50, 50))
        self.editpos.setObjectName("editpos")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(390, 0, 311, 81))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.label_40 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_57.addWidget(self.label_40)
        self.search_line_pos = QtWidgets.QLineEdit(self.layoutWidget3)
        self.search_line_pos.setObjectName("search_line_pos")
        self.horizontalLayout_57.addWidget(self.search_line_pos)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addemployee.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Добавить</span></p></body></html>"))
        self.addemployee.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.editemployee.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Выберите элемент для редактирования</p></body></html>"))
        self.deleteemployee.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Удалить</span></p></body></html>"))
        self.tableemp.setSortingEnabled(True)
        self.label_16.setText(_translate("MainWindow", "Найти:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Сотрудники"))
        self.addgroup.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Добавить</span></p></body></html>"))
        self.addgroup.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.editgroup.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Выберите элемент для редактирования</p></body></html>"))
        self.deletegroup.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Удалить</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Найти:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Группы"))
        self.deletedep.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Удалить</span></p></body></html>"))
        self.adddep.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Добавить</span></p></body></html>"))
        self.adddep.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.editdep.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Выберите элемент для редактирования</p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "Найти:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Отделы"))
        self.deletepos.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Удалить</span></p></body></html>"))
        self.addpos.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Добавить</span></p></body></html>"))
        self.addpos.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.editpos.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Выберите элемент для редактирования</p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "Найти:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Должности"))
        self.action_5.setText(_translate("MainWindow", "Шрифт"))
        self.action_6.setText(_translate("MainWindow", "Избранное"))
        self.action_2.setText(_translate("MainWindow", "Обычная"))
        self.action_3.setText(_translate("MainWindow", "Темная"))
