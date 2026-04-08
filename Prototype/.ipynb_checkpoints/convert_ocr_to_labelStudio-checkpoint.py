import json

def convert_ocr_to_ls(ocr_json, image_url, img_w, img_h):

    results = []

    polys = ocr_json["rec_polys"]
    texts = ocr_json["rec_texts"]

    for i, poly in enumerate(polys):

        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]

        x_min = min(xs)
        y_min = min(ys)

        x_max = max(xs)
        y_max = max(ys)

        w = x_max - x_min
        h = y_max - y_min

        results.append({
            "id": f"box_{i}",
            "type": "rectangle",
            "from_name": "bbox",
            "to_name": "image",
            "original_width": img_w,
            "original_height": img_h,
            "image_rotation": 0,
            "value": {
                "x": x_min/img_w*100,
                "y": y_min/img_h*100,
                "width": w/img_w*100,
                "height": h/img_h*100,
                "rotation": 0
            }
        })
        
        # OCR Text
        results.append({
            "id": f"box_{i}",
            "type": "textarea",
            "from_name": "transcription",
            "to_name": "image",
            "value": {
                "text": [texts[i]]
            }
        })
        
    return {
        "data": {
            "ocr": image_url
        },
        "predictions":[
            {
                "model_version":"paddleocr",
                "result": results
            }
        ]
    }

with open("output/paddle_ocr_result.json", "r") as f:
    ocr_json = json.load(f)

data=convert_ocr_to_ls(ocr_json, "http://localhost:8000/output/1.jpg", 2232, 3300)
print(data)
# with open("./output/paddle_ocr_result.json", "r") as f:
#     data = json.load(f)
#     print(data.get('ocr'))
with open("output/labelstudio_tasks.json", "w") as f:
    json.dump(data, f, indent=4)
