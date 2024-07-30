#import libraries
import cv2
import pytesseract

#specify the paths
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread(r"C:\Users\vedant raikar\Desktop\ocr health project\tesseract-ocr-project\test files\testimg.jpg")

#resize the image
img = cv2.resize(img, (600, 600))


text = pytesseract.image_to_string(img)




# Extract text and bounding boxes with confidence levels
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
print(data)

n_boxes = len(data['level'])
for i in range(n_boxes):
    (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    confidence = int(data['conf'][i])
    if confidence > 0:  # Only consider confident detections
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, str(confidence), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow("Image", img)

print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()