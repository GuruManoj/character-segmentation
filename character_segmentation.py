import cv2
import numpy as np

img = cv2.imread("/home/guru/Desktop/work/projects/chacter_segmentation/9.JPG",0)
ret,res = cv2.threshold(img,0,255,cv2.THRESH_OTSU+cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV)
a= res.shape
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
  if np.any(b==255):
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
      for q in range(sh[0]):
        unique,cou = np.unique(i[:,p], return_counts=True)
        ct  = dict(zip(unique,cou))
        try:
          if ct[255]<2:
            if p>2:
              b = i[0:sh[0]-1, 0:p]
              im[j]=b
              if sh[1]-p>2:
                b = i[0:sh[0]-1, p:sh[1]-1]
                im.insert(j+1,b)
                print(b)
            elif p<=2:
              if len(i)-p>2:
                b = i[0:sh[0]-1, p:sh[1]]
                im[j]=b
          break
        except KeyError:
          pass
cv2.imshow("img",img)
cv2.imshow("res",res)
for i,j in enumerate(im):
  cv2.imshow(str(i),j)
cv2.waitKey()