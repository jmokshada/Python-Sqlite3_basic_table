# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 18:33:33 2021

@author: dell
"""

import  sqlite3
conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()

#create the movies table 
cursor.execute("CREATE TABLE if not exists movies(movie_name char(50), actor_name char(50), actress_name char(50), release_year n(4), director_name char(50))")

m_name = input('Movie Name:')
a_name = input('Actor Name:')
as_name = input('Actress Name:')
r_year = input('Release Year:')
d_name = input('Director Name:')

cursor.execute("""
INSERT INTO movies(movie_name, actor_name, actress_name, release_year, director_name)
VALUES (?,?,?,?,?)
""", (m_name, a_name, as_name, r_year, d_name))
conn.commit ()
print ( 'Data entered successfully.' )

#retriving data from movies table
c = cursor.execute("SELECT * from movies")

for row in c:
    print ("Movie Name = ", row[0])
    print ("Actor Name = ", row[1])
    print ("Actress Name = ", row[2])
    print("Release Year = ", row[3])
    print ("Director Name = ", row[4], "\n")
    
conn . close ()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")
