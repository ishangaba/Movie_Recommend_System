# Movie_Recommend_System

Description:
The project is divided into 4 parts:
Task1: Reading Data
Task2: Processing Data
Tasks: Recomendation
Task4: User Focused Results

The data is provided in the two input files:
File1: movieRatings.txt
Ratings file: A text file that contains movie ratings. Each line has the name (with year) of a movie, its rating (range 0-5 inclusive), and the id of the user who rated the movie. A movie can have multiple ratings from different users. A user can rate a particular movie only once. A user can however rate multiple movies
File2: genreMovie.txt
Movies file: A text file that contains the genres of movies. Each line has a genre, a movie id, and the name (with year) of the movie. To keep it simple, each movie belongs to a single genre

Methods are designed as per each Task:

Task1:
1.1 The fucntion to display the dictionary containing the Movie name and its ratings as a list as value to the key.

1.2 The function is returning a dictinary containing movie name as key and genre as its value.

Task2:
2.1 The function is creating a dictionary with genre as the key and movie names as the list of movie belonging to that genre.

2.2 The function is creating a dictionary with movie name as key and average rating for the movie as the key. Average is computed using the dictionary created in part 1.

Task3:
3.1 A function to return the top 10 or less popular movies based on their average rating from top to bottom.

3.2 A function to return only the movies which have the rating higher than a certain threshold limit.

3.3 A function to return the top n movies for the given genre. Only the movies which are above the threshold limit in the above problem. The function would display a defualt of top 5 or else whatever mentioned in the function call.

3.4 A function to calculate the rating of a specific genre by calculating the average of the average rating of the movies in the given genre.

3.5 A function to return the top n rated genres. For this method the output from the problem above can be manipulated easily.

Task4:

4.1 A function creating a dictionary of user rated movies, with userID as key and a list of tuples containing the movie and rating as the key.

4.2 The function determines the genre of the user by taking the genre average for the user by calculating it using the ratings given for movies for each genre.

4.3 A function to recommend movies from users top genre, the movies which the user have not yet watched(no rated by the user).
