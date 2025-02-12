import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = ['superposition', 'entanglement', 'tunneling', 'decoherence']
        cognitive_processes = ['decision-making', 'memory formation', 'attention', 'consciousness']
        constraints = ['energy efficiency', 'speed of processing', 'scalability', 'biological plausibility']
        
        tasks = [
            {
                'quantum_concept': random.choice(quantum_concepts),
                'cognitive_process': random.choice(cognitive_processes),
                'constraint': random.choice(constraints)
            },
            {
                'quantum_concept': random.choice(quantum_concepts),
                'cognitive_process': random.choice(cognitive_processes),
                'constraint': random.choice(constraints)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model that explains the cognitive process of {t['cognitive_process']}, incorporating the quantum concept of {t['quantum_concept']}, while addressing the constraint of {t['constraint']}. Your response should include:

1. Model Overview (250-300 words):
   a) Describe the key components and principles of your quantum-inspired cognitive model.
   b) Explain how it incorporates the specified quantum concept into the cognitive process.
   c) Discuss how your model addresses the given constraint.

2. Quantum Mechanics Integration (200-250 words):
   a) Detail how the specified quantum concept is applied in your model.
   b) Explain how this quantum concept enhances our understanding of the cognitive process.
   c) Provide a mathematical or conceptual representation of a quantum operation in your model.

3. Neuroscientific Basis (200-250 words):
   a) Describe the neurobiological foundations of your model.
   b) Explain how your model aligns with current neuroscientific understanding of the cognitive process.
   c) Discuss any novel predictions or insights your model generates about brain function.

4. Artificial Intelligence Application (150-200 words):
   a) Propose how your quantum-inspired cognitive model could be implemented in an AI system.
   b) Discuss potential advantages and challenges of this implementation.
   c) Explain how this AI system might differ from classical approaches to modeling the same cognitive process.

5. Experimental Predictions (150-200 words):
   a) Describe two testable predictions that your model makes about human cognition or behavior.
   b) Outline an experimental setup to test one of these predictions.
   c) Discuss potential implications of these experiments for our understanding of quantum effects in cognition.

6. Philosophical Implications (100-150 words):
   a) Analyze the philosophical implications of your model, particularly regarding consciousness and free will.
   b) Discuss how your model might contribute to debates in philosophy of mind or cognitive science.

7. Ethical Considerations and Future Directions (100-150 words):
   a) Identify potential ethical concerns related to the development or application of your model.
   b) Propose guidelines for responsible research in this area.
   c) Suggest two future research directions that could extend or refine your model.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum concept and its application to the cognitive process.",
            "The model effectively addresses the given constraint while maintaining scientific plausibility.",
            "The integration of quantum mechanics, neuroscience, and artificial intelligence is well-explained and innovative.",
            "The experimental predictions and proposed tests are logical and well-designed.",
            "The philosophical and ethical implications are thoughtfully considered.",
            "The response shows creativity and originality in approach while maintaining scientific rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
