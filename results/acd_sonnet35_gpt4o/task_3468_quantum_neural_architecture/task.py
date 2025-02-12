import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_structure": "Cerebellum",
                "quantum_concept": "Superposition",
                "application": "Quantum error correction"
            },
            {
                "brain_structure": "Neocortex",
                "quantum_concept": "Entanglement",
                "application": "Quantum machine learning"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum neural network architecture inspired by the {t['brain_structure']}, incorporating the quantum concept of {t['quantum_concept']}. Then, apply your architecture to solve a complex problem in {t['application']}. Your response should include the following sections:

1. Neuroanatomical Basis (200-250 words):
   a) Describe the key features and functions of the {t['brain_structure']}.
   b) Explain how these features inform your quantum neural network design.
   c) Discuss any challenges in translating biological neural structures to quantum systems.

2. Quantum Neural Architecture (250-300 words):
   a) Present your quantum neural network architecture, explaining its key components and how they operate.
   b) Describe how you've incorporated the quantum concept of {t['quantum_concept']} into your design.
   c) Explain how your architecture mimics or improves upon the functionality of the {t['brain_structure']}.
   d) Include a text-based representation of your architecture (e.g., ASCII diagram or detailed textual description).

3. Quantum-Neural Integration (200-250 words):
   a) Analyze the theoretical advantages of your quantum neural approach compared to classical neural networks.
   b) Discuss potential limitations or challenges in implementing your architecture.
   c) Explain how your architecture maintains quantum coherence while performing neural network-like operations.

4. Application to {t['application']} (250-300 words):
   a) Describe how you would apply your quantum neural architecture to solve a specific problem in {t['application']}.
   b) Explain the step-by-step process of how your architecture would approach this problem.
   c) Compare your approach to current methods in {t['application']}, highlighting potential advantages.
   d) Discuss any novel insights or capabilities your architecture might bring to this field.

5. Theoretical Implications (150-200 words):
   a) Discuss the broader implications of your quantum neural architecture for quantum computing and neuroscience.
   b) Propose two testable hypotheses derived from your architecture.
   c) Suggest potential impacts on our understanding of quantum systems or brain function.

6. Future Research Directions (100-150 words):
   a) Propose two potential extensions or modifications to your architecture for future research.
   b) Briefly outline an experimental approach to validate or refine your quantum neural model.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1150-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['brain_structure']}, the quantum concept of {t['quantum_concept']}, and {t['application']}.",
            "The quantum neural architecture is innovative, well-described, and plausibly integrates neuroanatomical principles with quantum computing concepts.",
            f"The application to {t['application']} is clearly explained and demonstrates potential advantages over current methods.",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving.",
            "The theoretical implications and future research directions are insightful and well-reasoned.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
