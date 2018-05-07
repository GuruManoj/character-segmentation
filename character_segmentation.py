import cv2
import numpy as np
#from skimage.filters import threshold_yen
from skimage.filters.thresholding import threshold_yen

img = cv2.imread("/home/guru/Desktop/work/projects/chacter_segmentation/10.jpg",0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cv2.imshow("or",img)
img = clahe.apply(img)
ret,res = cv2.threshold(img,255,255,cv2.THRESH_OTSU+cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV)
#res = threshold_yen(img)
a= res.shape
#print(a)
x=[]
x.append(0)
for i in range(a[1]):
  for j in range(a[0]):
    if res[j][i] == 255:
      break
  else:
    x.append(i)
res = np.array(res)
im=[]
for i in range(len(x)-1):
  b = res[0:a[0]-1, x[i]:x[i+1]]
  if np.any(b==255) and x[i+1]-x[i]>2:
    im.append(b)
for j,i in enumerate(im):
  sh=i.shape
  change=i[sh[0]//2][0]
  count=0
  for value in i[sh[0]//2]:
    if change!=value:
      count+=1
      change=value
  if count>2:
    for p in range(sh[1]):
      #for q in range(sh[0]):
      unique,cou = np.unique(i[:,p], return_counts=True)
      ct  = dict(zip(unique,cou))
      try:
        if ct[255]<2:
          #print(len(im))
          if p>2 :
            #print(p)
            if np.any(i[0:sh[0]-1, 0:p]==255):
              b = i[0:sh[0]-1, 0:p]
              #print(im[j].shape,b.shape)
              im[j]=b
              #print(im[j])
              if sh[1]-p>2:
                if np.any(i[0:sh[0]-1, p:sh[1]-1]==255):
                  b = i[0:sh[0]-1, p:sh[1]-1]
                  im.insert(j+1,b)
              break
      except KeyError:
        pass
for j,i in enumerate(im):
  sh=i.shape
  change=i[sh[0]//2][0]
  count=0
  for value in i[sh[0]//2]:
    if change!=value:
      count+=1
      change=value
  if count>2:
    for p in range(sh[1]):
      index = np.array(np.where(i==255))
      print(index)
      #for ind in index[0]:
      #print(ind)
      '''try:
        if p+1<sh[1]:
          if np.any(i[index[0][0]:index[0][-1]][p+1]==255):
            print(j,index[0][0],index[0][-1],p)
            break
      except IndexError:
        pass
      else:
        try:

          #print(j,p)
          #print(i[5][:])
          if p>2:
            #print(j,p)
            if np.any(i[0:sh[0]-1, 0:p]==255):
              b = i[0:sh[0]-1, 0:p]
              im[j]=b
              if sh[1]-p>2:
                if np.any(i[0:sh[0]-1, p:sh[1]-1]==255):
                  b = i[0:sh[0]-1, p:sh[1]-1]
                  im.insert(j+1,b)
              break
          elif p<=2:
            if len(i)-p>2:
              b = i[0:sh[0]-1, p:sh[1]-1]
              im[j]=b
            break'''
        #except KeyError:
        #  pass
cv2.imshow("img",img)
cv2.imshow("res",res)
for i,j in enumerate(im):
  #if i==0:
  #  print(j[i].shape)
  cv2.imshow(str(i),j)
cv2.waitKey()