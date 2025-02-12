class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'story': 'In a small village, there lived a young boy named Alex who discovered a hidden cave filled with ancient treasures. Despite the warnings from the villagers, Alex ventured into the cave and found a mystical artifact that granted him extraordinary powers. With these powers, he protected the village from various threats and became a hero.'},
            '2': {'summary': 'A young girl named Lily moves to a new town and finds it difficult to make friends. She discovers an old library with magical books that come to life. With the help of these magical books, Lily embarks on adventures that help her gain confidence and make new friends.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'story' in t:
            return f"""Generate a concise summary for the following fictional story:

{t['story']}

Ensure your summary captures the main events, characters, and the overall plot. Submit your summary as a plain text string in the following format:

Summary: [Your summary here]"""
        elif 'summary' in t:
            return f"""Interpret the following summary of a fictional story and extract key details:

{t['summary']}

Provide the main character's name, the main challenge or conflict they face, and how it is resolved. Submit your response as a plain text string in the following format:

Main Character: [Name]
Conflict: [Conflict]
Resolution: [Resolution]"""
        else:
            return ''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'story' in t:
            criteria = [
                'The summary should capture the main events of the story.',
                'The summary should mention the main character and their actions.',
                'The summary should be concise and coherent.'
            ]
        elif 'summary' in t:
            criteria = [
                'The response should correctly identify the main character.',
                'The response should accurately describe the main conflict.',
                'The response should clearly state how the conflict is resolved.'
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
