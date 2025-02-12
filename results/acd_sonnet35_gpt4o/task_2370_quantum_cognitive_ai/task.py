import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Geopolitical Crisis Management",
                "description": "A complex international conflict involving multiple parties with ambiguous alliances and conflicting interests."
            },
            {
                "name": "Financial Market Prediction",
                "description": "Predicting market trends in a volatile economic environment with incomplete and potentially contradictory information."
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that implements quantum cognitive models to enhance decision-making processes, then apply it to the following complex scenario involving ambiguity and contextuality: {t['name']} - {t['description']}\n\nYour response should include the following sections:\n\n1. Quantum Cognitive Framework (250-300 words):\n   a) Explain the key principles of quantum cognition and how they differ from classical probability models.\n   b) Discuss how quantum superposition and interference can be used to model decision-making under uncertainty.\n   c) Describe how quantum entanglement might represent contextuality in cognitive processes.\n\n2. AI System Architecture (300-350 words):\n   a) Design an AI system that integrates quantum cognitive models for enhanced decision-making.\n   b) Explain the key components of your system and how they interact.\n   c) Describe how your system represents and processes information using quantum principles.\n   d) Discuss how your AI handles the transition between quantum and classical representations.\n\n3. Application to Scenario (300-350 words):\n   a) Apply your quantum cognitive AI system to the given scenario.\n   b) Explain how your system models the ambiguity and contextuality present in the scenario.\n   c) Provide a step-by-step example of how your AI would approach a specific decision point in the scenario.\n   d) Compare your quantum cognitive approach to a classical AI approach for this scenario.\n\n4. Mathematical Formulation (200-250 words):\n   a) Provide a mathematical representation of your quantum cognitive model.\n   b) Include key equations and explain their significance in your model.\n   c) Describe how you would measure or observe quantum states in your cognitive model.\n\n5. Performance Analysis (200-250 words):\n   a) Propose metrics to evaluate the performance of your quantum cognitive AI system.\n   b) Discuss potential advantages and limitations of your approach.\n   c) Suggest how the system could be improved or extended.\n\n6. Ethical and Philosophical Implications (150-200 words):\n   a) Discuss the ethical implications of using quantum cognitive models in AI decision-making systems.\n   b) Explore how your system might impact our understanding of human cognition and free will.\n   c) Propose guidelines for responsible development and use of quantum cognitive AI systems.\n\nEnsure your response demonstrates a deep understanding of quantum theory, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum cognition principles and their application to AI systems.",
            "The AI system architecture is well-designed and clearly integrates quantum cognitive models.",
            "The application to the given scenario is thorough and showcases the advantages of the quantum cognitive approach.",
            "The mathematical formulation is correct and relevant to the proposed model.",
            "The performance analysis and ethical considerations are thoughtful and comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
