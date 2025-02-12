class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "creation", "theme": "nature", "structure": "haiku", "requirements": "The poem should follow the 5-7-5 syllable structure."},
            "2": {"type": "analysis", "poem": "I wandered lonely as a cloud\nThat floats on high o'er vales and hills,\nWhen all at once I saw a crowd,\nA host, of golden daffodils;\nBeside the lake, beneath the trees,\nFluttering and dancing in the breeze.", "questions": ["What is the central theme of the poem?", "Identify and explain the use of any two literary devices in the poem."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "creation":
            theme = t["theme"]
            structure = t["structure"]
            requirements = t["requirements"]
            instructions = f"""Your task is to create a poem based on the following constraints:\n\nTheme: {theme}\n\nStructure: {structure}\n\nRequirements: {requirements}\n\nEnsure that your poem is creative, adheres to the given structure, and captures the essence of the theme. Provide your response in plain text format.\n\nExample Format:\n[Your poem here]\n\nExample:\nAn old silent pond...\nA frog jumps into the pond,\nSplash! Silence again."""
        else:
            poem = t["poem"]
            questions = t["questions"]
            instructions = f"""Your task is to analyze the following poem:\n\n{poem}\n\nAnswer the following questions:\n\n1. {questions[0]}\n2. {questions[1]}\n\nProvide your analysis in plain text format and ensure your answers are thorough and well-explained.\n\nExample Format:\n1. The central theme of the poem is [your answer].\n2. Two literary devices used in the poem are [device 1] and [device 2]."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "creation":
            criteria = ["The poem follows the 5-7-5 syllable structure.", "The poem captures the essence of the theme of nature.", "The poem is creative and original."]
        else:
            criteria = ["The analysis correctly identifies the central theme of the poem.", "The analysis correctly identifies and explains the use of two literary devices.", "The analysis is thorough and well-explained."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
