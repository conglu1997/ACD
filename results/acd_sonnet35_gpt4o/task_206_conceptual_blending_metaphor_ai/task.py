import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'abstract_concept': 'time',
                'concrete_domain': 'river',
                'target_blend': 'economics'
            },
            {
                'abstract_concept': 'knowledge',
                'concrete_domain': 'tree',
                'target_blend': 'technology'
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting novel metaphors based on conceptual blending theory, and use it to analyze complex abstract concepts. Your task has three parts:

1. System Design (300-350 words):
Create an AI system that generates and interprets metaphors using conceptual blending theory. Your system should:
a) Explain how it represents and processes conceptual spaces.
b) Describe the algorithms or techniques used for blending concepts and generating metaphors.
c) Outline how the system evaluates the coherence and novelty of generated metaphors.

2. Metaphor Generation and Analysis (250-300 words):
Use your system to generate a novel metaphor that blends the abstract concept of {t['abstract_concept']} with the concrete domain of a {t['concrete_domain']}. Then, analyze this metaphor by:
a) Explaining the conceptual blend and how it illuminates aspects of {t['abstract_concept']}.
b) Discussing potential cultural or contextual factors that might affect the interpretation of this metaphor.
c) Proposing how this metaphor could be extended or elaborated.

3. Application to Complex Domain (250-300 words):
Apply your system to generate a metaphor that explains a complex concept in {t['target_blend']} using the blend you created in part 2. Then:
a) Analyze how this new metaphor aids in understanding the complex concept.
b) Discuss any limitations or potential misunderstandings that might arise from this metaphor.
c) Propose how your system could be improved to generate more nuanced or domain-specific metaphors.

Ensure your response demonstrates a deep understanding of conceptual blending theory, metaphor comprehension, and AI technologies. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using the following structure:

1. System Design:
   [Your explanation here]

2. Metaphor Generation and Analysis:
   [Your analysis here]

3. Application to Complex Domain:
   [Your application and discussion here]

Your total response should be between 800-950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The system design clearly explains how conceptual spaces are represented and processed.",
            "The metaphor generation and analysis demonstrates a novel blend of the given abstract concept and concrete domain.",
            f"The application to {t['target_blend']} effectively uses the generated metaphor to explain a complex concept in that domain.",
            "The response shows a strong understanding of conceptual blending theory, metaphor comprehension, and AI technologies.",
            "The proposed improvements and limitations discussion demonstrates critical thinking about the system's capabilities and potential enhancements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
