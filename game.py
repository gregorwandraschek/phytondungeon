import random
eg=("mmmhhh,das war lecker!","*mampf*","*schmatz*","prost","*rülps*")
gg=("kaching!","juhu!","was kauf ich jetzt damit","so tolles gold","Money!")
#Dungeon Spiel!Super Wahl!
dungeon="....€.w.c..€...G.c.€.c.K..€..G.c..€.wK..G..€..w..€..c.€.w.€.G.w.€.G.w..€...P..p"
hero="@"
food=5
herox=0
hero_gold=0
hero_hunger=0
hp=90
level=list(dungeon)
while hero_hunger<100:
    hero_hunger+=random.choice((0,0,0,1,1,1,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print(c,end="")
    print()
    command=input("gold:{} food:{} hunger:{} hp:{} ?".format(hero_gold,food,hero_hunger,hp))
    dx=0
    if command=="a":
        #herox-=1
        dx=-1
    if command=="d":
       #herox+=1
       dx=1
    if command==" ":
        #herox+=2
        dx=2
        hero_hunger+=2
    if command=="e":
        if food > 0:
           food-=1
           if hero_hunger<0:
               hp+=5
           hero_hunger-=random.choice((2,3,3,3,3,3,3,4,4,4,4,5))
           print(random.choice(eg))
        else:
            print("*Kkknnnuurrr*")
    if command=="q":
        hp+=100
    #in monster gelaufen?
    target=level[herox+dx]
    #----- Gorilla Anfang-------
    if target=="G":
        print("Ein Gorilla blockiert deinen Weg!")
        print("Der Gorilla schlägt dich mit einer Banane!")
        schaden=random.randint(4,6)
        hp -=schaden
        print("Du erleidest {} schaden".format(schaden))
        if hp<1:
            print("Du stirbst.Versager.")
            break
        sieg=0.5
        if random.random() < sieg:
            print("Du hast gesiegt!")
            level[herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #-------Gorilla Ende------
    #-------Kobold Anfang------
    if target=="K":
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
            level[herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #-------Kobold Ende-------
        #-------Pandakrieger Anfang------
    if target=="P":
        print("Ein Pandakrieger greift dich an!")
        print("Der Pandakrieger holt ein eisnunchaku heraus und verwandelt den Boden in Eis!")
        schaden=random.randint(3,9)
        hp -=schaden
        print("Du erleidest {} schaden".format(schaden))
        print("")
        if hp<1:
            print("Du Verlierst!.Versager.")
            break
        sieg=0.1
        if random.random() < sieg:
            print("Bravo du bist der Sieger!")
            level[herox+dx]="."
        else:
            print("Du verlierst!")
            dx=0
    #--------Pandakrieger Ende-------
    herox+=dx
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
        level[herox]="."
    if stuff=="p":
        print ("Bravo!Du hast meinen Dungeon durchgespielt")
        break
        
print("Game Over")



