import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "domain": "Environmental Conservation",
                "languages": ["English", "Mandarin", "Swahili"],
                "concepts": ["circular economy", "森林浴 (forest bathing)", "ubuntu (interconnectedness)"]
            },
            {
                "domain": "Education",
                "languages": ["Spanish", "Japanese", "German"],
                "concepts": ["gamification", "空気を読む (reading the air)", "Bildung (self-cultivation)"]
            }
        ]
        return {str(i): random.choice(problems) for i in range(1, 3)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multilingual conceptual blending system to generate a creative solution for a problem in the domain of {t['domain']}. Your system should integrate concepts from the following languages and ideas:

{', '.join(f'{lang}: {concept}' for lang, concept in zip(t['languages'], t['concepts']))}

1. Conceptual Blending Framework (200-250 words):
   a) Explain how your system represents and processes concepts from different languages.
   b) Describe the mechanism for identifying potential connections between concepts.
   c) Detail how your system generates novel blended concepts.

2. Multilingual Processing (150-200 words):
   a) Explain how your system handles the semantic nuances of concepts in different languages.
   b) Describe any techniques used for cross-lingual concept alignment.
   c) Discuss how cultural context is incorporated into the conceptual blending process.

3. Creative Solution Generation (250-300 words):
   a) Present a creative solution to a problem in the given domain using your conceptual blending system.
   b) Explain how each of the provided concepts contributed to the solution.
   c) Describe the step-by-step process of how your system arrived at this solution.

4. Evaluation Metrics (100-150 words):
   a) Propose metrics to evaluate the creativity and effectiveness of the generated solution.
   b) Explain how these metrics account for cross-cultural and multilingual aspects.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using a multilingual conceptual blending system for problem-solving.
   b) Address any issues related to cultural appropriation or misrepresentation.

6. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how these developments could enhance its problem-solving capabilities or applicability.

Ensure your response demonstrates a deep understanding of conceptual blending theory, multilingual processing, and creative problem-solving. Use appropriate terminology and provide clear explanations for complex ideas. Be innovative in your approach while maintaining scientific plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of conceptual blending theory and its application in a multilingual context.",
            "The proposed system effectively integrates concepts from all specified languages and ideas.",
            "The creative solution generated is innovative, relevant to the given domain, and clearly explained.",
            "The evaluation metrics and ethical considerations are well-thought-out and address multilingual and cross-cultural aspects.",
            "The overall response shows high-level interdisciplinary thinking and problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
