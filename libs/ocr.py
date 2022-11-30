# python ocr.py --image ocr.png 

from pytesseract import*
import argparse 
import cv2 
  
ap = argparse.ArgumentParser() 
  
ap.add_argument("-i", "--image", 
                required=True, 
                help="path to input image to be OCR'd") 

ap.add_argument("-c", "--min-conf", 
                type=int, default=0, 
                help="mininum confidence value to filter weak text detection") 
args = vars(ap.parse_args()) 
  
images = cv2.imread(args["image"]) 

rgb = cv2.cvtColor(images, cv2.COLOR_BGR2RGB) 
results = pytesseract.image_to_data(rgb, output_type=Output.DICT) 

for i in range(0, len(results["text"])): 
    
    x = results["left"][i] 
    y = results["top"][i] 
    w = results["width"][i] 
    h = results["height"][i] 
      
    text = results["text"][i] 
    conf = int(results["conf"][i]) 
      
    if conf > args["min_conf"]: 
        print("Confidence: {}".format(conf)) 
        print("Text: {}".format(text)) 
        print("") 
        
        text = "".join(text).strip() 
        cv2.rectangle(images, 
                      (x, y), 
                      (x + w, y + h), 
                      (0, 0, 255), 2) 
        cv2.putText(images, 
                    text, 
                    (x, y - 10),  
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1.2, (0, 255, 255), 3) 
          
cv2.imshow("Image", images) 
cv2.waitKey(0) 
