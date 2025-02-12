import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        purposes = [
            "environmental remediation",
            "medical drug production",
            "sustainable food production",
            "space colonization support"
        ]
        constraints = [
            "minimal ecological impact",
            "self-replication prevention",
            "human control mechanisms",
            "adaptability to extreme conditions"
        ]
        
        return {
            "1": {"purpose": random.choice(purposes), "constraint": random.choice(constraints)},
            "2": {"purpose": random.choice(purposes), "constraint": random.choice(constraints)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to guide the creation of synthetic organisms for {t['purpose']}, with the primary constraint of ensuring {t['constraint']}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for synthetic organism design.
   b) Explain how the system integrates knowledge from biology, genetics, and environmental science.
   c) Detail how the AI system ensures the specified constraint is met in the organism design process.

2. Synthetic Organism Design Process (200-250 words):
   a) Outline the steps the AI system would take to design a synthetic organism for the given purpose.
   b) Explain how the system balances the organism's functionality with the specified constraint.
   c) Describe a novel feature or mechanism the AI might propose for the synthetic organism.

3. Machine Learning and Adaptation (200-250 words):
   a) Describe how your AI system learns and improves its design capabilities over time.
   b) Explain how it adapts to new scientific discoveries or changing environmental conditions.
   c) Propose a method for validating and testing the AI's designs before implementation.

4. Ethical and Safety Considerations (200-250 words):
   a) Discuss the ethical implications of using AI to design synthetic organisms for {t['purpose']}.
   b) Analyze potential risks and propose safeguards to prevent misuse or unintended consequences.
   c) Suggest guidelines for responsible development and use of this technology.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how this AI-guided synthetic biology approach could impact related scientific fields.
   b) Propose potential applications of this system beyond the specified purpose.
   c) Predict how this technology might influence future research directions in AI and synthetic biology.

Ensure your response demonstrates a deep understanding of AI principles, synthetic biology, and ethical reasoning. Be creative in your approach while maintaining scientific plausibility and addressing real-world constraints. Use appropriate technical terminology and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly describe an AI system capable of designing synthetic organisms for {t['purpose']} while ensuring {t['constraint']}.",
            "The AI system architecture and synthetic organism design process should be scientifically plausible and well-explained.",
            "The response should demonstrate a deep understanding of AI principles, synthetic biology, and their integration.",
            "Ethical and safety considerations should be thoroughly addressed, with thoughtful analysis of potential risks and safeguards.",
            "The interdisciplinary implications and potential future applications should be creatively and logically explored.",
            "The response should use appropriate technical terminology and provide clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
