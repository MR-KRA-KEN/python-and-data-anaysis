user={}
name=input("Enter your name : ")
age=input("Enter your age : ")
fav_movie= input("Enter fav movies : ").split(',')
fav_song= input("Enter fav songs : ").split(',')

user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_song']=fav_song

for key,value in user.items():
    print(f"{key}  :  {value}")
    