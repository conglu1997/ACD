import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        global_issues = [
            "Climate change mitigation",
            "Pandemic prediction and response",
            "Global food security",
            "Sustainable energy distribution",
            "Biodiversity conservation"
        ]
        quantum_techniques = [
            "Quantum annealing",
            "Quantum simulation",
            "Quantum machine learning",
            "Quantum cryptography",
            "Quantum error correction"
        ]
        constraints = [
            "Limited qubit coherence time",
            "Scalability issues",
            "Noise sensitivity",
            "Quantum-classical interface challenges",
            "Limited quantum memory"
        ]
        return {
            "1": {"global_issue": random.choice(global_issues), "quantum_technique": random.choice(quantum_techniques), "constraint": random.choice(constraints)},
            "2": {"global_issue": random.choice(global_issues), "quantum_technique": random.choice(quantum_techniques), "constraint": random.choice(constraints)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing system to address the global issue of {t['global_issue']} using the quantum technique of {t['quantum_technique']}, while addressing the constraint of {t['constraint']}. Then, analyze its potential impact and ethical implications. Your response should include:\n\n" + \
               "1. Quantum System Design (300-350 words):\n" + \
               "   a) Describe the architecture of your quantum computing system.\n" + \
               "   b) Explain how you incorporate the specified quantum technique to address the global issue.\n" + \
               "   c) Detail any novel algorithms or approaches you've developed for this system.\n" + \
               "   d) Discuss how your system interfaces with classical computing systems and existing infrastructure.\n" + \
               "   e) Explain how your design addresses the given constraint.\n\n" + \
               "2. Problem-Solving Approach (200-250 words):\n" + \
               "   a) Explain how your quantum system addresses the specific challenges of the given global issue.\n" + \
               "   b) Provide a step-by-step explanation of how your system would process and analyze relevant data.\n" + \
               "   c) Describe the expected outcomes and how they would contribute to solving the global issue.\n" + \
               "   d) Discuss how the constraint affects your problem-solving approach and any trade-offs made.\n\n" + \
               "3. Potential Impact Analysis (200-250 words):\n" + \
               "   a) Analyze the potential short-term and long-term impacts of implementing your quantum system.\n" + \
               "   b) Discuss how your solution compares to current approaches in addressing the global issue.\n" + \
               "   c) Identify any potential unintended consequences of your system and how they might be mitigated.\n" + \
               "   d) Consider the implications of the constraint on the system's impact and scalability.\n\n" + \
               "4. Ethical Implications (200-250 words):\n" + \
               "   a) Discuss the ethical considerations of using quantum computing to address this global issue.\n" + \
               "   b) Analyze potential concerns regarding data privacy, security, and equitable access to the technology.\n" + \
               "   c) Propose guidelines for the responsible development and use of your quantum system.\n" + \
               "   d) Examine any ethical dilemmas that may arise from the constraint and how to address them.\n\n" + \
               "5. Technical Challenges and Future Directions (150-200 words):\n" + \
               "   a) Identify the main technical challenges in implementing your quantum system, including the given constraint.\n" + \
               "   b) Propose potential solutions or research directions to address these challenges.\n" + \
               "   c) Suggest how your system could be expanded or improved in future iterations.\n\n" + \
               "Ensure your response demonstrates a deep understanding of quantum computing, the specified global issue, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.\n\n" + \
               "Your total response should be between 1050-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing and the {t['quantum_technique']} technique.",
            f"The proposed quantum system effectively addresses the global issue of {t['global_issue']}.",
            f"The design adequately addresses the constraint of {t['constraint']}.",
            "The answer includes a thorough analysis of potential impacts and ethical implications.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The answer is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
