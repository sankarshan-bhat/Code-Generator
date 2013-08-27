from PyQt4 import QtGui, QtCore
from gui import Ui_Form
import sys
import os
import eval
import usage
import InfixTopostfix
import postfix
import re
import table
import main

class Writer(QtGui.QMainWindow):
	def __init__(self, w):
		self.writer = w	
	
	def write(self, s):
		self.writer.append(s)


class Test(QtGui.QMainWindow):
	def __init__(self):
		super(Test, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.Upload.clicked.connect(self.openFile)
		self.ui.Generate.clicked.connect(self.Run)
		self.ui.Clear.clicked.connect(self.Clear)
		self.setStyleSheet("QMainWindow {background-color: #A4A4A4; color: #000000}")
		#self.setStyleSheet("QLineEdit { background-color: yellow}");
		self.show()

	def openFile(self):
		f = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
		f = open(f, 'r')
		self.ui.Input.setText(f.read())
		f.close()

	def Run(self):
		self.inputList = self.ui.Input.toPlainText().split('\n')
		register, ok = QtGui.QInputDialog.getText(self, 'Input',
                'Enter number of Registers')
		if not ok:
            		register = "2"
			QtGui.QMessageBox.question(self, 'Message', 'You pressed Cancel. Default r = 2 will be taken', QtGui.QMessageBox.Ok)
		elif register == "":
			register = "2"
			QtGui.QMessageBox.question(self, 'Message', 'You did not enter anything. Default r = 2 will be taken', QtGui.QMessageBox.Ok)
		register = int(register)
		main.Main(Writer(self.ui.Output), self.inputList, register)

	def Clear(self):
		self.ui.Output.setText('')

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Test()
	sys.exit(app.exec_())
