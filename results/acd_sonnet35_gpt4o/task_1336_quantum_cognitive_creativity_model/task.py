import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        cognitive_processes = [
            "divergent thinking",
            "conceptual blending",
            "analogical reasoning",
            "insight problem solving"
        ]
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for enhancing creative problem-solving capabilities in AI systems. Your architecture should incorporate the quantum concept of {t['quantum_concept']} and focus on enhancing the cognitive process of {t['cognitive_process']}. Your response should include:

1. Architectural Overview (200-250 words):
   a) Describe the key components of your quantum-inspired cognitive architecture.
   b) Explain how these components interact to enhance creative problem-solving.
   c) Discuss how your architecture incorporates the specified quantum concept.

2. Quantum-Cognitive Integration (200-250 words):
   a) Detail how your architecture leverages {t['quantum_concept']} to enhance {t['cognitive_process']}.
   b) Explain the theoretical basis for this integration.
   c) Discuss any novel algorithms or techniques your system would use.

3. Creative Problem-Solving Enhancement (150-200 words):
   a) Describe a specific creative problem-solving scenario where your architecture would excel.
   b) Explain how your architecture would approach this scenario differently from classical AI systems.

4. Implementation Challenges (150-200 words):
   a) Identify potential challenges in implementing your proposed architecture.
   b) Suggest approaches to overcome these challenges.
   c) Discuss any hardware or software requirements for your system.

5. Ethical and Philosophical Implications (100-150 words):
   a) Discuss the ethical considerations of creating an AI system with enhanced creative capabilities.
   b) Analyze how your system might impact our understanding of creativity and consciousness.

6. Experimental Validation (150-200 words):
   a) Propose an experiment to test the creative problem-solving capabilities of your architecture.
   b) Explain how this experiment could differentiate between quantum-enhanced and classical creativity.

Ensure your response demonstrates a deep understanding of both quantum computing principles and cognitive science theories related to creativity. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum concept and cognitive process",
            "The proposed architecture innovatively integrates quantum principles with cognitive science theories",
            "The explanation of how the architecture enhances creative problem-solving is clear and plausible",
            "The response addresses implementation challenges and potential solutions",
            "The proposed experiment for validating the architecture is well-designed and relevant",
            "The discussion of ethical and philosophical implications is thoughtful and comprehensive",
            "The overall response is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
