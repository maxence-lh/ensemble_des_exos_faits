"""
EXERcIcE LISTES ET VARIABLES

prix = int(input("quel est le prix ?"))
nb = int(input("combiens d'articles avez-vous ?"))
tva = (prix*nb)*0.2
total = prix*nb+tva
print("le prix de votre article est de",prix,"€","vous en avez:", nb,"ce qui vous fait",total,"€","dont", tva,"€ de TVA")

liste= [4,5]
print(liste)


liste= [4,"lhvd",8,"jvf"]
print(liste)
print(liste[0])
print(type(liste[2]))


x=[4,6]
y=[5,7]
z=x+y
print(z)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[4])
print(x[3:5:1])
print(x[2:8:2])
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
del(x[3:5])
print(x)



x = ["ok", 4, 2, 78, "bonjour"]
print(x[3])
x[1]="toto"
print(x)



r=[0,1,2,3,4,5]
print(r)
e=[0]+[i+1 for i in range(5)]
print(e)




x={"key":"valeur",
"key2":"valeur2"}
print(x)
print(x["key"])
x["titi"]="toto"
x["titi"]="tata"
print(x)
del(x["titi"])
# del(x["key"])
# print(x["key"])
print(x)
y=x
print(y)


x=[(1,2),(3,4),(5,6),(7,8)]
x.append("a")

print(x)
y=[1,2,3]
x=x+y
print(x)
x[4]=x[4]+"2"
print(x)
del(x[6])
print(x)
print(y)
z=y
y[:]=[]
print(y)
z[0:4:1]=[]
print(z)



EXERcIcES 2 TEST



nb1=int(input("un nombre"))
nb2=int(input("un autre nombre"))
produ=nb1*nb2
if produ < 0 :
    print("le produit est négatif ")
elif produ > 0 :
    print("le produit est positif")
else :
    print("le produit est nul")


age=int(input("votre age ?"))
if age<18:
    print("vous êtes mineur")
else:
    print("vous êtes majeur")


nombre=int(input("donnez un nombre"))
if nombre<10.5 and nombre>10 or nombre>5 and nombre<10:
    print("vrai")



nombre=int(input("donnez un nombre"))
if nombre<10.5 and nombre>10:
    print("vrai")
elif  nombre>5 and nombre<10:
    print("vrai")


EXERcIcES 3 BOUcLE


for i in range(6):
    print(i)




tab=["un","deux","trois"]
for caractere in tab:
    print(len(caractere))
    for lettre in caractere:
        print(lettre)




x = "anticonstitutionnellement"
for lettre in x:
    print(lettre)



x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for nombre in x:
    for liste in nombre:
        print(liste)



a=0
x = [1,10,20,30,40,50]
for i in x:
    a=a+i
print(a)



for i in range(5,0,-1):
    print(i)
print(0)



for i in range(1,10):
    if i>3:
        break
    print(i)



a,b=1,10
for i in range(a,b):
    if i>3:
        break
    print(i)




for i in range(1,10):
    if i==3:
        print("")
    else:
        print(i)



x=0
ordi = ["apple", "asus", "dell", "samsung"]
while x<len(ordi):
    for marque in ordi:
        print(marque)
        x+=1




while input("donnez un texte")!="exit":
    print(input)


x=0
while x<101:
    print(x)
    x+=5


EXERCICES 4 FONCTIONS


def multpl_5(x):
    return x*5

print(multpl_5(int(input("un nombre"))))



def lis(a):
    for i in a:
        if (i % 2 == 0 ):
            print(i)

            
       
x=[1,2,3,4,5,6,7]
lis(x)



pre=0
act=1
suiv=0

# def fibro():



while suiv<int(input("nombre")):
    suiv=pre+act
    print(suiv)
    pre=act
    act=suiv




count = 0
class carre:
    def __init__(self,nb_cote,lg_cote):
        self.nb_cote = nb_cote
        self.lg_cote = lg_cote
    def calculate_perimeter(self):
        return self.nb_cote * self.lg_cote
    def calculate_area(self):
        return self.lg_cote * self.lg_cote
    def factor(self):
        return (self.nb_cote * self.lg_cote) * multi
    count+=1


if __name__ == "__main__":
    c = carre(4, 10)
    multi= int(input("un nombre \n"))
    print(c.nb_cote)
    print(c.lg_cote)
    print(c.calculate_perimeter())
    print(c.calculate_area())
    print(c.factor())
    print(c.count)
    
print("Le carré à un côté d'une longueur de", c.lg_cote,"cm, une aire de", c.calculate_area(), "cm², et un périmètre de", c.calculate_perimeter(), "cm.")
print("le nouveau carré est",multi,"fois plus grand donc",c.factor(),"cm²")
print(c.count)


"""