import cv2

image = cv2.imread('Interface\\310-3106069_gradient-abstract.jpg')
image = cv2.resize(image, (660, 500))
cv2.imwrite('Interface\Background.png', image)