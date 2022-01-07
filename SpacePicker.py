import cv2, pickle

width, height = 110, 45

try:
    with open('ParkedPos','rb') as f:
            posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('ParkedPos','wb') as f:
        pickle.dump(posList, f)

def checkSpace():
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

while True:
    img = cv2.imread('lotsc.png')

    checkSpace()

    cv2.imshow('image',img)
    cv2.setMouseCallback('image', mouseClick)
    cv2.waitKey(1)
    