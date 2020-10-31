import cv2
import numpy as np
import imutils
from imutils import perspective
from imutils import contours
from scipy.spatial.distance import euclidean


#To show image
def show(images):
    for k, img in enumerate(images):
        cv2.imshow("image_" + str(k), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = "images/03.jpeg"

# Reading Image
image = cv2.imread(path)

# Setting gray and blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9, 9), 0)

edge = cv2.Canny(blur, 50, 100)
edge = cv2.dilate(edge, None, iterations=1)
edge = cv2.erode(edge, None, iterations=1)

# Contours
cn = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cn = imutils.grab_contours(cn)

# Sort Contour
(cn, _) = contours.sort_contours(cn)

# Remove small contours
cn = [j for j in cn if cv2.contourArea(j) > 100]

# Set dimension of Reference (leftmost)
ref_object = cn[0]
box = cv2.minAreaRect(ref_object)
box = cv2.boxPoints(box)
# we want size in int
box = np.array(box, dtype="int")
box = perspective.order_points(box)
(tl, tr, br, bl) = box
dist_pixel = euclidean(tl, tr)
dist_cm = 2
pixel_percm = dist_pixel/dist_cm

# Draw rest contours 
for i in cn:
    box = cv2.minAreaRect(i)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 2)
    mid_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), tl[1] + int(abs(tr[1] - tl[1])/2))
    mid_vertical = (tr[0] + int(abs(tr[0] - br[0])/2), tr[1] + int(abs(tr[1] - br[1])/2))
    width = euclidean(tl, tr)/pixel_percm
    height = euclidean(tr, br)/pixel_percm
    cv2.putText(image, "{:.1f}cm".format(width), (int(mid_horizontal[0] - 15), int(mid_horizontal[1] - 10)), 
        cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 0), 2)
    cv2.putText(image, "{:.1f}cm".format(height), (int(mid_vertical[0] + 10), int(mid_vertical[1])), 
        cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 0), 2)

show([image])
