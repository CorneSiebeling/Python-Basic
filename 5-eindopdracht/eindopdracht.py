import time
seconden = input("Sec: ")       #hier maak ik een input om in te vullen op welke seconden de klok moet starten
s = int(seconden)
minuut = input("minuut:")       #hier maak ik een input om in te vullen op welke minuut de klok moet starten
m = int(minuut)
uur = input("uur:")             #hier maak ik een input om in te vullen op welk uur de klok moet starten
h = int(uur)
while (s < 60):                 #hier begin ik de loop 
    print ("Hours:"+str(h) +" "+ "Minutes:"+ str(m)+" "+ "Seconds:" + str(s))   #hier print ik het schema hoe ik het op het scherm wil laten zien
    time.sleep(1)               #aangeven van de seconden op regel 1... oftewel de seconde tellen
    s=s+1
    if (s == 60):
        m=m+1
        s = 0

    elif(m == 60):
        h=h+1                   #dit hele blok zorgt ervoor dat de uren, minuuten en seconden bij elkaar worden geteld en de timer wordt gereset aan het eind van een dag
        m = 0
        s = 0
    
    elif(h == 24):
        h = 0



                                    
