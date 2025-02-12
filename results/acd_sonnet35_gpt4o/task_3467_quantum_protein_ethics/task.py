import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "protein_type": "enzyme",
                "application": "disease treatment",
                "ethical_focus": "human enhancement"
            },
            {
                "protein_type": "antibody",
                "application": "vaccine development",
                "ethical_focus": "global health equity"
            },
            {
                "protein_type": "receptor",
                "application": "drug design",
                "ethical_focus": "personalized medicine"
            },
            {
                "protein_type": "structural protein",
                "application": "biomaterial engineering",
                "ethical_focus": "environmental sustainability"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing system for predicting the folding of {t['protein_type']}s, then analyze its potential applications in {t['application']} through genetic engineering and the associated ethical implications, focusing on {t['ethical_focus']}. Your response should include the following sections:\n\n1. Quantum System Design (250-300 words):\n   a) Describe the key components of your quantum computing system for protein folding prediction.\n   b) Explain how quantum principles (e.g., superposition, entanglement) are leveraged to enhance prediction accuracy and efficiency.\n   c) Discuss any novel quantum algorithms or techniques incorporated in your design.\n   d) Address potential challenges and limitations of your quantum approach.\n\n2. Protein Folding Prediction Process (200-250 words):\n   a) Outline the step-by-step process your system uses to predict {t['protein_type']} folding.\n   b) Explain how your system handles the complexity and variability of {t['protein_type']} structures.\n   c) Discuss how your approach improves upon classical computational methods.\n\n3. Application in Genetic Engineering (200-250 words):\n   a) Describe how your quantum-powered protein folding prediction system could be applied to {t['application']}.\n   b) Explain the potential benefits and risks of using this technology in genetic engineering.\n   c) Discuss any modifications or extensions needed to adapt your system for this specific application.\n\n4. Ethical Implications (250-300 words):\n   a) Analyze the ethical considerations surrounding the use of your technology for {t['application']}, with a focus on {t['ethical_focus']}.\n   b) Discuss potential societal impacts, both positive and negative.\n   c) Address concerns related to privacy, equity, and potential misuse of the technology.\n   d) Propose guidelines or safeguards for the responsible development and use of this technology.\n\n5. Future Prospects and Challenges (150-200 words):\n   a) Speculate on future developments in quantum biology and their potential impact on genetic engineering.\n   b) Discuss ongoing challenges in the field and potential approaches to address them.\n   c) Consider how advancements in this area might shape the future of medicine and biotechnology.\n\nEnsure your response demonstrates a deep understanding of quantum computing, protein biology, genetic engineering, and bioethics. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1300 words.\n\nExample (partial): For a quantum system design, you might consider using quantum annealing to explore the energy landscape of protein conformations, or quantum phase estimation for determining energy eigenstates of protein Hamiltonians. However, don't limit yourself to these examples - be creative and innovative in your approach."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of quantum computing principles and their application to {t['protein_type']} folding prediction.",
            f"The proposed system for {t['application']} through genetic engineering is scientifically plausible.",
            f"The ethical analysis considers multiple perspectives on {t['ethical_focus']}.",
            "The response shows interdisciplinary integration of quantum physics, biology, and ethics.",
            "The writing uses appropriate scientific terminology.",
            "The response is between 1050-1300 words.",
            "The response includes novel ideas or approaches not explicitly mentioned in the instructions."
        ]
        
        result = eval_with_llm_judge(instructions, submission, criteria)
        if isinstance(result, bool):
            return 1.0 if result else 0.0
        elif isinstance(result, float):
            return result
        else:
            return 0.0
