# -*- coding: utf-8 -*-

class Command:
    
    endpoint = ''

    method = ''

    def __init__(self, endpoint, method):
        self.endpoint = endpoint
        self.method = method

    def getEndpoint(self):
        return self.endpoint

    def getMethod(self):
        return self.method

