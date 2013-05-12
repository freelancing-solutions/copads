'''
Neural example #1

Operations demonstrated:
1. Initialize brain with n neurons (n=5)
2. Establish synaptic connections between 2 neurons
3. Disconnect synapse between 2 neurons
4. Adding neurons into brain
'''
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))

import neural as n

names = ['A', 'B', 'C', 'D', 'E']
brain = n.Brain(list_of_neuron_names=names)

print 'Brain initiated with', len(names), 'neurons:', names
print 'Memory address for neuron A:', brain.neuron_pool['A'] 
print 'Memory address for neuron B:', brain.neuron_pool['B']
print 'Memory address for neuron C:', brain.neuron_pool['C']
print 'Memory address for neuron D:', brain.neuron_pool['D']
print 'Memory address for neuron E:', brain.neuron_pool['E']
print 'Synapses table:', brain.synapses
print

print 'Connect neuron: B -> C'
brain.connect_neurons('B', 'C')
print 'Synapses table after connection:', brain.synapses
print

print 'Connect neuron: A -> C'
print 'Connect neuron: C -> D'
brain.connect_neurons('A', 'C')
brain.connect_neurons('C', 'D')
print 'Synapses table after connection:', brain.synapses
print

print 'Disconnect synapse between neurons C and D'
brain.disconnect_neurons('C', 'D')
print 'Synapses table after disconnection:', brain.synapses
print

print 'Connect neuron: D -> E'
print 'Connect neuron: C -> E'
brain.connect_neurons('D', 'E')
brain.connect_neurons('C', 'E')
print 'Synapses table after connection:', brain.synapses
print

print 'Add neurons: F, G, H, I and J'
brain.add_neuron(n.Neuron(name='F'))
brain.add_neuron(n.Neuron(name='G'))
brain.add_neuron(n.Neuron(name='H'))
brain.add_neuron(n.Neuron(name='I'))
brain.add_neuron(n.Neuron(name='J'))
print 'Memory address for neuron F:', brain.neuron_pool['F']
print 'Memory address for neuron G:', brain.neuron_pool['G']
print 'Memory address for neuron H:', brain.neuron_pool['H']
print 'Memory address for neuron I:', brain.neuron_pool['I']
print 'Memory address for neuron I:', brain.neuron_pool['J']
print 'Synapses table after additions:', brain.synapses
print

print 'Connect neurons: F -> G -> H -> E'
print 'Connect neurons: I -> G'
brain.connect_neurons('F', 'G')
brain.connect_neurons('G', 'H')
brain.connect_neurons('H', 'E')
brain.connect_neurons('I', 'G')
print 'Synapses table after connection:', brain.synapses
print