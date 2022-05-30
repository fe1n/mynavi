from operator import le
import sqlite3

WORD_LEN=6
LETTER_LIST = ['a' for _ in range(10)]
ANS = ['m','y','n','a','v','i']
numlist = [3,8,5,7,2,6,6,9,1,4,0,2,9,6]

conn = sqlite3.connect("ejdic-hand-sqlite/ejdict.sqlite3")
c = conn.cursor()
wordlist = ["","",""]

def letter_check():
    for i in range(10):
        for j in range(i+1,10):
            if LETTER_LIST[i]==LETTER_LIST[j]:
                return 0
    return 1


def check3():
    sql = 'SELECT * FROM items WHERE word LIKE "{}%{}%"'.format(LETTER_LIST[1],LETTER_LIST[4])
    rows = list(c.execute(sql))
    for n in rows:
        word = n[1]
        if len(word)==WORD_LEN and word[0]==LETTER_LIST[1] and word[2]==LETTER_LIST[3] \
                and word[4]==LETTER_LIST[4]:
            if word[1]!=ANS[1] and word[1] in ANS and \
                    word[1]!=LETTER_LIST[1] and \
                    word[1]!=LETTER_LIST[4] and \
                    word[2] not in ANS and \
                    word[3] not in ANS and \
                    word[5] not in ANS:
                LETTER_LIST[1] = word[0]
                LETTER_LIST[2] = word[1]
                LETTER_LIST[5] = word[5]
                wordlist[2]=word
                if wordlist[0][1] not in LETTER_LIST and \
                        wordlist[1][0] not in LETTER_LIST and \
                        wordlist[2][3] not in LETTER_LIST and \
                        letter_check():
                    ans=""
                    for i in numlist:
                        ans+=LETTER_LIST[i]
                    print(ans)

def check2():
    sql = 'SELECT * FROM items WHERE word LIKE "%{}%{}"'.format(LETTER_LIST[4],LETTER_LIST[8])
    rows = list(c.execute(sql))

    for n in rows:
        word = n[1]
        if len(word)==WORD_LEN and word[3]==LETTER_LIST[4] and word[5]==LETTER_LIST[8] and word[1]!=ANS[1] and \
                word[1] in ANS and word[1]!=LETTER_LIST[4] and \
                word[0] not in ANS and \
                word[2] not in ANS and \
                word[4] not in ANS and \
                word[5] not in ANS:
                
            LETTER_LIST[3] = word[2]
            LETTER_LIST[6] = word[1]
            LETTER_LIST[7] = word[4]
            wordlist[1]=word
            check3()

def check1():
    sql = 'SELECT * FROM items WHERE word LIKE "%av%"'
    rows = list(c.execute(sql))

    for n in rows:
        word = n[1]
        if word[3:5]=="av" and len(word)==WORD_LEN and \
            word[0] not in ANS and \
            word[1] not in ANS and \
            word[2] not in ANS and \
            word[5] not in ANS:
            
            LETTER_LIST[0] = word[2]
            LETTER_LIST[1] = word[4]
            LETTER_LIST[4] = word[3]
            LETTER_LIST[8] = word[5]
            LETTER_LIST[9] = word[0]
            wordlist[0]=word
            check2()

check1()


