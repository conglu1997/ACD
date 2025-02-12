import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_process": "Decision Making",
                "quantum_phenomenon": "Superposition",
                "biological_system": "Photosynthesis"
            },
            {
                "cognitive_process": "Memory Formation",
                "quantum_phenomenon": "Entanglement",
                "biological_system": "Magnetoreception in birds"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that incorporates principles of quantum biology to model and enhance the cognitive process of {t['cognitive_process']}, inspired by the quantum phenomenon of {t['quantum_phenomenon']} observed in the biological system of {t['biological_system']}. Then, propose experiments to test its efficacy. Your response should include the following sections:

1. Quantum Biological Analysis (250-300 words):
   a) Explain the quantum phenomenon of {t['quantum_phenomenon']} and its role in {t['biological_system']}.
   b) Discuss how this quantum effect might relate to the cognitive process of {t['cognitive_process']}.
   c) Describe any existing theories or research linking quantum biology to cognition.

2. AI System Design (300-350 words):
   a) Propose a detailed AI architecture that incorporates the quantum biological principles.
   b) Explain how your system models and potentially enhances the cognitive process of {t['cognitive_process']}.
   c) Describe the key components of your AI system and their quantum-inspired functionalities.
   d) Discuss any novel approaches or algorithms in your design.

3. Implementation Challenges (200-250 words):
   a) Identify potential challenges in implementing your quantum-inspired AI system.
   b) Propose solutions or workarounds for these challenges.
   c) Discuss any specialized hardware or software requirements for your system.

4. Performance Predictions (200-250 words):
   a) Predict how your quantum-inspired AI system might outperform classical AI in {t['cognitive_process']}.
   b) Discuss potential limitations or trade-offs in your approach.
   c) Propose metrics to evaluate the success of your system.

5. Experimental Design (250-300 words):
   a) Design an experiment to test the efficacy of your quantum-inspired AI system.
   b) Describe the experimental setup, including control groups and variables.
   c) Explain how you would measure and analyze the system's performance in {t['cognitive_process']}.
   d) Discuss how you would validate any quantum effects in your system's operation.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of developing AI systems inspired by quantum biology.
   b) Explore the philosophical implications of quantum effects in cognition and AI.
   c) Propose guidelines for responsible development and use of quantum-inspired AI.

7. Conclusion (100-150 words):
   Summarize the key aspects of your quantum-inspired AI system, its potential impact on {t['cognitive_process']}, and the most significant challenges and ethical considerations.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, neuroscience, and artificial intelligence. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative and creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere to the word count guidelines for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a thorough analysis of {t['quantum_phenomenon']} in {t['biological_system']} and its potential relation to {t['cognitive_process']}.",
            "The AI system design clearly incorporates quantum biological principles and explains how it enhances the specified cognitive process.",
            "The response addresses implementation challenges and proposes innovative solutions.",
            "The experimental design is well-thought-out, specific, and tailored to test the quantum-inspired AI system.",
            "The response demonstrates a deep understanding of quantum mechanics, biology, neuroscience, and artificial intelligence.",
            "The ethical and philosophical implications of quantum-inspired AI are thoughtfully discussed.",
            "The response adheres to the specified format and word count guidelines.",
            "The conclusion effectively summarizes the key aspects of the proposed system and its implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
