movies = {'Terminator': ['M','A','E'],
         'Beauty in Black':['M','E'],
         'Fury':['A','E'],
         'Home Alone':['M','A','E'],
         'Rambo-LastBlood':['M','A','E']  }
def show_movies():
 print('Welcome to the Lilies Cinema')
 print('Available movies for today')
 for movie in movies:
    print(f'{movie} at showslot:{movies[movie]}')
 

def movie_selection():
 answer = input('Select a movie :')
 if answer in movies:
    show_time = input('Select show time(M,A OR E):')
    if show_time in movies[answer]:
        print('30 seats available')
    else:
     print('Invalid selection')
     exit()
 else:
   print('Invalid selection')
   exit()

def seat_selection():
 seat_type = {'Regular' : 10,
              'VIP': 20,
              'VVIP': 30,
              'XBOX': 40}

 answer2 = input('select seat type(Regular,VIP,VVIP or XBOX): ')
 if answer2 in seat_type:
   print(f'{answer2} costs {seat_type[answer2]} euros')
 else:
     print('Invalid selection')
     exit()
