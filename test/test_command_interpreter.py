# -*- coding: utf-8 -*-
# integration test case of parser

import unittest
from ../src/command_interpreter import CommandInterpreter

class TestCommandInterpreter(unittest.TestCase):

    def setUp(self):
        """ init test fixtures """

    def tearDown(self):
        """ remove test fixtures """

    """ test that calling next returns a Command """
    def testNextReturnsACommand(self):
        script = 'http://endpoint.com/thing'
        interpreter = CommandInterpreter(script)
        command = interpreter.next()
