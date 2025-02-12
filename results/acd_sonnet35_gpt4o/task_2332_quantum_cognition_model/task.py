import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Wave function collapse",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        cognitive_processes = [
            "Attention",
            "Memory formation",
            "Decision making",
            "Perception",
            "Emotional processing"
        ]
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a speculative model of consciousness that integrates the quantum mechanical principle of {t['quantum_principle']} with the cognitive process of {t['cognitive_process']}. Your response should include:

1. Model Description (250-300 words):
   a) Describe your proposed model of consciousness, explaining how it incorporates both the quantum principle and the cognitive process.
   b) Discuss the key components and mechanisms of your model.
   c) Explain how your model accounts for subjective experience or qualia.

2. Quantum-Cognitive Integration (200-250 words):
   a) Elaborate on how the quantum principle {t['quantum_principle']} is specifically applied to the cognitive process {t['cognitive_process']}.
   b) Discuss any novel emergent properties that arise from this integration.
   c) Address potential criticisms of applying quantum mechanics to cognitive processes.

3. Testable Predictions (150-200 words):
   a) Propose at least two testable predictions that your model makes about consciousness or cognition.
   b) Describe potential experiments or observations that could validate or refute these predictions.

4. Philosophical Implications (150-200 words):
   a) Discuss the philosophical implications of your model for our understanding of consciousness and free will.
   b) Compare your model to existing theories of consciousness, highlighting key differences and similarities.

5. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or weaknesses in your proposed model.
   b) Suggest future research directions or extensions of your model.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified quantum principle and cognitive process",
            "The proposed model creatively integrates concepts from quantum mechanics and cognitive science",
            "The model description is clear, coherent, and scientifically plausible",
            "The response includes testable predictions and potential experiments",
            "The philosophical implications are thoughtfully discussed",
            "Limitations and future directions are adequately addressed",
            "The response shows originality and innovative thinking in approaching the complex topic of consciousness"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
