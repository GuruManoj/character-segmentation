import cv2
import numpy as np

img = cv2.imread("/home/guru/Desktop/work/projects/chacter_segmentation/5.jpg",0)
ret,res = cv2.threshold(img,5,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
a= res.shape
print(a)
x=[]
for i in range(a[1]):
  for j in range(a[0]):
  	if res[j][i] == 255:
  	  break;
  else:
    x.append(i)
print(x)
res = np.array(res)
im=[]
for i in range(len(x)-1):
  b = res[0:29, x[i]:x[i+1]]
  if np.any(b==255):
    im.append(b)
cv2.imshow("img",img)
cv2.imshow("res",res)
for i,j in enumerate(im):
  cv2.imshow(str(i),j)
  cv2.imwrite("./1%s.jpg"%i,j)
cv2.waitKey()