o = 1
num = int(input("numero: "))
b = num*2
    
for i in range(num):
    
  print(" "*b,"*"*o,)
  o=o+2
  b=b-1
  
for c in range(round(num/7)+1):
 print(" "*b*2,"|"*round(num/10+1))