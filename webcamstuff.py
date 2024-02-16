import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.IsOpened():
  print("404:Webcam not found")
  break


while True:
  ret,frame = cap.read()

  if not ret:
    print("No Capture")
    break

  cap.imshow(frame)

  if cv.waitKey(1) == ord("q")
    break


cv.release()
cv.destroyAllWindows()


