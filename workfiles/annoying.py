import socket
skip = "-------------\n\n"
print("Choose language // Выберите язык")
print("Type en and press Enter // Введите ru и нажмите enter")
language = input()

while 1:
    if language == 'en':
        languagePack = open('localisation/en.txt')
        print('Choosed english language!')
        break
    else: 
        if language == 'ru':
            languagePack = open('localisation/ru.txt')
            print('Успешно выбран русский язык!')
            break
        else:
            print("Type valid language! // Выберите язык только из предложенных вариантов!")
            language = input()


languageStrings = languagePack.readlines()
print(skip)
print(languageStrings[0])
print(languageStrings[1])
print(languageStrings[2])
agree = input()
print(skip)
print(languageStrings[3])
Bancho = input()
while 1:
    if Bancho == 'y':
        Server = "192.241.219.151"
        Port = 6667
        break
    else:
        if Bancho == 'n':
            print(languageStrings[4])
            Server = input()
            print(languageStrings[5])
            Port = input()
            break
        else:
            print(languageStrings[3])
            Bancho = input()
print(skip)
print(languageStrings[6])
print(languageStrings[7])
print(languageStrings[8])
Login = input()
print("-------------")
print(languageStrings[9])
Password = input()
print(skip)
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
irc.connect((Server, Port))
irc.send(('PASS ' + Password + '\r\n').encode()) 
irc.send(('NICK ' + Login + '\r\n').encode()) 
irc.send(('END \r\n').encode())
print(languageStrings[10])
while True:
    r = irc.recv(4096)
    if r.decode().find('QUIT') and r != -1:
        print(languageStrings[11])
        irc.close()
        break
print(languageStrings[12])
while True:
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    irc.connect((Server, Port))
    irc.send(('PASS ' + Password + '\r\n').encode()) 
    irc.send(('NICK ' + Login + '\r\n').encode()) 
    irc.send(('END \r\n').encode())
    r = irc.recv(4096)
    if r.decode().find('QUIT') and r != -1:
        irc.close()



