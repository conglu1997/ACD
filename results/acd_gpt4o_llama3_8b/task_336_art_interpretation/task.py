class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artwork_details": "A painting of a starry night sky with swirling clouds, a bright crescent moon, and a peaceful village below. The artwork features a prominent cypress tree in the foreground, reaching towards the sky."},
            "2": {"artwork_details": "A surrealist painting with melting clocks draped over tree branches and a barren landscape in the background. In the foreground, there is a distorted figure with a soft, almost liquid appearance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        artwork_details = t["artwork_details"]
        return f"""Describe and interpret the following artwork based on the visual details provided:\n\n{artwork_details}\n\nYour interpretation should include:\n1. A detailed description of the artwork.\n2. An analysis of the possible meaning or message conveyed by the artist.\n3. Any emotional or intellectual responses the artwork evokes.\n\nSubmit your response as a plain text string in the following format:\n\nDescription: [Your description here]\nAnalysis: [Your analysis here]\nResponse: [Your emotional or intellectual response here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the visual details provided.",
            "The interpretation should offer a thoughtful analysis of the possible meaning or message of the artwork.",
            "The response should include any emotional or intellectual reactions to the artwork."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
