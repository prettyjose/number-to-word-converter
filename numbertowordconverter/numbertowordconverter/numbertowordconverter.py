#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#this will print 123456123 as
#123 456 123 = one hundred and twenty three million, four hundred and fifty six thousand, one hundred and twenty three

# numbers[0-9], ',' and ' ' are allowed in input
# all others will give invalid input error message

from re import sub as re_sub_func
from math import ceil

import numberdictionaries

class Number:
 def __init__(self, inNum, inSign=''):
  self.number = int(inNum)
  self.sign = inSign
  
 def getNumber(self):
  return self.number
  
 def getSign(self):
  return self.sign
  
 def get_sign_in_word(self):
  if self.sign=='-':
   return 'negative '
  elif self.sign=='+':
   return 'positive ' 
  else:
   return ''
    
 def get_formatted_number(self):
  #To format input, 54321 as 54 321
    number = self.getNumber()
    inStr = str(number)
    leng=len(inStr)
    formatedstr = ''
    subwordlen=-3
    strarr=[]
    
    #getting groups of 1000s
    strarr.append(inStr[-3:])
    for i in range(subwordlen,leng*-1,subwordlen ):
        strarr.append(inStr[i+subwordlen:i])
    
    #stylising
    leng=len(strarr)
    for i in range(leng-1, -1, -1):
        formatedstr = formatedstr + strarr[i] + ' '
    formatedstr = formatedstr[:-1]
    formatedstr = self.getSign()+ formatedstr
        
    return formatedstr
  
 def get_word_rep(self):
    in_str = str(self.number)
    num = self.number
   
    if '0' == in_str:
        return 'zero'
       
    leng = len(in_str)
    grpcount = ceil(leng/3)
    str_arr=[]
    for i in range(grpcount):
        str_arr.append(num%1000)
        num//=1000
    
    leng=len(str_arr)
    l=[]
    for i in range(leng-1, -1, -1):
        #processing groups of thousands
        number=int(str_arr[i])
        
        #654,321-->third=6,second=5,first=4 in 1st iteration, and
        #third=3,second=2,first=1 in 2nd iteration
        third=number//100
        if l and l[-1] != ',':#to avoid more than one comma
            l.append(',')
        if third>0:
            l.append(' '+numberdictionaries.dicSingles[third])
            l.append (' '+numberdictionaries.dic[0])
            numberstr=str(str_arr[i])[1:]
            number=int(numberstr)
        
        second=number/10
        first= 0
        if second>=2.0:
            second=int(second)
            first=int(number %10)
            if third>0:
                l.append(' and')
            l.append(' '+numberdictionaries.dicTens[second])
            if first >0:
                l.append (' '+numberdictionaries.dicSingles [first])
        elif second>=1:
            second=number
            if third>0:
                l.append(' and')
            l.append(' '+numberdictionaries.dicTeens[second])
        elif second>0:
            first=int(number %10)
            if third>0:
                l.append(' and')
            if first >0:
                l.append (' '+numberdictionaries.dicSingles [first])
    
        # To add thousand, million,billion, .etc.
        if (third>0 or second>0 or first >0) and i>0:
            l.append (' '+numberdictionaries.dic[i])
    
    #To remove comma or space, if any, at ends
    if l: 
        l[0] = l[0].lstrip(' ')
        if l[-1] is ',':
          del l[-1]
        
    #Forming the output string
    word=''.join(l)
    word = self.get_sign_in_word() + word 

    return word
    
 @staticmethod
 def isANumber(str):
  try:
   int(str)
   return True
  except ValueError:
   return False

def convertToWord(inStr):
 try:
    inStr=re_sub_func('[,\s]','',inStr)
    
    if Number.isANumber(inStr) == False:
     return '\ninvalid input'

    if inStr[0] in {'+','-'}:
     candidate = Number(inStr[1:],inStr[0])
    else:
     candidate = Number(inStr)
    return '\n{} = {}'.format(candidate.get_formatted_number(), candidate.get_word_rep())
 except ValueError:
    return '\ninvalid input'
 except:   
    print('\nAn error occured.')
    raise

print('\nmodule name :::: ',__name__)
if __name__=="__main__":
 print('hi there, pal. thx for cmg in person')
else:
 print('hi! thx fr sending yur representative')