import random
from AnilistPython import Anilist
anilist = Anilist()

l=anilist.search_anime(genre=['Slice of Life'], score=range(80, 95))

r=random.randint(0,len(l))
print(len(l))
print(r)
print(l[r])


