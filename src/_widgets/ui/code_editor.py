# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../python_scripter/_widgets/ui/code_editor.ui'
#
# Created: Sun Apr  1 09:53:36 2018
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_CodeEditor(object):
    def setupUi(self, CodeEditor):
        CodeEditor.setObjectName(_fromUtf8("CodeEditor"))
        CodeEditor.resize(753, 570)
        self.verticalLayout = QtGui.QVBoxLayout(CodeEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.t_button_open = QtGui.QToolButton(CodeEditor)
        self.t_button_open.setMinimumSize(QtCore.QSize(32, 30))
        self.t_button_open.setObjectName(_fromUtf8("t_button_open"))
        self.horizontalLayout.addWidget(self.t_button_open)
        self.t_button_save = QtGui.QToolButton(CodeEditor)
        self.t_button_save.setMinimumSize(QtCore.QSize(32, 30))
        self.t_button_save.setObjectName(_fromUtf8("t_button_save"))
        self.horizontalLayout.addWidget(self.t_button_save)
        self.line = QtGui.QFrame(CodeEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 30))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.t_button_clear_input = QtGui.QToolButton(CodeEditor)
        self.t_button_clear_input.setMinimumSize(QtCore.QSize(32, 30))
        self.t_button_clear_input.setObjectName(_fromUtf8("t_button_clear_input"))
        self.horizontalLayout.addWidget(self.t_button_clear_input)
        self.t_button_clear_output = QtGui.QToolButton(CodeEditor)
        self.t_button_clear_output.setMinimumSize(QtCore.QSize(32, 30))
        self.t_button_clear_output.setObjectName(_fromUtf8("t_button_clear_output"))
        self.horizontalLayout.addWidget(self.t_button_clear_output)
        self.t_button_clear_all = QtGui.QToolButton(CodeEditor)
        self.t_button_clear_all.setMinimumSize(QtCore.QSize(32, 30))
        self.t_button_clear_all.setObjectName(_fromUtf8("t_button_clear_all"))
        self.horizontalLayout.addWidget(self.t_button_clear_all)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.t_button_execute = QtGui.QToolButton(CodeEditor)
        self.t_button_execute.setMinimumSize(QtCore.QSize(32, 30))
        self.t_button_execute.setObjectName(_fromUtf8("t_button_execute"))
        self.horizontalLayout.addWidget(self.t_button_execute)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter_io = QtGui.QSplitter(CodeEditor)
        self.splitter_io.setOrientation(QtCore.Qt.Vertical)
        self.splitter_io.setObjectName(_fromUtf8("splitter_io"))
        self.text_edit_output = QtGui.QTextEdit(self.splitter_io)
        self.text_edit_output.setEnabled(True)
        self.text_edit_output.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_edit_output.setReadOnly(True)
        self.text_edit_output.setObjectName(_fromUtf8("text_edit_output"))
        self.verticalLayout.addWidget(self.splitter_io)

        self.retranslateUi(CodeEditor)
        QtCore.QMetaObject.connectSlotsByName(CodeEditor)

    def retranslateUi(self, CodeEditor):
        CodeEditor.setWindowTitle(_translate("CodeEditor", "CodeEditor", None))
        self.t_button_open.setText(_translate("CodeEditor", "O", None))
        self.t_button_save.setText(_translate("CodeEditor", "S", None))
        self.t_button_clear_input.setText(_translate("CodeEditor", "Ci", None))
        self.t_button_clear_output.setText(_translate("CodeEditor", "Co", None))
        self.t_button_clear_all.setText(_translate("CodeEditor", "Ca", None))
        self.t_button_execute.setText(_translate("CodeEditor", "E", None))

