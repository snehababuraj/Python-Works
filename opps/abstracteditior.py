from abc import ABC,abstractmethod
class Editor(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):
    def open(self):
        print("open method")
    def save(self):
        print("save method")
    def edit(self):
        print("edit method")
    def execute(self):
        print("execute method")
ch=Vscode()
ch.save()
ch.open()
ch.edit()
ch.execute()