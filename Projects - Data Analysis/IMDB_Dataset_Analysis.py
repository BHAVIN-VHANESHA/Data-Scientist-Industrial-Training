import numpy as np  # -> to perform mathematical operations
import pandas as pd  # -> data manipulation tool
import matplotlib.pyplot as plt  # -> data visualization tool
import seaborn as sb  # -> data visualization tool
import sqlite3  # -> server-less database


'''
Hints & Tips
1. Database connection
2. Use the curser function -> database_variable_name.cursor()
'''

'''
workflow
1. Establish connection
2. Create Cursor object
3. Execute query -> cursor_object.execute('query')
4. Fetch data using fetchall() method
'''


# connecting to the database
db = "D:\\Data Scientist Industrial Training\\Datasets\\movie.sqlite"
conn = sqlite3.connect(db)
cur = conn.cursor()
print("Connected to SQLite\n")


''' 1. check numbers of tables
sql_query = """SELECT name FROM sqlite_master
                WHERE type='table';"""
cur.execute(sql_query)
print(f"List of tables: {cur.fetchall()}")
cur.execute("SELECT * FROM sqlite_sequence")
print(f"List of tables with number of rows: {cur.fetchall()}")
# '''


''' 2. get all the data about movies
cur.execute("SELECT * FROM movies")
movies = cur.fetchall()
print(movies)  # raw data

# Use the description keyword of the cursor object to get the column names
column_names = [desc[0] for desc in cur.description]
print(f"movies table column names: {column_names}")

# creating dataframe
df1 = pd.DataFrame(movies, columns=["ID", "Title", "Budget", "Popularity", "Release_Date",
                                    "Revenue", "Name", "Avg_rating", "Total_rating", "Overview",
                                    "Tagline", "UID", "DID"])
print(df1)  # structured data
# '''

# table overview
# print(df1.info())


''' 3. get all the data about directors
cur.execute("SELECT * FROM directors")
directors = cur.fetchall()
print(directors)  # raw data

# Use the description keyword of the cursor object to get the column names
column_names = [desc[0] for desc in cur.description]
print(f"directors table column names: {column_names}")

# creating dataframe
df2 = pd.DataFrame(directors, columns=["Name", "DID", "Gender", "UID", "Department"])
print(df2)  # structured data
# '''

# table overview
# print(df2.info())


''' 4. checking number of movies present in IMDB table
cur.execute("SELECT COUNT(Title) FROM movies")
print(f"total movies: {cur.fetchall()}")
# '''


''' 5. find the directors (James Cameron, Luc Besson, John Woo)
cur.execute("""SELECT * FROM directors WHERE 
                Name in ('James Cameron', 'Luc Besson', 'John Woo')""")
print(f"Details of Directors are: {cur.fetchall()}")
# '''


''' 6. name of all the directors whose name is Steven
cur.execute("""SELECT * FROM directors WHERE
                Name LIKE 'Steven%' """)
print(f"directors having name Steven: {cur.fetchall()}")
# '''


''' 7. count female directors
cur.execute("SELECT COUNT(Gender) FROM directors WHERE Gender is 1")
females = cur.fetchall()
print(f"number of female directors: {females[0][0]}")
# '''


''' 8. names of 10th female director
cur.execute("SELECT Name FROM directors WHERE Gender is 1")
pos_10th = cur.fetchall()
print(pos_10th[9][0])
# '''


''' 9. which are the 3 most popular movies
cur.execute("SELECT Title FROM movies ORDER BY Popularity DESC LIMIT 3")
most_popular = cur.fetchall()
print(f"top 3 movies: {most_popular[0][0]}, {most_popular[1][0]}, {most_popular[2][0]}")
# '''


''' 10. three highest budget movies
cur.execute("SELECT Title FROM movies ORDER BY Budget DESC LIMIT 3")
budget = cur.fetchall()
print(f"three highest budget of movies: {budget[0][0]}, {budget[1][0]}, {budget[2][0]}")
# '''


