# -*- coding: utf-8 -*-

"""
 Executes a script
"""
class Exe:
    
    interpreter = None

    def __init__(self, interpreter):
        self.interpreter = interpreter    
    
    def run(self):
        response = None
        command = self.interpreter.next()
        while (command):
            response = self.sendRequest(command, response)
            command = self.interpreter.next()

        return response

    def sendRequest(self, command, body):
        return None 
