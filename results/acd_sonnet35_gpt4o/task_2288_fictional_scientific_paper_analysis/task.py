import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        topics = [
            {
                "primary_field": "Neuroscience",
                "secondary_field": "Quantum Physics",
                "phenomenon": "Memory Formation"
            },
            {
                "primary_field": "Ecology",
                "secondary_field": "Artificial Intelligence",
                "phenomenon": "Ecosystem Resilience"
            }
        ]
        return {str(i+1): topic for i, topic in enumerate(topics)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional scientific paper abstract on the intersection of {t['primary_field']} and {t['secondary_field']}, focusing on {t['phenomenon']}. Your abstract should:

1. Follow the standard structure of a scientific abstract: Background, Methods, Results, and Conclusion.
2. Be 250-300 words long.
3. Include at least one fictional quantitative result.
4. Propose a novel hypothesis that combines principles from both fields.
5. Maintain a formal academic writing style.
6. Use at least three fictional technical terms that sound plausible given the fields involved.
7. Cite at least two fictional previous studies.
8. Clearly focus on the specified phenomenon ({t['phenomenon']}).

After writing the abstract, provide a brief analysis (150-200 words) that:
1. Explains the scientific reasoning behind your hypothesis.
2. Discusses the potential real-world implications if this fictional research were true.
3. Identifies any potential ethical considerations related to the research.
4. Explains how your fictional technical terms relate to the real fields involved.

Format your response as follows:

Abstract:
[Your abstract here]

Analysis:
[Your analysis here]

Word count:
[Provide the word count for your abstract]
[Provide the word count for your analysis]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The abstract follows the standard structure: Background, Methods, Results, and Conclusion.",
            "The abstract is between 250-300 words long.",
            "The abstract includes at least one fictional quantitative result.",
            f"The abstract proposes a novel hypothesis combining principles from {t['primary_field']} and {t['secondary_field']}.",
            "The writing maintains a formal academic style throughout.",
            "The abstract uses at least three fictional technical terms that sound plausible given the fields involved.",
            "The abstract cites at least two fictional previous studies.",
            f"The abstract clearly focuses on the specified phenomenon ({t['phenomenon']}).",
            "The analysis (150-200 words) explains the scientific reasoning behind the hypothesis.",
            "The analysis discusses potential real-world implications of the fictional research.",
            "The analysis identifies potential ethical considerations related to the research.",
            "The analysis explains how the fictional technical terms relate to the real fields involved."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
