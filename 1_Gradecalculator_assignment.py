# Grade Calculator Exercise

## Problem
#You're building a grade calculator for a teacher who needs to calculate final grades for students. The teacher needs to:

#1. Calculate the average of multiple test scores
#2. Apply a curve (add points to boost grades)
#3. Convert numerical grades to letter grades
#4. Format the output nicely

## Requirements
#Without using functions, you would need to repeat the same calculations for each student. Your task is to:

#1. Create functions that eliminate code repetition
#2. Make the main program easy to read and understand
#3. Handle the grade calculations for multiple students

## Expected Behavior
#The program should ask for student names and their test scores, then display:
#- Student name
#- Original average
#- Curved average
#- Letter grade

## Sample Run
#```
#Enter student name (or 'done' to finish): Alice
#Enter test scores separated by spaces: 85 92 78 88
#Student: Alice
#Original Average: 85.8
#Curved Average: 90.8 (+5 curve)
#Letter Grade: A-

#Enter student name (or 'done' to finish): Bob  
#Enter test scores separated by spaces: 72 68 75 70
#Student: Bob
#Original Average: 71.2
#Curved Average: 76.2 (+5 curve)
#Letter Grade: B

#Enter student name (or 'done' to finish): done
#```

## Hints
#Think about what code you would repeat for each student and turn those into functions:
#- Calculating averages
#- Applying curves
#- Converting to letter grades
#- Formatting output

print('Welcome to your Grade Calculator')
student_name = input("Enter the student's name( or done to finish): ")

def ask_for_student_name():
 student_name = " "
 while student_name != 'done':
    student_name = input("Enter the student's name( or done to finish): ")
    if student_name == 'done': 
     print('thank you for using Grade Calculator')

def ask_for_student_score():
  scores_input = input(f"Enter {student_name}'s scores (separate with spaces): ")
  scores = list(map(int, scores_input.split())) # convert scores to list and make individual input and integer
  total = sum((scores))
  avr = total/len(scores)
  curves = avr + 5
  
  
  #for score in scores:   # this iterate thr the student score
  print(f'{student_name} scored {scores}')   # this shows the student score in a list
       
  print(f'{student_name} scored a Total of : {total}')
  print(f'{student_name} original average : {avr}')
  print(f'{student_name} curve 5 : {curves}')

  if curves <= 40:
    print(f'Letter Grade: D')
  elif 40 < curves <= 60:
    print(f'Letter Grade: C')
  elif 60 < curves <= 80:
    print(f'Letter Grade: B')
  elif curves > 80:
    print(f'Letter Grade: A')
  else:
    print('Invalid score')



ask_for_student_name()
ask_for_student_score()


       
    
    #calculate scores

# Prompt for multiple scores separated by spaces, e.g. "78 85 92"
#scores_input = input(f"Enter {student_name}'s scores (separate with spaces): ")

# Convert to a list of floats
#scores = [float(s) for s in scores_input.split()]

# Print each score and the total
#for score in scores:
    #print(f"{student_name} scored: {score}")


#print(f"Total score: {sum(scores)}")


   

