import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_process': 'DNA replication',
                'problem_domain': 'Information security'
            },
            {
                'biological_process': 'Cellular respiration',
                'problem_domain': 'Sustainable energy production'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves three steps related to the biological process of {t['biological_process']} and the problem domain of {t['problem_domain']}:

1. Explanation (100-150 words): Provide a clear, accurate explanation of the biological process. Include key components and steps involved.

2. Metaphor Creation (100-150 words): Develop a creative and apt metaphor for this biological process. Your metaphor should capture the essence of the process and make it understandable to a non-scientific audience. Explain how different elements of your metaphor correspond to components of the biological process.

3. Problem Solving (200-250 words): Apply your metaphorical understanding of the biological process to solve a problem in the given domain. Describe how the metaphor helps you approach the problem, and provide a detailed solution that draws parallels between the biological process and the problem domain.

Format your response as follows:

Biological Process Explanation:
[Your explanation here]

Metaphor:
[Your metaphor and explanation here]

Problem Solution:
[Your problem-solving approach and solution here]

Ensure your response demonstrates a deep understanding of the biological process, creativity in metaphor creation, and innovative problem-solving skills."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the biological process is accurate and comprehensive.",
            "The metaphor is creative, apt, and clearly explained in relation to the biological process.",
            "The problem-solving approach effectively applies the metaphor to the given domain.",
            "The solution is innovative and draws clear parallels between the biological process and the problem domain.",
            "The overall response demonstrates a deep understanding of both biology and the problem domain, as well as strong analogical reasoning skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
