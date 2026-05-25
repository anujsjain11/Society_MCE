from llama_cpp import Llama


class LLMParser:

    def __init__(self):

        self.llm = Llama(
            model_path="llama3-Q5_K_M.gguf",
            n_ctx=2048,
            n_threads=8,
            verbose=False
        )

    def extract_receipt(self, prompt ,ocr_result):

        ocr_text = "\n".join(ocr_result)
        if prompt == None:
            prompt = f"""
                            You are a receipt extraction API.
                            
                            Extract receipt items from OCR text.
                            
                            Return ONLY valid JSON.
                            No markdown.
                            No explanation.
                            No extra text.
                            No notes.
                            No python code.
                            
                            JSON schema:
                            {{
                              "items": [
                                {{
                                  "product": "string",
                                  "quantity": "string",
                                  "price": 0
                                }}
                              ],
                              "total_quantity": 0,
                              "total_price": 0
                            }}
                            
                            Rules:
                            - Extract ALL products
                            - Merge multiline products
                            - Ignore noise
                            - Extract quantity separately
                            - Extract total separately
                            - Price must be numeric
                            - Do NOT hallucinate products
                            
                            OCR:
                            {ocr_text}
                        """            
        
        output = self.llm(
            prompt,
            max_tokens=500,
            temperature=0.1
        )

        result = output["choices"][0]["text"]

        return result