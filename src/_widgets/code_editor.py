import keyword as _keyword
import re as _re
import sys as _sys

from cStringIO import StringIO

from PyQt4 import (
    QtGui as _QtGui,
    QtCore as _QtCore,
)

from python_scripter._widgets.ui import code_editor_ui as _code_editor_ui
from python_scripter._core import interpreter as _interpreter


class CodeEditor(_QtGui.QDialog, _code_editor_ui.Ui_CodeEditor):
    def __init__(self, parent=None):
        super(CodeEditor, self).__init__(parent=parent)

        self._setup_ui()

        self._interpreter = _interpreter.Interpreter(None)

        self._setup_connections()

    def _setup_ui(self):
        self.setupUi(self)
        self.text_edit_input = _QtGui.QTextEdit(
            self
        )
        self.text_edit_input.setAcceptRichText(False)
        self.splitter_io.addWidget(
            self.text_edit_input
        )

    def _setup_connections(self):
        # Connect Buttons
        self.t_button_execute.clicked.connect(
            self._execute_code
        )

        self.t_button_clear_input.clicked.connect(
            self._clear_input
        )

        self.t_button_clear_output.clicked.connect(
            self._clear_output
        )

        self.t_button_clear_all.clicked.connect(
            self._clear_all
        )

        # Setup Shortcuts
        self._shortcut_execute = _QtGui.QShortcut(
            _QtGui.QKeySequence(
                _QtCore.Qt.CTRL + _QtCore.Qt.Key_Return
            ), self
        )

        self._shortcut_execute.activated.connect(
            self._execute_code
        )

    def _execute_code(self):

        string_io = StringIO()

        _sys.stdout = string_io
        _sys.stderr = string_io

        code = self._get_code_to_execute()

        input_text = code
        if self._is_variable(code.strip()):
            # code = "import pprint; pprint.pprint(%s)" % code
            code = "print %s" % code
            input_text = ""

        self._interpreter.execute_script(code)

        self._update_output_log(input_text, string_io.getvalue())

        _sys.stdout = _sys.__stdout__
        _sys.stderr = _sys.__stderr__

    def _update_output_log(self, code, output):

        output_list = [
            code,
            "Result :",
            output,
            "",
        ]

        output_text = self.text_edit_output.toPlainText() + '\n'.join(output_list)
        self.text_edit_output.setPlainText(output_text)
        scroll_bar = self.text_edit_output.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

    def _get_code_to_execute(self):

        text_cursor = self.text_edit_input.textCursor()
        selected_text = text_cursor.selectedText()

        if selected_text:
            # TODO : find a better solution to the hack
            code = str(selected_text.toAscii()).replace('?', '\n')
        else:
            code = str(self.text_edit_input.toPlainText())

        code_lines = code.split('\n')
        for index, code_line in enumerate(code_lines):
            code_lines[index] = code_line.rstrip()
        code = '\n'.join(code_lines)

        return code

    @staticmethod
    def _is_variable(code):

        for key_word in _keyword.kwlist:
            if code.startswith(key_word):
                return False

        if " = " in code:
            return False

        pattern_list = [
            # "[^\n:]",
            "^[a-zA-Z0-9_.]+$",  # objects
            "^[a-zA-Z0-9_.]+(.*\n*)$",  # functions
            "^dir\([a-zA-Z0-9_.]+\)$",
        ]

        pattern = "|".join(pattern_list)
        if _re.match(pattern, code):
            return True
        return False

    def _clear_input(self):
        self._clear_text_edit(self.text_edit_input)

    def _clear_output(self):
        self._clear_text_edit(self.text_edit_output)

    def _clear_all(self):
        self._clear_input()
        self._clear_output()

    def _clear_text_edit(self, text_edit):
        text_edit.clear()


if __name__ == "__main__":
    app = _QtGui.QApplication(_sys.argv)
    editor = CodeEditor()
    editor.show()
    _sys.exit(app.exec_())
