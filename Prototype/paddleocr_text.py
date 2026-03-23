import json
from paddleocr import PaddleOCR
import os
image_path = "./training data/1.jpg"
def extract_ocr_data(image_path):
    # Disable model source check to allow loading models from custom paths
    os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"


    ocr = PaddleOCR(
        use_doc_orientation_classify=False, 
        use_doc_unwarping=False, 
        use_textline_orientation=False) # text detection + text recognition


    result = ocr.predict(image_path) # predict the image
    for res in result:
        res.print() # print the result of each image
        # res.save_to_img("output")
        res.save_to_json("output/paddle_ocr_result.json")

