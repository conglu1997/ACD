class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate song lyrics based on the theme of 'hope and resilience'. The lyrics should be at least 100 words long and should convey the emotions and message effectively. Provide your response in plain text format."},
            "2": {"prompt": "Interpret the following musical notation and describe the music in words. Focus on the melody, rhythm, and overall feel of the piece. Provide your response in plain text format.", "notation": "C4 E4 G4 A4 G4 E4 C4 | G4 F4 E4 D4 C4"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'notation' in t:
            return f"""Your task is to interpret the given musical notation and describe the music in words. Focus on the melody, rhythm, and overall feel of the piece. Ensure your description is vivid and captures the essence of the music. Provide your response in plain text format:\n\n{t['notation']}\n"""
        else:
            return f"""Your task is to generate song lyrics based on the given theme. Ensure that your lyrics are at least 100 words long and convey the emotions and message effectively. Provide your response in plain text format:\n\n{t['prompt']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'notation' in t:
            criteria = ["The description should be vivid and capture the essence of the music.", "The response should include elements of melody, rhythm, and overall feel.", "The description should be coherent and detailed."]
        else:
            criteria = ["The lyrics should be at least 100 words long.", "The lyrics should convey the emotions and message effectively.", "The lyrics should be coherent and follow a logical structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
