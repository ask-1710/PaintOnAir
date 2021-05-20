import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 320)
cap.set(10, 500)

# Use Object detection code to get the trackbar values for each color -> adjust trackbars
# until only your color turns black
# orange -- black -- green -> order of colors
myColors = [[0, 178, 111, 20, 255, 255],
            [63, 51, 0, 174, 239, 87],
            [38, 133, 47, 80, 255, 255]]

#  obtain BGR values for orange, black, green from websites like ' www.cloford.com/resources/colours/500col.htm '
myColorValues = [[31, 90, 255], [0, 0, 0], [46, 255, 60]]

myPoints = []  # [x,y,color id]


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 6, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])

        count += 1
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, z = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            per1 = cv2.arcLength(cnt, True)
            approx = (cv2.approxPolyDP(cnt, 0.02 * per1, True))
            x, y, w, z = cv2.boundingRect(approx)
    return x + w // 2, y  # returning centre


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 6, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    #  myPoints is used to retain the paint of every iteration

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("Modern Art", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
