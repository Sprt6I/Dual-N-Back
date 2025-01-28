from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from random import randint, choice

class App__(QMainWindow):
    shapes = ['triangle', 'square', 'circle', 'star']
    colors = ['red', 'green', 'blue', 'yellow']
    
    moves = [] # [ [position, color, shape, number] ]
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sprt6 I\'s Dual N Back")
        
        self.UI_()

    def UI_(self):
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        
        self.exercise_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.buttons_layout = QHBoxLayout()
        
        self.options_layout = QVBoxLayout()
        
        self.exercise_layout.addLayout(self.grid_layout)
        self.exercise_layout.addLayout(self.buttons_layout)
        
        self.main_layout.addLayout(self.exercise_layout)
        self.main_layout.addLayout(self.options_layout)
        
    def Exercise_Logic(self):
        #same_shape = randint(0, 100)
        #if same_shape > 50:
            
        position = randint(0, 9)
        number = randint(0, 100)
        color = choice(self.colors)
        shape = choice(self.shapes)
        pass
    
app = QApplication()
win = App__()
win.show()
app.start()