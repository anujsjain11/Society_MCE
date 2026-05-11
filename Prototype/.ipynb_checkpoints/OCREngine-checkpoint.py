import os
import cv2
import paddle
from paddleocr import PaddleOCR


class OCREngine:

    def __init__(self):

        self.ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            lang='en',
            device=paddle.device.get_device(),
            cpu_threads=8
        )

    def run_ocr(self, image_path):

        if not os.path.exists(image_path):
            print(f"{image_path} Path not found")
            return None

        img = cv2.imread(image_path)

        if img is None:
            print(f"{image_path} Image not found")
            return None

        result = self.ocr.predict(img)

        return result