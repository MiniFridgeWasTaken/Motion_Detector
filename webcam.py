import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
  print("404:Webcam not found")
  exit()

first_frame = None

while True:
  ret,frame = cap.read()
  gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
  gray = cv.GaussianBlur(gray,(21,21),0)

  if first_frame is None:
    first_frame = gray
    continue

  delta_frame = cv.absdiff(first_frame,gray)
  threshold_frame = cv.threshold(delta_frame,50,255,cv.THRESH_BINARY)[1]
  threshold_frame = cv.dilate(threshold_frame,None,iterations=5)

  (cntr,_) = cv.findContours(threshold_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
  
  for contour in cntr:
    if cv.contourArea(contour) < 1000:
      continue

    (x,y,w,h) = cv.boundingRect(contour)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

  if not ret:
    print("No Capture")
    break

  cv.imshow('Webcam',frame)


  if cv.waitKey(1) == ord("q"):
    break


cap.release()
cv.destroyAllWindows()
