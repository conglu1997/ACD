class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a sonnet about the changing seasons. Ensure it follows the traditional sonnet structure with 14 lines and a specific rhyme scheme (ABABCDCDEFEFGG)."},
            "2": {"poem": "An old silent pond...\nA frog jumps into the pond,\nsplash! Silence again."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a poem based on the following prompt:

{t['prompt']}

Ensure that your poem follows the specific structure and stylistic requirements mentioned in the prompt. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to interpret the following poem and identify the poetic structure and elements used. Provide your interpretation in a clear and organized format.

Poem: {t['poem']}\n
Your interpretation should include:
1. The type of poem (e.g., haiku, sonnet).
2. The rhyme scheme, if applicable.
3. The syllable count per line, if applicable.
4. Any notable poetic devices used (e.g., metaphor, simile, alliteration)."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The response should follow the specific poetic structure and rhyme scheme.",
                "The poem should be coherent and stylistically appropriate."]
        else:
            criteria = [
                "The interpretation should accurately identify the poetic structure and elements.",
                "The interpretation should be clear and organized.",
                "The interpretation should correctly identify any notable poetic devices used."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
