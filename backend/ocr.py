#import libraries
import cv2
import pytesseract

def perform_ocr(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread(img_path)
    img = cv2.resize(img , (800 , 500))
    text = pytesseract.image_to_string(img)
    data = pytesseract.image_to_data(img , output_type=pytesseract.Output.DICT)
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        confidence = int(data['conf'][i])
        if confidence > 0: # Only consider confident detections
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, str(confidence), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    print(text)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

        


image_path = r"C:\Users\vedant raikar\Desktop\ocr health project\tesseract-ocr-project\test files\img7.webp"
image , text  = perform_ocr(image_path)



