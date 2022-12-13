
text = 'Дана abcd'
def shifr(w):
    if(len(w) >= 4):
        w = ''.join((w[1],w[0],w[3],w[2],w[4:]))
    return w
    
 
words = text.split()
result = ' '.join(map(f, words))
 
print(result)
#def ko1(s):
 #   for i, e in enumerate(s):
  ##         print(e, end=' ')
#def ko(s):
 #   for l, o in enumerate(s):
  #      if l % 4 != 0:
   #         print(o, end=' ')       

#ko(s)