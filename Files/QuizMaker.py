#Quiz maker
import random

print ("This is a quiz. Answer the questions correctly, or die.")

q_db= open ("Quiz.txt")
print (type(q_db.read))
q_db.seek(0)
data = q_db.read()

q_db.close()

print (data)#with removed *@

#"""Todo list:
#Data structure stuff
#questionx.answers or questionx.true/false
#Then use file data to continue
#check templateParser.py