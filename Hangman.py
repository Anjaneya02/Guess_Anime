import random
from AnilistPython import Anilist
anilist = Anilist()
anilist.search_anime(genre=['Action', 'Adventure', 'Drama'], year=[2016, 2019], score=range(80, 95))

r=["Orange","Apple","Banana","Guava","Watermelon","Melon","Strawberry","Blueberry"]

x=random.choice(r)
y=list(x)
o=y.copy()
c=y.copy()
print("Guess the fruit name\n")
for i in range (0,len(y)):
    c[i]="_"
print(c)
tries=len(x)+5

for j in range (0,tries):
    if c==o:
        break
    else:
      gus=input("Enter a alphabet\t")
      tries-=1
 
  
      if gus in y:
           c[y.index(gus)]=gus 
           y[y.index(gus)]="*"
           print(c)
      else :
           
           print("try again!!")
           print("tries left:\t",tries)
           print(c)
print("Thank you for playing!!")