# -*- coding: utf-8 -*-

class Interpreter:
    
    commands = [];
    
    script = '';

    def __init__(self, script):
        self.script = script;
    
    """ 
        return the next Command ie. request to be made
        containing endpoint and method
    """
    def next(self):
        return False
