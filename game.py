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

# minmax
def minmax(matrix,move,value,win,level):
  res = check(matrix)
  score = 1000
  scorei = 0
  if(res[0]):
    if(res[1]==win):
      return level
    else:
      return -level
  else:
    if(move):
      for i in range(len(move)):
        tmo = copy.deepcopy(move)
        mat = copy.deepcopy(matrix)
        mat[3-move[i][1]][move[i][0]-1] = value
        tmo.pop(i)
        if(value=='X'):
          score = min(score,minmax(mat,tmo,'O',win,level-10))
        else:
          score = min(score,minmax(mat,tmo,'X',win,level-10))
      return score
    else:
      return 0

# hard level game
def checkhard(m,mo,v):
  score = -1000
  scorei = 0
  medres = checkmed(m,mo,v)
  if(medres[1]=='block' or medres[1]=='win'):
    return medres[0]
  for i in range(len(mo)):
    tm = copy.deepcopy(mo)
    mt = copy.deepcopy(m)
    tm.pop(i)
    mt[3-mo[i][1]][mo[i][0]-1] = v
    if(v=='X'):
      a = minmax(mt,tm,'O',v,100)
      if(a>=score):
        scorei = i
        score = a
    else:
      a = minmax(mt,tm,'X',v,100)
      if(a>=score):
        scorei = i
        score = a
  return scorei

# the game
def game(plr):
  mat,mov = makemat()
  #random.shuffle(mov)
  printmatrix(mat)
  curr = 0
  while(curr<10):
    if(curr%2==0):
      if(plr[0]=='user'):
        try:
          x,y = list(map(int,input('Enter the coordinates: ').split()))
        except Exception:
          print('You should enter numbers!')
          continue
        if(x>3 or y>3 or x<1 or y<1):
          print('Coordinates should be from 1 to 3!')
          continue
        elif(mat[3-y][x-1]!='_'):
          print('This cell is occupied! Choose another one!')
          continue
        else:
          mat[3-y][x-1] = 'X'
          mov.pop(mov.index([x,y]))
          curr+=1
      elif(plr[0]=='easy'):
        print('Making move level "easy"')
        ind = random.randint(0,len(mov)-1)
        move = mov[ind]
        mat[3-move[1]][move[0]-1] = 'X'
        mov.pop(ind)
        curr+=1
      elif(plr[0]=='medium'):
        print('Making move level "medium"')
        ind = checkmed(mat,mov,'X')
        move = mov[ind[0]]
        mat[3-move[1]][move[0]-1] = 'X'
        mov.pop(ind[0])
        curr+=1
      elif(plr[0]=='hard'):
        print('Making move level "hard"')
        ind = checkhard(mat,mov,'X')
        move = mov[ind]
        mat[3-move[1]][move[0]-1] = 'X'
        mov.pop(ind)
        curr+=1
    else:
      if(plr[1]=='user'):
        try:
          x,y = list(map(int,input('Enter the coordinates: ').split()))
        except Exception:
          print('You should enter numbers!')
          continue
        if(x>3 or y>3 or x<1 or y<1):
          print('Coordinates should be from 1 to 3!')
          continue
        elif(mat[3-y][x-1]!='_'):
          print('This cell is occupied! Choose another one!')
          continue
        else:
          mat[3-y][x-1] = 'O'
          mov.pop(mov.index([x,y]))
          curr+=1
      elif(plr[1]=='easy'):
        print('Making move level "easy"')
        ind = random.randint(0,len(mov)-1)
        move = mov[ind]
        mat[3-move[1]][move[0]-1] = 'O'
        mov.pop(ind)
        curr+=1
      elif(plr[1]=='medium'):
        print('Making move level "medium"')
        ind = checkmed(mat,mov,'O')
        move = mov[ind[0]]
        mat[3-move[1]][move[0]-1] = 'O'
        mov.pop(ind[0])
        curr+=1
      elif(plr[1]=='hard'):
        print('Making move level "hard"')
        ind = checkhard(mat,mov,'O')
        move = mov[ind]
        mat[3-move[1]][move[0]-1] = 'O'
        mov.pop(ind)
        curr+=1
    printmatrix(mat)
    #  check result
    winner = check(mat)
    if(winner[0]):
      print(winner[1],'wins')
      break
    if(9-curr == 0):
      print('Draw')
      break

# driver
while(True):
  b2 = ['easy','user','medium','hard']
  a = input('Input command: ').split()
  if(len(a)==1 and a[0]=='exit'):
    break
  if(len(a)!=3):
    print('Bad parameters!')
  elif(a[0]=='start' and a[1] in b2 and a[2] in b2):
    game(a[1:])
  else:
    print('Bad parameters!')
