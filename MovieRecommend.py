'''
Name: Ishan Gaba
The project is also part of a school assignment.

There are different ways to solve the problems effciently using the 
functions created as helper methods for the functions after which are 
not mentioned in this project.
'''

from collections import defaultdict 
#-------------------TASK1-------------------------
#-------Part1-----------

def read_ratings_data(f):
    # Read data from the file line by line splitting at "|" 
    movieDict = defaultdict(list) #default dictonary to append ratings for same movie in a list
    for line in open(f):
        movie, rating, userID = line.split('|') # split the file at "|" and assign to variables
        movieDict[movie.strip()].append(float(rating.strip())) #.strip() to get rid of pre and post spaces.
    return movieDict #Returning the default dictionary 

#-------Part2-----------

def read_movie_genre(f):
    #Function reads from the file line by line and split at "|"
    movieGenre = {}
    for line in open(f):
        genre, userID, movie = line.split('|') # assigining tokens to the variables 
        movieGenre[movie.strip()] = genre.strip() #.strip() to get rid of pre and post spaces.
    return movieGenre #Returns dictionary movie names as keys and genres as values.

#-------------------TASK2-------------------------
#-------Part1-----------

def create_genre_dict(movieGenDictionary):
    moviesWithSameGenre = defaultdict(list) #Default dict to append movies to same genre as required
    for m,g in movieGenDictionary.items(): # get keys and values from movie-to-genre dictionary
        moviesWithSameGenre[g].append(m) #append them to list as values for key
    return moviesWithSameGenre #Returns dictonary with Genre as keys and movie names list as values

#-------Part2-----------

def calculate_average_rating(movieRatingsDict):
    averageRatingDict = {}
    for m,r in movieRatingsDict.items():
        averageRatingDict[m] = float("%.2f" % round(sum(r)/len(r), 2)) #Taking the average of ratings list and assigned the rounded value to float; as value for dict 
    return averageRatingDict #Returns a dictionary with movie names as keys and avg rating for the movie as values

#-------------------TASK3-------------------------
#-------Part1-----------

def get_popular_movies(averageRatingDict, n=10):
    '''
    Function takes in movie-to-average dict and sort it based on average rating.
    sorted list is then sliced using the second argument and casted to dict function.
    Returns a dictionary with number of popular movies entered as argument to fucntion.
    '''
    sortedList = sorted(averageRatingDict.items(), key=lambda rating: rating[1], reverse= True)
    popularityDict = dict(sortedList[0:n])        
    return popularityDict

#-------Part2-----------        
def filter_movies(orderedAverageRatingDict, threshold=3):
    '''
    Function checks if the average rating is higher than given threshold 
    and assigns the movie name as key and average as value to a new dictionary.
    Dictionary is then sorted into a list and returned with a default of 10 most popular movies.
    '''
    thresholdDict = {}
    for movie,ratings in orderedAverageRatingDict.items():
        if(ratings>= threshold):
            thresholdDict[movie] = ratings          
        else:
            continue 
    sortedList = sorted(thresholdDict.items(), key=lambda rating: rating[1], reverse= True)
    thresholdDict = dict(sortedList[0:10])
    return thresholdDict

#-------Part3----------- 
def get_popular_in_genre(genre,genreMovieDict,movieAvgRatingDict,n=5):
    '''
    Return Top n most popular movies in given genre
    '''
    topRatingDict = {}
    for i in genreMovieDict[genre]: #gets the list of movies in genre
        if i in movieAvgRatingDict.keys():# checks for movie name as key in movie-to-average dict
            topRatingDict[i] = movieAvgRatingDict[i] # assign movie ratings to the movie names 
    sortedTopRatingDict = sorted(topRatingDict.items(),key=lambda rating: rating[1],reverse=True) # sort the list from high to low ratings
    topRatingDict = dict(sortedTopRatingDict[0:n]) #limit the output to dict using slicing.
    return topRatingDict

#-------Part4----------- 
def get_genre_rating(genre,genreMovieDict,movieAvgRatingDict):
    '''
    Function calculates rating of the given genre
    Take the average of sorted average ratings for movies in the genre 
    returns an average rating value for the genre.
    '''
    genreRating = {}
    for i in genreMovieDict[genre]:
        if i in movieAvgRatingDict.keys():
            genreRating[i] = movieAvgRatingDict[i]
    sortedgenreRating = sorted(genreRating.items(),key=lambda rating: rating[1],reverse=True)   
    valueSum = 0
    for i in range(len(sortedgenreRating)):
        valueSum += sortedgenreRating[i][1]
    average = valueSum/len(sortedgenreRating) 
    average = float("%.2f" % round(average, 2))
    return average

#-------Part5----------- 
def genre_popularity(genreMovieDict,movieAverageRating,n=5):
    '''
    Function compares the users movie to the movies of the genre
    the get rids of the movies already watched by user and return the
    movie list based on the movie average in sorted order.
    '''
    genrePopularity = {}
    for genre in genreMovieDict.keys():
        average = get_genre_rating(genre,genreMovieDict,movieAverageRating)
        genrePopularity[genre] = average  
    sortedGenrePopularity = sorted(genrePopularity.items(),key=lambda rating: rating[1],reverse=True)
    genrePopularity = dict(sortedGenrePopularity[0:n])
    return genrePopularity

#-------------------TASK4-------------------------
#-------Part1-----------

def read_user_ratings(ratingFile):
    '''
    Creates a Dictionary with userID as key and list of movie name and rating as the key.
    '''
    userToMovies = defaultdict(list)
    for line in open(ratingFile):
        movie, rating, userID = line.split('|')
        userToMovies[userID.strip()].append((movie,float(rating.strip())))
    return userToMovies

#-------Part2-----------
def get_user_genre(userID,userMovies,movieGenreDict):
    '''
    Gets the user Genre by comparing the user movies and ratings to movies and average for the movie 
    then choose max from dictionary to print out the genre with highest avgerage rating by the user.
    '''
    userGenreDict = defaultdict(list)
    avgDict = {}
    userList =  userMovies[userID]
    for i in userList:
        movie, rating = i
        moviegenre = movieGenreDict[movie]
        userGenreDict[moviegenre].append(rating)
        for valList in userGenreDict.values():
            average = sum(valList)/len(valList)
            avgDict[moviegenre] = round(average,2)
    return max(avgDict)
    
#-------Part3-----------
def recommend_movies(userID,usertomovies, moviegenre,movieavgrating):
    '''
    User movies are compared to the genre movies. The movies which are common are removed from 
    genre movies. The dictionary is sorted and movies not watch by user in the genre are returned.
    '''
    genreMovies = defaultdict(list)
    userMovies = defaultdict(list)
    userGenre = get_user_genre(userID,usertomovies,moviegenre)
    for movie, genre in moviegenre.items():
        if userGenre == genre:
            genreMovies[genre].append(movie) #create genre movie dictionary
    for userNum,movies in usertomovies.items():
        if userNum == userID:
            userMovies[userNum].append([m[0] for m in movies])#created a user movie and rating dictionary
    gm = genreMovies.get(userGenre)
    um = userMovies.get(userID)
    res = [''.join(ele) for ele in gm] 
    for m in um[0]:
        if m in res:
            res.remove(m)
    result ={}
    for m in res:
        result[m]= movieavgrating[m]
    sortedRes = sorted(result.items(),key=lambda rating: rating[1],reverse=True)
    recMovieAverageDict = dict(sortedRes[0:4])      
    return recMovieAverageDict
