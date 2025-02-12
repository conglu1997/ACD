import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "source_domain": "Quantum Physics",
                "target_domain": "Social Media",
                "concept": "Entanglement"
            },
            {
                "source_domain": "Ecology",
                "target_domain": "Economics",
                "concept": "Symbiosis"
            },
            {
                "source_domain": "Astronomy",
                "target_domain": "Psychology",
                "concept": "Black Hole"
            },
            {
                "source_domain": "Computer Science",
                "target_domain": "Urban Planning",
                "concept": "Recursion"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting metaphors across different domains, then apply it to the following scenario:

Source Domain: {t['source_domain']}
Target Domain: {t['target_domain']}
Concept to Metaphorize: {t['concept']}

Your task has the following parts:

1. Metaphor Generation Framework (200-250 words):
   Explain the cognitive processes involved in metaphor creation and comprehension. Describe how your AI system would implement these processes.

2. AI System Architecture (200-250 words):
   Provide a high-level overview of your AI system's architecture and its unique features for cross-domain metaphor generation.

3. Application to the Given Scenario (250-300 words):
   Apply your AI system to generate a metaphor explaining the concept from the source domain in terms of the target domain. Provide a detailed explanation of the metaphor and the system's process.

4. Metaphor Interpretation (150-200 words):
   Describe how your AI system would interpret and explain metaphors created by humans, addressing potential challenges.

5. Evaluation and Refinement (150-200 words):
   Propose a method for evaluating the generated metaphors and describe how your AI system would improve its process based on feedback.

6. Ethical and Societal Implications (100-150 words):
   Discuss potential ethical implications and societal impacts of this technology.

Ensure your response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and AI system design. Be creative and innovative while maintaining scientific rigor. Your total response should be between 1050-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics and metaphor theory",
            "The AI system design is innovative, plausible, and well-explained",
            "The generated metaphor for the given scenario is creative, meaningful, and properly explained",
            "The response addresses all required sections comprehensively",
            "The ethical and societal implications are thoughtfully considered"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
