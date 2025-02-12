class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "artificial intelligence", "setting": "near-future", "technical_elements": ["machine learning", "neural networks", "ethics"], "constraint": "Include a conflict between humans and AI."},
            "2": {"theme": "space exploration", "setting": "distant future", "technical_elements": ["faster-than-light travel", "alien ecosystems", "space habitats"], "constraint": "Describe a first contact scenario with an alien species."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        setting = t["setting"]
        technical_elements = ', '.join(t["technical_elements"])
        constraint = t["constraint"]
        return f"""Craft a fictional narrative based on the following theme and setting. Ensure that your story is engaging, well-structured, and incorporates accurate technical details related to the specified elements. Here are the details:

Theme: {theme}
Setting: {setting}
Technical Elements: {technical_elements}
Additional Constraint: {constraint}

Your story should be between 800 and 1500 words. Make sure to integrate the technical elements seamlessly into the narrative and address the additional constraint clearly.

Submit your story as a plain text string in the following format:

Title: [Your Story Title]

Story: [Your Story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be engaging and well-structured.", 
            "The technical details should be accurate and relevant to the specified elements.", 
            "The narrative should logically integrate the technical elements into the fictional setting.",
            "The story should meet the word count requirement.",
            "The story should adhere to the additional constraint provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
