import json

from paddleocr import PaddleOCR

import os
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"


ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False) # text detection + text recognition



image_path = "./training data/1.jpg"


result = ocr.predict(image_path) # predict the image
for res in result:
    res.print() # print the result of each image
    # res.save_to_img("output")
    res.save_to_json("output/paddle_ocr_result.json")



ocr_data = []

for line in result[0]:
    box, (text, score) = line

    xs = [p[0] for p in box]
    ys = [p[1] for p in box]

    x_min = min(xs)
    y_min = min(ys)
    x_max = max(xs)
    y_max = max(ys)

    ocr_data.append({
        "text": text,
        "bbox": [x_min, y_min, x_max, y_max]
    })

task = [{
    "data": {
        "image": image_path,
        "ocr": ocr_data
    }
}]

with open("labelstudio_tasks.json", "w") as f:
    json.dump(task, f, indent=4)





# with open("output/paddle_ocr_result.json", "r") as f:
#     data = json.load(f)
#     # detect correct polygon key
#     # polys = data.get("input_path") 
#     # print(polys)


# texts = data["rec_texts"]
# scores = data["rec_scores"]
# boxes = data["dt_polys"]

# filtered = []

# for text, score, box in zip(texts, scores, boxes):
#     if score > 0.8:
#         new_data = {
#     "data": {
#         "ocr": {
#             "texts": data["rec_texts"],
#             "boxes": data["dt_polys"],
#             "scores": data["rec_scores"]
#         }
#     }
# }

#         # filtered.append({
#         #     "text": text,
#         #     "score": score,
#         #     "box": box
#         # })




# with open("output/fixed_ocr.json", "w") as f:
#     json.dump(new_data, f, indent=2)





# for item in filtered:
#     print(item)


