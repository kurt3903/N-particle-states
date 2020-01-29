from IPython import get_ipython
get_ipython().magic('reset -sf')
import collections

state = [0, 0, 0]
particles = ('a', 'b', 'c')

#Distinguishable particles:

dist_wavefuns = []
combinations = []
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            cmb = [i, j, k]
            state[0] = '\u03C8'+str(i+1)+'(x'+particles[0]+')'
            state[1] = '\u03C8'+str(j+1)+'(x'+particles[1]+')'
            state[2] = '\u03C8'+str(k+1)+'(x'+particles[2]+')'
            dist_wavefuns.append(str(state[0])+str(state[1])+str(state[2]))
            combinations.append(cmb)
print('\n'+str(len(dist_wavefuns))+' possible three-particle states for distinguishable particles:\n')
for n in range(0, len(dist_wavefuns)):
    print(dist_wavefuns[n])
    
#Identical bosons:
    
state = [0, 0, 0]
boson_wavefuns = []

#each particle is in a unique state:
            
unique_cmb_state = []
unique_cmbs = []

for line in combinations:
    reduced_cmb = (set(tuple(line)))
    if len(reduced_cmb) == 3:
        unique_cmbs.append(line)

for line in unique_cmbs:
    i = line[0]
    j = line[1]
    k = line[2]
    state[0] = '\u03C8'+str(i+1)+'(x'+particles[0]+')'
    state[1] = '\u03C8'+str(j+1)+'(x'+particles[1]+')'
    state[2] = '\u03C8'+str(k+1)+'(x'+particles[2]+')'
    unique_cmb_state.append(str(state[0])+str(state[1])+str(state[2]))

combined_unique_state = '+'.join(unique_cmb_state)
boson_wavefuns.append('1/sqrt('+str(len(unique_cmb_state))+')*['+combined_unique_state+']')

#each particle is in the same state:

for line in combinations:
    if line[0] == line[1] == line[2]:
        n = line[0] +1
        state[0] = '\u03C8'+str(n)+'(x'+particles[0]+')'
        state[1] = '\u03C8'+str(n)+'(x'+particles[1]+')'
        state[2] = '\u03C8'+str(n)+'(x'+particles[2]+')'
        boson_wavefuns.append(str(state[0])+str(state[1])+str(state[2]))
    
#Two particles are in the same state

two_cmb_states = []
two_cmbs = []

for line in combinations:
    reduced_cmb = (set(tuple(line)))
    if len(reduced_cmb) == 2:
        two_cmbs.append(line)
    
for i in range(0, 4):
    for j in range(0, 3):
        for k in range(0, 3):
            cmb = [i, j, k]
            state[0] = '\u03C8'+str(k+1)+'(x'+particles[0]+')'
            state[1] = '\u03C8'+str(k+1)+'(x'+particles[1]+')'
            state[2] = '\u03C8'+str(k+1)+'(x'+particles[2]+')'
            
            state[j] = '\u03C8'+str(i+1)+'(x'+particles[j]+')'
            two_cmb_states.append(str(state[0])+str(state[1])+str(state[2]))
            
#print
print('\n'+str(len(boson_wavefuns))+' possible three-particle states for identical bosons:')
for n in range(0, len(boson_wavefuns)):
    print(boson_wavefuns[n])
    
    
#Identical fermions:
    
state = [0, 0, 0]
fermion_wavefuns = []

#each particle is in a unique state:
            
unique_cmb_state = []
unique_cmbs = []

for line in combinations:
    reduced_cmb = (set(tuple(line)))
    if len(reduced_cmb) == 3:
        unique_cmbs.append(line)

for line in unique_cmbs:
    i = line[0]
    j = line[1]
    k = line[2]
    state[0] = '\u03C8'+str(i+1)+'(x'+particles[0]+')'
    state[1] = '\u03C8'+str(j+1)+'(x'+particles[1]+')'
    state[2] = '\u03C8'+str(k+1)+'(x'+particles[2]+')'
    unique_cmb_state.append(str(state[0])+str(state[1])+str(state[2]))

combined_unique_state = '+'.join(unique_cmb_state)
fermion_wavefuns.append('1/sqrt('+str(len(unique_cmb_state))+')*['+combined_unique_state+']')
