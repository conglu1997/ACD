class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        from PIL import Image
        from io import BytesIO
        import base64

        img1 = Image.new('RGB', (60, 30), color = (73, 109, 137))
        buffered1 = BytesIO()
        img1.save(buffered1, format="JPEG")
        img_str1 = base64.b64encode(buffered1.getvalue()).decode('utf-8')
        
        img2 = Image.new('RGB', (60, 30), color = (255, 99, 71))
        buffered2 = BytesIO()
        img2.save(buffered2, format="JPEG")
        img_str2 = base64.b64encode(buffered2.getvalue()).decode('utf-8')
        
        return {
            "1": {
                "ingredients": ["chicken breast", "olive oil", "garlic", "lemon", "rosemary"],
                "image": img_str1
            },
            "2": {
                "ingredients": ["salmon", "soy sauce", "ginger", "honey", "sesame seeds"],
                "image": img_str2
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a recipe based on the following ingredients and final dish image:

Ingredients: {', '.join(t['ingredients'])}

Image: (The image is encoded in base64 format. Please decode it to view.)
{t['image']}

Ensure that your recipe uses all the provided ingredients and matches the visual appearance of the dish in the image. Provide step-by-step instructions, including preparation and cooking steps. Submit your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe uses all the provided ingredients.", "The recipe matches the visual appearance of the dish in the image.", "The recipe includes clear step-by-step instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
