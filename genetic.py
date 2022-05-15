import pygad
import numpy
import random

"""

Задача похожа на то, что было в одном из примеров. 

Решаем диофантово уравнение с пятью целыми случайными коэффициентами.

"""

function_inputs = [int(10 + random.random() * 90), int(1000 + random.random() * 100), int(10 + random.random() * 90),
                   int(10 + random.random() * 90), int(1 + random.random() * 9)]

"""

Это я сгенерировала "почти случайные" коэффициенты для того, чтобы у программы была хоть
какая-то надежда получить близкий к желаемому результат.

"""

desired_output = 2003  # Вот это значение я хочу получить

print(function_inputs)  # Вывожу список сгенерированных коэффициентов


def fitness_func(solution, solution_idx):
    output = numpy.sum(solution * function_inputs)
    fitness = 1.0 / (numpy.abs(output - desired_output) + 10 ** (-10))
    return fitness


num_generations = 50  # Количество поколений, в среднем требуется не более 50.
num_parents_mating = 10

sol_per_pop = 20
num_genes = len(function_inputs)

last_fitness = 0


def on_generation(ga_instance):
    global last_fitness
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       fitness_func=fitness_func,
                       gene_type=int,  # Хочу получать именно целочисленные решения,
                       gene_space={'low': -10, 'high': 10},  # находящиеся в этом диапазоне.
                       on_generation=on_generation)

ga_instance.run()

ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

prediction = numpy.sum(numpy.array(function_inputs) * solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

if ga_instance.best_solution_generation != -1:
    print("Best fitness value reached after {best_solution_generation} generations.".format(
        best_solution_generation=ga_instance.best_solution_generation))
