from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QKeyEvent
import time
import random
class App__(QMainWindow):
    shapes = ['triangle', 'square', 'circle', 'star']
    colors = ['red', 'green', 'blue', 'pink']
    
    moves = [] # [ [position, color, shape, number] ]
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sprt6 I\'s Dual N Back")
        self.setGeometry(200, 200, 500, 500)
        
        self.nodes = {}
        indx = 0
        for i in range(3):
            for j in range(3):
                self.nodes[indx] = [i, j, QPushButton(), None]
                self.nodes[indx][2].hide()
                self.nodes[indx][3] = QLabel("", self.nodes[indx][2])
                self.nodes[indx][3].setStyleSheet("font-weight: bold; color: white;")
                self.nodes[indx][3].hide()
                indx += 1
        
        self.UI_()

    def UI_(self):
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setStyleSheet("background-color: gray;")
        
        self.exercise_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        
        for a, b in self.nodes.items():
            self.grid_layout.addWidget(b[2], b[0], b[1])
                
        self.buttons_layout = QHBoxLayout()
        
        self.options_widget = QWidget()
        self.options_layout = QVBoxLayout()
        self.options_widget.setStyleSheet("background-color: green;")
        self.options_widget.setLayout(self.options_layout)
                
        self.exercise_layout.addLayout(self.grid_layout)
        self.exercise_layout.addLayout(self.buttons_layout)
        
        self.main_layout.addLayout(self.exercise_layout)
        self.main_layout.addLayout(self.options_layout)
        
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
    def Main_Game(self):
        self.moves = 25
        self.counter = 0
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Update_Game)
        self.timer.start(2500)
        
    def Update_Game(self):
        if self.counter >= self.moves:
            self.timer.stop()
        
        self.Create_Node()
        self.counter += 1
        
     
    def Get_Node_Inf(self):
        random.seed(time.time())
        position = random.randint(0, 8)
        random.seed(time.time())
        number = random.randint(0, 100)
        random.seed(time.time())
        color = random.choice(self.colors)
        random.seed(time.time())
        shape = random.choice(self.shapes)
        
        return position, number, color, shape
    
    def Create_Node(self):
        position, number, color, shape = self.Get_Node_Inf()
        
        self.nodes[position][2].show()
        self.nodes[position][2].setStyleSheet(f"background-color: {color};")
        self.nodes[position][3].show()
        self.nodes[position][3].setText(f'{number}')
        
        
        
    def keyPressEvent(self, event: QKeyEvent):
        # Get the key that was pressed
        key = event.key()
        print(f"Key Pressed: {event.text()} (Code: {key})")
        if event.text() == 'e': self.Main_Game()
    
app = QApplication()
win = App__()
win.show()
app.exec()