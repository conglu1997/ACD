import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "Quantum coherence",
            "Quantum entanglement",
            "Quantum tunneling",
            "Superposition"
        ]
        biological_systems = [
            "Photosynthesis",
            "Enzyme catalysis",
            "Magnetoreception in birds",
            "Olfaction (smell)"
        ]
        medical_applications = [
            "Cancer treatment",
            "Drug design",
            "Neurological disorders",
            "Genetic engineering"
        ]
        tasks = {}
        for i in range(1, 3):
            effect = random.choice(quantum_effects)
            system = random.choice(biological_systems)
            application = random.choice(medical_applications)
            tasks[str(i)] = {"effect": effect, "system": system, "application": application}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical quantum biology simulator that models {t['effect']} in {t['system']}, then propose and analyze a novel application in {t['application']}. Quantum biology is an emerging field that explores how quantum mechanical phenomena might play a role in biological processes.\n\nYour response should include:\n\n1. Quantum Biology Simulator Design (300-350 words):\n   a) Describe the key components and functionality of your quantum biology simulator.\n   b) Explain how it models {t['effect']} in {t['system']}.\n   c) Discuss any novel algorithms or approaches used in your simulator.\n   d) Address potential challenges in simulating quantum effects in biological systems.\n   e) Provide a simple diagram or pseudocode snippet illustrating a key component of your simulator.\n\n2. Theoretical Foundation (200-250 words):\n   a) Explain the current scientific understanding of how {t['effect']} might play a role in {t['system']}.\n   b) Discuss any existing experimental evidence or theoretical models.\n   c) Identify gaps in current knowledge that your simulator aims to address.\n\n3. Novel Medical Application (250-300 words):\n   a) Propose an innovative application of your quantum biology simulator in {t['application']}.\n   b) Explain how insights from your simulator could lead to advancements in this medical field.\n   c) Describe the potential benefits and limitations of your proposed application.\n\n4. Technical Implementation (200-250 words):\n   a) Outline the computational requirements for your quantum biology simulator.\n   b) Discuss any specific quantum computing technologies that could enhance your simulator's capabilities.\n   c) Address scalability and real-time simulation challenges.\n\n5. Ethical Implications (150-200 words):\n   a) Analyze potential ethical issues arising from your simulator and its medical application.\n   b) Discuss how these technologies might impact healthcare equity and access.\n   c) Propose guidelines for responsible development and use of quantum biology simulations in medicine.\n\n6. Experimental Validation (200-250 words):\n   a) Design an experiment to validate your quantum biology simulator's predictions.\n   b) Explain how you would compare your simulator's results with real-world biological systems.\n   c) Discuss potential challenges in experimental validation and how you would address them.\n\n7. Future Research Directions (100-150 words):\n   a) Suggest two key areas for further research in quantum biology and its medical applications.\n   b) Explain how these research directions could address current limitations or open new possibilities.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, biology, and medical technology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['effect']} and its potential role in {t['system']}",
            "The quantum biology simulator design is innovative and scientifically plausible",
            f"The proposed application in {t['application']} is novel and well-reasoned",
            "The ethical implications are thoughtfully analyzed",
            "The experimental validation proposal is well-designed and addresses potential challenges",
            "The response shows strong interdisciplinary knowledge integration across quantum mechanics, biology, and medical technology",
            "The technical implementation discussion is detailed and addresses computational challenges",
            "The future research directions are promising and well-justified",
            "The response adheres to the specified word count and formatting guidelines",
            "The explanation of complex concepts is clear and accessible",
            "The provided diagram or pseudocode snippet effectively illustrates a key component of the simulator"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
