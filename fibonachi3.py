a = int(input("How many students in programming class? "))
score_list = []

for i in range(a):
    score = float(input("Score: "))
    score_list.append(score)
    
print('AVG:', sum(score_list) / a)
print('MAX:', max(score_list))
print('MIN:', min(score_list))