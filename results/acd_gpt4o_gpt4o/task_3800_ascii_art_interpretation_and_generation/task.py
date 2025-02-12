class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'prompt': 'Generate an ASCII art representation of a tree. The tree should have a trunk, branches, and leaves. The leaves should be represented using different characters to indicate various types of foliage. Ensure that the tree is at least 10 lines tall.'},
            '2': {'ascii_art': '  /\ \n /  \ \n/____\ \n |  | \n |  | \n'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            instructions = f"Your task is to generate ASCII art based on the following prompt:\n\n{t['prompt']}\n\nEnsure that your ASCII art is clear, detailed, and matches the described elements. Provide your response in plain text format."
        else:
            instructions = f"Your task is to interpret the following ASCII art and describe the visual elements it represents. Provide your interpretation in a clear and organized format.\n\nASCII Art: {t['ascii_art']}\n\nYour interpretation should include:\n1. A description of the overall structure.\n2. Identification of key elements (e.g., trunk, branches, leaves).\n3. Any notable details or features.\n4. An assessment of the artistic style and any creative aspects.\n\nProvide your response in plain text format."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            criteria = [
                'The ASCII art should match the described elements.',
                'The ASCII art should be clear and recognizable.',
                'The ASCII art should be creative and detailed, using different characters where specified.',
                'The ASCII art should be at least 10 lines tall.']
        else:
            criteria = [
                'The interpretation should accurately describe the overall structure and key elements.',
                'The interpretation should be clear and organized.',
                'The interpretation should correctly identify any notable details or features.',
                'The interpretation should include an assessment of the artistic style and any creative aspects.',
                'The interpretation should be detailed and precise.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
