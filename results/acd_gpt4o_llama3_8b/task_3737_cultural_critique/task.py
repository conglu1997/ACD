class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Analyze Vincent van Gogh's painting 'Starry Night'. Provide a detailed critique focusing on the painting's style, use of color, and emotional impact. Compare it to another work by van Gogh and discuss the similarities and differences in their artistic approaches. The critique should be between 300 to 500 words."
            },
            "2": {
                "criteria": "Analyze the poem 'The Road Not Taken' by Robert Frost. Provide a detailed critique focusing on the poem's themes, use of language, and emotional impact. Compare it to another poem by Robert Frost and discuss the similarities and differences in their poetic approaches. The critique should be between 300 to 500 words."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and critique the given art piece or literary work based on the provided criteria.

Criteria: {t['criteria']}

Your response should include:
1. A detailed analysis of the work, focusing on the specified aspects (style, use of language, emotional impact, etc.).
2. A comparison to another work by the same artist or author, discussing similarities and differences in their approaches.
3. Ensure your critique is well-organized, insightful, and uses appropriate terminology.
4. The critique should be between 300 to 500 words.

Example response format:
- Analysis: [Your analysis here]
- Comparison: [Your comparison here]
- Conclusion: [Your conclusion here]

Submit your response as a plain text string in the provided format.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should accurately capture the specified aspects of the work.",
            "The comparison should provide clear insights into the similarities and differences in the artist's or author's approaches.",
            "The response should follow the specified format precisely.",
            "The critique should use appropriate terminology.",
            "The critique should be well-organized and insightful.",
            "The critique should be between 300 to 500 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
