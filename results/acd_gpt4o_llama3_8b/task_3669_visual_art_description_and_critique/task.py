class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_piece": "The Starry Night by Vincent van Gogh", "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Vincent_van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"},
            "2": {"art_piece": "The Persistence of Memory by Salvador Dalí", "image_url": "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the visual art piece '{t["art_piece"]}' in detail. Focus on the colors, composition, and emotional impact of the piece. Then, provide a critique of the artwork based on artistic principles and historical context. Your response should be at least 300 words long. Ensure that the description and critique are distinct sections and are coherent.

Response format:
Description: [Your detailed description here]
Critique: [Your critique here]

Submit your description and critique as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be detailed and vivid, focusing on colors, composition, and emotional impact.", "The critique should be based on artistic principles and historical context.", "The response should be at least 300 words long.", "The description and critique should be distinct sections and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
