print("Hello SnappFood")
print("My name is Khashayar Saemian")
print("This is Homework 2")
cypher = int(input("Select  your cypher type : 1- Caesar cipher , 2 – Pig Pen :"))
if cypher == 1 :
    print('you select Ceaser Cypher')
    code = input("please type your code :")
    i = 1
    j = len(code)+1
    x = ""
    y = 0
    c = 0
    for i in range(1,j) :
        c = code[1:i]
        y = ord(c)
        y = y+4
        k = chr(y)
        x = x+k
    print(x)
elif cypher == 2:
    print('you select Pig Pen')
    code = input("please type your code :")
    i = 0
    j = len(code)+1
    x = ""
    for i in range(0,j):
        c = code[i]
        if c == "A" :
            print("ᒧ") 
        elif c == "B" :
            print("⊔")
        elif c == "C" :
            print("ᒪ")
        elif c == "D" :
            print("⊐")
        elif c == "E" :
            print("□")
        elif c == "F" :
            print("⊏")
        elif c == "G" :
            print("ᒣ")
        elif c == "H" :
            print("⊓")
        elif c == "I" :
            print("ᒥ")
        elif c == "J" :
            print("ᒧx")
        elif c == "K" :
            print("⊔x")
        elif c == "L" :
            print("ᒪx")
        elif c == "M" :
            print("⊐x")
        elif c == "N" :
            print("□x")
        elif c == "O" :
            print("⊏x")
        elif c == "P" :
            print("ᒣx")
        elif c == "Q" :
            print("⊓x")
        elif c == "R" :
            print("ᒥx")
        elif c == "S" :
            print("ᒧo")
        elif c == "T" :
            print("⊔o")
        elif c == "U" :
            print("ᒪo")
        elif c == "V" :
            print("⊐o")
        elif c == "W" :
            print("□o")
        elif c == "X" :
            print("⊏o")
        elif c == "Y" :
            print("ᒣo")
        elif c == "Z" :
            print("⊓o")
        else : print(c)
else : print("you enter wrong value , please try again")
        
        
        

    
    




