import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Interference"
        ]
        linguistic_aspects = [
            "Semantic Analysis",
            "Syntactic Parsing",
            "Pragmatic Interpretation"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_aspect": random.choice(linguistic_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system that leverages the quantum computing principle of {t['quantum_principle']} to enhance {t['linguistic_aspect']}. Your response should include:

1. System Overview (200-250 words):
   a) Describe the key components of your quantum-inspired NLP system.
   b) Explain how it incorporates the given quantum principle.
   c) Outline how it enhances the specified linguistic aspect.

2. Quantum-Linguistic Integration (200-250 words):
   a) Explain the theoretical basis for applying {t['quantum_principle']} to {t['linguistic_aspect']}.
   b) Describe how this integration could potentially outperform classical NLP approaches.
   c) Discuss any challenges in implementing this quantum-inspired approach.

3. Algorithm Design (150-200 words):
   a) Provide a high-level description of a key algorithm in your system.
   b) Include a simple pseudocode representation (5-10 lines) of this algorithm.
   c) Explain how the algorithm leverages quantum principles.

4. Potential Applications (150-200 words):
   a) Propose two specific applications of your quantum-inspired NLP system.
   b) Explain how each application could benefit from the quantum enhancement.

5. Evaluation Framework (150-200 words):
   a) Suggest a method for evaluating the performance of your system.
   b) Propose specific metrics for measuring improvements in {t['linguistic_aspect']}.
   c) Describe a hypothetical experiment to test your system's effectiveness.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical implications of your quantum-inspired NLP system.
   b) Propose guidelines for responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theories, and AI architectures. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content",
            "The system design clearly incorporates the given quantum principle and enhances the specified linguistic aspect",
            "The response demonstrates a deep understanding of quantum computing, linguistics, and AI",
            "The algorithm design includes a relevant pseudocode representation",
            "The proposed applications and evaluation framework are well-reasoned and specific",
            "The response addresses ethical considerations and proposes responsible development guidelines",
            "The overall response is creative, scientifically plausible, and well-explained"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
