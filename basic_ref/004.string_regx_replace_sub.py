import re


'''
.   Matches any character 
*   0 or more times
+   1 or more times
\d  digit (Capital will be non digit)
\w  word (Capital will be non word)
\s  whitespace (Capital will be non whitespace)
\b  boundry (Capital will be non boundry)

'''


str='''
This is test
Jan-01-2018
Feb-10-2018 
Mar-25-2018 
this is test
'''


regx=re.compile(r'(\w+)-(\d{2})-(\d{4})')
replaced=regx.sub(r'\2-\1 -\3',str)
print(replaced)

'''
This is test
01-Jan -2018
10-Feb -2018 
25-Mar -2018 
this is test
'''

replaced=regx.sub(r'',str)
print(replaced)
'''
This is test

 
 
this is test
'''

print(replaced.replace("\n",""))
#This is test  this is test