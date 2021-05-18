import sys
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
    QButtonGroup,
    QCheckBox
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.Qt import QSize
from functools import partial
from random import shuffle



class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(200, 100, 333, 500)
        self.setMaximumSize(333, 500)
        self.setWindowTitle('tic tac toe')
        self.setWindowIcon(QIcon('.\\X_O.png'))
        
        self.widgets()
    
    def widgets(self):
        
        self.setStyleSheet("background-color: 'white'")
        h_box_1 = QHBoxLayout()
        self.replay_bt = QPushButton()
        self.replay_bt.setIcon(QIcon('.\\replay.png'))
        self.replay_bt.setFixedSize(50, 50)
        self.replay_bt.setStyleSheet('border: 2px solid black')
        self.replay_bt.clicked.connect(self.replay)
        h_box_1.addWidget(self.replay_bt)
        h_box_1.addStretch()

        self.default = {'P1': [True, 'X'], 'Bot': [True, 'O'], 'P2': [False, 'O']}
        self.players_score = {'X': 0, 'O': 0}
        self.score_points = QLabel(f"score: {self.players_score['X']} - {self.players_score['O']}")
        self.score_points.setFont(QFont('Arial', 30))
        h_box_1.addWidget(self.score_points)
        h_box_1.addStretch()


        h_row_1 = QHBoxLayout()
        self.button_0 = QPushButton()
        self.button_0.clicked.connect(partial(self.choosePlace, 0))
        self.button_0.setFixedSize(100, 100)
        self.button_0.setIconSize(QSize(80, 80))
        h_row_1.addWidget(self.button_0)
        h_row_1.addSpacing(3)
        


        self.button_1 = QPushButton()
        self.button_1.clicked.connect(partial(self.choosePlace, 1))
        self.button_1.setFixedSize(100, 100)
        self.button_1.setIconSize(QSize(80, 80))
        h_row_1.addWidget(self.button_1)
        h_row_1.addSpacing(3)

        self.button_2 = QPushButton()
        self.button_2.clicked.connect(partial(self.choosePlace, 2))
        self.button_2.setFixedSize(100, 100)
        self.button_2.setIconSize(QSize(80, 80))
        h_row_1.addWidget(self.button_2)

        h_row_2 = QHBoxLayout()
        self.button_3 = QPushButton()
        self.button_3.clicked.connect(partial(self.choosePlace, 3))
        self.button_3.setFixedSize(100, 100)
        self.button_3.setIconSize(QSize(80, 80))
        h_row_2.addWidget(self.button_3)
        h_row_2.addSpacing(3)

        self.button_4 = QPushButton()
        self.button_4.clicked.connect(partial(self.choosePlace, 4))
        self.button_4.setFixedSize(100, 100)
        self.button_4.setIconSize(QSize(80, 80))
        h_row_2.addWidget(self.button_4)
        h_row_2.addSpacing(3)

        self.button_5 = QPushButton()
        self.button_5.clicked.connect(partial(self.choosePlace, 5))
        self.button_5.setFixedSize(100, 100)
        self.button_5.setIconSize(QSize(80, 80))
        h_row_2.addWidget(self.button_5)

        h_row_3 = QHBoxLayout()
        self.button_6 = QPushButton()
        self.button_6.clicked.connect(partial(self.choosePlace, 6))
        self.button_6.setFixedSize(100, 100)
        self.button_6.setIconSize(QSize(80, 80))
        h_row_3.addWidget(self.button_6)
        h_row_3.addSpacing(3)

        self.button_7 = QPushButton()
        self.button_7.clicked.connect(partial(self.choosePlace, 7))
        self.button_7.setFixedSize(100, 100)
        self.button_7.setIconSize(QSize(80, 80))
        h_row_3.addWidget(self.button_7)
        h_row_3.addSpacing(3)

        self.button_8 = QPushButton()
        self.button_8.clicked.connect(partial(self.choosePlace, 8))
        self.button_8.setFixedSize(100, 100)
        self.button_8.setIconSize(QSize(80, 80))
        h_row_3.addWidget(self.button_8)
        
        h_option = QHBoxLayout()
        player = QButtonGroup(self)

        self.P2_b = QCheckBox('P2')
        self.P2_b.clicked.connect(self.option)
        h_option.addWidget(self.P2_b)
        player.addButton(self.P2_b)

        self.bot_b = QCheckBox('Bot')
        self.bot_b.setChecked(True)
        self.bot_b.clicked.connect(self.option)
        h_option.addWidget(self.bot_b)
        player.addButton(self.bot_b)


        self.role = 'X'
        container = QWidget()
        table = QVBoxLayout()
        table.addLayout(h_row_1)
        table.addSpacing(3)
        table.addLayout(h_row_2)
        table.addSpacing(3)
        table.addLayout(h_row_3)
        container.setLayout(table)
        container.setStyleSheet("background-color: black; border : 4px solid purple; border-radius: 5px")
        
        v_box = QVBoxLayout()
        v_box.addLayout(h_box_1)
        v_box.addSpacing(3)
        v_box.addWidget(container)
        
        v_box.addLayout(h_option)

        self.setLayout(v_box)


    def replay(self):
        self.P2_b.setEnabled(True)
        self.bot_b.setEnabled(True)
        self.bot_b.setChecked(True)
        self.players_score = {'X': 0, 'O': 0}
        self.default = {'P1': [True, 'X'], 'Bot': [True, 'O'], 'P2': [False, 'O']}
        for num in range(9):
            eval('self.button_%d.setEnabled(True)' % num)
            eval('self.button_%d.setIcon(QIcon())' % num)

        self.score_points.setText("score:0 - 0")

        

    def option(self):
        player = (lambda: 'P2' if self.P2_b.isChecked() else 'Bot')()
        players = ['P2', 'Bot']
        players.remove(player)
        self.default[player][0] = True
        self.default[players[0]][0] = False

    def choosePlace(self, num):
        self.P2_b.setEnabled(False)
        self.bot_b.setEnabled(False)
        eval("self.button_%d.setIcon(QIcon('.\\%s.png'))" % (num, self.role))
        eval("self.button_%d.setDisabled(True)" % num)
        if self.role == 'X':
            self.default['P1'].append(num)
        
        else:
            self.default['Bot'].append(num)
            self.default['P2'].append(num)

        win =  self.isWin()

        def setup():
            self.default = {'P1': [True, 'X'], 'Bot': [True, 'O'], 'P2': [False, 'O']}
            for num in range(9):
                eval('self.button_%d.setEnabled(True)' % num)
                eval('self.button_%d.setIcon(QIcon())' % num)

        def addPoint():
            self.players_score[self.role] += 1
            self.score_points.setText(f"score: {self.players_score['X']} - {self.players_score['O']}")
            setup()

        if win in ('P1', 'P2'):
            QMessageBox.information(self, 'WINER', win + ' is the winer', QMessageBox.Ok)
            addPoint()

        elif win == 'Bot':
            QMessageBox.information(self, 'LOSER', 'You lose', QMessageBox.Ok)
            addPoint()
        
        elif len(self.default['P1'][2:]) + len(self.default['P2'][2:]) == 9:
            QMessageBox.information(self, 'DRAW', 'No one win, it\'s a draw', QMessageBox.Ok)
            setup()

        role_next = ['X', 'O']
        role_next.remove(self.role)
        self.role = role_next[0]
        if self.bot_b.isChecked() and self.role == 'O':
            self.choosePlace(self.bot())
            

    def isWin(self):
        wining = [
            [0 ,1 , 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
            ]
        
        
        if self.role == 'X':
            player = 'P1'
        
        elif self.role == 'O':
            player = (lambda: 'P2' if self.P2_b.isChecked() else 'Bot')()
    
        places = self.default[player][2:]
        count = 0
        for win in wining:
            count = sum(list(map(lambda place: 1 if place in win else 0, places)))
            
            if count == 3: return player
            count = 0
    
    def bot(self):
        places = [
            [0 ,1 , 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
            ]
        shuffle(places)

        token_places = self.default['P1'][2:] + self.default['Bot'][2:]
        lowest_empty = 4
        for place in places:
            try:
                if self.best_way:
                    if len(
                        list(filter(lambda p: True if p not in token_places else False, self.best_way))
                        ) < len(self.best_way):
                        break
            except AttributeError:
                self.best_way = []

            shuffle(place)
            empty_places = sum(list(map(lambda p: 1 if p not in token_places else 0, place)))
            if empty_places < lowest_empty:
                lowest_empty = empty_places
                new_way = (
                    list(filter(lambda p: True if p not in token_places else False, place))
                )
                if len(self.best_way) < len(new_way):
                    self.best_way = new_way
                
        shuffle(self.best_way)
        if lowest_empty > 0 and self.best_way:
            while self.best_way:
                p = self.best_way.pop()
                if p not in token_places:
                    return p
            
            else:
                return self.bot()
        
        else:
            for i in range(9):
                if i not in token_places:
                    return i
        





def main():
    app = QApplication(sys.argv)
    X_O = TicTacToe()
    X_O.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()