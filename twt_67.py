for I in[I:=input]*int(I()):
 for m in I().split():
  if len(m)==17 and len(M:=m.split('-'))==6:
   try:[int(v,16)for v in M];print(m)
   except:pass
