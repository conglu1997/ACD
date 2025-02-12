class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"genre": "Science Fiction", "characters": ["a robot", "a scientist"], "setting": "a distant planet", "additional_constraints": ["include a plot twist", "mention advanced technology"], "word_limit": 500},
            "2": {"genre": "Fantasy", "characters": ["a dragon", "a young wizard"], "setting": "an ancient forest", "additional_constraints": ["include a magical artifact", "mention a prophecy"], "word_limit": 500}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a creative short story following these constraints:

Genre: {t['genre']}
Characters: {', '.join(t['characters'])}
Setting: {t['setting']}
Additional Constraints: {', '.join(t['additional_constraints'])}
Word Limit: {t['word_limit']} words

Instructions:
1. The story should belong to the specified genre.
2. It must include the given characters and take place in the specified setting.
3. The story should incorporate the additional constraints.
4. The story must be coherent, engaging, and adhere to the word limit.

Your response should be a single, well-written short story. Format your response as follows:

Title: [Your story title]

Story: [Your story text]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The story should be within the word limit of {t['word_limit']} words.", "The story should belong to the specified genre.", "The story should include the given characters and setting.", "The story should incorporate the additional constraints.", "The story should be coherent and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
