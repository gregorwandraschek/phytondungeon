import random
eg=("mmmhhh,das war lecker!","*mampf*","*schmatz*","prost","*rülps*")
gg=("kaching!","juhu!","was kauf ich jetzt damit","so tolles gold","Money!")
#Dungeon Spiel!Super Wahl!
dungeon1="""
########################################################################
#.....c.c.#............#.w..............#.....w.............#..w.......#
#......c........G......K.........K......G.......K....G......K..........#
#..c€...c.#..€.........#..€.............#..€................#..........#
###################################################################.####
#ccccc#......#................#..<...................K.........#.......#
#..GG.#...c..........K........#..w.....K.......w...........c...K.......#
#€€€€€#...G..#...........w....G..............€€€€..G...........#.......#
#..<..#......#................#.........K......................#.......#
##########################################.#############################
#........#................#............#............w.....#............#
#..c.....#...c.....K......G..w.........K..................#............#
#...c....#................#............#........€.........G............#
#....c...G.#############################################################
#........###......G...........#.......................#.........########
##########....................#.......................P.........##.....#
#........#......P.........<...K..................€....#.........###....#
#..................K..........#........€€€€...........#...........#....#
#........#....................#.......................#...........######
########################################################################
"""
dungeon2="""
########################################################################
#...................#.................K.....#........K.................#
#..........w...G.....########.....w.........#...<...w..............P...#
#...................#...P....#..............#..........................#
##########K#########.........#......G.......#.............G............#
#............................#.....€........#......P.c........€........#
#...........w.........c.....#.....>....w....#..........................#
#...P.....................#................#######.#####################
#...............€.......#...................#..........................#
#..>......K.........###############################.####################
#...................#.........c.............#..........................#
#...........................................#..........................#
####################...........K...........................w..G........#
#..................#........................#.....P....................#
#..............€...#.c.................€....#..................€.......#
#...P..............#.###########################.#######################
#..........w.......#........K.............#............................#
#........G.........#.......>.....................c...........K.........#
#.....................w.......G...........#............................#
#.............€....#..............€.......#...€.....P.......w..........#
#.....K............#......................#............................#
########################################################################
"""
dungeon3="""
########################################################################
#.....................c.€€€€.########.................#.....G..........#
#....................c.w....#..ww.w..#..........>.....#................#
############.##############..........#.....Pp...D.....#......G....ccccc#
#..........#..............#....P......#.........D.....#................#
#.c...K....#......G..................#................#......P.........#
#.........................#.........#.................#................#
#....G.....##################w#########################P################
#..w.......#.....w...#............#............#...........#......€€€€€#
############.................c...#.....P...................KKK....ccccc#
#............K.......#....G.......#.........G..#...........#......€€€€€#
#############.##################################.#######################
#...c...#...............G...........#.........€.........#...P..........#
#..c....K....G..€....................#......K...................€......#
#...c...#........................ww..#...........G......#..............#
###############.###############......###############.###################
#.......Pc€€€......#...........#######.................................#
#..G..............#.....K....................€..GP.....K.......€.......#
#...K.........................G......#.........K.......................#
#............w.....#.................#.................................#
########################################################################
"""
hero="@"
food=5
herox=1
heroy=2
heroz=0
hero_gold=0
hero_hunger=0
hp=90
#level=list(dungeon)
level=[]
for d in (dungeon1,dungeon2,dungeon3):
    l=[]
    for line in d.splitlines():
        l.append(list(line))
    level.append(l) 
while hero_hunger<100:
    hero_hunger+=random.choice((0,0,0,1,1,1,2))
    #for x,c in enumerate(level):
        #if x==herox:
            #print(hero,end="")
        #else:
            #print(c,end="")
    #print()
    for y, line in enumerate(level[heroz]):
        for x,c in enumerate(line):
            if x==herox and y==heroy:
                print(hero,end="")
            else:
                print(c,end="")
        print()
    command=input("gold:{} food:{} hunger:{} hp:{} ?".format(hero_gold,food,hero_hunger,hp))
    dx=0
    dy=0
    if command=="a":
        #herox-=1
        dx=-1
    if command=="d":
       #herox+=1
       dx=1
    if command=="s":
        dy=1
    if command=="w":
        dy=-1
    if command==" ":
        #herox+=2
        dx=2
        hero_hunger+=2
    if command=="e":
        if food > 0:
           food-=1
           if hero_hunger<0:
               hp+=5
               d
           hero_hunger-=random.choice((2,3,3,3,3,3,3,4,4,4,4,5))
           print(random.choice(eg))
        else:
            print("*Kkknnnuurrr*")
    if command=="q":
        hp+=100
    #-------in Wand gelaufen------
    target=level[heroz][heroy+dy][herox+dx]
    if target=="#":
        dx=0
        dy=0
        print("Autsch!Das tat weh!")
    #in monster gelaufen?
    #target=level[herox+dx]
    #----- Gorilla Anfang-------
    elif target=="G":
        print("Ein Gorilla blockiert deinen Weg!")
        print("Der Gorilla schlägt dich mit einer Banane!")
        schaden=random.randint(4,6)
        hp-=schaden
        print("Du erleidest {} schaden".format(schaden))
        if hp<1:
            print("Du stirbst.Versager.")
            break
        sieg=0.5
        if random.random() < sieg:
            print("Du hast gesiegt!")
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #-------Gorilla Ende------
    #-------Kobold Anfang------
    elif target=="K":
        print("Ein Kobold greift dich an!")
        print("Der Kobold holt einen Dolch heraus und greift dich an!")
        schaden=random.randint(2,8)
        hp -=schaden
        print("Du erleidest {} schaden".format(schaden))
        print("Stech")
        if hp<1:
            print("Du Verlierst!.Versager.")
            break
        sieg=0.5
        if random.random() < sieg:
            print("Bravo du bist der Sieger!")
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #-------Kobold Ende-------
    #-------Pandakrieger Anfang------
    elif target=="P":
        print("Ein Pandakrieger greift dich an!")
        print("Der Pandakrieger holt ein eisnunchaku heraus und verwandelt den Boden in Eis!")
        schaden=random.randint(3,9)
        hp -=schaden
        print("Du erleidest {} schaden".format(schaden))
        print("")
        if hp<1:
            print("Du Verlierst!.Versager.")
            break
        sieg=0.3
        if random.random() < sieg:
            print("Bravo du bist der Sieger!")
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #--------Pandakrieger Ende-------
    #--------Drache Anfang-----------
    elif target=="D":
        print("Ein Drache blockiert deinen Weg!")
        print("DerDrache schlägt spuckt dir Feuer entgegen!")
        schaden=random.randint(5,p)
        hp -=schaden
        print("Du erleidest {} schaden".format(schaden))
        if hp<1:
            print("Du stirbst.Versager.")
            break
        sieg=0.12
        if random.random() < sieg:
            print("Du hast die Prinzessin gerettet!")
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #--------Drache Ende------------
    herox+=dx
    heroy+=dy
    #aufheben
    stuff=level[heroz][heroy][herox]
    if stuff=="€":
        hero_gold+=1
        level[heroz][heroy][herox]="."
        print(random.choice(gg))
    if stuff=="w":
        food+=1
        level[heroz][heroy][herox]="."
    if stuff=="c":
        food+=3
        level[heroz][heroy][herox]="."
    if stuff=="p":
        print ("Bravo!Du hast meinen Dungeon durchgespielt")
        break
        
print("Game Over")



