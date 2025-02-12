import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_phenomena = [
            "decision making",
            "memory retrieval",
            "conceptual combination",
            "cognitive dissonance"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference",
            "contextuality"
        ]
        applications = [
            "predicting consumer behavior",
            "enhancing AI learning algorithms",
            "modeling social dynamics",
            "improving mental health treatments"
        ]
        return {
            "1": {
                "cognitive_phenomenon": random.choice(cognitive_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "application": random.choice(applications)
            },
            "2": {
                "cognitive_phenomenon": random.choice(cognitive_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human cognitive processes using principles from quantum mechanics, focusing on the cognitive phenomenon of {t['cognitive_phenomenon']}. Your system should incorporate the quantum principle of {t['quantum_principle']} and be applied to {t['application']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key aspects of the specified cognitive phenomenon.
   b) Describe how the given quantum principle can be applied to model this phenomenon.
   c) Discuss the potential advantages of using a quantum-inspired approach for this cognitive process.

2. AI System Architecture (300-350 words):
   a) Outline your quantum-inspired AI system for modeling the cognitive phenomenon.
   b) Explain how it incorporates the specified quantum principle.
   c) Describe the key components and their roles in the cognitive modeling process.
   d) Include at least one equation or formal representation of a critical component in your system.

3. Implementation Strategy (200-250 words):
   a) Discuss how your AI system would be implemented, considering current technological limitations.
   b) Explain any data requirements or preprocessing needed for your approach.
   c) Address potential scalability issues and how they might be overcome.

4. Application and Predictions (200-250 words):
   a) Describe how your system would be applied to {t['application']}.
   b) Provide specific examples of insights or predictions your system might generate.
   c) Discuss how these predictions differ from classical cognitive models.

5. Evaluation Methodology (150-200 words):
   a) Propose methods to evaluate the performance and accuracy of your quantum cognition model.
   b) Discuss how you would compare its performance to classical cognitive modeling approaches.
   c) Address potential challenges in validating a quantum-inspired cognitive model.

6. Ethical and Philosophical Implications (150-200 words):
   a) Analyze the ethical considerations of modeling human cognition using quantum-inspired AI.
   b) Discuss the philosophical implications of applying quantum principles to understanding the mind.
   c) Propose guidelines for responsible development and use of quantum cognition models.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary. Your total response should be between 1250-1550 words.

Format your response with clear headings for each section and use subheadings where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['cognitive_phenomenon']} and {t['quantum_principle']}.",
            "The AI system architecture is clearly explained and incorporates the specified quantum principle in a plausible manner.",
            f"The application to {t['application']} is well-developed with specific examples and predictions.",
            "The evaluation methodology is sound and addresses the challenges of validating a quantum-inspired cognitive model.",
            "The ethical and philosophical implications are thoroughly discussed with thoughtful guidelines proposed.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
