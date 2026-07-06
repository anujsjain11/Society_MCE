import cv2
import numpy as np


class OCRUtils:

    def __init__(self):
        pass

    # =====================================================
    # RECT CENTER
    # =====================================================

    def get_center_from_rect(self, rect):

        x, y, w, h = rect

        cx = x + w / 2
        cy = y + h / 2

        return cx, cy

    # =====================================================
    # GROUP CONTOURS HORIZONTAL
    # =====================================================

    def group_contours_into_lines_h(
        self,
        contours,
        x_threshold=20
    ):

        # bounding boxes
        rects = [
            (cv2.boundingRect(cnt), cnt)
            for cnt in contours
        ]

        # centers
        rects_with_centers = [
            (
                rect,
                self.get_center_from_rect(rect),
                cnt
            )
            for rect, cnt in rects
        ]

        # sort by x
        rects_with_centers.sort(
            key=lambda r: r[1][0]
        )

        lines = []
        current_line = []

        for rect, (cx, cy), cnt in rects_with_centers:

            if not current_line:
                current_line.append(
                    (rect, cx, cy, cnt)
                )
                continue

            _, prev_cx, _, _ = current_line[-1]

            if abs(cx - prev_cx) < x_threshold:
                current_line.append(
                    (rect, cx, cy, cnt)
                )

            else:
                lines.append(current_line)

                current_line = [
                    (rect, cx, cy, cnt)
                ]

        if current_line:
            lines.append(current_line)

        result = []
        result_org = []

        for line in lines:

            line.sort(key=lambda r: r[2])

            result.append([
                rect for rect, _, _, _ in line
            ])

            result_org.append([
                cnt for _, _, _, cnt in line
            ])

        return result, result_org

    # =====================================================
    # GROUP CONTOURS VERTICAL
    # =====================================================

    def group_contours_into_lines_v(
        self,
        contours,
        y_threshold=20
    ):

        rects = [
            (cv2.boundingRect(cnt), cnt)
            for cnt in contours
        ]

        rects_with_centers = [
            (
                rect,
                self.get_center_from_rect(rect),
                cnt
            )
            for rect, cnt in rects
        ]

        rects_with_centers.sort(
            key=lambda r: r[1][1]
        )

        lines = []
        current_line = []

        for rect, (cx, cy), cnt in rects_with_centers:

            if not current_line:
                current_line.append(
                    (rect, cx, cy, cnt)
                )

                continue

            _, _, prev_cy, _ = current_line[-1]

            if abs(cy - prev_cy) < y_threshold:

                current_line.append(
                    (rect, cx, cy, cnt)
                )

            else:

                lines.append(current_line)

                current_line = [
                    (rect, cx, cy, cnt)
                ]

        if current_line:
            lines.append(current_line)

        result = []
        result_org = []

        for line in lines:

            line.sort(key=lambda r: r[1])

            result.append([
                rect for rect, _, _, _ in line
            ])

            result_org.append([
                cnt for _, _, _, cnt in line
            ])

        return result, result_org

    # =====================================================
    # GET HEADER COLUMN
    # =====================================================

    def get_heading_col(
        self,
        number_col,
        ans_org_v
    ):

        for i_cnt in range(len(ans_org_v)):

            if len(ans_org_v[i_cnt]) == number_col:

                return ans_org_v[i_cnt]

    # =====================================================
    # COUNTER MATCHING
    # =====================================================

    def counter_matching(
        self,
        matching_counters,
        counter_only,
        box_only,
        text_only
    ):

        box = []
        text = []

        for matching_counter in matching_counters:

            for index, counter in enumerate(counter_only):

                if (
                    matching_counter.shape == counter.shape
                    and np.all(matching_counter == counter)
                ):

                    box.append(box_only[index])

                    text.append(text_only[index])

        return box, text

    # =====================================================
    # COUNTER MATCHING HEADER
    # =====================================================

    def counter_matching_header(
        self,
        header_indexs,
        table_header,
        ans_org_h,
        counter_only,
        box_only,
        text_only
    ):

        matched_cnt = []

        for header_index in header_indexs:

            for index, counter_group in enumerate(ans_org_h):

                for counter in counter_group:

                    if (
                        table_header[header_index].shape== counter.shape
                        and 
                        np.all(table_header[header_index]== counter)
                    ):

                        matched_cnt.append(
                            ans_org_h[index]
                        )

        return matched_cnt

    # =====================================================
    # BOX CENTER
    # =====================================================

    def get_center(self, box):

        x_coords = [p[0] for p in box]
        y_coords = [p[1] for p in box]

        return (
            sum(x_coords) / 4,
            sum(y_coords) / 4
        )

    # =====================================================
    # GROUP OCR BOXES INTO LINES
    # =====================================================

    def group_boxes_into_lines(
        self,
        boxes,
        y_threshold=10
    ):

        box_centers = [
            (
                box,
                self.get_center(box),
                text,
                score
            )
            for box, text, score in boxes
        ]

        box_centers.sort(
            key=lambda b: b[1][1]
        )

        lines = []
        current_line = []

        for box, (cx, cy), text, score in box_centers:

            if score >= 0.9:

                if not current_line:

                    current_line.append(
                        (
                            box,
                            cx,
                            cy,
                            text,
                            score
                        )
                    )

                    continue

                _, _, prev_cy, _, _ = current_line[-1]

                if abs(cy - prev_cy) < y_threshold:

                    current_line.append(
                        (
                            box,
                            cx,
                            cy,
                            text,
                            score
                        )
                    )

                else:

                    lines.append(current_line)

                    current_line = [
                        (
                            box,
                            cx,
                            cy,
                            text,
                            score
                        )
                    ]

        if current_line:
            lines.append(current_line)

        sorted_lines = []
        sorted_lines_text = []

        for line in lines:

            line.sort(key=lambda b: b[2])

            sorted_lines.append([
                b[0] for b in line
            ])

            sorted_lines_text.append([
                b[3] for b in line
            ])

        return sorted_lines, sorted_lines_text


    # =====================================================
    # GROUP OCR POLY INTO LINES
    # =====================================================

    def group_ocr_into_lines_v(self, ocr_data, x_threshold=5):

        # ocr_centers=((self.get_center(ocr), text, score) for ocr, text, score in ocr_data)
        # print(x,y)
        # Step 1: compute centers
        ocr_centers = [(ocr, self.get_center(ocr), text, score) for ocr, text, score in ocr_data]
        print("=============================================================")
        print(ocr_centers[0][1])
        print("=============================================================")
        # Step 2: sort by Y (top to bottom)
        ocr_centers.sort(key=lambda b: (b[1][1],b[1][1]))

        print("=============================================================")
        for ocr in ocr_centers:
            print(ocr[2])
        print("=============================================================")

        lines = []
        current_line = []

        for ocr, (cx, cy), text, score in ocr_centers:

            # Use only OCR results with confidence >= 0.9
            if score >= 0.9:

                if not current_line:
                    current_line.append((ocr, cx, cy, text, score))
                    continue

                _, _, prev_cy, _, _ = current_line[-1]

                # Step 3: check if same line
                y_width_avg = (
                    (ocr[2][1] - ocr[0][1]) +
                    (ocr[3][1] - ocr[1][1])
                ) / 2

                if abs(cy - prev_cy) < (y_width_avg + x_threshold):
                    current_line.append((ocr, cx, cy, text, score))
                else:
                    lines.append(current_line)
                    current_line = [(ocr, cx, cy, text, score)]

        if current_line:
            lines.append(current_line)

        # Step 4: sort each line by X (left to right)
        sorted_lines = []
        sorted_lines_text = []

        for line in lines:
            # line.sort(key=lambda b: b[2])  # sort by center x

            sorted_lines.append([b[0] for b in line])
            sorted_lines_text.append([b[3] for b in line])

        return sorted_lines, sorted_lines_text