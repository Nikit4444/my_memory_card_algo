from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle, randint

class Que():
    def __init__(self, questions, r_ans, wrn1, wrn2, wrn3):
        self.questions = questions
        self.r_ans = r_ans
        self.wrn1 = wrn1
        self.wrn2 = wrn2
        self.wrn3 = wrn3


p = QApplication([])
w = QWidget()
w.setGeometry(100,100,400,400)
w.setWindowTitle('Memory Card')
bt_ok = QPushButton('Нажми на меня')
label_q = QLabel('Хочешь узнать правду?')

RadioGroupBox = QGroupBox('yes или no')

rbt1 = QRadioButton('где?')
rbt2 = QRadioButton('кто?')
rbt3 = QRadioButton('когда?')
rbt4 = QRadioButton('почему?')

a1 = QVBoxLayout()
a2 = QHBoxLayout()
a3 = QHBoxLayout()

a2.addWidget(rbt1)
a2.addWidget(rbt2)
a3.addWidget(rbt3)
a3.addWidget(rbt4)
a1.addLayout(a2)
a1.addLayout(a3)

RadioGroupBox.setLayout(a1)

layout_c = QVBoxLayout()
l_l1 = QHBoxLayout()
l_l2 = QHBoxLayout()
l_l3 = QHBoxLayout()

l_l1.addWidget(label_q, alignment=Qt.AlignCenter)
l_l2.addWidget(RadioGroupBox)
l_l3.addWidget(bt_ok, alignment=Qt.AlignCenter)

layout_c.addLayout(l_l1, stretch=2)
layout_c.addLayout(l_l2, stretch=8)
layout_c.addLayout(l_l3, stretch=3)
layout_c.setSpacing(5)

w.setLayout(layout_c)

AGroupBox = QGroupBox('Результат теста')

label_result = QLabel('прав ты или нет?')
l_cor = QLabel('Правильный ответ')

layout_result = QVBoxLayout()
layout_result.addWidget(label_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(l_cor, 2, Qt.AlignCenter)
AGroupBox.setLayout(layout_result)
l_l2.addWidget(AGroupBox)

AGroupBox.hide()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbt1)
RadioGroup.addButton(rbt2)
RadioGroup.addButton(rbt3)
RadioGroup.addButton(rbt4)

def s_tx():
    RadioGroupBox.show()
    AGroupBox.hide()
    bt_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    RadioGroup.setExclusive(True)

ans = [rbt1, rbt2, rbt3, rbt4]

def s_res():
    RadioGroupBox.hide()
    AGroupBox.show()
    bt_ok.setText('Хочешь узнат правду?')

def ask(q: Que):
    shuffle(ans)
    ans[0].setText(q.r_ans)
    ans[1].setText(q.wrn1)
    ans[2].setText(q.wrn2)
    ans[3].setText(q.wrn3)
    label_q.setText(q.questions) #label_q layout_c
    l_cor.setText(q.r_ans)
    s_tx()

def ch_ans():
    if ans[0].isChecked():
        label_result.setText('Правильно!')
        w.score += 1
        print('Статистика\n-Всего вопросов:', w.total, '\n-Правильных ответов:', w.score)
        print('',(w.score/w.total*100), '%')
    if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        label_result.setText('Неверно!')
        print('Рейтинг:', '\n-Всего правильных ответов:', w.score)
    s_res()
w.c_q = -1

ql = []
ql.append(Que('Государственный язык Аргентины', 'Испанкский', 'Португальский', 'Итальянский', 'Русский'))
ql.append(Que('В каком году был создан майнкрафт', '2009', '2011', '2005', '2013'))
ql.append(Que('Сколько цветов в флаге Польши', '2', '3', '4', '1'))
ql.append(Que('Самый лучший архонт в геншине', 'Венти', 'Чжун ли', 'Райден', 'Нахида'))
ql.append(Que('Сколько фармишь пп в осу', '500', '300', '100', '25'))
ql.append(Que('Самый лучший дроп, только на', 'ггстандофф', 'буллдроп', 'стадидроп', 'стандоф2'))
ql.append(Que('Корень из 100', '10', '20', '1', '100'))
ql.append(Que('Сколько месяцев в году имеет 28 дней', '12', '1', '4', '5'))
ql.append(Que('Какого цвета нет на флаге Великобритании', 'Жёлтый', 'Белый', 'Красный', 'Синий'))
ql.append(Que('Кого австралийцы называют морской осой', 'Медузу', 'Осьминога', 'Акулу', 'Зевса'))

def next_question():
    w.total += 1
    print('Статистика\n-Всего вопросов:', w.total, '\n-Правильных ответов:', w.score)
    cur_question = randint(0, len(ql) - 1)
    q = ql[cur_question]
    ask(q)

def click_ok():
    if bt_ok.text() == 'Ответить':
        ch_ans()
    else:
        next_question()


cur_question = -1
w.score = 0
w.total = 0

bt_ok.clicked.connect(click_ok)
next_question()
w.show()
p.exec_()