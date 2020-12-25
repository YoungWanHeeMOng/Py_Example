
import cv2

img=cv2.imread('lenna.png',-1)

print(img)
print(len(img))

cv2.imshow('Lenna',img)
k=cv2.waitKey(00)

if k == 27:	# esc key
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('Lena_copy.jpg',img)
	cv2.destroyAllWindows()