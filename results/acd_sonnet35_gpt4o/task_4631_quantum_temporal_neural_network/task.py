import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "neural_timescale": "milliseconds",
                "cognitive_function": "working memory"
            },
            {
                "quantum_principle": "entanglement",
                "neural_timescale": "seconds",
                "cognitive_function": "decision making"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical quantum-enhanced neural network that mimics the brain's ability to process information across multiple timescales, focusing on the quantum principle of {t['quantum_principle']}, the neural timescale of {t['neural_timescale']}, and its application to the cognitive function of {t['cognitive_function']}. Then, analyze its potential applications in AI and cognitive science. Your response should include:\n\n" + \
               "1. Quantum-Enhanced Neural Architecture (300-350 words):\n" + \
               "   a) Describe the key components of your quantum-enhanced neural network.\n" + \
               "   b) Explain how {t['quantum_principle']} is integrated into the neural processing.\n" + \
               "   c) Detail how your system models information processing at the {t['neural_timescale']} timescale.\n" + \
               "   d) Provide a high-level diagram or pseudocode snippet illustrating a crucial part of your system's architecture.\n\n" + \
               "2. Temporal Information Processing (250-300 words):\n" + \
               "   a) Explain how your quantum-enhanced network processes information across multiple timescales.\n" + \
               "   b) Compare this to how biological neural networks handle temporal information.\n" + \
               "   c) Discuss any novel algorithms or techniques used to optimize temporal processing.\n\n" + \
               "3. Application to Cognitive Function (200-250 words):\n" + \
               "   a) Describe how your system could enhance or model {t['cognitive_function']}.\n" + \
               "   b) Provide a specific example of how it might outperform classical AI systems in this domain.\n" + \
               "   c) Discuss potential limitations or challenges in applying your system to this cognitive function.\n\n" + \
               "4. Implications for AI and Cognitive Science (250-300 words):\n" + \
               "   a) Analyze how your quantum-temporal neural network could advance our understanding of biological cognition.\n" + \
               "   b) Discuss potential applications in artificial intelligence beyond the specified cognitive function.\n" + \
               "   c) Explore how this technology might bridge gaps between AI and biological intelligence.\n\n" + \
               "5. Ethical Considerations and Future Research (200-250 words):\n" + \
               "   a) Identify potential ethical concerns related to the development and use of quantum-enhanced neural networks.\n" + \
               "   b) Propose guidelines for responsible research and application of this technology.\n" + \
               "   c) Suggest two future research directions to further develop or validate your proposed system.\n\n" + \
               "Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\n" + \
               "Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1450 words. Include a word count at the end of your submission."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence, using appropriate technical terminology throughout.",
            f"The quantum-enhanced neural architecture effectively incorporates {t['quantum_principle']} and models {t['neural_timescale']} timescale processing, with a clear diagram or pseudocode provided.",
            f"The application to {t['cognitive_function']} is well-explained, plausible, and includes a specific example of potential advantages over classical AI systems.",
            "The implications for AI and cognitive science are thoroughly analyzed, covering advancements in biological cognition understanding and potential AI applications.",
            "Ethical considerations are thoughtfully addressed, with specific guidelines proposed, and two concrete future research directions are suggested.",
            "The response is creative and innovative while maintaining scientific plausibility, and adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
