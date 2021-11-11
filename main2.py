import sys

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QFileDialog, QMessageBox, QTableWidget

from employeedbservice import *
from mainwindow import Ui_MainWindow
from employeedialog import Ui_Dialog
from groupdialog import Ui_Group_Dialog
from deppos import Ui_DepPos_Dialog

import enum


class WindowMode(enum.Enum):
    insert = 0
    update = 1


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dbservice = EmployeesDBService()

        self.buttons_connections()

        self.table_employees = QTableWidget()
        self.table_groups = QTableWidget()
        self.table_departments = QTableWidget()
        self.table_positions = QTableWidget()

        self.select_data()
        self.select_data1()

    def buttons_connections(self):
        self.addemployee.clicked.connect(self.add)
        self.addgroup.clicked.connect(self.add)
        self.adddep.clicked.connect(self.add)
        self.addpos.clicked.connect(self.add)

        self.deletepos.clicked.connect(self.delete_position)
        self.deleteemployee.clicked.connect(self.delete_employee)
        self.deletegroup.clicked.connect(self.delete_group)
        self.deletedep.clicked.connect(self.delete_department)

        self.editemployee.clicked.connect(self.edit_employees)
        self.editgroup.clicked.connect(self.edit_groups)
        self.editpos.clicked.connect(self.edit_positions)
        self.editdep.clicked.connect(self.edit_departments)

        self.search_line.textChanged.connect(self.find_employee)
        self.search_line_group.textChanged.connect(self.find_group)
        self.search_line_dep.textChanged.connect(self.find_dep)
        self.search_line_pos.textChanged.connect(self.find_pos)

        self.tableemp.itemClicked.connect(self.set_photo)

    def get_id_by_row(self, table):
        ID = False
        row = table.currentRow()
        if row >= 0:
            fl = table.item(row, 0).text()
            ID = int(fl)
        return ID

    def set_photo(self):
        image_path = self.dbservice.get_employee(window.get_id_by_row(window.tableemp)).picture
        pixmap = QPixmap(f'{image_path}')
        pixmap = pixmap.scaled(640, 480)
        self.picture.setPixmap(pixmap)

    def select_data1(self):
        self.insert_data_in_table(self.dbservice.get_employees_for_display(), self.table_employees, *EmployeesDBService.model_field_names[Employee])
        self.insert_data_in_table(self.dbservice.get_groups_for_display(), self.table_groups, *EmployeesDBService.model_field_names[Group])
        self.insert_data_in_table(self.dbservice.get_departments_for_display(), self.table_departments, *EmployeesDBService.model_field_names[Department])
        self.insert_data_in_table(self.dbservice.get_positions_for_display(), self.table_positions, *EmployeesDBService.model_field_names[Position])

    def select_data(self):
        self.insert_data_in_table(self.dbservice.get_employees_for_display(), self.tableemp, *EmployeesDBService.model_field_names[Employee])
        self.insert_data_in_table(self.dbservice.get_groups_for_display(), self.tablegroup, *EmployeesDBService.model_field_names[Group])
        self.insert_data_in_table(self.dbservice.get_departments_for_display(), self.tabledep, *EmployeesDBService.model_field_names[Department])
        self.insert_data_in_table(self.dbservice.get_positions_for_display(), self.tablepos, *EmployeesDBService.model_field_names[Position])

    def insert_data_in_table(self, res, table, number_of_columns, columns_names):
        table.setSortingEnabled(False)
        table.setColumnCount(number_of_columns)
        table.setRowCount(0)
        table.setHorizontalHeaderLabels(columns_names)
        for i, row in enumerate(res):
            table.setRowCount(
                table.rowCount() + 1)
            for j, elem in enumerate(row):
                if elem is None:
                    elem = "Не назначено"
                table.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        table.setSortingEnabled(True)

    def closeEvent(self, event):
        self.dbservice.close()

    def add(self):
        source = self.sender()
        if source == self.addemployee:
            self.child = EmployeeWindow(self.dbservice, WindowMode.insert, self)
            self.child.show()
        elif source == self.addgroup:
            self.child1 = GroupWindow(self.dbservice, WindowMode.insert)
            self.child1.show()
        elif source == self.adddep:
            self.child2 = DepartmentWindow(self.dbservice, WindowMode.insert)
            self.child2.show()
        elif source == self.addpos:
            self.child3 = PositionWindow(self.dbservice, WindowMode.insert)
            self.child3.show()

    def edit_employees(self):
        ID = self.get_id_by_row(self.tableemp)
        if ID:
            employee = self.dbservice.get_employee(ID)
            try:
                cur_group_title = self.dbservice.get_group(employee.groupid).title
            except:
                cur_group_title = None
            try:
                cur_pos_title = self.dbservice.get_position(employee.positionid).title
            except:
                cur_pos_title = None
            self.child = EmployeeWindow(self.dbservice, WindowMode.update, ID, employee, cur_group_title, cur_pos_title)
            self.child.show()

    def edit_groups(self):
        ID = self.get_id_by_row(self.tablegroup)
        if ID:
            group = self.dbservice.get_group(ID)
            try:
                res = self.dbservice.get_department(group.departmentid).title
            except:
                res = None
            self.child1 = GroupWindow(self.dbservice, WindowMode.update, ID, group.title, res)
            self.child1.show()

    def edit_departments(self):
        ID = self.get_id_by_row(self.tabledep)
        if ID:
            department = self.dbservice.get_department(ID)
            self.child2 = DepartmentWindow(self.dbservice, WindowMode.update, ID, department.title)
            self.child2.show()

    def edit_positions(self):
        ID = self.get_id_by_row(self.tablepos)
        if ID:
            position = self.dbservice.get_position(ID)
            self.child3 = PositionWindow(self.dbservice, WindowMode.update, ID, position.title)
            self.child3.show()

    def delete_item(self, ID, item):
        if ID:
            valid = QMessageBox.question(
                self, '', f"Действительно удалить элемент с ИД {ID}",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.dbservice.delete_item(item)
                self.select_data()

    def delete_employee(self):
        ID = self.get_id_by_row(self.tableemp)
        self.delete_item(ID, Employee(ID, "", None, -1, -1, ""))

    def delete_group(self):
        ID = self.get_id_by_row(self.tablegroup)
        self.delete_item(ID, Group(ID, "", -1))

    def delete_department(self):
        ID = self.get_id_by_row(self.tabledep)
        self.delete_item(ID, Department(ID, ""))

    def delete_position(self):
        ID = self.get_id_by_row(self.tablepos)
        self.delete_item(ID, Position(ID, ""))

    def find_employee(self):
        search_text = self.search_line.text()
        result = self.table_employees.findItems(search_text, QtCore.Qt.MatchStartsWith)
        self.tableemp.clear()
        rows = [item.row() for item in result] if search_text else list(range(self.table_employees.rowCount()))
        self.extract_rows(rows, self.table_employees, self.tableemp, *EmployeesDBService.model_field_names[Employee])

    def find_group(self):
        search_text = self.search_line_group.text()
        result = self.table_groups.findItems(search_text, QtCore.Qt.MatchStartsWith)
        self.tablegroup.clear()
        rows = [item.row() for item in result] if search_text else list(range(self.table_groups.rowCount()))
        self.extract_rows(rows, self.table_groups, self.tablegroup, *EmployeesDBService.model_field_names[Group])

    def find_dep(self):
        search_text = self.search_line_dep.text()
        result = self.table_departments.findItems(search_text, QtCore.Qt.MatchStartsWith)
        self.tabledep.clear()
        rows = [item.row() for item in result] if search_text else list(range(self.table_departments.rowCount()))
        self.extract_rows(rows, self.table_departments, self.tabledep, *EmployeesDBService.model_field_names[Department])

    def find_pos(self):
        search_text = self.search_line_pos.text()
        result = self.table_positions.findItems(search_text, QtCore.Qt.MatchStartsWith)
        self.tabledep.clear()
        rows = [item.row() for item in result] if search_text else list(range(self.table_positions.rowCount()))
        self.extract_rows(rows, self.table_positions, self.tablepos, EmployeesDBService.model_field_names[Position])

    def extract_rows(self, r, storing_data_table, table, num, field_names):
        r = set(r)
        rows = [[storing_data_table.item(i, j).text() for j in range(num)] for i in r]
        self.insert_data_in_table(rows, table, num, field_names)


class EmployeeWindow(QDialog, Ui_Dialog):

    def __init__(self, dbservice: EmployeesDBService, mode: WindowMode, ID=None, employee=None, cur_group_title=None,
                 cur_pos_title=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # uic.loadUi('dialog.ui', self)
        self.dbservice = dbservice
        self.groups = self.dbservice.get_groups()
        self.positions = self.dbservice.get_positions()
        self.update_combo()
        self.lineEdit.textChanged.connect(self.on_text_changed)
        if employee:
            self.lineEdit.setText(employee.fullname)
            self.dateEdit.setDate(employee.dob)
            self.picture = employee.picture
        else:
            self.picture = None
        if ID:
            self.ID = ID
        if cur_group_title:
            self.comboBox.setCurrentText(cur_group_title)
        if cur_pos_title:
            self.comboBox_2.setCurrentText(cur_pos_title)
        self.mode = mode
        self.buttonBox.accepted.connect(self.dialog)

    def on_text_changed(self):
        self.buttonBox.setEnabled(bool(self.lineEdit.text()))

    def update_combo(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        result = [g.title for g in self.groups]
        for i in result:
            self.comboBox.addItem(i)
        result = [p.title for p in self.positions]
        for i in result:
            self.comboBox_2.addItem(i)

    def dialog(self):
        fullname = self.lineEdit.text()
        if fullname != "":
            DOB = self.dateEdit.text().split(".")
            DOB.reverse()
            DOB = ".".join(DOB)
            cur_group_title = self.comboBox.currentText()
            cur_position_title = self.comboBox_2.currentText()

            groupid = -1
            for i in self.groups:
                if i.title == cur_group_title:
                    groupid = i.id

            positionid = -1
            for i in self.positions:
                if i.title == cur_position_title:
                    positionid = i.id

            if self.mode == WindowMode.insert:
                self.dbservice.add_item(Employee(-1, fullname, DOB, groupid, positionid, self.picture))
            else:
                self.dbservice.update_item(Employee(self.ID, fullname, DOB, groupid, positionid, self.picture))
            window.select_data()

    def mybutton_clicked(self):
        options = QFileDialog.Options()
        self.picture, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                      options=options)


class GroupWindow(QDialog, Ui_Group_Dialog):
    def __init__(self, dbservice: EmployeesDBService, mode: WindowMode, ID=None, title=None, cur_text=None,
                 parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # uic.loadUi('dialog1.ui', self)
        self.dbservice = dbservice
        self.departments = self.dbservice.get_departments()
        self.update_combo()
        self.lineEdit.textChanged.connect(self.on_text_changed)
        if title:
            self.lineEdit.setText(title)
        if cur_text:
            self.comboBox.setCurrentText(cur_text)
        self.mode = mode
        self.ID = ID
        self.buttonBox.accepted.connect(self.dialog)

    def on_text_changed(self):
        self.buttonBox.setEnabled(bool(self.lineEdit.text()))

    def update_combo(self):
        self.comboBox.clear()
        result = [d.title for d in self.departments]
        for i in result:
            self.comboBox.addItem(i)

    def dialog(self):
        title = self.lineEdit.text()
        if title != "":

            cur_dep_title = self.comboBox.currentText()
            departmentid = -1

            for i in self.departments:
                if i.title == cur_dep_title:
                    departmentid = i.id

            if self.mode == WindowMode.insert:
                self.dbservice.add_item(Group(-1, title, departmentid))
            else:
                self.dbservice.update_item(Group(self.ID, title, departmentid))
            window.select_data()


class BaseWindow(QDialog, Ui_DepPos_Dialog):
    def __init__(self, dbservice: EmployeesDBService, mode: WindowMode, id=None, title=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # uic.loadUi('dialog2.ui', self)
        self.lineEdit.textChanged.connect(self.on_text_changed)
        self.mode = mode
        self.ID = id
        if title:
            self.lineEdit.setText(title)
        self.dbservice = dbservice
        self.buttonBox.accepted.connect(self.dialog)

    def on_text_changed(self):
        self.buttonBox.setEnabled(bool(self.lineEdit.text()))


class DepartmentWindow(BaseWindow):

    def dialog(self):
        self.title = self.lineEdit.text()
        if self.title != "":
            if self.mode == WindowMode.insert:
                self.dbservice.add_item(Department(-1, self.title))
            else:
                self.dbservice.update_item(Department(self.ID, self.title))
        window.select_data()


class PositionWindow(BaseWindow):

    def dialog(self):
        self.title = self.lineEdit.text()
        if self.title != "":
            if self.mode == WindowMode.insert:
                self.dbservice.add_item(Position(-1, self.title))
            else:
                self.dbservice.update_item(Position(self.ID, self.title))
        window.select_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
