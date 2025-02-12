class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Design a summer dress suitable for a casual outing. The dress should be light, airy, and comfortable. It should incorporate floral patterns and be made from eco-friendly materials. Describe the design in detail, including the colors, patterns, fabric, and any unique features.",
                "principles": "Fashion design involves creating aesthetically pleasing and functional clothing items. Descriptions should cover all aspects of the design, including materials, patterns, colors, and unique features."
            },
            "2": {
                "criteria": "Design a formal suit for a business meeting. The suit should be professional, elegant, and tailored to fit. It should include a jacket, trousers, and a tie. Describe the design in detail, including the colors, fabric, cut, and any unique features.",
                "principles": "Fashion design for formal wear requires attention to detail, fit, and professional appearance. Descriptions should cover all aspects of the design, including materials, colors, fit, and unique features."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and describe a fashion design based on the given criteria. Ensure your design is detailed and covers all aspects, including colors, patterns, materials, and unique features.\n\nCriteria:\n{t['criteria']}\n\nPrinciples:\n{t['principles']}\n\nFormat your response as follows:\n1. Describe the overall concept and inspiration behind the design.\n2. Detail the colors, patterns, and materials used.\n3. Highlight any unique features or elements that make the design stand out.\n\nExample Response:\n1. Concept and Inspiration:\n    - The summer dress is inspired by the beauty of blooming flowers and the need for comfort during hot weather.\n2. Colors, Patterns, and Materials:\n    - The dress features a floral pattern with shades of pink, yellow, and green. It is made from organic cotton, which is light and breathable.\n3. Unique Features:\n    - The dress has a fitted bodice with a flared skirt, and it includes pockets for added convenience.\n    - The neckline is adorned with delicate lace, adding a touch of elegance to the casual design."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should describe the overall concept and inspiration behind the design.",
            "The details about colors, patterns, and materials should be included.",
            "The description should highlight any unique features or elements that make the design stand out.",
            "The design should be coherent, detailed, and align with the given criteria."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
