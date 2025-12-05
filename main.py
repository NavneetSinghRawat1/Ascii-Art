import os
import msvcrt as msv
import sys

try:
    from colorama import init, Fore, Style
    init()
    COLORAMA_AVAILABLE = True
except Exception:
    COLORAMA_AVAILABLE = False
    print("\n[colorama not installed] To enable colors run: pip install colorama\n")
    sys.exit()
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
CYAN = Fore.CYAN
RESET = Style.RESET_ALL
data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

ascii_lowercase_7x7 = {
"a": [
"       ",
"  ###  ",
"     # ",
"  #### ",
" #   # ",
"  #### ",
"       "
],

"b": [
"#      ",
"#      ",
"####   ",
"#   #  ",
"#   #  ",
"####   ",
"       "
],

"c": [
"       ",
"  #### ",
" #     ",
" #     ",
" #     ",
"  #### ",
"       "
],

"d": [
"     # ",
"     # ",
"  #### ",
" #   # ",
" #   # ",
"  #### ",
"       "
],

"e": [
"       ",
"  ###  ",
" #   # ",
" ##### ",
" #     ",
"  ###  ",
"       "
],

"f": [
"   ##  ",
"  #    ",
" ####  ",
"  #    ",
"  #    ",
"  #    ",
"       "
],

"g": [
"       ",
"  #### ",
" #   # ",
" #   # ",
"  #### ",
"     # ",
"  ###  "
],

"h": [
"#      ",
"#      ",
"####   ",
"#   #  ",
"#   #  ",
"#   #  ",
"       "
],

"i": [
"   #   ",
"       ",
"  ##   ",
"   #   ",
"   #   ",
"  ###  ",
"       "
],

"j": [
"    #  ",
"       ",
"    #  ",
"    #  ",
"#   #  ",
" ###   ",
"       "
],

"k": [
"#      ",
"#   #  ",
"#  #   ",
"###    ",
"#  #   ",
"#   #  ",
"       "
],

"l": [
"  ##   ",
"   #   ",
"   #   ",
"   #   ",
"   #   ",
"  ###  ",
"       "
],

"m": [
"       ",
"## # ##",
"# # # #",
"# # # #",
"#   # #",
"#   # #",
"       "
],

"n": [
"       ",
"## ##  ",
"#  #   ",
"#   #  ",
"#   #  ",
"#   #  ",
"       "
],

"o": [
"       ",
"  ###  ",
" #   # ",
" #   # ",
" #   # ",
"  ###  ",
"       "
],

"p": [
"       ",
"####   ",
"#   #  ",
"####   ",
"#      ",
"#      ",
"       "
],

"q": [
"       ",
"  ###  ",
" #   # ",
" #   # ",
"  #### ",
"     # ",
"     # "
],

"r": [
"       ",
"###    ",
"#  #   ",
"#      ",
"#      ",
"#      ",
"       "
],

"s": [
"       ",
"  #### ",
" #     ",
"  ###  ",
"     # ",
" ####  ",
"       "
],

"t": [
"   #   ",
"  ###  ",
"   #   ",
"   #   ",
"   #   ",
"    ## ",
"       "
],

"u": [
"       ",
"#   #  ",
"#   #  ",
"#   #  ",
"#   #  ",
" ####  ",
"       "
],

"v": [
"       ",
"#   #  ",
"#   #  ",
"#   #  ",
" # #   ",
"  #    ",
"       "
],

"w": [
"       ",
"#   #  ",
"#   #  ",
"# # #  ",
"## ##  ",
"#   #  ",
"       "
],

"x": [
"       ",
"#   #  ",
" # #   ",
"  #    ",
" # #   ",
"#   #  ",
"       "
],

"y": [
"       ",
"#   #  ",
" # #   ",
"  #    ",
"  #    ",
" ##    ",
"       "
],

"z": [
"       ",
" ##### ",
"    #  ",
"   #   ",
"  #    ",
" ##### ",
"       "
]
}




def render(letter, fill='*'):
    grid = ascii_lowercase_7x7[letter.lower()]
    for row in grid:
        print(RED+row.replace('*', fill)+RESET)


