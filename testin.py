points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]



li = [x for x in points if abs(x[0])==abs(9) or abs(x[1])==abs(9)]
# print(li)

dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

alarm=["Alarm!" for x in range(0,len(dbs)) if dbs[x]>=10 and dbs[x+1]>=10]

reducir = [ x-18 if x>30 else (x-12 if x>20 else x) for x in dbs ]
# [0 if number % 2 == 0 else (1 if number % 3 == 0
# else number) for number in numbers]

# print(reducir)

# print(alarm)
db = [x for x in dbs if x>=10]

dbm = [i for i,x in list(enumerate(dbs)) if x>10]
# dbm = [i for i in list(enumerate(db))]
# print(dbm)


dbss = [i for i,x in list(enumerate(dbs)) if x>10]

listado = [(db[y],dbm[y]) for y in range(0,len(dbm))]
# print(listado)
temperatures_C = [33, 66, 65, 62.0, 59, 60, 62, 64, 70, 56, 80, 81, 50, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]


f = [x*1.8+32 for x in temperatures_C]
# print(f)


status="False"
for i in range(0,len(temperatures_C)):
	if temperatures_C[i]>70 and temperatures_C[i+1]>70 and temperatures_C[i+2]>70 and temperatures_C[i+3]>70:
		status="True"
# print(status)

over = [i for i,x in list(enumerate(temperatures_C)) if x>=70]
# print(over)

# Variable

babyshark = '''Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…'''

firstparagraph=""
exclamation="!"
i=0
song=[x for x in babyshark]
lyrics="".join(song)
# print(str(lyrics))

for x in babyshark:
	if x!=exclamation and i==0: 
		firstparagraph+=x
	else:
		i+=1
firstparagraph+="!"
# print(firstparagraph)


def combat_acu_min(mc,hc,n):
    m = mc
    print("Machine choice",m)
    h = hc
    nog = n
    print("Human choice",h)
    point_human=0
    point_machine=0  

    if point_human >= 5 or point_machine >=5:
        while True:
            if point_human >= nog:
                print("2")
                break
            elif point_machine >= nog:
                print("1")
                break
        else:
            if m==h:
                point_machine+=0
            elif m=="stone" and h=="scissors":
                point_machine+=1
            elif m=="paper" and h=="rock":
                point_machine+=1
            elif m=="scissors" and h=="paper":
                point_machine+=1
            else:
                point_human+=1
            results = (point_machine-point_human)

            continue

mcsa="rock"
hcsa="paper"
combat_acu_min(mcsa,hcsa,5)
