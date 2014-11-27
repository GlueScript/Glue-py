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
        response = None
        command = self.interpreter.next()
        while (command):
            response = self.sendRequest(command, response)
            command = self.interpreter.next()

        return response.text

    def sendRequest(self, command, response):
        body = None
        if (response):
            body = response.text

        print 'sending request ', command.getMethod(), command.getEndpoint(), body

        if (command.getMethod() == 'GET'):
            return requests.get(command.getEndpoint())
        elif (command.getMethod() == 'POST'):
            headers = {'content-type': response.headers['Content-Type']}
            return requests.post(command.getEndpoint(), body, headers=headers)
        
        return None 
