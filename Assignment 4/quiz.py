def mystery(l):
     if l == []:
        return (l)
     else:
        return (l[-1:] + mystery(l[:-1]))
print(mystery([13,23,17,81,15]))

pairs = [ (x,y) for x in range(4) for y in range(3) if (x+y)%3 == 0 ]
print(pairs)

marks = {"Quizzes":{"Mahesh":[3,5,7,8],"Suresh":[9,4,8,8],"Uma":[9,9,7,6]},"Exams":{"Mahesh":[37],"Uma":[36]}}
#marks["Exams"]["Suresh"].extend([44])  #generates error
#marks["Exams"]["Suresh"] = [44]            #does not generates error
#marks["Exams"]["Suresh"].append(44)    #generates error
#marks["Exams"]["Suresh"][0:] = [44]     #generates error

d={}
#d[[1,2]]=5                                             generates error
#d[(1,2)]=5                                             does not genrates error
#d["1,2"]=5                                             does not generates error
#d[12]=5                                                does not generates error

