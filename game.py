import random
eg=("mmmhhh,das war lecker!","*mampf*","*schmatz*","prost","*rülps*")
gg=("kaching!","juhu!","was kauf ich jetzt damit","so tolles gold","Money!")
#Dungeon Spiel!Super Wahl!
dungeon="....€.w.c..€.....c.€.c....€....c..€.w......€..w..€..c.€.w.€...w.€...w..€........€.........c........"
hero="@"
food=0
herox=0
hero_gold=0
hero_hunger=0

level=list(dungeon)
while hero_hunger<100:
    hero_hunger+=random.choice((0,0,0,1,1,1,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print(c,end="")
    print()
    command=input("gold:{} food:{} hunger:{} ?".format(hero_gold,food,hero_hunger))
    if command=="a":
        herox-=1
    if command=="d":
        herox+=1
    if command==" ":
        herox+=2
        hero_hunger+=2
    if command=="e":
        if food > 0:
           food-=1
           hero_hunger-=random.choice((2,2,2,2,2,3,3))
           print(random.choice(eg))
        else:
            print("*Kkknnnuurrr*")
    #aufheben
    stuff=level[herox]
    if stuff=="€":
        hero_gold+=1
        level[herox]="."
        print(random.choice(gg))
    if stuff=="w":
        food+=1
        level[herox]="."
    if stuff=="c":
        food+=3
        level[herox]
print ("Game Over")
