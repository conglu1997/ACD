import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_function': 'decision making',
                'philosophical_question': 'free will',
                'comparison_aspect': 'adaptability to novel situations'
            },
            {
                'cognitive_function': 'memory formation and retrieval',
                'philosophical_question': 'nature of consciousness',
                'comparison_aspect': 'emotional influence on cognition'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial cognitive architecture that models the cognitive function of {t['cognitive_function']}. Your task has four parts:

1. Architecture Design (300-350 words):
   - Describe the components and processes of your artificial cognitive architecture.
   - Explain how it models {t['cognitive_function']}.
   - Include a diagram or flowchart representing your architecture (describe it textually).

2. Comparison with Human Cognition (250-300 words):
   - Compare your artificial architecture with human cognition, focusing on {t['comparison_aspect']}.
   - Discuss similarities and differences, and explain the reasoning behind your design choices.

3. Philosophical Analysis (250-300 words):
   - Discuss how your architecture relates to the philosophical question of {t['philosophical_question']}.
   - Explain any insights or challenges your model presents for this philosophical issue.

4. Evaluation and Limitations (200-250 words):
   - Propose a method to evaluate the performance of your cognitive architecture.
   - Discuss potential limitations of your design and suggest areas for future improvement.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and philosophy of mind. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response as follows:

Architecture Design:
[Your design description]

Comparison with Human Cognition:
[Your comparison]

Philosophical Analysis:
[Your analysis]

Evaluation and Limitations:
[Your evaluation and limitations discussion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of an artificial cognitive architecture modeling {t['cognitive_function']}.",
            f"The architecture is compared to human cognition, focusing on {t['comparison_aspect']}.",
            f"The design is analyzed in relation to the philosophical question of {t['philosophical_question']}.",
            "The response proposes a method to evaluate the architecture and discusses its limitations.",
            "The design demonstrates creativity while maintaining scientific plausibility.",
            "The response shows a deep understanding of cognitive science, AI, and philosophy of mind."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
