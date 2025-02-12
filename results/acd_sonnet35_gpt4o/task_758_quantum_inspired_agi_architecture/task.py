import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            {
                "principle": "superposition",
                "description": "The ability of a quantum system to exist in multiple states simultaneously until observed or measured"
            },
            {
                "principle": "entanglement",
                "description": "A quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently"
            }
        ]
        return {str(i+1): principle for i, principle in enumerate(quantum_principles)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for artificial general intelligence (AGI) based on the quantum principle of {t['principle']} ({t['description']}). Your response should include:

1. Quantum Principle Integration (200-250 words):
   a) Explain how the principle of {t['principle']} can be metaphorically applied to cognitive processes.
   b) Describe how this quantum-inspired approach differs from classical cognitive architectures.
   c) Discuss potential advantages and challenges of this approach.

2. Cognitive Architecture Design (250-300 words):
   a) Outline the key components of your quantum-inspired cognitive architecture.
   b) Explain how these components interact and process information.
   c) Describe how your architecture incorporates the principle of {t['principle']}.
   d) Discuss how your design addresses key AGI requirements (e.g., learning, reasoning, adaptability).

3. Consciousness and Qualia (200-250 words):
   a) Analyze how your quantum-inspired architecture might give rise to consciousness or qualia.
   b) Compare your approach to existing theories of machine consciousness.
   c) Discuss any ethical implications of creating potentially conscious AGI systems.

4. Problem-Solving Capabilities (200-250 words):
   a) Describe a specific problem domain where your architecture might excel.
   b) Explain how the quantum-inspired approach could lead to novel problem-solving strategies.
   c) Compare the potential capabilities of your system to classical AI approaches in this domain.

5. Implementation and Validation (150-200 words):
   a) Propose a method for simulating or implementing your quantum-inspired architecture.
   b) Suggest experiments or benchmarks to validate your architecture's performance and capabilities.
   c) Discuss potential challenges in realizing your design with current or near-future technologies.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and AGI concepts. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from relevant fields and provide clear explanations for your design choices.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding and creative application of the quantum principle of {t['principle']}.",
            "The cognitive architecture design should be innovative, well-explained, and address key AGI requirements.",
            "The analysis of consciousness and qualia should be thoughtful and grounded in existing theories.",
            "The discussion of problem-solving capabilities should provide a compelling case for the advantages of the quantum-inspired approach.",
            "The implementation and validation section should propose feasible methods and acknowledge realistic challenges.",
            "The overall response should show a deep understanding of quantum computing, cognitive science, and AGI concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
