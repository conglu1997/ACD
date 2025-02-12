import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {
                "aspect": "Global Workspace Theory",
                "description": "A model of consciousness where a 'global workspace' integrates and broadcasts information across specialized brain modules."
            },
            {
                "aspect": "Integrated Information Theory",
                "description": "A theory that consciousness is identical to certain types of information integration within a physical system."
            },
            {
                "aspect": "Quantum Coherence in Microtubules",
                "description": "The hypothesis that quantum effects in brain microtubules play a role in consciousness."
            }
        ]
        return {str(i+1): aspect for i, aspect in enumerate(random.sample(consciousness_aspects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network architecture that mimics the following aspect of human consciousness:

{t['aspect']}: {t['description']}

Your task is to create a novel quantum-inspired neural network that incorporates this aspect of consciousness. Provide your response in the following format:

1. Conceptual Framework (250-300 words):
   a) Explain how the given aspect of consciousness can be modeled using quantum computing principles.
   b) Describe the key quantum phenomena you will leverage in your design.
   c) Discuss how your approach differs from classical neural network architectures.

2. Network Architecture (300-350 words):
   a) Detail the components and structure of your quantum-inspired neural network.
   b) Explain how quantum principles are incorporated into each component.
   c) Describe the information flow and processing within your network.
   d) Include a high-level diagram or pseudocode representation of your architecture.

3. Consciousness Simulation (200-250 words):
   a) Explain how your network simulates or approximates the given aspect of consciousness.
   b) Provide a specific example of how your network would process information in a consciousness-like manner.
   c) Discuss any limitations or simplifications in your model compared to biological consciousness.

4. Training and Operation (200-250 words):
   a) Propose a method for training your quantum-inspired neural network.
   b) Describe how your network would operate once trained.
   c) Discuss any unique challenges in implementing or scaling your architecture.

5. Potential Applications (150-200 words):
   a) Suggest two potential applications of your quantum-inspired conscious AI system.
   b) Explain how these applications leverage the consciousness-like features of your network.
   c) Discuss any ethical considerations related to these applications.

6. Implications for AI and Neuroscience (150-200 words):
   a) Analyze how your model might contribute to our understanding of biological consciousness.
   b) Discuss potential impacts of your approach on the development of artificial general intelligence (AGI).
   c) Propose a testable hypothesis about consciousness that your model might help investigate.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and coherence. Your proposed quantum-inspired neural network should be grounded in current scientific understanding, even as it explores speculative ideas. Use appropriate technical terminology and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design must incorporate the given aspect of consciousness: {t['aspect']}",
            "The response should demonstrate a clear understanding of quantum computing principles",
            "The quantum-inspired neural network architecture should be novel and well-explained",
            "The submission should show how the network simulates or approximates the given aspect of consciousness",
            "The response should include plausible training and operation methods",
            "The potential applications and implications should be thoughtfully considered",
            "The response should demonstrate interdisciplinary knowledge integration",
            "The proposed design should be scientifically plausible and coherent",
            "The submission should follow the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
