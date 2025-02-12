class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A serene landscape painting depicting a sunset over a calm lake, with a lone boat floating gently in the water. The sky is a gradient of warm colors, and the surrounding trees are reflected in the water."
            },
            "2": {
                "description": "A bustling cityscape at night, with bright neon signs illuminating the streets. People are walking hurriedly, and cars are passing by. The buildings are tall and closely packed, creating a sense of energy and movement."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You will be given a description of a visual artwork. Your task is to create a coherent narrative that aligns with the visual elements described. Your narrative should be vivid, imaginative, and capture the essence of the artwork. Ensure your narrative is at least 200 words long."
        instructions += f"\nDescription: {t['description']}"
        instructions += "\nSubmit your response as a plain text string."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be at least 200 words long.",
            "The narrative should align with the visual elements described in the artwork.",
            "The narrative should be vivid and imaginative.",
            "The narrative should capture the essence of the artwork."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
