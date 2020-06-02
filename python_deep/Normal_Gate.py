def theta_con(w1,w2,theta,tmp):
  if(tmp > theta):
    print("("+str(w1)+","+str(w2)+","+str(theta)+")");
    print("1 print");
    print("");
  #else:
    #print("("+str(w1)+","+str(w2)+","+str(theta)+")");
    #print("0 print");
    #print("");
  

def AND_var_search(x1,x2):
  print("<"+str(int(x1))+","+str(int(x2))+">");
  w1 = 0.1;
  w2 = 0.1;
  theta = 0.1;
  for i in range(1,10):
    w1 = i/10;
    for j in range(1,10):
      w2 = j/10;
      for k in range(1,10):
        theta = k/10;
        tmp = x1*w1 + x2*w2;
        theta_con(w1,w2,theta,tmp);
  print("");

print("start");
AND_var_search(0.0,1.0);
print("finish");
