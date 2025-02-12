import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "Rhythm",
            "Harmony",
            "Melody",
            "Timbre"
        ]
        cognitive_processes = [
            "Attention",
            "Memory",
            "Emotion",
            "Pattern recognition"
        ]
        mathematical_concepts = [
            "Fractals",
            "Graph theory",
            "Information theory",
            "Dynamical systems"
        ]
        
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "mathematical_concept": random.choice(mathematical_concepts)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "mathematical_concept": random.choice(mathematical_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel system that integrates music theory, mathematics, and cognitive science to analyze and generate music. Your system should focus on the musical element of {t['musical_element']}, incorporate the cognitive process of {t['cognitive_process']}, and utilize the mathematical concept of {t['mathematical_concept']}. Your response should include:\n\n1. System Overview (200-250 words):\n   a) Describe the key components and functionality of your system.\n   b) Explain how it incorporates the specified musical element, cognitive process, and mathematical concept.\n   c) Outline the system's approach to analyzing and generating music.\n\n2. Mathematical Framework (200-250 words):\n   a) Develop a mathematical representation of your system, integrating the specified mathematical concept.\n   b) Explain the key variables, functions, or equations in your framework.\n   c) Discuss how this framework captures the relationship between the musical element and the cognitive process.\n\n3. Music Analysis Method (150-200 words):\n   a) Describe how your system would analyze an existing piece of music.\n   b) Explain what insights about the specified cognitive process it might reveal.\n   c) Provide an example of the type of output your analysis would generate.\n\n4. Music Generation Algorithm (200-250 words):\n   a) Outline an algorithm for generating music based on your system.\n   b) Explain how it incorporates the specified musical element and cognitive process.\n   c) Describe how the generated music might differ from traditionally composed music.\n\n5. Cognitive Science Integration (150-200 words):\n   a) Discuss how your system might be used to test hypotheses about music perception and cognition.\n   b) Propose an experiment that uses your system to investigate the specified cognitive process.\n\n6. Practical Applications (100-150 words):\n   a) Suggest two practical applications of your system in fields such as music therapy, education, or AI-assisted composition.\n   b) Explain how these applications leverage the unique features of your design.\n\n7. Limitations and Future Directions (100-150 words):\n   a) Identify potential limitations or challenges of your system.\n   b) Propose two directions for future research or system enhancement.\n\nEnsure your response demonstrates a deep understanding of music theory, the specified mathematical concept, and cognitive science. Be creative in your system design while maintaining scientific plausibility and theoretical soundness. Use appropriate terminology from all three fields and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1100-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, the specified mathematical concept, and cognitive science.",
            "The system design is creative and innovative while maintaining scientific plausibility.",
            "The mathematical framework effectively integrates the specified concept and relates it to the musical element and cognitive process.",
            "The music analysis and generation methods are well-explained and logically consistent with the system's design.",
            "The proposed experiment and practical applications are innovative and leverage the unique features of the system.",
            "The response addresses all required sections and adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
