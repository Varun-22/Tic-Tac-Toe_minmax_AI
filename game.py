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
