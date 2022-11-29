curr_x = 2
precision = 0.000001
rate = 0.001
derivativ = lambda x:2*(x+3)
diff = 1
itr = 0
max_iterations = 3000

gradients = []
iterations = []

while diff >= precision and itr < max_iterations:
    prev_x = curr_x
    curr_x = curr_x - (rate*derivativ(prev_x))
    
    diff = abs(curr_x - prev_x)
    
    itr = itr + 1
    
    gradients.append(curr_x)
    iterations.append(itr)
    
print("Local Minima of the equation is at : ", gradients[-10:-1])