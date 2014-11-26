# -*- coding: utf-8 -*-
# integration test case of parser

import unittest
from .interpreter import Interpreter
from .command import Command

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        """ init test fixtures """

    def tearDown(self):
        """ remove test fixtures """

    """ test that calling next returns a Command """
    def testNextReturnsACommand(self):
        script = 'http://endpoint.com/thing >> http://service.net/'
        interpreter = Interpreter(script)
        command = interpreter.next()
        self.assertTrue(isinstance(command, Command))
