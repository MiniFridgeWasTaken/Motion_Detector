import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():  #troubleshoot
  print("404:Webcam not found")
  exit()

first_frame = None

while True:
  ret,frame = cap.read() # getting info from webcam
  gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)  # Gray scaling
  gauss_frame = cv.GaussianBlur(gray,(21,21),0)
  blur = cv.blur(gauss_frame,(21,21),0)

  if first_frame is None: 
    first_frame = blur # setting first frame to gray scale frame
    continue

  delta_frame = cv.absdiff(first_frame,blur) #comparing curent frame to first frame
  threshold_frame = cv.threshold(delta_frame,50,255,cv.THRESH_BINARY)[1]
  threshold_frame = cv.dilate(threshold_frame,None,iterations=2)

  

  (cntr,_) = cv.findContours(threshold_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) #using noise for detection
  
  for contour in cntr:  #making sure the noise is not too much or else image is weird
    if cv.contourArea(contour) < 1000:
      continue

    (x,y,w,h) = cv.boundingRect(contour)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)  # drawing a rectangle around the changes

  if not ret:
    print("No Capture")  # troubleshoot
    break

  cv.imshow('Webcam',frame)   # window show webcam


  if cv.waitKey(1) == ord("q"):  # exiting the code
    break


cap.release()
cv.destroyAllWindows()
