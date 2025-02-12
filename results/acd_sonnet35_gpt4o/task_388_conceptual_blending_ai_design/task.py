import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "domain": "Climate change mitigation",
                "concept1": "Carbon sequestration",
                "concept2": "Urban planning"
            },
            {
                "domain": "Space exploration",
                "concept1": "Terraforming",
                "concept2": "Nanotechnology"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(domains, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses conceptual blending to generate novel ideas and solutions in the domain of {t['domain']}. Your task has the following parts:

1. Conceptual Blending Framework (200-250 words):
   a) Explain the theory of conceptual blending and its relevance to creative AI.
   b) Describe how your AI system would implement conceptual blending, including:
      - The method for representing and storing concepts
      - The process for selecting and combining concepts
      - The mechanism for evaluating and refining blended concepts

2. AI System Architecture (150-200 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Explain how different components work together to perform conceptual blending.
   c) Describe any novel or unique features of your system.

3. Application to {t['domain']} (200-250 words):
   a) Apply your AI system to blend the concepts of "{t['concept1']}" and "{t['concept2']}".
   b) Describe the resulting blended concept and how it could contribute to {t['domain']}.
   c) Explain the step-by-step process your AI system would follow to generate this blend.

4. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the quality and usefulness of the blended concepts.
   b) Describe how your AI system would refine and improve its blending process based on feedback or evaluation.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for conceptual blending in the context of {t['domain']}.
   b) Propose guidelines or safeguards to address these ethical concerns.

Ensure your response demonstrates a deep understanding of conceptual blending theory, AI system design, and the specific domain. Be creative and innovative in your approach while maintaining scientific rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of conceptual blending theory and its application to AI.",
            "The proposed AI system architecture is well-designed and clearly explained.",
            f"The application to {t['domain']} is creative and shows a good understanding of both {t['concept1']} and {t['concept2']}.",
            "The evaluation and refinement process is well-thought-out and feasible.",
            "Ethical considerations are addressed thoughtfully and comprehensively.",
            "The overall response is creative, well-structured, and demonstrates strong interdisciplinary reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
