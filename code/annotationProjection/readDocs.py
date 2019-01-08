import sys

def readDoc(fn,index0=1):
  hh=[]
  hd = {}
  h=[]
  for line in open(fn):
    line = line.strip()
    if line=="":
      if h!=[]: 
        hh.append(h)
        str=" ".join([x[0] for x in h])
        hd[str] = h
      h=[]
    else:
      x = line.split("\t")
      word,label = x[index0],x[-1]
      h.append((word,label))
  if h!=[]:
    hh.append(h)
    str=" ".join([x[0] for x in h])
    hd[str] = h
  return hh,hd
