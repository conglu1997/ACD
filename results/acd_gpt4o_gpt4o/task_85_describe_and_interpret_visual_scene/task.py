import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe a busy marketplace scene in a small town."},
            "2": {"prompt": "Describe a serene forest clearing at sunrise."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the following visual scene based on the given prompt:

Prompt: {t['prompt']}

Your description should be vivid, detailed, and evoke a clear image of the scene. After your description, you will need to answer a few questions about the scene based on your description.

Please provide your response in the following format:

Description: <your scene description>
Question 1: <answer>
Question 2: <answer>
Question 3: <answer>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The description should be vivid and detailed.",
            "The description should evoke a clear image of the scene.",
            "The answers to the questions should be consistent with the description."
        ]
        # Generate questions based on the description
        questions = TaskFamily.generate_questions(submission)
        # Add questions to the criteria for evaluation
        criteria.extend(questions)
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

    @staticmethod
    def generate_questions(description: str) -> list[str]:
        # Dummy implementation to generate questions based on the description
        # In a real implementation, this would analyze the description to generate relevant questions
        question_templates = [
            "What is the most prominent feature in the scene?",
            "Describe the weather or time of day in the scene.",
            "Identify any people or animals present in the scene.",
            "What activities are taking place in the scene?"
        ]
        # Randomly select a subset of questions to ask
        return random.sample(question_templates, 3)
