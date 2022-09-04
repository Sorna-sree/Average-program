friend_watched = []# viruman, sitha raman, sillunu oru kadhal,3,
total_movie_friend_watched = int(input("enter the total movies your friend watched : "))
i_watched = [] # sitha raman,maari,singam,KGF
total_movie_i_watched = int(input("enter the total movies you watched : "))
both_we_watched = []
i_alone_watched = []
friend_alone_watched = []
my_count=0
friend_count=0
print("enter the movies names that your friend watched")
for i in range(0,total_movie_friend_watched):
    friend_watched.append(input("movie name "))
print("enter movies names that you watched")
for i in range(0,total_movie_i_watched):
    i_watched.append(input("movie name " ))
for movie in range(0,len(friend_watched)): 
    for film in range(0,len(i_watched)):
        if(friend_watched[movie] == i_watched[film]):
            both_we_watched.append(friend_watched[movie])#sitha raman
            friend_count += 1 #count 1
    if(friend_count == 0):
        friend_alone_watched.append(friend_watched[movie])
    friend_count = 0 
for movie in range(0,len(i_watched)):
    for film in range(0,len(friend_watched)):
        if(i_watched[movie] == friend_watched[film]):
            my_count += 1 #count 1
    if(my_count == 0):
        i_alone_watched.append(i_watched[movie])
    my_count = 0
print("I alone watched movies:")
print(*i_alone_watched)
print("Friend alone watched movies:")
print(*friend_alone_watched)
print("We both watched the movies:")
print(*both_we_watched)
