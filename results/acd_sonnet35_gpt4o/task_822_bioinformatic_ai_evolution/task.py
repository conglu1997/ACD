import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_principles = [
            "DNA replication",
            "RNA transcription",
            "Protein synthesis",
            "Cell division"
        ]
        information_theory_concepts = [
            "Shannon entropy",
            "Mutual information",
            "Kolmogorov complexity",
            "Error correction"
        ]
        ai_architectures = [
            "Neural networks",
            "Genetic algorithms",
            "Reinforcement learning",
            "Bayesian networks"
        ]
        
        tasks = {}
        for i in range(1, 3):
            principle = random.choice(biological_principles)
            concept = random.choice(information_theory_concepts)
            architecture = random.choice(ai_architectures)
            tasks[str(i)] = {"principle": principle, "concept": concept, "architecture": architecture}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates the evolution of artificial life forms based on the biological principle of {t['principle']}, incorporating the information theory concept of {t['concept']}, and drawing inspiration from the AI architecture of {t['architecture']}. Your response should include:\n\n1. System Design (300-350 words):\n   a) Describe the key components and mechanisms of your AI system.\n   b) Explain how it incorporates the specified biological principle and information theory concept.\n   c) Detail how it draws inspiration from the given AI architecture.\n   d) Provide a high-level diagram or pseudocode representing your system's structure and processes.\n\n2. Evolutionary Simulation (250-300 words):\n   a) Explain how your system simulates the evolution of artificial life forms.\n   b) Describe the 'genetic' representation of your artificial organisms.\n   c) Detail the mechanisms for mutation, selection, and reproduction in your system.\n   d) Discuss how your system handles environmental pressures and fitness evaluation.\n\n3. Information Processing Analysis (200-250 words):\n   a) Analyze how information flows and is processed within your simulated ecosystem.\n   b) Explain how the incorporated information theory concept influences the system's behavior.\n   c) Discuss any emergent informational properties you would expect to observe.\n\n4. Biological Insights (200-250 words):\n   a) Explore how your system might provide insights into real biological evolution.\n   b) Discuss potential limitations in drawing parallels between your simulation and natural systems.\n   c) Propose an experiment using your system to test a hypothesis about biological evolution.\n\n5. AI Architecture Implications (200-250 words):\n   a) Analyze how the bioinformatic principles in your system could inform novel AI architectures.\n   b) Discuss potential advantages and challenges of applying these principles to general AI development.\n   c) Propose a specific AI application that could benefit from your bioinformatic approach.\n\n6. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss potential ethical implications of simulating evolving artificial life forms.\n   b) Propose two future research directions based on your system.\n   c) Speculate on the long-term impact of such bioinformatic AI systems on science and technology.\n\nEnsure your response demonstrates a deep understanding of molecular biology, information theory, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response using clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of molecular biology, information theory, and artificial intelligence",
            "The AI system design is creative, novel, and scientifically plausible",
            "The analysis of evolutionary simulation, information processing, and biological insights is thorough and insightful",
            "The implications for AI architectures and ethical considerations are well-reasoned and thought-provoking",
            "The response includes all required sections with appropriate length and detail",
            "The proposed experiments and future directions are innovative and relevant",
            "The response uses appropriate technical terminology from all relevant fields"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
