import random
import time

OPERATORS = ['+','-','*']
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10

def problem():
    right_operand = random.randint(MIN_OPERAND,MAX_OPERAND)
    left_operand = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)
    exp = str(left_operand)+' '+ operator +' '+str(right_operand) 
    answer = eval(exp)
    return exp,answer

wrong=0
input("press 'ENTER' to start the game \n")
print('---------------------')
start_time = time.time()


for i in range (TOTAL_QUESTIONS):
    exp,answer = problem()
    while True:
        guess=input("question"+' #'+str(i+1)+': '+' '+ exp +' '+'= ')
        if guess == str(answer):
         break
        wrong+=1

end_time = time.time()
total_time = round(end_time-start_time,2)

print("-----GAME OVER-----")
print("well done!!")
print("total time taken: " ,total_time,'sec')    
print("total wrong answers:",wrong)






