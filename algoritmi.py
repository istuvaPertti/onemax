import random

num = int(input("agenttien määrä: "))

length = int(input("genomien koko: "))

agents = []

agents_fitness = []

tournament_selected = []

tournament_fit = []

parent1=0
parent2=0

lis = []

tournament_size = 3

total_fitness_points = 0

def create_genome(length):
    return [random.randint(0,1)for _ in range(length)]

for i in range(num):
    lis.append(i)
    agents_fitness.append(0)

    agents.append(create_genome(length))



    for c in range(length):

        agents_fitness[i] += agents[i][c]

        total_fitness_points += agents[i][c]

tournament_selected.append(random.sample(lis,tournament_size))

for h in range(tournament_size):
    tournament_fit.append(agents_fitness[tournament_selected[0][h]])

tournament_fit.index(max(tournament_fit))


#seuraavaksi tournament selection ja mutaatio