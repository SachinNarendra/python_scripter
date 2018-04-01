import __main__
import code as _code
import sys as _sys


class Interpreter(_code.InteractiveInterpreter):
    def __init__(self, local_variables):
        # InteractiveInterpreter is an OldStyle class so super can't be used
        # super(Interpreter, self).__init__(Interpreter, local_variables)
        _code.InteractiveInterpreter.__init__(self, local_variables)

    def execute_script(self, script):
        _code.InteractiveInterpreter.runcode(self, script)


if __name__ == "__main__":
    test_script = '''
my_var = 'Interpreter is working!'
import os
print os
    '''
    test_interpreter = Interpreter(None)

    test_interpreter.execute_script(test_script)
    test_interpreter.execute_script("print my_var")

