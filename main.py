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
coordinate = {}
x_array_step = []
y_array_step = []
eps = 0

# axes initialization
# x-axis title
x_axis_name = "x"
x_axis_location = "center"
x_axis_rotation = 0
x_axis_size = 16
x_axis_color = "#000000"

# y axis title
y_axis_name = "y"
y_axis_location = "center"
y_axis_rotation = 0
y_axis_size = 16
y_axis_color = "#000000"

# axis notation
x_log_axis = False
y_log_axis = False
axis_scientific = False
automatic_scientific = False
scientific_power = 1
comment_drawing = False
axes_size = 10
axes_color = "#000000"

# title
title = "predrawing"
title_size = 20
title_color = "#000000"

# Comments part
comments_x_axis = []
comments_x_coordinates = []
comments_x_size = 16
comments_x_color = "#000000"

comments_drawing_x = []
comments_drawing_y = []
comments_drawing_text = []
comments_size = []
comments_initial_color = "#000000"
comments_color = []

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

        # Comment Button
        self.pushButton_AddComment.clicked.connect(self.add_drawing_comments)
        self.pushButton_RemoveComment.clicked.connect(self.remove_drawing_comment)

        # Color Button Initialization
        self.button_names = [
            'pushButton_ColorTitle',
            'pushButton_ColorXAxis',
            'pushButton_ColorYAxis',
            'pushButton_ColorAxisNotation',
            'pushButton_ColorCommentX',
            'pushButton_ColorDrawing'
        ]

        # Dictionary to store button widgets
        self.buttons = {name: getattr(self, name) for name in self.button_names}

        # Connect each button to the color dialog
        for key, button in self.buttons.items():
            button.clicked.connect(lambda _, b=button, k=key: self.color_dialog(b, k))

    def color_dialog(self, button, setting):
        global title_color, x_axis_color, y_axis_color, axes_color, comments_x_color, comments_color, \
            comments_initial_color
        color = QColorDialog.getColor()
        if color.isValid():
            hex_color = color.name()
            button.setText(hex_color)
            button.setStyleSheet(
                f'border: 2px solid {hex_color};'
            )
            setattr(self, setting, hex_color)

            # Update the corresponding global color parameter based on the button
            button_name = button.objectName()
            if button_name == 'pushButton_ColorTitle':
                title_color = hex_color
            elif button_name == 'pushButton_ColorXAxis':
                x_axis_color = hex_color
            elif button_name == 'pushButton_ColorYAxis':
                y_axis_color = hex_color
            elif button_name == 'pushButton_ColorAxisNotation':
                axes_color = hex_color
            elif button_name == 'pushButton_ColorCommentX':
                comments_x_color = hex_color
            elif button_name == 'pushButton_ColorDrawing':
                comments_initial_color = hex_color

            # debug color
            print(f"title_color: {title_color}")
            print(f"x_axis_color: {x_axis_color}")
            print(f"y_axis_color: {y_axis_color}")
            print(f"axes_color: {axes_color}")
            print(f"comments_x_color: {comments_x_color}")
            print(f"comments_color: {comments_color}")

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

        header = self.tableWidget_DrawingComment.horizontalHeader()
        header.setSectionResizeMode(0, 70)
        header.setSectionResizeMode(1, 70)
        header.setSectionResizeMode(2, 70)
        header.setSectionResizeMode(3, 70)
        header.setSectionResizeMode(4, 70)

    def predrawing(self):
        Plotter.plot_graph(self)

    def update_table(self):
        global x_array, y_array
        self.update_comment_drawing()
        self.tableWidget_Coordinates.setRowCount(len(x_array))
        self.tableWidget_CoordinatesComment.setRowCount(len(x_array))
        for row in range(len(x_array)):
            item_x = QtWidgets.QTableWidgetItem(str(x_array[row]))
            item_x.setFlags(item_x.flags() & ~QtCore.Qt.ItemIsEditable)

            self.tableWidget_Coordinates.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x_array[row])))
            self.tableWidget_Coordinates.setItem(row, 1, QtWidgets.QTableWidgetItem(str(y_array[row])))
            self.tableWidget_CoordinatesComment.setItem(row, 0, item_x.clone())

    def update_comment_drawing(self):
        global x_array, y_array, comments_drawing_x, comments_drawing_y, comments_drawing_text, comments_size, \
            comments_color
        self.tableWidget_DrawingComment.setRowCount(len(comments_drawing_x))
        for row in range(len(comments_drawing_x)):
            self.tableWidget_DrawingComment.setItem(row, 0, QtWidgets.QTableWidgetItem(str(comments_drawing_x[row])))
            self.tableWidget_DrawingComment.setItem(row, 1, QtWidgets.QTableWidgetItem(str(comments_drawing_y[row])))
            self.tableWidget_DrawingComment.setItem(row, 2, QtWidgets.QTableWidgetItem(comments_drawing_text[row]))
            self.tableWidget_DrawingComment.setItem(row, 3, QtWidgets.QTableWidgetItem(str(comments_size[row])))
            self.tableWidget_DrawingComment.setItem(row, 4, QtWidgets.QTableWidgetItem(comments_color[row]))

    def get_coordinate_comments(self):
        global x_array, comments_x_axis, comments_x_coordinates
        comments_x_coordinates = []
        comments_x_axis = []
        if self.checkBox_CommentX.checkState() == 0:
            return
        for row in range(len(x_array)):
            item = self.tableWidget_CoordinatesComment.item(row, 1)
            if item is not None and item.text() != '':
                comments_x_coordinates.append(float(self.tableWidget_CoordinatesComment.item(row, 0).text()))
                comments_x_axis.append(item.text())

        print("comment by x axis")
        print(comments_x_coordinates)
        print(comments_x_axis)

    def add_drawing_comments(self):
        global comments_drawing_x, comments_drawing_y, comments_drawing_text, comments_color, comments_size, \
            comments_initial_color
        x_value = self.LineEdit_CommentOnDrawingX.text()
        y_value = self.LineEdit_CommentOnDrawingY.text()
        text_value = self.LineEdit_CommentOnDrawingText.text()
        color_value = comments_initial_color
        size_value = self.spinBox_CommentDrawing.value()

        if x_value == '' or y_value == '' or text_value == '':
            return  # Do nothing if any of the fields are empty

        try:
            x_value_float = float(x_value)
            y_value_float = float(y_value)
        except ValueError:
            # Show an error message box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Invalid input")
            msg.setInformativeText("x_value and y_value must be valid float numbers")
            msg.setWindowTitle("Input Error")
            msg.exec_()
            return

        # Check for duplicates
        for x, y, text in zip(comments_drawing_x, comments_drawing_y, comments_drawing_text):
            if x == x_value_float and y == y_value_float and text == text_value:
                # Show a duplicate error message box
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Duplicate comment")
                msg.setInformativeText("The comment you are trying to add already exists.")
                msg.setWindowTitle("Duplicate Error")
                msg.exec_()
                return

        # If no duplicates are found, append the new comment
        comments_drawing_x.append(x_value_float)
        comments_drawing_y.append(y_value_float)
        comments_drawing_text.append(text_value)
        if not color_value.startswith('#') or len(color_value) != 7:
            color_value = '#000000'
        comments_color.append(color_value)
        comments_size.append(size_value)

        print("comment on drawing")
        print(comments_drawing_x)
        print(comments_drawing_y)
        print(comments_drawing_text)
        print(comments_color)
        print(comments_size)
        self.update_comment_drawing()

    def remove_drawing_comment(self):
        global comments_drawing_x, comments_drawing_y, comments_drawing_text

        index_value = self.spinBox_RemoveIndex.value()

        # Adjust for 0-based index
        index = index_value - 1

        if index < 0 or index >= len(comments_drawing_x):
            # Show an error message box if index is out of range
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Invalid index")
            msg.setInformativeText("The index you provided is out of range.")
            msg.setWindowTitle("Index Error")
            msg.exec_()
            return

        # Remove the comment at the specified index
        comments_drawing_x.pop(index)
        comments_drawing_y.pop(index)
        comments_drawing_text.pop(index)

        print("comment removed")
        print(comments_drawing_x)
        print(comments_drawing_y)
        print(comments_drawing_text)
        self.update_comment_drawing()

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
        global x_array, y_array, graph_font, math_font, x_axis_name, y_axis_name, title, \
            x_axis_rotation, y_axis_rotation, x_axis_location, y_axis_location, \
            axis_scientific, automatic_scientific, scientific_power, comments_x_axis, comments_x_coordinates, \
            x_axis_size, x_axis_color, y_axis_size, y_axis_color, axes_size, axes_color, title_size, title_color, \
            comments_x_size, comments_x_color, comments_size, comments_color
        if len(x_array) == 0:
            self.predrawing()
            return

        self.general_update()
        self.MplWidget.canvas.axes.clear()
        if self.checkBox_StepLine.checkState() == 0:
            Plotter.plot_graph(self, x_array, y_array, x_axis_name, y_axis_name, x_axis_rotation, y_axis_rotation,
                               x_axis_location, y_axis_location, title, x_log_axis, y_log_axis, graph_font, math_font,
                               comments_x_axis, comments_x_coordinates,
                               comment_drawing, comments_drawing_x, comments_drawing_y, comments_drawing_text,
                               axis_scientific, automatic_scientific, scientific_power,
                               x_axis_size, x_axis_color, y_axis_size, y_axis_color, axes_size, axes_color, title_size,
                               title_color, comments_x_size, comments_x_color, comments_size, comments_color)
        if self.checkBox_StepLine.checkState() == 2:
            Plotter.plot_graph(self, x_array_step, y_array_step, x_axis_name, y_axis_name, x_axis_rotation,
                               y_axis_rotation, x_axis_location, y_axis_location, title,
                               x_log_axis, y_log_axis, graph_font, math_font,
                               comments_x_axis, comments_x_coordinates,
                               comment_drawing, comments_drawing_x, comments_drawing_y, comments_drawing_text,
                               axis_scientific, automatic_scientific, scientific_power,
                               x_axis_size, x_axis_color, y_axis_size, y_axis_color, axes_size, axes_color, title_size,
                               title_color, comments_x_size, comments_x_color, comments_size, comments_color)

    def general_update(self):
        global x_array, y_array, graph_font, math_font, x_axis_name, y_axis_name, title, \
            x_axis_rotation, y_axis_rotation, x_axis_location, y_axis_location, \
            axis_scientific, automatic_scientific, scientific_power, comment_drawing, \
            x_axis_size, x_axis_color, y_axis_size, y_axis_color, axes_size, axes_color, title_size, title_color, \
            comments_x_size, comments_x_color, comments_size, comments_color

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
        title_size = self.spinBox_TitleSize.value()
        x_axis_size = self.spinBox_XAxisSize.value()
        y_axis_size = self.spinBox_YAxisSize.value()
        axes_size = self.spinBox_AxisNotationSize.value()
        comments_x_size = self.spinBox_CommentXSize.value()

        if self.checkBox_ScientificNotation.checkState() == 2:
            axis_scientific = True
        else:
            axis_scientific = False
        if self.checkBox_AutomaticPower.checkState() == 2:
            automatic_scientific = True
        else:
            automatic_scientific = False
        scientific_power = self.spinBox_PowerLimit.value()

        if self.checkBox_CommentOnDrawing.checkState() == 2:
            comment_drawing = True
        else:
            comment_drawing = False

        self.stepgraph_coordinates()
        self.get_coordinate_comments()

    def pan(self):
        self.MplWidget.canvas.toolbar.pan()

    def zoom(self):
        self.toolbar.zoom()

    def home(self):
        self.toolbar.home()

    def save(self):
        self.toolbar.save_figure()

    def open_file(self):
        global x_array, y_array, x_array_step, y_array_step
        filename = None
        nofile = ('', '')
        current_folder_path = os.getcwd()
        filename = QFileDialog.getOpenFileName(self, "Open File", current_folder_path,
                                               "Maxima Files (*.mac)")

        print(filename)
        # Output filename to screen
        if filename != nofile:
            x_array, y_array = InputFileHandler.OpenFileHandler(filename[0])
            base_name = os.path.basename(filename[0])  # Extract the filename without the path
            self.Label_Location.setText(base_name)
            self.update_table()
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
