# -*- coding: utf-8 -*-

from .command import Command

class Interpreter:
    
    commands = None
    
    script = ''
    
    index = 0

    def __init__(self, script):
        self.script = script
    
    """ 
        return the next Command ie. request to be made
        containing endpoint and method
    """
    def next(self):
        'if comands is null then parse script'
        if (self.commands == None):
            self.commands = []
            self.runParser()

        index = self.index
        self.index += 1
        if (index < len(self.commands)):
            return self.commands[index]
    
    """
        replace with a Parser class, a Tokeniser and a Token class
    """
    def runParser(self):
        tokens = self.script.split(' ')
        ' iterate over tokens creating Commands '
        ' expect sequence to be method endpoint or just endpoint in which case method is GET'
        method = endpoint = None
        for token in tokens:
            if (method == None):
                if (self.isOperator(token)):
                    method = self.getMethod(token)
                else:
                    endpoint = token
                    method = 'GET'
            elif (endpoint == None):
                endpoint = token
            
            if (method and endpoint):
                command = Command(endpoint, method)
                self.commands.append(command)
                method = endpoint = None

    def isOperator(self, token):
        return token[0] == '>'

    def getMethod(self, token):
        if (token == '>>'):
            return 'POST'
