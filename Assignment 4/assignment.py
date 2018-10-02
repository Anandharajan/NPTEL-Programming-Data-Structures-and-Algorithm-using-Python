def orangecap(d):
    if not d:
        return()
    else:
        totalscore=dict()
        for match in d:
            for player in d[match]:
                if player in totalscore:
                    totalscore[player]=totalscore[player]+d[match][player]
                else:
                    totalscore[player]=d[match][player]
        bestplayer=max(totalscore,key=totalscore.get)
        return (bestplayer,totalscore[bestplayer])
    
def addpoly(p1,p2):
    for i in range(len(p1)):
        for item in p2:
            p1[i]=((p1[i][0]+item[0]),p1[i][1])
            p2.remove(item)
    p3=p1+p2
    for item in p3:
        if item[0]==0:
            p3.remove(item)
    return(sorted(p3))

def multpoly(p1,p2):
    for i in range(len(p1)):
        for item in p2:
            p1[i]=((p1[i][0]*item[0]),(p1[i][1]+item[1]))
            p2.remove(item)
    return(p1)

print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))
print(orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}}))
print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
print(addpoly([(2,1)],[(-2,1)]))
print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))
print(multpoly([(2,1)],[(-2,1)]))
