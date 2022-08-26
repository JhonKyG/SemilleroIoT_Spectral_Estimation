var = {'f1':100e6, 'f2':108e6, 'step':1e5}#var = {'f1': 88e6, 'f2':108e6, 'step':1e5}

f1 = var['f1']; f2 = var['f2']; step = var['step']; 
velocidad = 1; timeI = 1;

def sweeper(prob_lvl):
 global f1, f2, step
 if f1 < f2:
  f1+=step
  return f1
 else:
  return f2
 
def funTime(funcTime):
 global timeI
 timeI += 1 
 return timeI

def vel(prob_lvl):
 global velocidad, timeI
 print(prob_lvl)
 if timeI > 5:
  return 1
 else:
  return 1
