from xmlplus import parse, count_nodes, height, sum_values, generate_dot
from time import perf_counter

arquivo = "T1/casos-cohen/casom5.txt"

with open(arquivo) as f:
    dados = [int(x) for x in f.read().split()]

tree1 = parse(dados)

generate_dot(tree1, "casom5.dot")