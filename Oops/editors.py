class Editor:
    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    def open (self):

        print(f"{self.name}open")


    def execute(self):

        print(f"{self.name} execute")


class Vscode:

    def __init__(self,name,vendor):

        super().__init__(name,vendor)


class PyCharm:

    vscinstance=Vscode("visualcode","vsvendor")

    vscinstance.open()

    pyc_instance=PyCharm("pychram","bilbrains")
    