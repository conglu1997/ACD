class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concepts": "Battery is to Phone as Fuel is to ?"},
            "2": {"analogy": "Just as a river carves out a canyon over time, continuous effort can lead to significant achievements."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'concepts' in t:
            return f"""Generate an analogy based on the given concepts. Ensure that the analogy is coherent and meaningful. Your analogy should clearly illustrate the relationship between the given concepts and provide a logical and relevant comparison. Avoid using overly simple or common analogies; aim for creativity and depth in your response.

Concepts:
{t['concepts']}

Submit your analogy as a plain text string in the following format:

Analogy: [Your analogy here]"""
        else:
            return f"""Analyze the following analogy. Discuss its coherence, relevance, and any potential weaknesses. Provide a detailed analysis that includes examples or counterexamples if necessary. Your analysis should explain why the analogy is effective or not, and how well it illustrates the intended relationship. Consider the depth and creativity of the analogy in your evaluation.

Analogy:
{t['analogy']}

Submit your analysis as a plain text string in the following format:

Analysis: [Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'concepts' in t:
            criteria = [
                "The analogy should be coherent and meaningful.",
                "The relationship between the concepts should be clear and logical.",
                "The analogy should provide a relevant and logical comparison.",
                "The analogy should demonstrate creativity and depth."
            ]
        else:
            criteria = [
                "The analysis should discuss the coherence and relevance of the analogy.",
                "The analysis should provide examples or counterexamples if necessary.",
                "The analysis should explain why the analogy is effective or not and how well it illustrates the intended relationship.",
                "The analysis should consider the depth and creativity of the analogy.",
                "The analysis should be detailed and thorough."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
