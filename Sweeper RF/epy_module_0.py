# this module will be imported in the into your flowgraph
t = 1; step_freq = 100000; f1 = 88000000; time_max = 0; step_time= 1;
#88.6e6+(freq*1e6)
def frecuencia(prob_lvl):
    global t, step, time_max, f1
    if t != time_max:
     f1 += step_freq
     print(prob_lvl)
    return f1
    
        
def tiempo(prob_lvl, time):
    global t, step, time_max
    time_max = time
    if t != time_max:
     if prob_lvl:
      t += step_time
    return (time_max-t)
