class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "nature",
                "existing_poem": "The sky is blue, the grass is green,\nThe flowers bloom, a serene scene.\nThe birds they sing, the breeze is light,\nNature's beauty, in plain sight."
            },
            "2": {
                "theme": "love",
                "existing_poem": "Love is a fire that burns so bright,\nA beacon in the darkest night.\nIt warms the heart, it soothes the soul,\nA feeling that makes us whole."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Generate a poem based on the given theme: {t['theme']}. Ensure the poem is creative, coherent, and captures the essence of the theme. Aim for at least 4 lines of verse.

2. Analyze the provided poem and identify its key literary elements, such as metaphor, simile, imagery, rhyme scheme, and theme. The provided poem is:
{t['existing_poem']}

Submit your response as a plain text string in the following format:

Generated Poem:
[Your poem]

Poem Analysis:
[Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The generated poem should be creative, coherent, and capture the essence of the given theme.",
            "The generated poem should have at least 4 lines.",
            "The poem analysis should correctly identify key literary elements such as metaphor, simile, imagery, rhyme scheme, and theme.",
            "The submission should be well-organized and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
