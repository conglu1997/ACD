import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        memory_processes = [
            "encoding",
            "consolidation",
            "retrieval",
            "reconsolidation"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "memory_process": random.choice(memory_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "memory_process": random.choice(memory_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum biological model of {t['memory_process']} in human memory, incorporating the quantum principle of {t['quantum_principle']}. Your response should include:

1. Quantum-Biological Model (300-350 words):
   a) Describe your model, explaining how it incorporates the specified quantum principle into the memory process.
   b) Explain how your model accounts for known neurobiological aspects of memory.
   c) Discuss how your model differs from classical neuroscientific explanations of memory.
   d) Provide a conceptual diagram or detailed description of your model's key components and interactions. (You may use ASCII art or a text-based representation for the diagram)

2. Quantum Mechanisms (200-250 words):
   a) Explain in detail how the specified quantum principle manifests in your model.
   b) Describe the potential advantages of quantum processes in memory function.
   c) Address potential criticisms regarding the plausibility of quantum effects in the warm, wet environment of the brain.

3. Predictions and Testable Hypotheses (200-250 words):
   a) Derive at least two specific, testable predictions from your model.
   b) Explain how these predictions differ from those of classical memory models.
   c) Propose experiments to test these predictions, considering both behavioral and neuroimaging approaches.

4. Information Theoretical Analysis (150-200 words):
   a) Analyze your model from an information theory perspective.
   b) Discuss how quantum principles might affect information storage and retrieval capacity in the brain.
   c) Compare the theoretical efficiency of your quantum model to classical neural network models of memory.

5. Implications for Artificial Intelligence (150-200 words):
   a) Discuss how your quantum biological model of memory could inform the development of quantum-inspired AI systems.
   b) Propose a novel AI architecture based on your model.
   c) Speculate on the potential advantages and challenges of implementing such a system.

6. Ethical Considerations and Societal Impact (100-150 words):
   a) Discuss ethical implications of developing quantum biological models of cognition.
   b) Consider potential societal impacts if such models lead to enhanced memory technologies.
   c) Propose guidelines for responsible research and application in this field.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and information theory. Be creative and original in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and neuroscience.",
            "The quantum biological model is innovative, well-explained, and scientifically plausible.",
            "The model effectively incorporates the specified quantum principle and memory process.",
            "A conceptual diagram or detailed description of the model is provided.",
            "The quantum mechanisms are thoroughly explained and potential criticisms are addressed.",
            "The predictions and proposed experiments are specific, testable, and logically derived from the model.",
            "The information theoretical analysis is insightful and compares quantum and classical approaches.",
            "The implications for AI are creative and well-reasoned.",
            "Ethical considerations and societal impacts are thoughtfully addressed.",
            "The response is within the specified word count range (1100-1400 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
