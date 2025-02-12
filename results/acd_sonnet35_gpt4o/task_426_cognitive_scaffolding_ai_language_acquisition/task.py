import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "scaffolding_technique": "zone of proximal development",
                "language_aspect": "syntax acquisition",
                "target_language": "Mandarin Chinese"
            },
            {
                "scaffolding_technique": "guided participation",
                "language_aspect": "pragmatics and social cues",
                "target_language": "Arabic"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that implements cognitive scaffolding techniques for language acquisition, focusing on the {t['scaffolding_technique']} technique for {t['language_aspect']} in {t['target_language']}. Your response should include the following sections:

1. Theoretical Foundation (200-250 words):
   - Explain the concept of {t['scaffolding_technique']} and its role in human language acquisition.
   - Discuss how this technique specifically applies to {t['language_aspect']}.
   - Describe any unique challenges or considerations for applying this technique to {t['target_language']}.

2. AI System Architecture (250-300 words):
   - Design an AI system that implements the {t['scaffolding_technique']} for {t['language_aspect']} acquisition.
   - Describe the key components of your system and how they interact.
   - Explain how your system simulates or adapts the scaffolding process for AI language learning.
   - Include a high-level diagram or pseudocode to illustrate your architecture.

3. Learning Process Simulation (200-250 words):
   - Describe how your AI system would progress through the language acquisition process.
   - Provide a specific example of how it would learn an aspect of {t['language_aspect']} in {t['target_language']}.
   - Explain how the system would adjust its scaffolding as the AI's language proficiency improves.

4. Comparative Analysis (200-250 words):
   - Compare your cognitive scaffolding approach to traditional machine learning methods for language acquisition.
   - Discuss potential advantages and limitations of your approach.
   - Propose a method to evaluate the effectiveness of your system compared to existing language learning AI.

5. Ethical Considerations and Future Directions (150-200 words):
   - Discuss any ethical implications of using cognitive scaffolding techniques in AI language acquisition.
   - Propose two potential applications of your system beyond language learning.
   - Suggest one area for future research or improvement in cognitive scaffolding for AI.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['scaffolding_technique']} and its application to {t['language_aspect']}.",
            f"The AI system design must specifically address how it implements {t['scaffolding_technique']} for learning {t['target_language']}.",
            "The learning process simulation should provide a concrete example of language acquisition using the proposed system.",
            "The comparative analysis should offer insightful comparisons between the proposed approach and traditional methods.",
            "The response should demonstrate creativity and innovation while maintaining scientific plausibility.",
            "All sections should be comprehensive, well-reasoned, and demonstrate interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
