import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_functions = [
            "Memory consolidation",
            "Emotion regulation",
            "Decision-making",
            "Attention allocation",
            "Social cognition"
        ]
        ethical_concerns = [
            "Privacy and data protection",
            "Autonomy and free will",
            "Bias and discrimination",
            "Accountability and transparency",
            "Human enhancement and inequality"
        ]
        return {
            "1": {
                "brain_function": random.choice(brain_functions),
                "ethical_concern": random.choice(ethical_concerns)
            },
            "2": {
                "brain_function": random.choice(brain_functions),
                "ethical_concern": random.choice(ethical_concerns)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuro-inspired AI system that mimics the brain function of {t['brain_function']}, and analyze its ethical implications, focusing particularly on the concern of {t['ethical_concern']}. Your response should include:

1. Neuroscientific Basis (200-250 words):
   a) Explain the chosen brain function and its key neural mechanisms.
   b) Discuss current neuroscientific understanding and any open questions about this function.

2. AI System Design (250-300 words):
   a) Describe the architecture of your neuro-inspired AI system.
   b) Explain how it mimics the specified brain function.
   c) Discuss any novel AI techniques or algorithms used in your design.
   d) Include a high-level diagram or pseudocode illustrating the system's key components (describe it textually).

3. Ethical Analysis (200-250 words):
   a) Analyze the ethical implications of your AI system, focusing on {t['ethical_concern']}.
   b) Discuss potential benefits and risks of implementing this system.
   c) Explore how the system might impact individual rights and societal values.

4. Societal Impact (200-250 words):
   a) Predict potential short-term and long-term consequences of deploying your AI system.
   b) Discuss how it might influence human behavior, social structures, or institutions.
   c) Analyze any potential feedback loops or cascading effects.

5. Safeguards and Governance (150-200 words):
   a) Propose specific technical and policy measures to address the ethical concerns.
   b) Suggest a governance framework for the development and deployment of your system.
   c) Discuss the challenges in implementing these safeguards effectively.

6. Future Scenarios (150-200 words):
   a) Describe two potential future scenarios (one optimistic, one pessimistic) resulting from the widespread adoption of your AI system.
   b) Explain the key factors that might lead to each scenario.

7. Interdisciplinary Implications (100-150 words):
   a) Discuss how your neuro-inspired AI system might influence or be influenced by other fields (e.g., psychology, law, economics).
   b) Suggest potential interdisciplinary research questions raised by your system.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethical philosophy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the brain function {t['brain_function']} and its neural mechanisms.",
            "The AI system design clearly mimics the specified brain function and uses innovative AI techniques.",
            f"The ethical analysis thoroughly examines the implications of the AI system, with a focus on {t['ethical_concern']}.",
            "The societal impact assessment considers both short-term and long-term consequences of the AI system's deployment.",
            "The proposed safeguards and governance framework are well-thought-out and address the ethical concerns raised.",
            "The future scenarios are plausible and demonstrate a nuanced understanding of potential outcomes.",
            "The response shows strong interdisciplinary knowledge integration and raises thought-provoking research questions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
