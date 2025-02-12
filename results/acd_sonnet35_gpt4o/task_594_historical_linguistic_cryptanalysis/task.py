import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "era": "Medieval Europe",
                "linguistic_feature": "Alliteration",
                "hidden_concept": "Chivalric code"
            },
            {
                "era": "Ancient Egypt",
                "linguistic_feature": "Metaphor",
                "hidden_concept": "Afterlife beliefs"
            },
            {
                "era": "Renaissance Italy",
                "linguistic_feature": "Anagram",
                "hidden_concept": "Heliocentrism"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze a historical text from {t['era']} using the linguistic feature of {t['linguistic_feature']} to uncover a hidden meaning related to {t['hidden_concept']}. Then, create and solve a related linguistic puzzle. Follow these steps:

1. Historical Text Analysis (200-250 words):
   a) Provide a brief, fictional historical text (2-3 sentences) from the given era that contains the specified linguistic feature.
   b) Analyze how the linguistic feature is used in the text.
   c) Explain how this usage might reveal a hidden meaning related to the given concept.
   d) Discuss the historical and cultural context that supports your interpretation.

2. Linguistic Puzzle Creation (150-200 words):
   a) Based on your analysis, create a linguistic puzzle that incorporates the same feature and hidden concept.
   b) Provide clear instructions for solving the puzzle.
   c) Explain how your puzzle reflects historical linguistic practices from the given era.

3. Puzzle Solution and Explanation (150-200 words):
   a) Provide the solution to your puzzle.
   b) Explain the solving process step-by-step.
   c) Discuss how the solution relates to the hidden concept and historical context.

4. Comparative Linguistic Analysis (200-250 words):
   a) Compare the use of the linguistic feature in your historical text and puzzle to its use in modern language.
   b) Discuss how the feature's function or meaning may have evolved over time.
   c) Hypothesize how this linguistic evolution reflects broader cultural or societal changes.

Ensure your response demonstrates a deep understanding of historical linguistics, the specified era, and creative problem-solving. Use appropriate terminology and provide clear explanations where necessary.

Format your response using clear headings for each section, numbered as above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a fictional historical text from {t['era']}",
            f"The analysis should correctly identify and explain the use of {t['linguistic_feature']}",
            f"The hidden meaning should be plausibly related to {t['hidden_concept']}",
            "The created puzzle should incorporate the specified linguistic feature and hidden concept",
            "The puzzle solution should be logically explained and relate to the historical context",
            "The comparative analysis should demonstrate understanding of linguistic evolution"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
