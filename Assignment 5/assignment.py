def main():
    courses=list()
    students=dict()
    grades=dict()
    while True:
        s=input()
        if (s=="Courses"):
            d=1
        elif (s=="Students"):
            d=2
        elif (s=="Grades"):
            d=3
        elif (s=="EndOfInput"):
            break
        else:
            s=s.split("~")
            if(d==1):
                courses.append(s)
            elif(d==2):
                students[s[0]]=s[1]
                grades[s[0]]=[]
            elif(d==3):
                grades[s[-2]].append(s[-1])
    points={"A":10,"AB":9,"B":8,"BC":7,"C":6,"CD":5,"D":4}
    for idx in sorted(grades):
        p=[points[x] for x in grades[idx]]
        n=len(p) or 1
        marks=str(round((sum(p)/n),2)) if p else "0"
        d=[idx,students[idx],marks]
        print("~".join(d))
main()
'''
Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
'''
'''
Courses
POT~Potions~1~2011-2012~Severus Snape
DADA~Defence Against the Dark
ARTS~1~2011-2012~Gilderoy Lockhart 
Students
RAV4309~Angelina Johnson
HUF7201~Gwenog Jones
GRF9110~Parvati Patil
RAV4308~Olive Hornby
Grades
POT~1~2011-2012~RAV4308~C
POT~1~2011-2012~RAV4309~B
POT~1~2011-2012~GRF9110~A
EndOfInput
'''
