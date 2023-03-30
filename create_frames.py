import cv2

vidcap = cv2.VideoCapture('nature.mp4')
success, image = vidcap.read()
count = 0
while success:
    print(count)
    cv2.imwrite(f'C:/Users/rwbak/Documents/GitHub/389-final-project/frames/frame{count}.jpg',image)
    success, image = vidcap.read()
    count+=1