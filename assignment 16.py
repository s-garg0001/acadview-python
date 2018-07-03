#question
import sqlite3
a=sqlite3.connect('test.db')
a.execute(''' CREATE TABLE BOOKS
 (  BOOK_ID  INT  PRIMARY KEY  NOT NULL,

    TITLE_ID INT               NOT NULL,

    LOCATION CHAR(50)             NOT NULL,

    GENRE    CHAR(50)             NOT NULL)''')

a.execute('''CREATE TABLE Titles
 (   Titles_ID      CHAR      NOT NULL,

    Title         CHAR                  NOT NULL,

    ISBN          CHAR(50)              NOT NULL,

    Publisher_ID  INT        NOT NULL,

    Publication_Year     CHAR(50))''')

a.execute('''CREATE TABLE Publishers
   ( Publishers_ID      CHAR       NOT NULL,

    Name              CHAR(50)             NOT NULL,

    Street_Address    CHAR(50)             NOT NULL,

    Zip_Code_ID       INT      NOT NULL)''')

a.execute('''CREATE TABLE Zip_Codes
  (  Zip_Codes_ID      CHAR       NOT NULL,

    City             CHAR(50)             NOT NULL,

    State            CHAR(50)             NOT NULL,

    Zip_Code         CHAR(50)             NOT NULL)''')

a.execute('''CREATE TABLE Authors_Titles
  (  Author_Title_ID      INT       NOT NULL,

    Author_ID            INT       NOT NULL,

    Title_ID             INT              NOT NULL)''')

a.execute('''CREATE TABLE Authors
 (   Authors_ID      CHAR      NOT NULL,

    First_Name     CHAR(50)             NOT NULL,

    Middle_Name     CHAR(50),

    Last_Name        CHAR(50)             NOT NULL)''')

print("tables created")

a.execute("INSERT INTO BOOKS(Book_ID,Title_ID,Location,Genre) VALUES(1,20,'kaithal','Shubham')")
a.execute("INSERT INTO BOOKS(Book_ID,Title_ID,Location,Genre) VALUES(1,25,'kurukshetra','Raman')")
a.execute("INSERT INTO Titles(Titles_ID,Title,ISBN,Publisher_ID,Publication_Year) VALUES('1','acadview python','432-5452-344',1453,'2018')")
a.execute("INSERT INTO Titles(Titles_ID,Title,ISBN,Publisher_ID,Publication_Year) VALUES('1','acadview machine learning','342-5343-346',1233,'2018')")
a.execute("INSERT INTO Publishers(Publishers_ID, Name,Street_Address,Zip_Code_ID) VALUES('432-5452-344','Shubham Garg','Kaithal',403106)")
a.execute("INSERT INTO Publishers(Publishers_ID, Name,Street_Address,Zip_Code_ID) VALUES('342-5343-346','Raman','Kuruksshetra',110012)")
a.execute("INSERT INTO Zip_Codes(Zip_Codes_ID,City,State,Zip_Code) VALUES('403106','Kaithal','Delhi','123')")
a.execute("INSERT INTO Zip_Codes(Zip_Codes_ID,City,State,Zip_Code) VALUES('110012','Kaithal','Delhi','123')")
a.execute("INSERT INTO Authors_Titles(Author_Title_ID ,Author_ID ,Title_ID) VALUES(1,2345,344-433-3435)")
a.execute("INSERT INTO Authors_Titles(Author_Title_ID ,Author_ID ,Title_ID) VALUES(2,3242,354-435-4535)")
a.execute("INSERT INTO Authors(Authors_ID,First_Name,Middle_Name,Last_Name) VALUES('1','Mr.','Shubham','Garg')")
a.execute("INSERT INTO Authors(Authors_ID,First_Name,Middle_Name,Last_Name) VALUES('2','Mr.','Raman','Sharma')")
a.commit()

print("BEFORE UPDATION")
b=a.execute("SELECT Book_ID,Title_ID,Location,Genre from Books")
for B in b:
    print("Book_ID:%s,\tTitle_ID:%s,\tLocation:%s,\tGenre:%s"%(B[0],B[1],B[2],B[3]))
c=a.execute("SELECT Titles_ID,Title,ISBN,Publisher_ID,Publication_Year from Titles")
for C in c:
    print("Titles_ID:%s,Title:%s,ISBN:%s,Publisher_ID:%s,Publication_Year:%s"%(C[0],C[1],C[2],C[3],C[4]))
d=a.execute("SELECT Publishers_ID, Name,Street_Address,Zip_Code_ID from Publishers")
for D in d:
    print("Publishers_ID:%s\t, Name:%s\t,Street_Address:%s\t,Zip_Code_ID:%s"%(D[0],D[1],D[2],D[3]))
e=a.execute("SELECT Zip_Codes_ID,City,State,Zip_Code from Zip_Codes")
for E in e:
    print("Zip_Codes_ID:%s\t,City:%s\t,State:%s\t,Zip_Code:%s\t"%(E[0],E[1],E[2],E[3]))
f=a.execute("SELECT Author_Title_ID ,Author_ID ,Title_ID from Authors_Titles")
for F in f:
    print("Author_Title_ID:%s\t,Author_ID:%s\t,Title_ID:%s"%(F[0],F[1],F[2]))
g=a.execute("SELECT Authors_ID,First_Name,Middle_Name,Last_Name from Authors")
for G in g:
    print("Authors_ID:%s\t,First_Name:%s\t,Middle_Name:%s\t,Last_Name:%s"%(G[0],G[1],G[2],G[3]))
a.execute("UPDATE Books set Title_ID=2 where Genre='Aman'")
a.execute("UPDATE Authors set Authors_ID=2 where Middle_Name='Aman'")
a.commit()
print("AFTER UPDATION")
b=a.execute("SELECT Book_ID,Title_ID,Location,Genre from Books")
for B in b:
    print("Book_ID:%s,\tTitle_ID:%s,\tLocation:%s,\tGenre:%s"%(B[0],B[1],B[2],B[3]))
c=a.execute("SELECT Titles_ID,Title,ISBN,Publisher_ID,Publication_Year from Titles")
for C in c:
    print("Titles_ID:%s,Title:%s,ISBN:%s,Publisher_ID:%s,Publication_Year:%s"%(C[0],C[1],C[2],C[3],C[4]))
d=a.execute("SELECT Publishers_ID, Name,Street_Address,Zip_Code_ID from Publishers")
for D in d:
    print("Publishers_ID:%s\t, Name:%s\t,Street_Address:%s\t,Zip_Code_ID:%s"%(D[0],D[1],D[2],D[3]))
e=a.execute("SELECT Zip_Codes_ID,City,State,Zip_Code from Zip_Codes")
for E in e:
    print("Zip_Codes_ID:%s\t,City:%s\t,State:%s\t,Zip_Code:%s\t"%(E[0],E[1],E[2],E[3]))
f=a.execute("SELECT Author_Title_ID ,Author_ID ,Title_ID from Authors_Titles")
for F in f:
    print("Author_Title_ID:%s\t,Author_ID:%s\t,Title_ID:%s"%(F[0],F[1],F[2]))
g=a.execute("SELECT Authors_ID,First_Name,Middle_Name,Last_Name from Authors")
for G in g:
    print("Authors_ID:%s\t,First_Name:%s\t,Middle_Name:%s\t,Last_Name:%s"%(G[0],G[1],G[2],G[3]))#1. Create a database. Create the following tables:
##1. Book
##2. Titles
##3. Publishers
##4. Zipcodes
##5. AuthorsTitles
##6. Authors
