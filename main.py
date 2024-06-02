import sys
import os

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import matplotlib.font_manager
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import InputFileHandler
import Plotter
import Coordinate
import Icons
import numpy as np
import random

# Param initialization
x_array = []
y_array = []
x_array_step = []
y_array_step = []
eps = 0

# axis initialization
x_axis_name = "x"
y_axis_name = "y"
x_axis_location = "center"
y_axis_location = "center"
x_axis_rotation = 0
y_axis_rotation = 0
x_log_axis = False
y_log_axis = False

title = "predrawing"
comments_x_axis = []
comments_x_coordinates = []

# font initialization
fonts = []
graph_font = "Times New Roman"
math_font = "dejavusans"


class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("interface.ui", self)

        self.setWindowTitle("UWWWWEEEEEEEEEEEEEEEEEE")

        # Navigation Toolbar
        self.toolbar = NavigationToolbar(self.MplWidget.canvas, self)  # For toolbar interaction
        self.toolbar.hide()  # Hide the default toolbar

        # Initialization
        self.initial_font()
        self.initial_table()
        self.predrawing()

        # Left Buttons Code
        self.pushButton_Pan.clicked.connect(self.pan)
        self.pushButton_Draw.clicked.connect(self.draw_graph)
        self.pushButton_Reset.clicked.connect(self.home)
        self.pushButton_OpenFile.clicked.connect(self.open_file)
        self.pushButton_Save.clicked.connect(self.save)
        self.pushButton_Zoom.clicked.connect(self.zoom)

    def initial_font(self):
        global fonts, graph_font, math_font
        fpaths = matplotlib.font_manager.findSystemFonts()
        for i in fpaths:
            f = matplotlib.font_manager.get_font(i)
            fonts.append(f.family_name)
        fonts.sort()
        fonts = list(dict.fromkeys(fonts))
        self.comboBox_GraphFont.addItems(fonts)
        math_fonts = ['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans']
        self.comboBox_MathFont.addItems(math_fonts)

    def initial_table(self):
        # table_width = self.tableWidget_Coordinates.viewport().width()
        header = self.tableWidget_Coordinates.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        # table_width = self.tableWidget_CoordinatesComment.viewport().width()
        header = self.tableWidget_CoordinatesComment.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        '''self.tableWidget_Coordinates.item(0, 0).setBackground(QtGui.QColor(125, 125, 125))
        self.tableWidget_Coordinates.item(0, 0).setBackground(QtGui.QColor(125, 125, 125))'''

    def predrawing(self):
        Plotter.plot_graph(self)

    def update_coordinate_table(self):
        global x_array, y_array
        row = 0
        self.tableWidget_Coordinates.setRowCount(len(x_array))
        self.tableWidget_CoordinatesComment.setRowCount(len(x_array))
        for x in x_array:
            item_x = QtWidgets.QTableWidgetItem(str(x_array[row]))
            item_x.setFlags(item_x.flags() & ~QtCore.Qt.ItemIsEditable)

            self.tableWidget_Coordinates.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x_array[row])))
            self.tableWidget_CoordinatesComment.setItem(row, 0, item_x.clone())
            self.tableWidget_Coordinates.setItem(row, 1, QtWidgets.QTableWidgetItem(str(y_array[row])))
            row = row + 1

    def get_coordinate_comments(self):
        row = 0
        global x_array, comments_x_axis, comments_x_coordinates
        comments_x_coordinates = []
        comments_x_axis = []
        if self.checkBox_CommentX.checkState() == 0:
            return
        for i in x_array:
            item = self.tableWidget_CoordinatesComment.item(row, 1)
            if item is not None and item.text() != '':
                comments_x_coordinates.append(float(self.tableWidget_CoordinatesComment.item(row, 0).text()))
                comments_x_axis.append(item.text())
            row += 1

        print("comment by x axis")
        print(comments_x_coordinates)
        print(comments_x_axis)

    def stepgraph_coordinates(self):
        global x_array, y_array, x_array_step, y_array_step, eps
        eps = (self.LineEdit_eps.text())
        if eps == "":
            eps = 0
        # Duplicate the coordinates to make a stepwise graph
        x_coordinates, y_coordinates = Coordinate.duplicate_coordinates(x_array, y_array)
        # Parameters for lower and higher border
        x_array_step, y_array_step = Coordinate.add_boundaries(x_coordinates, y_coordinates, eps)

    def draw_graph(self):
        global x_array, y_array, x_array_step, y_array_step, graph_font, math_font, x_axis_name, y_axis_name, title,\
            x_axis_rotation, y_axis_rotation, x_axis_location, y_axis_location, comments_x_axis, comments_x_coordinates
        if len(x_array) == 0:
            self.predrawing()
            return

        self.general_update()
        self.MplWidget.canvas.axes.clear()
        if self.checkBox_StepLine.checkState() == 0:
            Plotter.plot_graph(self, x_array, y_array, x_axis_name, y_axis_name, x_axis_rotation, y_axis_rotation,
                               x_axis_location, y_axis_location, title, x_log_axis, y_log_axis, graph_font, math_font,
                               comments_x_axis, comments_x_coordinates)
        if self.checkBox_StepLine.checkState() == 2:
            Plotter.plot_graph(self, x_array_step, y_array_step, x_axis_name, y_axis_name, x_axis_rotation,
                               y_axis_rotation, x_axis_location, y_axis_location, title,
                               x_log_axis, y_log_axis, graph_font, math_font,
                               comments_x_axis, comments_x_coordinates)

    def general_update(self):
        global x_array, y_array, graph_font, math_font, x_axis_name, y_axis_name, title, \
            x_axis_rotation, y_axis_rotation, x_axis_location, y_axis_location
        graph_font = self.comboBox_GraphFont.currentText()
        math_font = self.comboBox_MathFont.currentText()
        title = self.LineEdit_GraphTitle.text()
        x_axis_name = self.LineEdit_XAxisName.text()
        y_axis_name = self.LineEdit_YAxisName.text()
        x_axis_location = self.comboBox_XLocation.currentText()
        y_axis_location = self.comboBox_YLocation.currentText()
        x_axis_location.lower()
        y_axis_location.lower()
        x_axis_rotation = self.spinBox_XAxisRotate.value()
        y_axis_rotation = self.spinBox_YAxisRotate.value()

        self.stepgraph_coordinates()
        self.get_coordinate_comments()


    def pan(self):
        """
        Enable panning mode for the Matplotlib canvas.
        """
        self.MplWidget.canvas.toolbar.pan()

    def zoom(self):
        """
        Enable zooming mode for the Matplotlib canvas.
        """
        self.toolbar.zoom()

    def home(self):
        """
        Reset the view to the original limits.
        """
        self.toolbar.home()

    def save(self):
        """
        Save the current figure.
        """
        self.toolbar.save_figure()

    def open_file(self):
        global x_array, y_array, x_array_step, y_array_step
        filename = None
        nofile = ('', '')
        filename = QFileDialog.getOpenFileName(self, "Open File", "D:\3. belajar\9. diplom code\WithUI",
                                               "Maxima Files (*.mac)")

        print(filename)
        # Output filename to screen
        if filename != nofile:
            x_array, y_array = InputFileHandler.OpenFileHandler(filename[0])
            base_name = os.path.basename(filename[0])  # Extract the filename without the path
            self.Label_Location.setText(base_name)
            self.update_coordinate_table()
            self.stepgraph_coordinates()

        print("Input Data")
        print("X values:", x_array)
        print("Y values:", y_array)
        print("X-Step values:", x_array_step)
        print("Y-Step values:", y_array_step)


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
