#MUST BE RUN USING 2.x NOT 3.x

from string import maketrans

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab,outtab)

str = "map"
print str.translate(trantab)
