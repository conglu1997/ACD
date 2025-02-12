import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_problems = [
            {
                "name": "The Hard Problem of Consciousness",
                "description": "How and why we have qualia or phenomenal experiences"
            },
            {
                "name": "The Chinese Room Argument",
                "description": "Whether a computer can truly understand language or merely simulate understanding"
            }
        ]
        return {
            "1": random.choice(philosophical_problems),
            "2": random.choice(philosophical_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel cognitive architecture inspired by both biological and artificial neural networks, then use it to explore {t['name']}: {t['description']}. Your response should include:

1. Cognitive Architecture Design (300-350 words):
   a) Describe the key components of your cognitive architecture.
   b) Explain how it incorporates principles from both biological neural networks and artificial neural networks.
   c) Discuss any novel features that distinguish it from existing architectures.
   d) Provide a diagram or detailed description of the architecture's structure.

2. Neuroscientific Basis (200-250 words):
   a) Explain which specific neuroscientific principles or findings your architecture is based on.
   b) Discuss how these principles are implemented in your design.
   c) Describe any simplifications or abstractions you've made from biological reality.

3. Computational Implementation (200-250 words):
   a) Describe how your architecture could be implemented computationally.
   b) Explain any novel algorithms or data structures you would use.
   c) Discuss potential challenges in implementing this architecture and propose solutions.

4. Philosophical Problem Exploration (300-350 words):
   a) Apply your cognitive architecture to explore the given philosophical problem.
   b) Explain how specific features of your architecture address aspects of the problem.
   c) Discuss any new insights or perspectives your architecture might provide on the problem.
   d) Consider potential objections to your approach and provide counterarguments.

5. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your architecture for AI and cognitive science.
   b) Propose two potential experiments or studies to further explore or validate your architecture.
   c) Suggest how your approach might be extended to other problems in philosophy of mind.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind. Be creative and innovative in your design while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.

Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind.",
            "The cognitive architecture design is novel, well-explained, and incorporates principles from both biological and artificial neural networks.",
            "The neuroscientific basis is clearly explained and accurately reflects current scientific understanding.",
            "The computational implementation is feasible and innovative.",
            "The exploration of the philosophical problem using the designed architecture is insightful and well-reasoned.",
            "The implications and future directions are thoughtful and demonstrate a broad understanding of the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
