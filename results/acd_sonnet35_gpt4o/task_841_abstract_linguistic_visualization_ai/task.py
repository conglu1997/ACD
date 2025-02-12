import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'concept': 'causality',
                'linguistic_theory': 'force dynamics',
                'target_language': 'Mandarin Chinese'
            },
            {
                'concept': 'time',
                'linguistic_theory': 'conceptual metaphor theory',
                'target_language': 'Hopi'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret abstract visual representations of the linguistic concept of {t['concept']}, based on {t['linguistic_theory']}, with a focus on {t['target_language']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system.
   b) Explain how the system integrates knowledge from linguistics, cognitive science, and computer vision.
   c) Detail the process of generating and interpreting visual representations.

2. Linguistic-Visual Mapping (200-250 words):
   a) Explain your approach to mapping linguistic concepts to visual elements.
   b) Discuss how your system incorporates {t['linguistic_theory']} in its representations.
   c) Provide an example of how a specific aspect of {t['concept']} would be visually represented.

3. Cross-linguistic Adaptation (150-200 words):
   a) Describe how your system adapts to the specific features of {t['target_language']}.
   b) Discuss challenges in representing {t['concept']} in {t['target_language']} and how your system addresses them.
   c) Explain how the system could be extended to other languages.

4. Interpretation and Analysis (150-200 words):
   a) Describe the process by which your AI system interprets and analyzes visual representations.
   b) Explain how the system handles ambiguity and context-dependence in interpretation.
   c) Propose a method for validating the accuracy of the AI's interpretations.

5. Potential Applications and Implications (150-200 words):
   a) Discuss potential applications of this technology in fields such as language education, cross-cultural communication, or cognitive research.
   b) Analyze ethical considerations related to visual representation of linguistic concepts.
   c) Speculate on how this technology might influence our understanding of language and cognition.

6. Limitations and Future Directions (100-150 words):
   a) Identify three major limitations or challenges of your proposed system.
   b) For each limitation, suggest a potential avenue for future research to address it.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 1000-1300 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['linguistic_theory']} and how it relates to the concept of {t['concept']}.",
            f"The proposed system shows a clear and innovative approach to visually representing linguistic concepts, with specific consideration for {t['target_language']}.",
            "The explanation of the system architecture and linguistic-visual mapping is detailed and scientifically plausible.",
            "The response addresses cross-linguistic adaptation and interpretation challenges thoughtfully.",
            "Potential applications, ethical implications, and future directions are discussed insightfully.",
            "The total response is between 1000-1300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
