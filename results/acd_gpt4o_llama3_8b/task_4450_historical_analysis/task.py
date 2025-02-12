class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Compare the causes and impacts of the American Revolution and the French Revolution. Highlight similarities and differences in their origins, key events, and outcomes. Provide specific examples to support your analysis."
            },
            "2": {
                "prompt": "Analyze the impact of the Industrial Revolution on European society during the 19th century. Discuss both positive and negative effects, focusing on changes in social structure, economy, and daily life. Include specific examples to illustrate your points."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical prompt and provide a detailed response. Your response should include:

1. An introduction to the topic.
2. An analysis addressing the specific points mentioned in the prompt.
3. A conclusion summarizing your insights.

Prompt: {t['prompt']}

Submit your response as a plain text string in the following format:

Introduction: [Your introduction]
Analysis: [Your analysis]
Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a clear introduction, detailed analysis, and a summarizing conclusion.",
            "The analysis should accurately address the specific points mentioned in the prompt and provide well-reasoned insights with specific examples."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
