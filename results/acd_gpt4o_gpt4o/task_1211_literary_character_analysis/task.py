class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "narrative": "In the novel 'To Kill a Mockingbird,' Scout Finch begins as a naive child who doesn't understand the complexities of the world around her. As the story progresses, she faces various challenges that shape her understanding of morality, justice, and empathy.",
                "character": "Scout Finch"
            },
            "2": {
                "narrative": "In the novel '1984,' Winston Smith starts as a disillusioned and oppressed citizen living under a totalitarian regime. Throughout the story, his internal and external struggles reveal his desire for freedom and truth, ultimately leading to his tragic fate.",
                "character": "Winston Smith"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the development of the literary character mentioned below within the given narrative. Explain their motivations, challenges, and growth throughout the story. Ensure your analysis is detailed, well-structured, and supported by examples from the narrative. Focus on analyzing the character rather than summarizing the plot.

Narrative: {t['narrative']}
Character: {t['character']}

Provide your analysis in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should detail the character's motivations.",
            "The analysis should describe the challenges faced by the character.",
            "The analysis should explain the character's growth throughout the story.",
            "Examples from the narrative should support the analysis.",
            "The response should focus on character analysis rather than plot summary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
