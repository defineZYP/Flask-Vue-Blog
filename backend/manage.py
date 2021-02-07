'''
This file is used to manage the backend
'''
from .utils import init_app

def main():
    app = init_app()
    print("Hello world")