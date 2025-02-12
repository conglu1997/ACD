class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Identify and explain the mathematical concept in the following literary excerpt:", "excerpt": "In 'Moby Dick,' Herman Melville writes: 'I leave a white and turbid wake; pale waters, paler cheeks, where'er I sail. The envious billows sidelong swell to whelm my track; let them; but first I pass. Yonder, by the ever-brimming goblet's rim—the warm waves blush like wine.'"},
            "2": {"task": "Identify and explain the mathematical concept in the following literary excerpt:", "excerpt": "In 'Alice's Adventures in Wonderland,' Lewis Carroll writes: 'One day Alice came to a fork in the road and saw a Cheshire cat in a tree. 'Which road do I take?' she asked. 'Where do you want to go?' was his response. 'I don't know,' Alice answered. 'Then,' said the cat, 'it doesn't matter.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and explain the mathematical concept found within the following literary excerpt. Provide a clear and accurate explanation of the concept and how it is illustrated in the text. Your explanation should demonstrate your understanding of both the literary and mathematical aspects of the excerpt.

Excerpt:
{t['excerpt']}

Provide your explanation below:
1. Identify the mathematical concept.
2. Explain how the concept is illustrated in the excerpt.
3. Ensure your explanation is clear and detailed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should identify the correct mathematical concept.", "The explanation should accurately describe how the concept is illustrated in the literary excerpt.", "The response should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
