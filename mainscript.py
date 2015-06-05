#!/usr/bin/env python
import os
import sys
loc = sys.argv[0] 
s1path = os.path.join(loc,'s1.py')
f1 = open("s1.py","w+")
f1.write("#!/usr/bin/env python\n") 
f1.write("import MySQLdb\n")
f1.write("mydb = MySQLdb.connect(host=\"localhost\", user=\"root\", passwd=\"opennow\")\n")
f1.write("cursor = mydb.cursor()\n"); 

f1.write("cursor.execute(\"CREATE DATABASE IF NOT EXISTS delta\")\n")
f1.write("cursor.execute(\"USE delta\n") 
f1.write("cursor.execute(\"CREATE TABLE IF NOT EXISTS time (currenttime char(20))\")\n")

os.system("python s1.py") 
f1.close()



s2path = os.path.join(loc,'s2.py')
f2 = open("s2.py","w+")
f2.write("#!usr/bin/env python\n")
f2.write("import MySQLdb\n")
f2.write("mydb = MySQLdb.connect(host=\"localhost\", user=\"root\",passwd=\"opennow\")\n")
f2.write("cursor = mydb.cursor()\n")
f2.write("import datetime\n") 
f2.write("cursor.execute(\"USE delta\n")
f2.write("cursor.execute(\"INSERT INTO time VALUES(CURTIME())\")\n") 
f2.write("mydb.commit()\n") 
f2.close()


from crontab import CronTab
user_cron = CronTab(user='keerthana96')



cmd = '/usr/bin/env python s2.py' 


job = user_cron.new(command=cmd)
job.minute.every(10)
user_cron.write()
print user_cron.render()
 








 






