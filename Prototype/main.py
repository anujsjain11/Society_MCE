from paddleocr import PaddleOCR

import os
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"


ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False) # text detection + text recognition


# ocr = PaddleOCR(use_doc_orientation_classify=True, use_doc_unwarping=True) # text image preprocessing + text detection + textline orientation classification + text recognition
# ocr = PaddleOCR(use_doc_orientation_classify=False, use_doc_unwarping=False) # text detection + textline orientation classification + text recognition
# ocr = PaddleOCR(
#     text_detection_model_name="PP-OCRv5_mobile_det",
#     text_recognition_model_name="PP-OCRv5_mobile_rec",
#     use_doc_orientation_classify=False,
#     use_doc_unwarping=False,
#     use_textline_orientation=False) # Switch to PP-OCRv5_mobile models


result = ocr.predict("./training data/1.jpg")
for res in result:
    res.print() # print the result of each image
    print("-----")
    res.save_to_img("output")
    res.save_to_json("output")