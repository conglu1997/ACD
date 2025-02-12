class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_property": "superposition",
                "neural_process": "synaptic plasticity",
                "musical_element": "harmony",
                "emotional_state": "melancholy"
            },
            "2": {
                "quantum_property": "entanglement",
                "neural_process": "neural oscillations",
                "musical_element": "rhythm",
                "emotional_state": "excitement"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates neural processes to compose music based on specific emotional states and musical theory principles. Your system should incorporate the following elements:

Quantum property: {t['quantum_property']}
Neural process: {t['neural_process']}
Musical element: {t['musical_element']}
Emotional state: {t['emotional_state']}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum neural music composition system.
   b) Explain how the specified quantum property is utilized in the system.
   c) Detail how the neural process is simulated using quantum computing.
   d) Discuss how the system incorporates the given musical element and emotional state.

2. Quantum-Neural Interface (200-250 words):
   a) Explain how quantum states are mapped to neural activity patterns.
   b) Describe the mechanism for translating quantum computations into simulated neural processes.
   c) Discuss any novel approaches or algorithms used in this interface.

3. Music Generation Process (200-250 words):
   a) Detail the step-by-step process of how your system generates music.
   b) Explain how the specified musical element is implemented in the composition process.
   c) Describe how the system ensures the composed music reflects the given emotional state.

4. Theoretical Foundation (150-200 words):
   a) Provide the theoretical basis for using quantum computing in neural simulation for music composition.
   b) Explain how your approach advances current understanding in this interdisciplinary field.

5. Challenges and Solutions (150-200 words):
   a) Identify key technical challenges in implementing this system.
   b) Propose innovative solutions to these challenges.
   c) Discuss any limitations of your approach and potential future improvements.

6. Ethical and Artistic Implications (100-150 words):
   a) Discuss the ethical considerations of using AI and quantum computing in artistic creation.
   b) Explore the potential impact of this technology on human creativity and the music industry.

7. Evaluation Framework (100-150 words):
   a) Propose a method to evaluate the quality and emotional accuracy of the composed music.
   b) Describe how you would measure the system's performance compared to traditional composition methods.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively incorporates the specified quantum property ({t['quantum_property']}) in the system design.",
            f"The neural process ({t['neural_process']}) is accurately simulated using quantum computing principles.",
            f"The system convincingly implements the given musical element ({t['musical_element']}) in the composition process.",
            f"The design ensures that the composed music reflects the specified emotional state ({t['emotional_state']}).",
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and music theory.",
            "The proposed system presents an innovative and plausible approach to quantum neural music composition.",
            "The response addresses ethical implications and provides a thoughtful evaluation framework.",
            "The overall response is well-structured, coherent, and adheres to the word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
