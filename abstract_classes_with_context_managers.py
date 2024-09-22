"""Abstract classes can define context managers that are shared among all subclasses, while still requiring subclasses to implement certain methods."""

from abc import ABC, abstractmethod

class Resource(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass  

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

class FileResource(Resource):
    def __init__(self, file_name):
        self.file_name = file_name 

    def open(self):
        print(f"Opening a file: {self.file_name}")

    def close(self):
        print(f"Closing a file: {self.file_name}")

file = FileResource('text.txt')

with file as f:
    print(f"Processing a file: {f}")
        
# Opening a file: text.txt
# Processing a file: <__main__.FileResource object at 0x7f42ab333910>
# Closing a file: text.txt