from typing import (
    List,
    Tuple,
    Any
)

class HtmlPage:
    def __init__(self):
        self.stack : List[str] = []
        self.top = """
        <link rel="stylesheet" href="https://ulyzium.mooo.com/css/materialize.min.css">

        <nav class="light-green">
            <div class="container">
                <div class="nav-wrapper">
                    <a href="index.php?page=home" class="brand-logo">Ulyzium</a>
                    <ul class="right hide-on-med-and-down">
                        <li><a href="../index.php?page=home">Quitter</a></li>
                        <li><a href="index.php?page=logout">Déconnexion</a></li>
                    </ul>
                </div>
            </div>
        </nav>"""

    def addLine(self, line:str):
        self.stack.append(line)

    def addLineAt(self, index:int, line:str):
        self.stack.insert(index, line)
    
    def removeLastLine(self) -> str:
        return self.stack.pop()

    def removeLineAt(self, index:int):
        return self.stack.remove(index)

    def __str__(self) -> str:
        __page : str = ""
        for line in self.stack:
            __page += line + '\n'
        return __page