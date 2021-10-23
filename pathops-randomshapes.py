from random import random, randint, seed
from pathops import Path, PathVerb
from pathops.operations import union


def randCoord():
    return randint(0, 800), randint(0, 800)


def randShape(pen):
        pen.moveTo(randCoord())
        for k in range(3, 8):
            if random() > 10.7:
                pen.curveTo(randCoord(), randCoord(), randCoord())
            else:
                pen.lineTo(randCoord())
        pen.closePath()


# seed(0)

N = 300
for i in range(N):
    print(f"--- {i} of {N}")
    path = []
    for j in range(randint(2, 4)):
        sub = Path()
        randShape(sub.getPen())
        path.append(sub)

    result = Path()
    union(path, result.getPen())
