# libraries
import random
import copy

# check for winner
def check(trix):
  for i in range(3):
    if(len(set(trix[i]))==1):
      if('X' in set(trix[i])):
        return (1,'X')
      elif('O' in set(trix[i])):
        return (1,'O')
  for i in range(3):
    temp = []
    temp.append(trix[0][i])
    temp.append(trix[1][i])
    temp.append(trix[2][i])
    if(len(set(temp))==1):
      if('X' in set(temp)):
        return (1,'X')
      elif('O' in set(temp)):
        return (1,'O')
  temp = []
  temp.append(trix[0][0])
  temp.append(trix[1][1])
  temp.append(trix[2][2])
  if(len(set(temp))==1):
    if('X' in set(temp)):
      return (1,'X')
    elif('O' in set(temp)):
      return (1,'O')
  temp = []
  temp.append(trix[0][2])
  temp.append(trix[1][1])
  temp.append(trix[2][0])
  if(len(set(temp))==1):
    if('X' in set(temp)):
      return (1,'X')
    elif('O' in set(temp)):
      return (1,'O')
  return (0,0)

# print the matrix
def printmatrix(mat):
  boun = '---------'
  print(boun)
  for i in mat:
    print('|',end = ' ')
    for k in range(3):
      if(i[k]=='_'):
        print(' ',end=' ')
        continue
      print(i[k],end=' ')
    print('|')
  print(boun)

# create matrix
def makemat():
  mat = []
  mov = []
  for i in range(3):
    mat.append([])
    for j in range(3):
      mat[i].append('_')
      mov.append([i+1,j+1])
  return mat,mov

# medium level game
def checkmed(m,x,val):
  for i in x:
    temp = []
    temp.append(3-i[1])
    temp.append(i[0]-1)
    #check rc, for win
    if(temp[0]!=temp[1]):
      r1 = (m[(temp[0]+1)%3][(temp[1])%3] == m[(temp[0]+2)%3][(temp[1])%3]) and (m[(temp[0]+2)%3][(temp[1])%3]==val)
      r2 = (m[(temp[0])%3][(temp[1]+1)%3] == m[(temp[0])%3][(temp[1]+2)%3]) and (m[(temp[0])%3][(temp[1]+2)%3]==val)
      raw = r1 or r2
      if(raw):
        return [x.index(i),'win']
    #check rcd, for win
    elif(temp[0]==temp[1]):
      r1 = (m[(temp[0]+1)%3][(temp[1]+1)%3] == m[(temp[0]+2)%3][(temp[1]+2)%3]) and (m[(temp[0]+2)%3][(temp[1]+2)%3]==val)
      r2 = (m[(temp[0]+1)%3][(temp[1])%3] == m[(temp[0]+2)%3][(temp[1])%3]) and (m[(temp[0]+2)%3][(temp[1])%3]==val)
      r3 = (m[(temp[0])%3][(temp[1]+1)%3] == m[(temp[0])%3][(temp[1]+2)%3]) and (m[(temp[0])%3][(temp[1]+2)%3]==val)
      raw = r1 or r2 or r3
      if(raw):
        return [x.index(i),'win']
  for i in x:
    temp = []
    temp.append(3-i[1])
    temp.append(i[0]-1)
    #check rc, for block
    if(temp[0]!=temp[1]):
      r1 = (m[(temp[0]+1)%3][(temp[1])%3] == m[(temp[0]+2)%3][(temp[1])%3]) and (m[(temp[0]+2)%3][(temp[1])%3]!=val) and (m[(temp[0]+2)%3][(temp[1])%3]!='_')
      r2 = (m[(temp[0])%3][(temp[1]+1)%3] == m[(temp[0])%3][(temp[1]+2)%3]) and (m[(temp[0])%3][(temp[1]+2)%3]!=val) and (m[(temp[0])%3][(temp[1]+2)%3]!='_')
      raw = r1 or r2
      if(raw):
        return [x.index(i),'block']
    #check rcd, for block
    elif(temp[0]==temp[1]):
      r1 = (m[(temp[0]+1)%3][(temp[1]+1)%3] == m[(temp[0]+2)%3][(temp[1]+2)%3]) and (m[(temp[0]+2)%3][(temp[1]+2)%3]!=val) and (m[(temp[0]+2)%3][(temp[1]+2)%3]!='_')
      r2 = (m[(temp[0]+1)%3][(temp[1])%3] == m[(temp[0]+2)%3][(temp[1])%3]) and (m[(temp[0]+2)%3][(temp[1])%3]!=val) and (m[(temp[0]+2)%3][(temp[1])%3]!='_')
      r3 = (m[(temp[0])%3][(temp[1]+1)%3] == m[(temp[0])%3][(temp[1]+2)%3]) and (m[(temp[0])%3][(temp[1]+2)%3]!=val) and (m[(temp[0])%3][(temp[1]+2)%3]!='_')
      raw = r1 or r2 or r3
      if(raw):
        return [x.index(i),'block']    
  return [random.randint(0,len(x)-1),'random']
