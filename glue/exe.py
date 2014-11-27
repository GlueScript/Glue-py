# -*- coding: utf-8 -*-

import requests

"""
 Executes a script
"""
class Exe:
    
    interpreter = None

    def __init__(self, interpreter):
        self.interpreter = interpreter    
    
    def run(self):
        response = body = None
        command = self.interpreter.next()
        while (command):
            if (response):
                body = response.text

            response = self.sendRequest(command, body)
            print response.text
            command = self.interpreter.next()

        return response.text

    def sendRequest(self, command, body):
        print 'sending request ', command.getMethod(), command.getEndpoint()

        if (command.getMethod() == 'GET'):
            return requests.get(command.getEndpoint())
        elif (command.getMethod() == 'POST'):
            return requests.post(command.getEndpoint(), body)
        
        return None 
