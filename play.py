#name = input("what is your name:")
#print("Hello",name)
#country = input(f"{name}, Where are you from?:")
#print(name, "is from",country )
#age = input(f"{name}, how old are you:")
#print(name,"is from",country, "and is ",age,"years old")


#phonenumber= "+49(176)123-456"
#print(phonenumber.replace("(","").replace(")","").replace("-",""))

text = " Engineering "
text1 = " Engineering ".strip()
#print(text)

#a = " ~~book"

#print(text[2:])
#print(text.upper())
#print(text.lower())
#print(a.strip().strip("~"))

# excercise 2. clean data 
#"968-maria " (D@t@ Engineer) ;; "27 y
#name = "968-Maria".strip("968-").strip()
#role = "(D@t@ Engineer );;".replace("(","").replace(")","").replace("@","a").replace(";","")
#age = "27y  ".strip().replace("y","")
#print(f"{name} | role: {role} | age: {age}")

#maria| role: data engineer| age: 27


#generate a random number btween 1 and 100 and ck is the result is an integer

#import random
#a = random.randint(1,100)
#b = random.random()
#print(isinstance(a,int))
#print(isinstance(b,int))

#exercise 3
#allows registration if any part is true
#email = "rukayyat@gmail.com"
#phone_number = "01-22-88-371"
#home_address = ""
#print(any([email, phone_number, home_address]))
#print(all([email, phone_number, home_address]))

#exercise 3 trigger alert if one of the conditions is true
#cpu_usage = 90
#temperature = 80
#A= cpu_usage < 90 and temperature < 80
#B= cpu_usage >= 90 or temperature > 80
#print(f"trigger alarm: {A}") 
#print(f"trigger alarm: {B}") 

#exercise 4
#allow access only if user is logged in or they are guest
#they must not be banned
#is_logged_in = True
#is_guest  = False
#is_banned = True #False

#print(is_logged_in or is_guest and is_banned)
#print((is_logged_in or is_guest) and not is_banned)

#exercise 5
#check if a user name is not empty and the age is greater than or equal to 18
#user_name = False
#Age = True
#print(user_name is not None and Age >= 18)



#excercise 6
#ck if the password is at least 8 xters long anddoes not contain space
#password_8xters_long = True
#contain_space = True
#print(password_8xters_long and not contain_space)
#print(password_8xters_long and contain_space)

#exercise 7
#ck if a user email is not empty, contains @ and ends with .com
user_email = True
contains_at = True
ends_with_com = False
#print(user_email is None or (contains_at and ends_with_com))

#execrcise 8
#ck if a username is a string is not None and is longer than 5 xters
username_isstring = True
username_not_none =True
username_longer_than5xters = True
#print(username_isstring and username_not_none and username_longer_than5xters)

#exercise 9
#ck if the user is either an admin or a moderator and either they are not banned or they've verified their email.
is_admin = True
is_moderator = False #True
is_banned = True
email_verified = False #True
#print((is_admin or is_moderator) and (not is_banned or email_verified))

#FOR LOOPS
#items = (1,2,3,4,5)
#for item in items:
    #print(f"Round:{item}")

#a = range(1,101)
#for i in a:
 #   print(f"{i}. I will not do that again")

scores = [80, 90, 100, 70, 60, 20]
total = 0
for score in scores:
    total += score
    #print("total scores: ", total)
#print("final score is: ", total)


scores = [80, 90, 100, 70, 60, 20]
total = 0
for score in scores:
    total += score
#print("Running total: ", total)

files = [" report.csv", "DATA.CSV ", "Final.txt "]
for file in files:
    file = file.strip().lower().replace("txt", "csv")
    #print("processing now :", file)

# build the 7 times table using for loops

for i in range(1,13):
    total= 7*i
    #print("7 *",i, "=", total)

number = 7
#for i in range(1, 13):
    #print(f"{number} * {i} = {number * i}")


days= ['mon', 'tue', 'sat', 'wed', 'sun', 'thur', 'fri']
for day in days:
    if day in ['sat','sun']:
      #print("its weekend")
      continue
    #print(f'{day} is a workday')

#print duplicate found if a duplicate exist otherwise print all files are unique
#files = ['report.csv', 'data.xlsx', 'summary.doxc', 'report.csv', 'data.csv']
#for file in files:
    #if files.count(file) >1:
       #print('Duplicate found', file)
       #break
#else:
    #print('all files are unique')

start = 0
while start != 100:
    print(f'boiling at {start} degrees')
    start +=5
print('boiling at 100 degrees')

# allow up to 3 attempts
#if the user type yes, print 'Glad we are on the same page'
#otherwise print 3 strike you are out
#using true while loop
attempt = 0
max_attempt = 3
while True:
    answer = input('Do you agree? (yes/no): ')
    if answer == 'yes':
        print('Glad we are on the same page')
        break  # Exit the loop if user agrees
    attempt += 1
    if attempt == max_attempt:
        print('3 strikes, you are out')
        break  # Exit loop after max attempts

#same exercise using a while loop
count = 0
answer = " "
while answer != "yes":
    answer = input('Do you agree? (yes/no): ')
    if answer == 'yes':
        print('Glad we are on the same page')
        break
    count += 1
    if count == 3:
     print('3 strikes, you are out')
     break
#corrections
attempt = 3
while attempt < 3:
    answer = input('Do you agree? (yes/no): ')
    if answer == 'yes':
      print('Glad we are on the same page')
      break
    attempt+=1
else:
        print('3 strikes, you are out')











