import cv2

cascade = cv2.CascadeClassifier("cascade.xml")
cap = cv2.VideoCapture('./sample.mp4')

if not cap.isOpened():
    print("カメラが正常ではありません")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("画像を正しく読み込めませんでした")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lists = cascade.detectMultiScale(frame_gray, minSize=(50, 50))

    for (x,y,w,h) in lists:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)

    cv2.imshow('video image', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()