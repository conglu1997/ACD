import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        biological_targets = [
            "protein folding",
            "enzyme kinetics",
            "gene expression regulation",
            "membrane transport"
        ]
        drug_discovery_goals = [
            "identify novel drug targets",
            "optimize lead compounds",
            "predict drug-target interactions",
            "design multi-target drugs"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_target": random.choice(biological_targets),
                "drug_discovery_goal": random.choice(drug_discovery_goals)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_target": random.choice(biological_targets),
                "drug_discovery_goal": random.choice(drug_discovery_goals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired AI system for modeling and manipulating biological systems at the molecular level, with a specific application in drug discovery. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the biological target of {t['biological_target']}, and aim to {t['drug_discovery_goal']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the overall structure of your quantum-inspired bio-AI system.\n   b) Explain how it incorporates the specified quantum principle in its design.\n   c) Detail how the system will model and analyze the given biological target.\n   d) Discuss how the system will approach the specified drug discovery goal.\n   e) Include a high-level diagram or pseudocode to illustrate your system's architecture.\n\n2. Quantum-Biological Interface (250-300 words):\n   a) Explain how your system translates biological information into quantum states or processes.\n   b) Describe how these quantum representations enhance modeling or analysis capabilities.\n   c) Discuss any novel quantum operations or algorithms you've designed for biological data processing.\n   d) Provide an example of how your system would process a specific type of biological data related to the given target.\n\n3. AI Integration and Drug Discovery Application (250-300 words):\n   a) Describe how AI techniques are integrated with quantum-inspired biological modeling.\n   b) Explain the role of machine learning in achieving the specified drug discovery goal.\n   c) Discuss how your system would handle the large-scale data processing required for drug discovery.\n   d) Provide a specific example of how your system would approach a task related to the given drug discovery goal.\n\n4. Performance Analysis and Validation (200-250 words):\n   a) Propose methods to evaluate the performance of your quantum-inspired bio-AI system.\n   b) Compare your approach to traditional computational methods in drug discovery.\n   c) Discuss potential advantages and limitations of your system.\n   d) Suggest an experiment to validate a key aspect of your system's design.\n\n5. Ethical Considerations and Societal Impact (200-250 words):\n   a) Discuss potential ethical implications of using quantum-inspired AI for drug discovery.\n   b) Address concerns about data privacy, algorithmic bias, and equitable access to the technology.\n   c) Consider potential impacts on the pharmaceutical industry and global health.\n   d) Propose guidelines for responsible development and use of such systems.\n\n6. Future Directions and Challenges (150-200 words):\n   a) Identify key technical challenges in implementing your system.\n   b) Suggest approaches to overcome these challenges.\n   c) Propose two potential future enhancements or applications of your system.\n   d) Discuss how advancements in quantum computing might influence the evolution of your system.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, molecular biology, artificial intelligence, and drug discovery processes. Use technical terminology appropriately and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1350-1650 words, with each section adhering to the specified word count range."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system design effectively incorporates the quantum principle of {t['quantum_principle']}.",
            f"The approach to modeling and analyzing the biological target of {t['biological_target']} is scientifically sound and innovative.",
            f"The system's application to the drug discovery goal of {t['drug_discovery_goal']} is well-developed and plausible.",
            "The response demonstrates a deep understanding of quantum computing, molecular biology, AI, and drug discovery processes.",
            "The ethical considerations and future directions are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
