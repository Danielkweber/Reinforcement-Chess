from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
import sys
import itertools

class Chessboard(QWidget):
    def __init__(self):
            super().__init__()
            self.title='Chess'
            self.left=10
            self.top=10
            self.width=1400
            self.height=800
            
            self.initUI()    

    def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left,self.top,self.width,self.height)
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), Qt.darkGray)
            self.setPalette(p)
            self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBoard(qp)
        qp.end()

        
    def drawBoard(self, qp):
      
        colors = ((135, 206, 250, 255), (30, 144, 255, 200))
        color = itertools.cycle(colors)
        color_ = next(color)
        
        self.rows = 8
        self.cols = 8
        self.square_size = 85
        self.border_side = 45
        self.border_top = 25
        col_pen = QColor(255, 255, 255)
        qp.setPen(col_pen)

        for row in range(self.rows):
            for col in range(self.cols):
                qp.setBrush(QColor(color_[0], color_[1], color_[2], color_[3]))
                qp.drawRect(self.border_side + self.square_size * row, self.border_top + self.square_size * col,
                            self.square_size, self.square_size)
                color_ = next(color)

                if col == self.cols - 1:
                    color_ = next(color)


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Chessboard()
    sys.exit(app.exec_())






