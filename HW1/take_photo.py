import cv2

def cap_num(max:int=5) -> list[int]:
    """
    Get camera number.

    # Example
    ```
    N = cap_num()
    print(N)
    cap = cv2.VideoCapture(N[0])
    print(cap.isOpened())
    ```
    """
    _ = []
    for n in range(max):
        cap = cv2.VideoCapture(0,n)
        ret, frame = cap.read()
        if ret: _.append(n)
    return _
        
N = cap_num()
cap = cv2.VideoCapture(N[0])

i = 0
while cap.isOpened():    # https://www.codegrepper.com/code-examples/python/cv2+cap.isOpened

    ret, frame = cap.read()  # returned value of ret is either True (successful) or False (failed). frame: captured image frames
    
    if ret:
        cv2.imshow('frame', frame) # display captured video in gray level.

        key = cv2.waitKey(1)
        if  key == ord('q') or key == 27:
            break
        elif key==ord('s'): # Save photo.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)
            cv2.imwrite('./picture/'+str(i)+'.jpg',gray)
            i+=1
    else:
        break

cap.release()
cv2.destroyAllWindows()