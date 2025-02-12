import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling"
        ]
        network_objectives = [
            "information flow",
            "collective decision-making",
            "resilience to misinformation"
        ]
        
        tasks = {}
        for i in range(1, 3):
            principle = random.choice(quantum_principles)
            objective = random.choice(network_objectives)
            tasks[str(i)] = {"quantum_principle": principle, "network_objective": objective}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that uses the quantum computing principle of {t['quantum_principle']} to model and optimize complex social networks, focusing on enhancing {t['network_objective']}. Your response should include the following sections:\n\n1. Conceptual Framework (250-300 words):\n   a) Explain the chosen quantum principle ({t['quantum_principle']}) and its relevance to social network optimization.\n   b) Describe how this principle can be analogously applied to model and enhance {t['network_objective']} in social networks.\n   c) Discuss the key characteristics of complex social networks and the specific challenges in optimizing {t['network_objective']}.\n\n2. AI System Architecture (300-350 words):\n   a) Outline the main components of your AI system and their functions.\n   b) Explain how your system incorporates the quantum principle into its architecture or algorithms.\n   c) Describe how your system models social networks and optimizes {t['network_objective']}.\n   d) Include a diagram or flowchart illustrating your system's architecture (describe it textually).\n\n3. Quantum Algorithm Design (250-300 words):\n   a) Detail the quantum algorithm(s) your system uses to model and optimize social networks.\n   b) Explain how these algorithms leverage the quantum principle to enhance {t['network_objective']}.\n   c) Describe how your algorithm handles the complexity and dynamics of social networks.\n   d) Include a brief pseudocode or mathematical formulation of a key part of your quantum algorithm.\n\n4. Data Requirements and Processing (200-250 words):\n   a) Specify the types of data your system would require to model and optimize social networks.\n   b) Describe any necessary data preprocessing or feature extraction steps.\n   c) Explain how your system would handle privacy and ethical concerns related to social network data.\n\n5. Optimization Process and Output (200-250 words):\n   a) Detail the step-by-step process of how your system optimizes {t['network_objective']} in social networks.\n   b) Explain how the system generates and evaluates potential optimizations.\n   c) Describe the output format and how it can be interpreted by social scientists or policymakers.\n\n6. Evaluation and Validation (200-250 words):\n   a) Propose methods for evaluating the effectiveness of your system in optimizing {t['network_objective']}.\n   b) Discuss the challenges in validating quantum-inspired social network models.\n   c) Suggest how your system could be tested or calibrated using real-world social network data.\n\n7. Ethical Considerations and Potential Applications (150-200 words):\n   a) Identify potential ethical issues or concerns related to using quantum-inspired AI to optimize social networks.\n   b) Discuss the potential applications of your system in fields such as public health, education, or governance.\n   c) Propose guidelines for the responsible development and use of quantum-inspired AI in social network optimization.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, social network theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, social network theory, and artificial intelligence",
            "The conceptual framework clearly explains how the quantum principle can be applied to social network optimization",
            "The AI system architecture and quantum algorithm design are innovative and plausible",
            "The response addresses the complexity and ethical considerations of working with social network data",
            "The optimization process and evaluation methods are well-thought-out and scientifically sound",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts",
            "The proposed system shows potential for real-world applications and addresses ethical concerns",
            "The response is well-structured, following the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
