# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd.ui'
#
# Created: Sun Dec 23 06:21:43 2012
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(912, 696)
        Form.setMouseTracking(True)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(True)
        self.Input = QtGui.QTextEdit(Form)
        self.Input.setGeometry(QtCore.QRect(20, 60, 871, 151))
        self.Input.setObjectName(_fromUtf8("Input"))
        self.Output = QtGui.QTextEdit(Form)
        self.Output.setGeometry(QtCore.QRect(20, 260, 871, 361))
        self.Output.setObjectName(_fromUtf8("Output"))
        #self.Verbose = QtGui.QCheckBox(Form)
        #self.Verbose.setGeometry(QtCore.QRect(20, 650, 96, 22))
        #self.Verbose.setObjectName(_fromUtf8("Verbose"))
        self.Generate = QtGui.QPushButton(Form)
        self.Generate.setGeometry(QtCore.QRect(330, 640, 561, 41))
        self.Generate.setObjectName(_fromUtf8("Generate"))
        self.input = QtGui.QLabel(Form)
        self.input.setGeometry(QtCore.QRect(190, 20, 241, 21))
        self.input.setObjectName(_fromUtf8("input"))
        self.Upload = QtGui.QPushButton(Form)
        self.Upload.setGeometry(QtCore.QRect(450, 20, 441, 31))
        self.Upload.setObjectName(_fromUtf8("Upload"))
        self.ouput = QtGui.QLabel(Form)
        self.ouput.setGeometry(QtCore.QRect(20, 230, 171, 17))
        self.ouput.setObjectName(_fromUtf8("ouput"))
        self.Clear = QtGui.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(160, 640, 141, 41))
        self.Clear.setObjectName(_fromUtf8("Clear"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Code Generator", None))
        #self.Verbose.setText(_translate("Form", "Verbose", None))
        self.Generate.setText(_translate("Form", "Generate", None))
        self.input.setText(_translate("Form", "Enter the input or upload input file", None))
        self.Upload.setText(_translate("Form", "Upload", None))
        self.ouput.setText(_translate("Form", "Ouput", None))
        self.Clear.setText(_translate("Form", "Clear Output", None))

