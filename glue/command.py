# -*- coding: utf-8 -*-

class Command:
    
    endpoint = '';

    method = '';

    def __init__(self, endpoint, method):
        self.endpoint = endpoint
        self.method = method

    def endpoint():
        return self.endpoint

    def method():
        return self.method

