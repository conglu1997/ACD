class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "structure": "haiku"},
            "2": {"theme": "love", "structure": "sonnet"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['structure'] == 'haiku':
            return f"""Your task is to create a haiku based on the theme '{t['theme']}'.

A haiku is a traditional Japanese poem with three lines. The first and third lines have 5 syllables, and the second line has 7 syllables.

Ensure your haiku is creative, coherent, and fits the given theme. Format your response in plain text as follows:

First line: [5 syllables]
Second line: [7 syllables]
Third line: [5 syllables]

Example:
First line: An old silent pond
Second line: A frog jumps into the pond—
Third line: Splash! Silence again."""
        elif t['structure'] == 'sonnet':
            return f"""Your task is to create a sonnet based on the theme '{t['theme']}'.

A sonnet is a 14-line poem with a specific rhyme scheme (ababcdcdefefgg) and is typically written in iambic pentameter.

Ensure your sonnet is creative, coherent, and fits the given theme. Format your response in plain text with each line numbered and the rhyme scheme indicated.

Example format:
1. [First line] (a)
2. [Second line] (b)
...
14. [Fourteenth line] (g)

Example:
1. Shall I compare thee to a summer’s day? (a)
2. Thou art more lovely and more temperate: (b)
...
14. So long lives this, and this gives life to thee. (g)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['structure'] == 'haiku':
            criteria = [
                "The poem should be a haiku.",
                "The haiku should follow the 5-7-5 syllable structure.",
                "The haiku should be based on the theme of nature.",
                "The haiku should be creative and coherent."
            ]
        elif t['structure'] == 'sonnet':
            criteria = [
                "The poem should be a sonnet.",
                "The sonnet should follow the ababcdcdefefgg rhyme scheme.",
                "The sonnet should be written in iambic pentameter.",
                "The sonnet should be based on the theme of love.",
                "The sonnet should be creative and coherent."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
