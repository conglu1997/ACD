class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Nature",
                "example_poem": "The sky is blue, the grass is green, \nIn nature's embrace, a serene scene. \nBirds sing songs, the rivers flow, \nIn this peaceful world, let your worries go.",
                "example_analysis": "The poem describes a tranquil natural scene, highlighting the beauty of the sky, grass, birds, and rivers. It evokes a sense of peace and encourages the reader to release their worries and find solace in nature."
            },
            "2": {
                "theme": "Love",
                "example_poem": "In your eyes, I see the stars, \nA love so deep, it heals all scars. \nHand in hand, we walk through time, \nForever yours, forever mine.",
                "example_analysis": "The poem speaks of a profound love, comparing the beloved's eyes to stars and expressing how this love has the power to heal. It conveys a timeless bond and a deep connection between two individuals."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given theme:

Task 1: Generate a poem based on the theme '{t['theme']}'. Your poem should be at least 4 lines long, have a clear rhyme scheme, and evoke the theme effectively. Submit your poem as a plain text string.

Task 2: Analyze the given poem and describe its meaning and emotional impact. Your analysis should be clear, concise, and capture the essence of the poem. Include the poem's rhyme scheme in your analysis. Submit your analysis as a plain text string in the following format:

- Poem Analysis:
[Your analysis]

Example Poem: {t['example_poem']}
Example Analysis: {t['example_analysis']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The poem should be at least 4 lines long.",
            "The poem should have a clear rhyme scheme.",
            "The poem should effectively evoke the given theme.",
            "The analysis should be clear, concise, and capture the essence of the poem.",
            "The analysis should include the poem's rhyme scheme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
