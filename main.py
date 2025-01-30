from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QKeyEvent
import time
import random
class App__(QMainWindow):
    shapes = ['triangle', 'square', 'circle', 'star']
    colors = ['red', 'green', 'blue', 'pink']
    
    # moves = [] # [ [position, color, shape, number] ]
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sprt6 I\'s Dual N Back")
        self.setGeometry(200, 200, 500, 500)
        
        # For counting points
        self.position_overall = 0 # how many times postition was same
        self.position_good = 0    # how many times it was clicked at good time
        self.position_wrong = 0   # how many times someone missclicked
        
        self.number_overall = 0
        self.number_good = 0
        self.number_wrong = 0
        
        self.color_overall = 0
        self.color_good = 0
        self.color_wrong = 0
        
        self.shape_overall = 0
        self.shape_good = 0
        self.shape_wrong = 0
        
        # 
        self.clicked_a = False # Postion
        self.clicked_w = False # Number
        self.clicked_s = False # Color
        self.clicked_d = False # Shape
        
        self.same_position = False
        self.same_number = False
        self.same_color = False
        self.same_shape = False
    
        
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
        
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.Main_Game)
        self.exercise_layout.addWidget(self.start_button)
        
        self.end_button = QPushButton("Cancel")
        self.end_button.clicked.connect(self.End_Game)
        self.exercise_layout.addWidget(self.end_button)
        self.end_button.hide()
        
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
        self.start_button.hide()
        self.end_button.show()
        self.moves = 25 # number of nodes in round
        self.counter = 0
        self.back = 1
        self.history = [None] * self.back # [ [position, number, color, shape] ]
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Update_Game)
        self.timer.start(2500)
    
    def End_Game(self):
        self.timer.stop()
        self.start_button.show()
        self.end_button.hide()
        
        for i in self.nodes:
            self.nodes[i][2].hide()
            self.nodes[i][3].hide()
        
    def Update_Game(self):
        if self.counter >= self.moves:
            self.timer.stop()
        print(self.clicked_a, self.clicked_w, self.clicked_s, self.clicked_d)
        print(self.same_position, self.same_number, self.same_color, self.same_shape)
        
        if self.same_position:
            self.position_overall += 1
            if self.clicked_a:
                self.position_good += 1
        else:
            if self.clicked_a: self.position_wrong += 1
            
        if self.same_number:
            self.number_overall += 1
            if self.clicked_w:
                self.number_good += 1
        else:
            if self.clicked_w: self.number_wrong += 1
            
        if self.same_color:
            self.color_overall += 1
            if self.clicked_s:
                self.color_good += 1
        else:
            if self.clicked_s: self.color_wrong += 1
            
        if self.same_shape:
            self.shape_overall += 1
            if self.clicked_d:
                self.shape_good += 1
        else:
            if self.clicked_a: self.shape_wrong += 1
            
        self.same_position, self.same_number, self.same_color, self.same_shape = False, False, False, False
        self.clicked_a, self.clicked_w, self.clicked_s, self.clicked_d = False, False, False, False
        
        x = self.Create_Node()
        
        if self.history[0]:
            if x[0] == self.history[0][0]: self.same_position = True
            if x[1] == self.history[0][1]: self.same_number = True
            if x[2] == self.history[0][2]: self.same_color = True
            if x[3] == self.history[0][3]: self.same_shape = True
        #print(x, self.history[0])
        
        for i in range(self.back):
            if i + 1 < self.back:
                self.history[i] = self.history[i+1]
        self.history[-1] = x
        print(self.history)
        print()
        
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
        
        return [position, number, color, shape]
        
        
        
    def keyPressEvent(self, event: QKeyEvent):
        # Get the key that was pressed
        key = event.key()
        print(f"Key Pressed: {event.text()} (Code: {key})")
        if event.text() == 'e': self.Main_Game()
        elif event.text() == 'a': self.clicked_a = True
        elif event.text() == 'w': self.clicked_w = True
        elif event.text() == 's': self.clicked_s = True
        elif event.text() == 'd': self.clicked_d = True
        
    
app = QApplication()
win = App__()
win.show()
app.exec()