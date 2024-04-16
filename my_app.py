from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication,QWidget,QHBoxLayout,QVBoxLayout,
QGroupBox,QRadioButton,QPushButton,QLabel
)
from random import shuffle
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):

        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Кто я ?', 'ладно','ты','я','?'))
question_list.append(Question('акунда','лялюля','лакака','лилупа','хапунга'))
question_list.append(Question('тимо','тютя','тити','тяпа','тютичка'))



app = QApplication([]) #создаём приложение 
window = QWidget()
window.setWindowTitle('Я Не умею печатать') #NAME

btn_ok = QPushButton('Ответить')
lb_Questtion = QLabel('КТО Я')

RadioGroupBox = QGroupBox('Варианты ответа')

rtts_1 = QRadioButton('Дв1')
rtts_2 = QRadioButton('Д434')
rtts_3 = QRadioButton('Д253')
rtts_4 = QRadioButton('Д1')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()#Вертикальные линии будут внутри гориз.
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rtts_1)#2 ответа в левый столбец
layout_ans2.addWidget(rtts_2)
layout_ans3.addWidget(rtts_3)#2 ответа в правый
layout_ans3.addWidget(rtts_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)#Разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1)#готовы понели ответов

layout_line1 = QHBoxLayout()#вопрос
layout_line2 = QHBoxLayout()#Варианты ответов
layout_line3 = QHBoxLayout()#Кнопка 'Ответ'

layout_card = QVBoxLayout()#размещение строк
layout_line1.addWidget(lb_Questtion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter) )
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(btn_ok)

layout_card = QVBoxLayout()#размещение строк
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

AnsGroupBox = QGroupBox('')
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Result,alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

window.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    #RadioGroup.setExslusive()
    rtts_1.setChecked(False)
    rtts_2.setChecked(False)
    rtts_3.setChecked(False)
    rtts_4.setChecked(False)

answers = [rtts_1,rtts_2,rtts_3,rtts_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():

           show_correct('Неправильно')  
def next_question():
    window.cur_question = window.cur_question + 1 
    if window.cur_question >= len(question_list):
        window.cur_question = 0
        q = question_list[window.cur_question]
        ask(q)
             
def click_OK():
    
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.resize(600,390)
window.cur_question = -1
btn_ok.clicked.connect(click_OK)
next_question()
window.show()#показать окно
app.exec()#оставляет прил. откр.