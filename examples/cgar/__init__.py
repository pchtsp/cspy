from read_input import read_input
from algorithm import algorithm

airline = 'Finnair'

DataObj = read_input(airline=airline)

model, data = algorithm(DataObj, n_runs=50, airline=airline)