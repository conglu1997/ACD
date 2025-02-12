import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "Metaphor Understanding",
                "input_concepts": ["Time", "Money"],
                "target_application": "Financial Planning AI"
            },
            {
                "domain": "Creative Problem Solving",
                "input_concepts": ["Quantum Mechanics", "Social Networks"],
                "target_application": "Innovative Search Algorithm"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system based on the cognitive theory of conceptual blending, focusing on the domain of {t['domain']}. Your system should be capable of blending the concepts of {t['input_concepts'][0]} and {t['input_concepts'][1]}, with the goal of creating a {t['target_application']}. Provide your response in the following format:

1. Conceptual Blending Theory Overview (150-200 words):
   Briefly explain the cognitive theory of conceptual blending and its relevance to AI.

2. AI System Architecture (250-300 words):
   a) Describe the main components of your AI system and how they implement conceptual blending.
   b) Explain how your system represents and processes the input concepts.
   c) Detail the blending mechanisms and how they generate novel outputs.
   d) Discuss how your system evaluates and refines the blended concepts.

3. Application to {t['domain']} (200-250 words):
   a) Explain how your system blends {t['input_concepts'][0]} and {t['input_concepts'][1]}.
   b) Provide an example output from your system, demonstrating a novel blended concept.
   c) Analyze how this blended concept contributes to the {t['target_application']}.

4. Learning and Adaptation (150-200 words):
   Describe how your system could learn from feedback and adapt its blending processes over time.

5. Comparative Analysis (200-250 words):
   Compare your conceptual blending AI system to traditional approaches in {t['domain']}, discussing advantages and potential limitations.

6. Ethical Implications (150-200 words):
   Discuss the ethical considerations of implementing a conceptual blending AI system, particularly in the context of {t['target_application']}.

7. Future Research Directions (100-150 words):
   Propose two specific research questions or experiments to further develop and validate your conceptual blending AI system.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific domain of application. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a design for an AI system based on conceptual blending theory, applied to {t['domain']}",
            f"The system should demonstrate the blending of {t['input_concepts'][0]} and {t['input_concepts'][1]}",
            f"The response should explain how the system contributes to creating a {t['target_application']}",
            "The answer should show understanding of cognitive science, AI, and the specific domain of application",
            "The response should include creative yet scientifically plausible ideas",
            "The ethical implications of the system should be thoughtfully discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
