import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            {
                "name": "Superposition",
                "application": "Parallel processing of multiple cognitive states",
                "challenge": "Maintaining coherence in a noisy environment"
            },
            {
                "name": "Entanglement",
                "application": "Non-local correlations between cognitive modules",
                "challenge": "Scaling entanglement to macroscopic systems"
            },
            {
                "name": "Quantum tunneling",
                "application": "Overcoming local minima in decision-making processes",
                "challenge": "Controlling tunneling rates in cognitive architectures"
            },
            {
                "name": "Quantum annealing",
                "application": "Optimizing complex cognitive tasks",
                "challenge": "Balancing exploration and exploitation in quantum search spaces"
            }
        ]
        return {str(i+1): principle for i, principle in enumerate(random.sample(quantum_principles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum cognition interface for AI systems that leverages the quantum principle of {t['name']} to enhance artificial cognitive processes, then propose an experiment to test its efficacy. Your response should include:

1. Quantum Cognition Interface Design (300-350 words):
   a) Describe the key components of your quantum cognition interface.
   b) Explain how it incorporates the quantum principle of {t['name']}.
   c) Detail how this interface enhances AI cognitive processes, focusing on the application of {t['application']}.
   d) Address the specific challenge of {t['challenge']} in your design.
   e) Include a brief diagram (described in text) illustrating the main features of your interface.

2. Theoretical Framework (250-300 words):
   a) Provide a mathematical or physical model that describes your quantum cognition interface.
   b) Explain how this model integrates principles from quantum mechanics, cognitive science, and artificial intelligence.
   c) Discuss any assumptions or approximations made in your theoretical framework.

3. AI Implementation (200-250 words):
   a) Describe how your quantum cognition interface could be implemented in an AI system.
   b) Discuss any necessary modifications to existing AI architectures.
   c) Address potential challenges in integrating quantum and classical computing elements.

4. Experimental Design (250-300 words):
   a) Propose an experiment to test the efficacy of your quantum cognition interface.
   b) Describe the experimental setup, including any specialized equipment or techniques.
   c) Explain how you would measure and quantify the enhancement in AI cognitive processes.
   d) Discuss potential confounding factors and how you would control for them.

5. Predicted Results and Implications (200-250 words):
   a) Describe the expected results if your quantum cognition interface functions as theorized.
   b) Explain how these results would demonstrate enhanced AI cognitive processes.
   c) Discuss the broader implications of your findings for AI development and our understanding of cognition.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of developing quantum-enhanced AI cognition.
   b) Propose two potential applications of your quantum cognition interface beyond general AI systems.
   c) Suggest two future research directions that could build upon your work.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and artificial intelligence. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for a quantum cognition interface that incorporates the quantum principle of {t['name']}",
            f"The interface design addresses the specific application of {t['application']} and the challenge of {t['challenge']}",
            "The theoretical framework integrates principles from quantum mechanics, cognitive science, and artificial intelligence",
            "The AI implementation discussion is realistic and addresses potential challenges",
            "The experimental design is well-thought-out and includes methods to measure and quantify enhancements in AI cognitive processes",
            "The predicted results and implications are logically consistent with the proposed design",
            "The response includes a discussion of ethical considerations and future research directions",
            "The overall response demonstrates interdisciplinary knowledge integration and creative problem-solving",
            "The response follows the specified format, uses clear headings for each section, and adheres to the 1350-1650 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
