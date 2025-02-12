import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "quantum entanglement",
            "quantum superposition",
            "quantum coherence",
            "quantum tunneling"
        ]
        biological_systems = [
            "neural networks",
            "cellular membranes",
            "DNA replication",
            "protein folding"
        ]
        information_theories = [
            "Shannon entropy",
            "Kolmogorov complexity",
            "Integrated Information Theory",
            "Algorithmic Information Theory"
        ]
        
        tasks = [
            {
                "quantum_concept": random.choice(quantum_concepts),
                "biological_system": random.choice(biological_systems),
                "information_theory": random.choice(information_theories)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that integrates quantum physics, biology, and information theory to explain consciousness and information processing in living systems. Your model should incorporate {t['quantum_concept']} from quantum physics, focus on {t['biological_system']} in biological systems, and utilize {t['information_theory']} from information theory. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how {t['quantum_concept']} could play a role in consciousness and information processing in living systems.
   b) Describe how {t['biological_system']} might exhibit quantum effects or properties.
   c) Discuss how {t['information_theory']} can be applied to understand consciousness in this context.
   d) Propose a unified model that integrates these concepts to explain consciousness.

2. Mathematical Formulation (250-300 words):
   a) Develop a mathematical representation of your model, incorporating elements from quantum physics, biology, and information theory.
   b) Explain the key variables, equations, or algorithms in your formulation.
   c) Discuss how your mathematical model captures the interplay between quantum effects, biological processes, and information processing.

3. Predictions and Testable Hypotheses (200-250 words):
   a) Describe at least two specific, testable predictions that your model makes about consciousness or information processing in living systems.
   b) Explain how these predictions differ from those of conventional theories of consciousness.
   c) Propose experiments or observations that could validate or refute your model.

4. Implications and Philosophical Considerations (250-300 words):
   a) Discuss the implications of your model for our understanding of consciousness, free will, and the nature of reality.
   b) Address how your model might resolve or reframe existing problems in consciousness studies (e.g., the hard problem of consciousness).
   c) Explore potential technological applications that could arise from your model.

5. Limitations and Future Directions (150-200 words):
   a) Acknowledge the limitations and potential criticisms of your model.
   b) Suggest areas for future research or refinement of your theory.
   c) Discuss how advancements in quantum biology or neuroscience might impact your model.

Ensure your response demonstrates a deep understanding of quantum physics, biology, neuroscience, and information theory. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative and speculative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model must incorporate {t['quantum_concept']} from quantum physics",
            f"The model must focus on {t['biological_system']} in biological systems",
            f"The model must utilize {t['information_theory']} from information theory",
            "The response should demonstrate interdisciplinary knowledge integration across quantum physics, biology, neuroscience, and information theory",
            "The mathematical formulation should be well-reasoned and clearly explained",
            "The model should make specific, testable predictions about consciousness or information processing in living systems",
            "The response should address philosophical implications and potential technological applications",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1150-1400 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