''' 11. what is the most awarded average vote movie since jan 1st 2000
cur.execute("""SELECT Title FROM movies WHERE Release_Date > '2000-01-01'
                ORDER BY vote_average DESC LIMIT 1""")
best_movie = cur.fetchall()
print(f"most awarded movie is: {best_movie[0][0]}")
# '''


''' 12. movies directed by Brenda Chapman
cur.execute("""SELECT Title FROM movies JOIN directors ON directors.id = movies.director_id
                WHERE directors.name is 'Brenda Chapman' """)
movie_name = cur.fetchall()
print(f"movies directed by Brenda Chapman are: {movie_name[0][0]}")
# '''


''' 13. name the director who made most movies
cur.execute("""SELECT name FROM directors JOIN movies ON directors.id = movies.director_id
                GROUP BY director_id ORDER BY COUNT(name) DESC LIMIT 1""")
director_name = cur.fetchone()
print(f"max movies directed by: {director_name[0]}")
# '''


''' 14. name of director with max budget
cur.execute("""SELECT name FROM directors JOIN movies ON directors.id = movies.director_id
                GROUP BY director_id ORDER BY SUM(budget) DESC """)
director_name = cur.fetchone()
print(f"max movies directed by: {director_name[0]}")
# '''


""" B U D G E T   A N A L Y S I S """
''' 1. top 10 highest budget movie
cur.execute("SELECT * FROM movies ORDER BY budget DESC")
high_budget = cur.fetchmany(10)
df = pd.DataFrame(high_budget, columns=["ID", "Title", "Budget", "Popularity", "Release_Date",
                                        "Revenue", "Name", "Avg_rating", "Total_rating", "Overview",
                                        "Tagline", "UID", "DID"])
print(df)
# '''


""" R E V E N U E   A N A L Y S I S """
''' 1. top 10 highest revenue movie
cur.execute("SELECT * FROM movies ORDER BY revenue DESC")
high_budget = cur.fetchmany(10)
df = pd.DataFrame(high_budget, columns=["ID", "Title", "Budget", "Popularity", "Release_Date",
                                        "Revenue", "Name", "Avg_rating", "Total_rating", "Overview",
                                        "Tagline", "UID", "DID"])
print(df)
# '''


""" V O T I N G   A N A L Y S I S """
''' 1. most popular movie with the highest avg votes
cur.execute("SELECT * FROM movies ORDER BY vote_average DESC")
high_vote = cur.fetchmany(10)
df = pd.DataFrame(high_vote, columns=["ID", "Title", "Budget", "Popularity", "Release_Date",
                                      "Revenue", "Name", "Avg_rating", "Total_rating", "Overview",
                                      "Tagline", "UID", "DID"])
print(df)
# '''


""" D I R E C T O R   A N A L Y S I S """
''' 1. name all the director with the number of movies & highest revenue
cur.execute("""SELECT name, COUNT(*) AS 'total_movies', SUM(revenue) AS 'total_revenue' FROM directors JOIN movies 
                WHERE directors.id = movies.director_id GROUP BY director_id
                ORDER BY SUM(revenue) DESC """)
names = cur.fetchall()
df = pd.DataFrame(names, columns=["name", "total_movies", "total_revenue"])
print(df)
# '''


''' 2. name all the director with the highest number of movies & revenue
cur.execute("""SELECT name, COUNT(title), SUM(revenue) FROM directors JOIN movies 
                ON movies.director_id = directors.id GROUP BY director_id
                ORDER BY COUNT(title) DESC """)
names = cur.fetchall()
df = pd.DataFrame(names, columns=["name", "title", "revenue"])
print(df)
# '''


# ''' 3. title, release_date, budget, revenue, popularity, avg vote of movie made by Steven Spielberg
cur.execute("""SELECT title, release_date, budget, revenue, popularity, vote_average FROM movies 
                JOIN directors ON directors.id = movies.director_id WHERE name is 'Steven Spielberg' """)
names = cur.fetchall()
df = pd.DataFrame(names, columns=["name", "title", "release_date", "budget", "revenue"
                                  "popularity", "vote_average"])
print(df)
# '''
