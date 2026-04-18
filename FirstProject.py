import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("pixel.jpg")
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Before modifying background")
plt.axis("off")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#  NB: this function can be let go after figuring out the HSV code of the targeted color

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("HSV value:", hsv[y, x])

cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
#we have now HSV value: [ 87  11 214]! 
lower = np.array([77, 0, 180])
upper = np.array([97, 60, 255])

mask = cv2.inRange(hsv, lower, upper)
hsv[mask != 0] = [20, 202, 255]
img = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

plt.subplot(1,2,2)
cv2.imwrite("Github PFP.png", img)
plt.imshow(img)
plt.title("After modifying background")
plt.axis("off")
plt.show()



