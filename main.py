import random

MATING_PERCENT=50
ELITISM_FACTOR=10
POPULATION_SIZE=100
TARGET="i love machine learning"
GENES= '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ,.-_;:!@$[]'''

class individual(object):

    def __init__(self, chromosome):
        self.chromosome=chromosome
        self.fitness=self.calculate_fitness()

    @classmethod
    def mutated_genes(self):
        global GENES
        gene=random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self):
        global TARGET
        gnome_length = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_length)]

    def mate(self, second_parent):
        # create a new offspring using 2 parents
        child_chromosome = []

        for gp1, gp2 in zip(self.chromosome, second_parent.chromosome):
            prob=random.random()
            if(prob < 0.45):
                child_chromosome.append(gp1)
            elif(prob < 0.9):
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return individual(child_chromosome)

    def calculate_fitness(self):
        global TARGET
        fitness=0
        for cg,ct in zip(self.chromosome, TARGET):
            if(cg !=ct):
                fitness+=1
        return fitness

def main():
    global MATING_PERCENT
    global ELITISM_FACTOR
    global POPULATION_SIZE
    population=[]
    solved=False
    generation=1

    for _ in range(POPULATION_SIZE):
        gnome=individual.create_gnome()
        new_individual=individual(gnome)
        population.append(new_individual)

    while not solved:
        population[0].chromosome
        population=sorted(population, key = lambda x:x.fitness)

        if(population[0].fitness <=0):
            solved=True
            break

        new_population = []

        # perform elitism
        s=int((ELITISM_FACTOR * POPULATION_SIZE)/100)  # finding the exact number of elites
        new_population.extend(population[:s])

        # perform the process of mating
        MATING_FACTOR= 100 - ELITISM_FACTOR
        s=int((MATING_FACTOR * POPULATION_SIZE)/100)   # finding the exact number of offsprings

        for _ in range(s):
            real_size = int((MATING_PERCENT*POPULATION_SIZE)/100)

            parent_1 = random.choice(population[:real_size])
            parent_2 = random.choice(population[:real_size])

            child = parent_1.mate(parent_2)

            new_population.append(child)
            print("Generation: {}\tString: {}\tFitness: {}".format(generation,"".join(population[0].chromosome),population[0].fitness))
     
        population=new_population
        #print("Generation: " + str(generation) + "Guess:" + str(population[0].chromosome) + "Fitness: " + str(population[0].fitness))
        generation += 1
     
         
    print("Generation: {}\tString: {}\tFitness: {}".format(generation,"".join(population[0].chromosome),population[0].fitness))
        
        

if __name__ =='__main__':
    main()