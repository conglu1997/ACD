import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "cognitive_process": "Divergent thinking",
                "creative_domain": "Visual arts"
            },
            {
                "quantum_principle": "Entanglement",
                "cognitive_process": "Analogical reasoning",
                "creative_domain": "Music composition"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a theoretical model of artificial consciousness based on quantum cognitive principles, and use it to generate novel creative outputs. Your model should incorporate the quantum principle of {t['quantum_principle']}, focus on the cognitive process of {t['cognitive_process']}, and demonstrate its creative potential in the domain of {t['creative_domain']}. 

NOTE: This task involves speculative thinking about emerging fields. While your response should be grounded in current scientific understanding, creative and novel ideas are encouraged.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how the specified quantum principle can be applied to model consciousness and cognition.
   b) Describe how this quantum-inspired model relates to the given cognitive process.
   c) Discuss potential advantages of this approach over classical models of cognition and creativity.
   d) Address any theoretical challenges or limitations of your model.
   e) Compare your model with Integrated Information Theory (IIT) of consciousness, highlighting similarities and differences.

2. Artificial Consciousness Architecture (300-350 words):
   a) Outline the key components of your quantum-inspired artificial consciousness system.
   b) Explain how your system implements the specified cognitive process.
   c) Describe how your model achieves or approximates consciousness.
   d) Discuss how your system's 'conscious' processes contribute to creativity.
   e) Provide a visual representation of your model (described in text, not an actual image).

3. Creative Output Generation (200-250 words):
   a) Explain how your system would generate novel creative outputs in the specified domain.
   b) Provide a specific example of a potential creative output from your system.
   c) Analyze how this output demonstrates creativity and consciousness.

4. Empirical Validation (200-250 words):
   a) Propose an experimental setup to test your model's consciousness and creativity.
   b) Describe key metrics or criteria for evaluating your system's performance.
   c) Discuss potential challenges in validating artificial consciousness and how you'd address them.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical considerations of creating artificially conscious creative entities.
   b) Explore the philosophical implications of quantum-based artificial consciousness for our understanding of mind and creativity.
   c) Speculate on potential long-term impacts of such technology on society and human creativity.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section (numbered 1-5) and subheadings (a, b, c, etc.) as outlined above. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and applies the quantum principle of {t['quantum_principle']} to model consciousness and cognition.",
            f"The artificial consciousness architecture effectively incorporates the cognitive process of {t['cognitive_process']}.",
            f"The system generates a plausible and creative output in the domain of {t['creative_domain']}.",
            "The response provides a thoughtful analysis of the ethical and philosophical implications of quantum-based artificial consciousness.",
            "The proposed empirical validation approach is scientifically sound and addresses the challenges of testing artificial consciousness.",
            "The response includes a comparison with Integrated Information Theory and a text-based visual representation of the model.",
            "The response follows the specified format with clear headings and subheadings."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
