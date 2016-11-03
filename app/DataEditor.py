import sqlite3

""" for make table and input manual data """

conn = sqlite3.connect('Data.db') #connect db name Data.db
print "Connect : pass"
c= conn.cursor()    #prepare from modify db


# create table name user
try :
    c.executescript("""
    CREATE TABLE `User` (
      `ID` bigint(20) NOT NULL,
      `Password` varchar(45) NOT NULL,
      `Title` varchar(45) DEFAULT NULL,
      `Name` varchar(45) DEFAULT NULL,
      `Surname` varchar(45) DEFAULT NULL,
      `E-mail` varchar(45) DEFAULT NULL,
      `Role` varchar(45) DEFAULT NULL,
      `Faculty` varchar(45) DEFAULT NULL,
      `Major` varchar(45) DEFAULT NULL,
      `Enro-Yearl` varchar(45) DEFAULT NULL,
      `Picture` varchar(45) DEFAULT NULL
    )""")
except Exception:
    print "Table User has created"


# create table name Enrol
try :
    c.executescript("""CREATE TABLE `Enrol` (
      `ID` bigint(11) NOT NULL,
      `Subject_ID` varchar(45) NOT NULL,
      `subject_Year` int(11) NOT NULL
    )""")
except Exception:
    print "Table Enrol has created"


# create table name Group
try:
    c.executescript("""
    CREATE TABLE `Group` (
      `Subject_ID` varchar(45) NOT NULL,
      `Year` int(11) NOT NULL,
      `WorkID` int(11) NOT NULL,
      `ID` bigint(11) NOT NULL
    )""")
except Exception:
    print "Table group has created"


# create table name media
try :
    c.executescript("""
    CREATE TABLE `media` (
      `Subject_ID` varchar(45) NOT NULL,
      `Year` int(11) NOT NULL,
      `File_name` varchar(45) DEFAULT NULL,
      `time` varchar(45) DEFAULT NULL,
      `address` varchar(45) DEFAULT NULL,
      `ID` bigint(45) DEFAULT NULL
    )""")
except Exception:
    print "Table media has created"


#create table name subject
try:
    c.executescript("""
    CREATE TABLE `subject` (
      `Subject_ID` varchar(45) NOT NULL,
      `Year` int(11) NOT NULL,
      `Description` varchar(45) DEFAULT NULL,
      `FullMark` int(11) DEFAULT NULL,
      `Grading` varchar(45) DEFAULT NULL
    )""")
except Exception:
    print "Table Subject has created"


#create table name Submitwork
try:
    c.executescript("""
    CREATE TABLE `SubmitWork` (
      `Subject_ID` varchar(45) NOT NULL,
      `Year` int(11) NOT NULL,
      `WorkID` int(11) NOT NULL,
      `ID` bigint(20) NOT NULL,
      `Address` varchar(45) DEFAULT NULL,
      `Status` varchar(45) DEFAULT NULL,
      `Mark` varchar(45) DEFAULT NULL
    )""")
except Exception:
    print "Table Submit work has created"

#create table name work
try :
    c.executescript("""
    CREATE TABLE `work` (
      `Subject_ID` varchar(45) NOT NULL,
      `Year` int(11) NOT NULL,
      `WorkID` int(11) NOT NULL,
      `Deadlines` varchar(45) DEFAULT NULL,
      `status` varchar(45) DEFAULT NULL,
      `type` varchar(45) DEFAULT NULL,
      `FullMark` varchar(45) DEFAULT NULL,
      `Grading` varchar(45) DEFAULT NULL,
      `lim_member` int(11) DEFAULT NULL
    )""")
except Exception:
    print "Table Work has created"


    #insert data in Enrol table
    c.execute("""INSERT INTO `Enrol` (`ID`, `Subject_ID`, `subject_Year`) VALUES
    (58340500017, 'FRA222', 59);""")

    #insert data in subject table
    c.execute("""INSERT INTO `subject` (`Subject_ID`, `Year`, `Description`, `FullMark`, `Grading`) VALUES
    ('FRA222', 59, NULL, 100, NULL);""")

    # insert data in User table
    c.execute("""INSERT INTO `User` (`ID`, `Password`, `Title`, `Name`, `Surname`, `E-mail`, `Role`, `Faculty`, `Major`, `Enro-Yearl`, `Picture`) VALUES
    (58340500017, 'Boomming1*', 'Mr.', 'Chaiyaporn', 'Boonyasathian', 'chaiya45689@gmail.com', 'student', 'FIBO', 'robotic and automation', '58', NULL);
    """)

    #insert data in Work table
    c.execute("""INSERT INTO `work` (`Subject_ID`, `Year`, `WorkID`, `Deadlines`, `status`, `type`, `FullMark`, `Grading`, `lim_member`) VALUES
    ('FRA222', 59, 1, NULL, NULL, NULL, NULL, NULL, NULL);
    """)

conn.commit() #save data into db

cursor1 = c.execute("SELECT ID, Password from User") #choose table for search data
for row in cursor1:
    print "ID = ", row[0]
    print "Password = ", row[1]

cursor2 = c.execute("SELECT ID, Subject_ID from Enrol")
for row in cursor2:
    print "ID = ",row[0]
    print "Subject ID = ",row[1]

cursor1.close()
cursor2.close()