import cv2

data = cv2.VideoCapture('./sample.mp4')
type(data)
data.isOpened()

while True:
    ret, frame = data.read()
    key = input()
    if key == "q":
        cv2.destroyWindow('sample data')
    elif ret:
        cv2.imshow('sample data', frame)
        cv2.waitKey(1)
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)
        cv2.destroyWindow('sample data')
        