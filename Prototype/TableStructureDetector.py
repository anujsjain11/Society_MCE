import os
import cv2
import numpy as np


class TableStructureDetector:

    def __init__(self):

        # CLAHE settings
        self.clip_limit = 2.0
        self.tile_grid_size = (8, 8)

        # Threshold settings
        self.adaptive_block_size = 15
        self.adaptive_c = 10

        # Morphology settings
        self.horizontal_kernel_size = (60, 1)
        self.vertical_kernel_size = (1, 60)
        self.close_kernel_size = (10, 10)

    def process(self, image_path, image_id):

        # Check file exists
        if not os.path.exists(image_path):
            print(f"{image_path} Path not found")
            return None

        # Read image
        img = cv2.imread(image_path)

        if img is None:
            print(f"{image_path} Image not found")
            return None

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # CLAHE
        clahe = cv2.createCLAHE(
            clipLimit=self.clip_limit,
            tileGridSize=self.tile_grid_size
        )

        gray_clahe = clahe.apply(gray)

        # Adaptive threshold
        thresh = cv2.adaptiveThreshold(
            gray_clahe,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY_INV,
            self.adaptive_block_size,
            self.adaptive_c
        )

        # Horizontal line detection
        horizontal_kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            self.horizontal_kernel_size
        )

        horizontal = cv2.morphologyEx(
            thresh,
            cv2.MORPH_OPEN,
            horizontal_kernel
        )

        horizontal = cv2.dilate(
            horizontal,
            np.ones((2, 2), np.uint8),
            iterations=2
        )

        # Vertical line detection
        vertical_kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            self.vertical_kernel_size
        )

        vertical = cv2.morphologyEx(
            thresh,
            cv2.MORPH_OPEN,
            vertical_kernel
        )

        vertical = cv2.dilate(
            vertical,
            np.ones((2, 2), np.uint8),
            iterations=2
        )

        # Combine horizontal + vertical
        boxes = cv2.add(horizontal, vertical)

        # Close gaps
        kernel = np.ones(self.close_kernel_size, np.uint8)

        boxes = cv2.morphologyEx(
            boxes,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=2
        )

        # Add border
        h, w = img.shape[:2]

        border = cv2.rectangle(
            boxes.copy(),
            (0, 0),
            (w, h),
            (255, 255, 255),
            3
        )

        # Find contours
        # contours, hierarchy = cv2.findContours(
        #     border,
        #     cv2.RETR_TREE,
        #     cv2.CHAIN_APPROX_SIMPLE
        # )

        return img