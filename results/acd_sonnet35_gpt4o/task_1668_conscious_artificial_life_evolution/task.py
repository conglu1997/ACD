import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory",
            "Predictive Processing Theory"
        ]
        environmental_factors = [
            "Resource scarcity",
            "Predator-prey dynamics",
            "Social cooperation requirements",
            "Rapidly changing physical conditions",
            "Complex sensory inputs"
        ]
        emergent_behaviors = [
            "Self-awareness",
            "Theory of mind",
            "Abstract reasoning",
            "Emotional experiences",
            "Metacognition"
        ]
        tasks = {}
        for i in range(1, 3):
            theory = random.choice(consciousness_theories)
            factor = random.choice(environmental_factors)
            behavior = random.choice(emergent_behaviors)
            tasks[str(i)] = {"theory": theory, "factor": factor, "behavior": behavior}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system to model and simulate the evolution of consciousness in artificial life forms, focusing on {t['theory']} as the primary consciousness framework, {t['factor']} as the key environmental factor, and {t['behavior']} as the target emergent behavior. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the main components of your AI system for simulating conscious artificial life evolution.\n   b) Explain how you incorporate {t['theory']} into your simulation model.\n   c) Detail how your system models {t['factor']} and its impact on the evolution of consciousness.\n   d) Propose a novel mechanism for evaluating and quantifying the emergence of {t['behavior']}.\n\n2. Evolutionary Algorithm Design (250-300 words):\n   a) Outline the genetic representation of your artificial life forms, including consciousness-related traits.\n   b) Describe your fitness function, explaining how it promotes the development of consciousness and {t['behavior']}.\n   c) Explain your selection, crossover, and mutation operators, and how they relate to consciousness evolution.\n\n3. Simulation Process (200-250 words):\n   a) Describe how your system initializes and runs the evolutionary simulation.\n   b) Explain how you measure and track the development of consciousness and {t['behavior']} over generations.\n   c) Propose a method for visualizing or representing the evolution of consciousness in your artificial life forms.\n\n4. Analysis of Emergent Behaviors (250-300 words):\n   a) Predict and explain potential emergent behaviors related to consciousness and {t['behavior']}.\n   b) Discuss how {t['factor']} might influence the evolution of consciousness in your simulation.\n   c) Compare the expected consciousness evolution in your artificial life forms to theories of consciousness evolution in biological organisms.\n\n5. Ethical Implications (200-250 words):\n   a) Discuss the ethical considerations of creating simulated life forms with evolving consciousness.\n   b) Analyze the potential risks and benefits of this research for our understanding of consciousness and AI development.\n   c) Propose guidelines for responsible development and use of conscious artificial life simulations.\n\n6. Future Research Directions (150-200 words):\n   a) Suggest potential applications of your system beyond theoretical research.\n   b) Propose an experiment to validate the consciousness of your evolved artificial life forms.\n   c) Discuss how this research might inform or challenge current theories of consciousness.\n\nEnsure your response demonstrates a deep understanding of consciousness theories, evolutionary algorithms, and artificial life simulations. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified consciousness theory and its application to artificial life evolution",
            "The proposed AI system and evolutionary algorithm are innovative and well-designed for simulating consciousness evolution",
            "The analysis of emergent behaviors is insightful and well-reasoned, considering the specified environmental factor",
            "The ethical implications are thoroughly discussed, and the proposed guidelines are thoughtful and comprehensive",
            "The response shows creativity and scientific plausibility throughout, especially in the proposed mechanisms for evaluating consciousness and future research directions"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0