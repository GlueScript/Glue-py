# -*- coding: utf-8 -*-

from glue.interpreter import Interpreter
from glue.exe import Exe

script = 'http://forum.net/forums/ >> http://template.net/html'

interpreter = Interpreter(script)
exe = Exe(interpreter)

response = exe.run()

print response

