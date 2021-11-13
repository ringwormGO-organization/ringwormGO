from turtle import*
import os
import psutil
battery = psutil.sensors_battery()

#login

print("""

█▀█ █ █▄░█ █▀▀ █░█░█ █▀█ █▀█ █▀▄▀█ █▀▀ █▀█   █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█   █▀█ █▀
█▀▄ █ █░▀█ █▄█ ▀▄▀▄▀ █▄█ █▀▄ █░▀░█ █▄█ █▄█   █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█   █▄█ ▄█


█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀ █ █
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄ ▄ ▄

""")

print("""

[1] Virtual register
[2, ...] Without virtual register

""")
setup = input("[?]: ")
if setup == '1':
    print("If you want to come into workspace, type your username and password like this 'Example/123'.")
    register = input("You need to register. ")
    login = input("Type username and password ")
    if login == register:
        goodlog = print("Welcome to workspace. ©2021")
        welhelp = print("You can run this virtual DOS OS from Python text editor or IDE editor; from PowerShell in Windows or from CMD.")
        print("Your battery level is:", battery.percent, "%")
    
    else:
        print("Error during register or login. Try again. If error show again, restart virtual OS or your host OS.")
        exit()

if setup == '2':
    print("Welcome. You may have some restictions.")


#GUI
a=input("Unesi naredbu: ")
if a == "print":
    b=input("Unesi nešto unutar tvoje naredbe: ")
    print(b)
if a=="input":
    c=input("Unesi broj: ")
    print(c)
    if c=="int":
        d=int(input("Unesi broj: "))
        print(d)
if a == "Help":
    print("int = input number","exit = exit",)
    print("Our mail is", "ringwormgo@gmail.com", "or", "van.gutan2@gmail.com")
if a == "Exit":
    exit()
if a == "GUI change":
    print("Error...!")
if a == "Math":
    x=float(input("Unesi prvi broj: "))
    op=input("Unesi operatora: ")
    y=float(input("Unesi drugi broj: "))
    if op=="+":
        print(x + y)
    elif op== "-":
        print(x - y)
    elif op=="*":
        print(x * y)
    elif op=="/":
        print(x / y)
    elif op=="*2":
        zz=x*x
        zzz=y*y
        print(zz,zzz,"Rješenje. Dva na kvadrat prvog i drugog broja.")
    if a == "turtle":
        fd(100)
        lt(90)
        fd(100)
        lt(90)
        fd(100)
        lt(90)
        fd(100)
        lt(90)
if a == "while":
        while True:
            print("DOS Python... .")
if a == "quiz":
    pitanje1 = input("Which generation of ringwormGO webbrowsers supprot any website? ")
    if pitanje1 == "Second" or "Druga":
        tocno = print("Correct")
    else:
        netocno = print("Incorrect", "Second")
    pitanje2 = input("In which year ringwormGO is founded? ")
    if pitanje2 == "2021":
        print("Correct")
    else:
        print("Incorrect", "2021")
        print("This is all question. If you have more than 90% you likes our products.")
if a == "Crash":
    print("""
    
    C̦͓̙R͙̦̞A̪͖͙S͕͇͇H̡͙͙
    M̢͍a͚͚͇n̠͕̞u͉̟̘a̝̻͜l͙̼͙ 0͉͜x̻̫͍0̝͕͜0͍͚0̡̟̻0͚̪0̞͇̝0̡̘̘0͍̞̼0͙͚̫

    """)
    exit()
if a == "File Explorer":
    print("Check out our special file.")
if a == "Pong":
    print("Check out special Python file 'Pong2.py'. Made by Stjepan.")
ex=input("Type eXit for final exit: ")
if ex == "eXit":
    print("Bye, bye! Thank you on use... Made by ringwormGO")
    print("Source: https://github.com/Cyber-Coding-Scripts/OS")
    exit()
if ex == "bAck to print":
    b=input("Unesi nešto unutar tvoje naredbe: ")
    print(b)
    ex=input("Type eXit for final exit: ")
    if ex == "eXit":
        print("Bye, bye! Thank you on use... Made by ringwormGO")
        print("Source: https://github.com/Cyber-Coding-Scripts/OS")
        exit()


