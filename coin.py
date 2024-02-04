import random
print("Добро пожаловать в игру 'Орел и решка'")
podbr=int(input("Сколько раз хотите подбросить монету?"))
raz=0
orel=0
rejka=0
while raz<podbr:
    pir=random.randint(1,2)
    raz+=1
    if pir==1:
        orel+=1
    elif pir==2:
                 rejka+=1
print("Орел выпал",orel,"раз")
print("Решка выпала",rejka,"раз")