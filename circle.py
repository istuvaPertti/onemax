import random
import string

target = "HELLO WORLD"
population_size = 15
max_generations = 5000
mutation_chance = 0.01

def random_character():
    return random.choice(string.ascii_uppercase+" ")

def random_string(length):
    return ''.join(random_character() for _ in range(length))

def fitness(agent):
    return sum(1 for i, c in enumerate(agent)if c == target[i])

def mutate(agent):
    return ''.join(c if random.random() > mutation_chance else random_character()for c in agent)

def crossover(parent1,parent2):
    split = random.randint(0,len(parent1))
    return parent1[:split] + parent2[split:]

population = [random_string(len(target))for _ in range(population_size)]

for generation in range(max_generations):
    population.sort(key = fitness,reverse = True)

    best = population[0]
    print(f"Gen {generation}: {best}(Fitness: {fitness(best)})")
  
    if best == target:
        print("\n jee!")
        print(population)
        break

    next_generation = population[:10]
    while len(next_generation) < population_size:
        parent1 = random.choice(population[:50])
        parent2 = random.choice(population[:50])
        child = crossover(parent1,parent2)
        child = mutate(child)
        next_generation.append(child)

    population = next_generation


