class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story_start": "Once upon a time, in a small village nestled between two towering mountains, there lived a young girl named Elara. Every day, she would explore the lush forests and sparkling streams around her home, dreaming of the adventures that lay beyond the mountains. One day, while wandering deeper into the woods than ever before, she stumbled upon a hidden path..."},
            "2": {"story_start": "In a futuristic city where skyscrapers touched the sky and flying cars zipped through the air, a young inventor named Max was on the verge of a groundbreaking discovery. He had been working tirelessly in his small lab, tucked away in the basement of his apartment building, on a device that could change the world. Just as he was about to give up hope, a sudden flash of inspiration struck him..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        story_start = t["story_start"]
        instructions = f"""Your task is to continue the given story in a logical, coherent, and engaging manner. Ensure that your continuation maintains the style and tone of the original text and develops the narrative in an interesting way.\n\nStory Start: {story_start}\n\nResponse Format:\nContinuation: <Your story continuation>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should be logical and coherent.",
            "The continuation should maintain the style and tone of the original text.",
            "The continuation should develop the narrative in an engaging way."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
