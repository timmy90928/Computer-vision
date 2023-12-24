import cv2

def cap_num(max:int=5) -> list[int]:
    """
    ```
    N = cap_num()
    print(N)
    cap = cv2.VideoCapture(N[0])
    print(cap.isOpened())

    while cap.isOpened():    # https://www.codegrepper.com/code-examples/python/cv2+cap.isOpened

        ret, frame = cap.read()  # returned value of ret is either True (successful) or False (failed). frame: captured image frames
        width,height=cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # print(f"width,height={width},{height}")
        if ret:
            
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert color video to gray level.
            cv2.imshow('frame', frame) # display captured video in gray level.

            key = cv2.waitKey(1)
            if  key == ord('q') or key == 27:
                break
        else:
            break

    cap.release()
    ```
    """
    _ = []
    for n in range(max):
        cap = cv2.VideoCapture(0,n)
        ret, frame = cap.read()
        if ret: _.append(n)
    return _
        
def video_write():
    """
    ```
    out = video_write()
    out.write(frame)        # captured video is saved as output.avi
    out.release()
    ```
    """
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    # cv2.VideoWriter_fourcc(‘X’, ‘V’, ‘I’, ‘D’), MPEG-4 encoding，.avi (video format)
    # cv2.VideoWriter_fourcc(‘I’, ‘4’, ‘2’, ‘0’), YUV encoding， .avi (video format)
    # cv2.VideoWriter_fourcc(‘P’, ‘I’, ‘M’, ‘I’), MPEG-1 encoding，.avi (video format)
    # cv2.VideoWriter_fourcc(‘T’, ‘H’, ‘E’, ‘O’), Ogg Vorbis encoding, .ogv (video format)
    # cv2.VideoWriter_fourcc(‘F’, ‘L’, ‘V’, ‘1’), Flash encoding，.flv (video format)

    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    # output.avi: output video's file name and format.
    # fourcc: video format.
    # 20.0: 20 frames per second.
    # Resolution is 640x480
    return out

N = cap_num()
cap = cv2.VideoCapture(N[0])

i = 0
while cap.isOpened():    # https://www.codegrepper.com/code-examples/python/cv2+cap.isOpened

    ret, frame = cap.read()  # returned value of ret is either True (successful) or False (failed). frame: captured image frames

    # width,height=cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # print(f"width,height={width},{height}")
    
    if ret:

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert color video to gray level
        cv2.imshow('frame', frame) # display captured video in gray level

        key = cv2.waitKey(1)
        if  key == ord('q') or key == 27:
            break
        elif key==ord('s'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)
            cv2.imwrite('./picture/'+str(i)+'.jpg',gray)
            i+=1
    else:
        break

cap.release()
cv2.destroyAllWindows()