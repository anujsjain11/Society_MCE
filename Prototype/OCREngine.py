import os
import cv2
from paddleocr import PaddleOCR
import paddle
import numpy as np


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
        
    def downscaling(self, poly_list):

        poly_downscaling = []

        for poly in poly_list:

            # convert to float
            poly = np.array(poly, dtype=np.float32)

            # draw original polygon
            cv2.polylines(
                output,
                [np.array(poly, dtype=np.int32)],
                isClosed=True,
                color=(255, 0, 0),
                thickness=2
            )

            # bounding box
            x_min, y_min = np.min(poly, axis=0)
            x_max, y_max = np.max(poly, axis=0)

            w = x_max - x_min
            h = y_max - y_min

            # adaptive shrink
            shrink_factor_h = max(0.6, min(0.9, 1 - 20 / w))
            shrink_factor_v = max(0.6, min(0.9, 1 - 20 / h))

            # center
            center_x = np.mean(poly[:, 0])
            center_y = np.mean(poly[:, 1])

            poly_box = []

            for (x, y) in poly:

                x_new = int(
                    center_x + (x - center_x) * shrink_factor_h
                )

                y_new = int(
                    center_y + (y - center_y) * shrink_factor_v
                )

                poly_box.append([x_new, y_new])

            poly_downscaling.append(
                np.array(poly_box, dtype=np.int16)
            )

        return poly_downscaling

    def downscaling_poly_ocr_result(self, result):

        # downscale polygons
        downscaling_poly = self.downscaling(
            result[0]['dt_polys']
        )
        
        # combine polygon + text + score
        ocr_result = [
            (poly, text, scores)
            for poly, text, scores in zip(
                downscaling_poly,
                result[0]['rec_texts'],
                result[0]['rec_scores']
            )
        ]
        
        return ocr_result
    

ocr = OCREngine()