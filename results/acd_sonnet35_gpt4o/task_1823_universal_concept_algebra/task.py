import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'concept': 'Time',
                'cultural_context': 'Linear vs. Cyclical time perception',
                'cognitive_domain': 'Temporal reasoning'
            },
            {
                'concept': 'Causality',
                'cultural_context': 'Deterministic vs. Probabilistic worldviews',
                'cognitive_domain': 'Causal inference'
            },
            {
                'concept': 'Self',
                'cultural_context': 'Individualistic vs. Collectivist societies',
                'cognitive_domain': 'Self-awareness and theory of mind'
            },
            {
                'concept': 'Nature',
                'cultural_context': 'Anthropocentric vs. Ecocentric perspectives',
                'cognitive_domain': 'Environmental cognition'
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for manipulating abstract concepts across cultures and cognitive systems, then apply it to solve a complex interdisciplinary problem. Focus on the concept of {t['concept']} within the context of {t['cultural_context']} and the cognitive domain of {t['cognitive_domain']}. Your response should include the following sections:

1. Conceptual Framework Design (300-350 words):
   a) Outline the key components of your universal concept algebra.
   b) Explain how it accounts for cultural variations in concept representation and manipulation.
   c) Describe how it interfaces with different cognitive systems (human and artificial).
   d) Provide a formal notation or symbolic representation for your framework, including a detailed explanation of the notation.
   e) Present a text-based visual representation of your framework (e.g., ASCII diagram or detailed textual description of a visual model).

2. Cultural Analysis (200-250 words):
   a) Analyze how the concept of {t['concept']} is understood and used in different cultures, focusing on {t['cultural_context']}.
   b) Explain how your framework captures and represents these cultural differences.
   c) Discuss potential challenges in creating a truly universal system for this concept.

3. Cognitive Integration (200-250 words):
   a) Describe how your framework integrates with the cognitive domain of {t['cognitive_domain']}.
   b) Explain how it could be implemented in both human cognition and artificial intelligence systems.
   c) Discuss any limitations or adaptations needed for different cognitive architectures.

4. Problem-Solving Application (250-300 words):
   a) Present a complex interdisciplinary problem that involves the concept of {t['concept']}.
   b) Apply your universal concept algebra to break down and analyze the problem.
   c) Demonstrate how your framework leads to novel insights or solutions.
   d) Explain how the cultural and cognitive aspects of your framework contribute to the problem-solving process.

5. Theoretical Implications (150-200 words):
   a) Discuss the broader implications of your framework for cognitive science, artificial intelligence, and cross-cultural understanding.
   b) Propose two novel research questions that arise from your universal concept algebra.
   c) Speculate on how this framework might evolve or be applied in the future.

6. Ethical Considerations (100-150 words):
   a) Address potential ethical concerns related to creating a universal system for concept manipulation.
   b) Discuss any risks of cultural bias or misuse of the framework.
   c) Propose guidelines for the responsible development and application of your universal concept algebra.

Ensure your response demonstrates a deep understanding of cognitive science, cultural anthropology, and formal systems. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response using clear headings for each section. Adhere strictly to the word count limits provided for each section. Your total response should be between 1200-1500 words. Include a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the concept of {t['concept']} across different cultures and cognitive systems.",
            "The universal concept algebra framework is well-defined, innovative, and plausibly applicable to both human and artificial cognitive systems.",
            "The formal notation or symbolic representation is provided and clearly explained.",
            "A text-based visual representation of the framework is included and effectively communicates the framework's structure.",
            f"The cultural analysis effectively addresses {t['cultural_context']} and its implications for the concept.",
            f"The cognitive integration section clearly explains how the framework relates to {t['cognitive_domain']}.",
            "The problem-solving application demonstrates a novel and insightful use of the framework.",
            "The response addresses ethical considerations and potential risks of the framework.",
            "The overall response is creative, scientifically grounded, and well-structured.",
            "The response adheres to the specified word count limits for each section and includes a total word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
