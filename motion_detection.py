import cv2
import numpy as np


# Capture 3 frames and capture the difference
def diffimg(a,b,c):
	t0= cv2.absdiff(a,b)
	t1 = cv2.absdiff(b,c)
	t3 = cv2.bitwise_and(t0,t1)
	return t3

cap=cv2.VideoCapture(0)
t=cap.read()[1]
tp=cap.read()[1]
tpp = cap.read()[1]

t = cv2.cvtColor(t, cv2.COLOR_BGR2GRAY)
tp = cv2.cvtColor(tp, cv2.COLOR_BGR2GRAY)
tpp = cv2.cvtColor(tpp, cv2.COLOR_BGR2GRAY)

while True:
	img = diffimg(t,tp,tpp)
	cv2.imshow('output',img)
	ret, img=cap.read()
	t=tp
	tp=tpp
	tpp=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# img2 =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('grayscale', img2)
	# imgthreshold = cv2.inRange(img, cv2.cv.Scalar(3,3,125), cv2.cv.Scalar(40,40,255))
	# cv2.imshow('imgthreshold', imgthreshold)

	k=cv2.waitKey(10)
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()