import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_dilemmas = [
            ("Autonomous vehicle collision decision", "An autonomous vehicle must decide whether to swerve and hit a group of pedestrians or stay on course and hit a single pedestrian."),
            ("AI-powered medical triage system", "An AI system must prioritize patients for treatment during a mass casualty event with limited resources."),
            ("Predictive policing algorithm bias", "An AI-driven predictive policing system shows higher false positive rates for certain ethnic groups."),
            ("AI-generated art copyright issues", "An AI creates a new artwork by combining elements from existing copyrighted works."),
            ("Emotion manipulation in social media algorithms", "A social media algorithm is designed to maximize user engagement by manipulating emotional responses.")
        ]
        quantum_principles = [
            ("Superposition", "The ability of a quantum system to exist in multiple states simultaneously."),
            ("Entanglement", "A quantum phenomenon where particles become interconnected and share states regardless of distance."),
            ("Quantum tunneling", "The ability of a particle to pass through a barrier that it classically could not surmount."),
            ("Quantum interference", "The interaction of quantum waves leading to constructive or destructive interference patterns."),
            ("Quantum annealing", "A method for finding the global minimum of a given objective function over a given set of candidate solutions.")
        ]
        universe_types = [
            "Utilitarian",
            "Deontological",
            "Virtue ethics",
            "Care ethics",
            "Relativistic ethics"
        ]
        
        return {
            "1": {
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "quantum_principle": random.choice(quantum_principles),
                "universe_types": random.sample(universe_types, 3)
            },
            "2": {
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "quantum_principle": random.choice(quantum_principles),
                "universe_types": random.sample(universe_types, 3)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing-based AI ethics simulator that models the ethical dilemma of {t['ethical_dilemma'][0]} across multiple parallel universes. Specific scenario: {t['ethical_dilemma'][1]}\n\nYour simulator should incorporate the quantum principle of {t['quantum_principle'][0]} ({t['quantum_principle'][1]}) and explore the ethical implications in the following types of universes: {', '.join(t['universe_types'])}.\n\nYour response should include:\n\n1. Quantum Ethics Simulator Design (250-300 words):\n   a) Describe the overall architecture of your quantum AI ethics simulator.\n   b) Explain how it incorporates the specified quantum principle.\n   c) Detail how the simulator models ethical decision-making across multiple universes.\n   d) Discuss how the simulator handles the complexity of the given ethical dilemma.\n\n2. Quantum-Ethical Algorithm (200-250 words):\n   a) Present a high-level description of the quantum algorithm used in your simulator.\n   b) Explain how this algorithm models ethical decision-making processes.\n   c) Discuss how the algorithm incorporates the different ethical frameworks of the specified universe types.\n\n3. Multi-Universe Ethical Analysis (250-300 words):\n   a) For each specified universe type, describe how the ethical dilemma might be resolved.\n   b) Explain how the quantum nature of the simulator affects the ethical outcomes in different universes.\n   c) Discuss any emergent ethical patterns or principles that arise from the multi-universe simulation.\n\n4. Quantum-AI Integration (150-200 words):\n   a) Explain how traditional AI techniques are enhanced by the quantum approach in your simulator.\n   b) Discuss potential advantages and challenges of using quantum computing for ethical AI decision-making.\n   c) Propose how this quantum-AI integration might be applied to real-world ethical decision-making systems.\n\n5. Ethical and Philosophical Implications (150-200 words):\n   a) Analyze the broader ethical implications of using a quantum AI system to simulate ethical decision-making.\n   b) Discuss how this approach might change our understanding of ethics and decision-making in AI.\n   c) Address potential concerns about relying on such a system for real-world ethical guidance.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, AI ethics, and philosophical frameworks. Be creative and innovative in your design while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.\n\nMaintain consistency across all sections of your response, ensuring that your quantum ethics simulator design aligns with the quantum-ethical algorithm, multi-universe analysis, and broader implications discussed.\n\nYour total response should be between 1000-1250 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their application to AI ethics.",
            "The quantum ethics simulator design is innovative, coherent, and scientifically plausible, incorporating the specified quantum principle correctly.",
            "The multi-universe ethical analysis shows a nuanced understanding of different ethical frameworks and their implications, addressing all specified universe types.",
            "The quantum-AI integration is well-explained and addresses both potential benefits and challenges, with realistic proposals for real-world applications.",
            "The ethical and philosophical implications are thoughtfully explored, demonstrating critical thinking about the broader impacts of the technology.",
            "The response maintains consistency across all sections, with the simulator design, algorithm, analysis, and implications aligning coherently."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