def oneCharacter():
     os.system("cls")
     print("\n\n",CYAN+"*"*10+RESET,CYAN+"ASCII ART PROJECT"+RESET,CYAN+"*"*10+RESET,end="\n\n")
     print("\n\n",CYAN+"*"*10+RESET,CYAN+"One Character Module"+RESET,CYAN+"*"*10+RESET,end="\n\n")
     text = input(GREEN+"Enter a Character (Only One Character) -- "+RESET)
     if text.isupper():
         if len(text) != 1:
                print(GREEN+"\n\nPlease Enter Only One Letter -- \n\n"+RESET)
                oneCharacter()
         else:
            print(YELLOW+"\n\nYou Entered -- {0}\n\n".format(text)+RESET)
            n=((ord(text)-65)*6 if ord(text)>64 and ord(text)<92 else 26*6 if text==" " else 27 * 6 if text == "@" else 28 * 6 if text == "_" else 29 * 6 if text == "-" else 30 * 6 if text == "." else (31+ord(text)-48)*6)
            for i in data:
                for j in range(n , n + 6):
                    print(RED+i[j]+RESET,end="")
                print()
     else:
        #  print("hohohohoho")
        if len(text) != 1:
            print(GREEN+"\n\nPlease Enter Only One Letter -- \n\n"+RESET)
            oneCharacter()
        else:
         print(YELLOW+"\n\nYou Entered -- {0}\n\n".format(text)+RESET)
         render(text)
           
def alphaNumWords():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n",CYAN+"*"*10+RESET,CYAN+"ASCII ART PROJECT"+RESET,CYAN+"*"*10+RESET,end="\n\n")
    print("\n\n",CYAN+"*"*10+RESET,CYAN+"One Character Module"+RESET,CYAN+"*"*10+RESET,end="\n\n")
    text = input(GREEN+"Enter String (output will show according to terminal size)-- "+RESET)
    print(YELLOW+"\n\nYou Entered -- {0}\n\n".format(text)+RESET)
    if text.isupper():
        for i in data:
                for x in text:
                    n=((ord(x)-65)*6 if ord(x)>64 and ord(x)<92 else 26*6 if x==" " else 27 * 6 if x == "@" else 28 * 6 if x == "_" else 29 * 6 if x == "-" else 30 * 6 if x == "." else (31+ord(x)-48)*6) 
                    for j in range(n , n + 6):
                        print(RED+i[j]+RESET,end="")
                print()
    else:
        for x in text:
                if x.isdigit() or x==" ":
                    continue
                else:
                    render(x)
                    print("\n")


def alphaRange():
     
     os.system("cls")
     sys.stdin.flush()
     print("\n\n",CYAN+"*"*10+RESET,CYAN+"ASCII ART PROJECT"+RESET,CYAN+"*"*10+RESET,end="\n\n")
     print("\n\n",CYAN+"*"*10+RESET,CYAN+"One Character Module"+RESET,CYAN+"*"*10+RESET,end="\n\n")
     text = input(GREEN+"Enter Range Between (1 to 15 Character) & in Sequence Like (A-D) -- "+RESET)
     if not (len(text)==3):
        print(GREEN+"\n\nPlease Enter Valid Range -- \n\n"+RESET)
        alphaRange()
     else:
        print(YELLOW+"\n\nYou Entered -- {0}\n\n".format(text)+RESET)
        temp=""
        if text.isupper():
            st=ord(text[0])-65
            en=ord(text[2])-65
            if st>en:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                temp = alphabet[en:st+1]
                temp=temp[::-1]
            else:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                temp = alphabet[st:en+1]
            for i in data:
                for x in temp:
                    n=((ord(x)-65)*6 if ord(x)>64 and ord(x)<92 else 26*6 if x==" " else 27 * 6 if x == "@" else 28 * 6 if x == "_" else 29 * 6 if x == "-" else 30 * 6 if x == "." else (31+ord(x)-48)*6) 
                    for j in range(n , n + 6):
                        print(RED+i[j]+RESET,end="")
                print()
        else:
            st=ord(text[0])-97
            en=ord(text[2])-97
            temp=""
            if st>en:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                temp = alphabet[en:st+1]
                temp=temp[::-1]
            else:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                temp = alphabet[st:en+1]

            for x in temp:
                render(x)
                print("\n")

