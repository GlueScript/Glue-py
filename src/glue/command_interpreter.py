# -*- coding: utf-8 -*-

class CommandInterpreter:
    
    commands = [];
    
    script = '';

    def __init__(self, script):
        self.script = script;
    
    """ 
        return the next 'command' ie request to be made
        containing endpoint and method
    """
    def nextCommand(self):
        return False
