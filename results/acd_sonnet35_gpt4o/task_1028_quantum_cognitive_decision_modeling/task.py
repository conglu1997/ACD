class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "scenario": "Career decision-making",
                "quantum_concept": "Superposition",
                "context": "A recent graduate choosing between multiple job offers in different fields and locations"
            },
            "2": {
                "scenario": "Ethical dilemma resolution",
                "quantum_concept": "Entanglement",
                "context": "A medical researcher deciding whether to publish potentially controversial findings"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model for complex decision-making processes, apply it to the scenario of {t['scenario']}, and analyze its implications for our understanding of human cognition. Your model should incorporate the quantum concept of {t['quantum_concept']}. The specific context for your scenario is: {t['context']}.

Provide your response in the following format:

1. Quantum Cognitive Model (250-300 words):
   a) Describe the key components and structure of your quantum-inspired cognitive model.
   b) Explain how you've incorporated the quantum concept of {t['quantum_concept']} into your model.
   c) Discuss how your model represents decision states, cognitive processes, and outcome probabilities.
   d) Include at least one mathematical formulation or equation that is central to your model.

2. Application to Scenario (200-250 words):
   a) Apply your quantum cognitive model to the given scenario and context.
   b) Explain how the model represents the decision-making process in this specific context.
   c) Describe how the quantum concept of {t['quantum_concept']} influences the decision outcomes in your model.
   d) Provide a hypothetical example of how an individual's decision might evolve according to your model.

3. Model Analysis (200-250 words):
   a) Discuss the strengths and limitations of your quantum-inspired cognitive model.
   b) Compare your model to traditional (non-quantum) cognitive decision-making models.
   c) Propose an experiment that could potentially validate or refute your model.

4. Cognitive Implications (150-200 words):
   a) Analyze how your model challenges or extends current understanding of human cognition.
   b) Discuss potential implications of your model for fields such as psychology, neuroscience, or artificial intelligence.
   c) Speculate on how quantum-inspired models might influence future research in cognitive science.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of applying quantum concepts to human cognition.
   b) Address concerns about determinism, free will, or consciousness that your model might raise.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. While being creative in your approach, maintain scientific plausibility and rigor. Your model should be speculative but grounded in current scientific understanding. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science, integrating concepts from both fields creatively and plausibly.",
            "The quantum cognitive model is well-defined, incorporating the specified quantum concept in a meaningful way, with at least one relevant mathematical formulation or equation.",
            "The application to the given scenario and context is thorough and logically consistent with the proposed model.",
            "The analysis of the model's strengths, limitations, and comparison to traditional models is insightful and well-reasoned.",
            "The discussion of cognitive implications and potential future research directions is thoughtful and grounded in current scientific understanding.",
            "The response addresses ethical considerations related to the model in a nuanced manner.",
            "The writing is clear, well-structured, and adheres to the specified word limits and format requirements.",
            "The model and its application strike a balance between creativity and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
