class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a sonnet about the changing seasons."
            },
            "2": {
                "poem": "I wandered lonely as a cloud\nThat floats on high o'er vales and hills,\nWhen all at once I saw a crowd,\nA host, of golden daffodils;\nBeside the lake, beneath the trees,\nFluttering and dancing in the breeze.\nContinuous as the stars that shine\nAnd twinkle on the Milky Way,\nThey stretched in never-ending line\nAlong the margin of a bay:\nTen thousand saw I at a glance,\nTossing their heads in sprightly dance.\nThe waves beside them danced; but they\nOut-did the sparkling waves in glee:"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to create a poem based on the following prompt:\n\n{t['prompt']}\n\nEnsure that your poem follows the structure and style of a sonnet, which typically consists of 14 lines with a specific rhyme scheme (e.g., ABABCDCDEFEFGG). Your poem should also be coherent, emotionally resonant, and grammatically correct. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to analyze the following poem:\n\n{t['poem']}\n\nProvide an analysis that includes the following aspects:\n1. The central theme of the poem.\n2. The emotional impact of the poem.\n3. The use of poetic devices (such as metaphor, simile, personification, etc.).\n4. The overall style and tone of the poem.\n\nProvide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The poem should follow the structure and style of a sonnet.",
                "The poem should have 14 lines.",
                "The poem should be coherent and emotionally resonant.",
                "The poem should be grammatically correct."
            ]
        else:
            criteria = [
                "The analysis should accurately identify the central theme of the poem.",
                "The analysis should describe the emotional impact of the poem.",
                "The analysis should identify and explain the use of poetic devices.",
                "The analysis should discuss the overall style and tone of the poem."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
