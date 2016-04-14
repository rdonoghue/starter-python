import random

#randoem NUmber, inclusive
print random.randint(1,6)

#Pick one from a list
stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print random.choice(stuff)

graph=[];



for z in range(0,13):
    graph.append(0);
for z in range(0,20):
    val = int(random.randint(1,6) + random.randint(1,6))
    graph[val]= graph[val] + 1
print graph
for foo in range(2,13):
    print foo,
    for holder in range(0,graph[foo]):
        print "*",
    print
