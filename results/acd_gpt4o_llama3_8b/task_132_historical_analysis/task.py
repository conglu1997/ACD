class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the impact of the Industrial Revolution on European society."},
            "2": {"prompt": "Compare the causes and consequences of the French Revolution with a modern political movement of your choice."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Industrial Revolution" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Provide a detailed analysis of the impact of the Industrial Revolution on European society. Your analysis should include:
1. The economic changes brought about by the Industrial Revolution, including specific examples.
2. The social changes and challenges faced by different classes, with examples.
3. The long-term consequences on European society, including both positive and negative aspects.

Ensure your analysis is coherent, well-structured, and insightful. Submit your response as a plain text string."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Compare the causes and consequences of the French Revolution with a modern political movement of your choice. Your comparison should include:
1. The key causes of both the French Revolution and the modern political movement, with detailed examples.
2. The major consequences and outcomes of both events, with examples.
3. Similarities and differences between the two in terms of causes, processes, and outcomes, including specific instances.

Ensure your comparison is coherent, well-structured, and insightful. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "Industrial Revolution" in t["prompt"]:
            criteria = ["The analysis should cover economic changes, social changes, and long-term consequences, with specific examples.", "The analysis should be coherent, well-structured, and insightful."]
        else:
            criteria = ["The comparison should cover key causes, major consequences, and similarities and differences, with detailed examples.", "The comparison should be coherent, well-structured, and insightful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