def onlyAlpha():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n",CYAN+"*"*10+RESET,CYAN+"ASCII ART PROJECT"+RESET,CYAN+"*"*10+RESET,end="\n\n")
    print("\n\n",CYAN+"*"*10+RESET,CYAN+"One Character Module"+RESET,CYAN+"*"*10+RESET,end="\n\n")
    text = input(GREEN+"Enter String (Only <= 15 Character) -- "+RESET)
    if not (len(text)>=1 and len(text)<=15):
        print(GREEN+"\n\nPlease Enter Only <=15 Letter -- \n\n"+RESET)
        msv.getch()
        onlyAlpha()
    else:
        if text.isalpha() == False:
            print(GREEN+"\n\nPlease Enter Only Alphabets -- \n\n"+RESET)
            msv.getch()
            onlyAlpha()
        else:
            print(GREEN+"\n\nYou Entered -- {0}\n\n".format(text)+RESET)
            if text.isupper():
                for i in data:
                    for x in text:
                        n =(ord(x) - 65)*6 
                        for j in range(n , n + 6):
                            print(RED+i[j]+RESET,end="")
                    print()
            else:
                for x in text:
                    if x==" ":
                        continue
                    else:
                        render(x)
                        print("\n")
    
def onlyNum():
     os.system("cls")
     sys.stdin.flush()
     print("\n\n",CYAN+"*"*10+RESET,CYAN+"ASCII ART PROJECT"+RESET,CYAN+"*"*10+RESET,end="\n\n")
     print("\n\n",CYAN+"*"*10+RESET,CYAN+"One Character Module"+RESET,CYAN+"*"*10+RESET,end="\n\n")
     text = input(GREEN+"Enter String (Only <= 15 Character) -- "+RESET).upper()
     if not (len(text)>=1 and len(text)<=15):
        print(GREEN+"\n\nPlease Enter Only <=15 Letter -- \n\n"+RESET)
        msv.getch()
        onlyNum()
     else:
        if text.isnumeric() == False:
            print(GREEN+"\n\nPlease Enter Only Numbers -- \n\n"+RESET)
            msv.getch()
            onlyNum()
        else:
            print(GREEN+"\n\nYou Entered -- {0}\n\n".format(text)+RESET)
            for i in data:
                for x in text:
                    n =(31+ord(x)-48)*6
                    for j in range(n , n + 6):
                        print(RED+i[j]+RESET,end="")
                print()
def mainUI():
    os.system("cls")
    print("\n\n",CYAN+"*"*10+RESET,CYAN+"ASCII ART PROJECT"+RESET,CYAN+"*"*10+RESET,end="\n\n")
    print(CYAN+"OPTIONS -- \n\n"+RESET)
    print(YELLOW+"1. One Character"+RESET)
    print(YELLOW+"2. Words"+RESET)
    print(YELLOW+"3. Range (input in Sequence - Max 15 Letters)"+RESET)
    print(YELLOW+"4. Only Alphabets"+RESET)
    print(YELLOW+"5. Only Numbers"+RESET)
    print(YELLOW+"6. Exit"+RESET)
    print(GREEN+"\n\nEnter Your Choice -- "+RESET,end="")
    ch = msv.getch()
    if ch.decode() == "1":
        oneCharacter()
    elif ch.decode() == "2":
        alphaNumWords()
    elif ch.decode() == "3":
        alphaRange()
    elif ch.decode() == "4":
        onlyAlpha()
    elif ch.decode() == "5":
        onlyNum()
    elif ch.decode() == "6":
        pass
    
    print(CYAN+"\n\nDo you want to continue Project.. Press y else any key..."+RESET)
    ch = msv.getch()
    if ch.decode() == "y" or ch.decode() == "Y":
        mainUI()
mainUI()