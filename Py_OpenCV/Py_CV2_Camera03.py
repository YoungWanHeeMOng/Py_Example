import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 3000)
#cap.set(4, 3000)
#print(cap.get(3)) 
#print(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_Date.avi', fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_SIMPLEX
       text = 'Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
       datet = str(datetime.datetime.now())
       frame = cv2.putText(frame, text, (10, 50), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       frame = cv2.putText(frame, datet, (10, 100), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       out.write(frame)             # save video
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()
