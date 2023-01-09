from translator import translate
from chat import chatbot






def vibot():
    while True:
        user_input = input("Nobita: ")
        yousaid = translate(user_input, 'vi_en')
        botrep = chatbot(yousaid)
        botsaid = translate(botrep, 'en_vi')
        print("Doraemon: " + botsaid)
    


vibot()