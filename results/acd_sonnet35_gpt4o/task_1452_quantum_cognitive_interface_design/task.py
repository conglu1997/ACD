import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            "memory formation and retrieval",
            "decision-making processes",
            "pattern recognition and learning",
            "attention and focus",
            "emotional regulation",
            "language processing and acquisition"
        ]
        quantum_phenomena = [
            "superposition",
            "entanglement",
            "tunneling",
            "quantum coherence",
            "quantum annealing",
            "quantum error correction"
        ]
        return {
            "1": {
                "cognitive_function": random.choice(cognitive_functions),
                "quantum_phenomenon": random.choice(quantum_phenomena)
            },
            "2": {
                "cognitive_function": random.choice(cognitive_functions),
                "quantum_phenomenon": random.choice(quantum_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-cognitive interface that leverages {t['quantum_phenomenon']} to enhance human {t['cognitive_function']}. Then, analyze its implications for neuroscience, AI development, and ethics. Your response should include the following sections:

1. Interface Design (250-300 words):
   a) Describe the key components of your quantum-cognitive interface.
   b) Explain how it integrates {t['quantum_phenomenon']} with neural processes.
   c) Detail how this interface could potentially enhance {t['cognitive_function']}.
   d) Discuss any novel technologies or techniques required for your interface.

2. Neuroscientific Implications (200-250 words):
   a) Analyze how your interface might alter our understanding of neural processing.
   b) Propose a testable hypothesis about the interface's effects on brain function.
   c) Suggest an experimental design to investigate these effects.

3. AI Development Impact (200-250 words):
   a) Discuss how insights from your interface could influence AI architectures.
   b) Propose a novel AI algorithm or model inspired by your quantum-cognitive interface.
   c) Compare the potential capabilities of this AI system to current state-of-the-art models.

4. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues arising from the development and use of your interface.
   b) Discuss implications for cognitive enhancement, privacy, and human identity.
   c) Propose guidelines for the responsible development and use of quantum-cognitive technologies.

5. Limitations and Future Directions (150-200 words):
   a) Discuss current technological or scientific barriers to realizing your interface.
   b) Propose future research directions to overcome these limitations.
   c) Speculate on potential long-term impacts of quantum-cognitive interfaces on society.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate scientific terminology and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['quantum_phenomenon']} and its potential application to {t['cognitive_function']}.",
            "The interface design should be innovative yet scientifically plausible.",
            "The neuroscientific implications should be logically derived and include a testable hypothesis.",
            "The AI development impact should propose a novel and relevant AI algorithm or model.",
            "The ethical considerations should be comprehensive and thoughtful.",
            "The limitations and future directions should be realistic and insightful.",
            "The overall response should demonstrate interdisciplinary thinking and creative problem-solving.",
            "The response should adhere to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
