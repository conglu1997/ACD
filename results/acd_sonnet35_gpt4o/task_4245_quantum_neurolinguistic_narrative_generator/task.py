import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_concept": "superposition",
                "neurolinguistic_principle": "semantic priming",
                "narrative_theme": "time travel"
            },
            "2": {
                "quantum_concept": "entanglement",
                "neurolinguistic_principle": "syntactic parsing",
                "narrative_theme": "parallel universes"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired language model based on neurolinguistic principles, then use it to generate and analyze a creative narrative. Your task has the following components:\n\n1. Model Design (300-350 words):\n   a) Describe the key components of your quantum-inspired neurolinguistic language model.\n   b) Explain how you integrate the quantum concept of {t['quantum_concept']} with the neurolinguistic principle of {t['neurolinguistic_principle']}.\n   c) Discuss how your model represents and processes language in a way that mimics both quantum phenomena and neural processes.\n   d) Provide a high-level diagram or detailed description of your model's architecture.\n\n2. Quantum-Neurolinguistic Integration (250-300 words):\n   a) Explain in detail how {t['quantum_concept']} is implemented in your language model.\n   b) Describe how {t['neurolinguistic_principle']} is incorporated into the model's language processing.\n   c) Discuss any novel algorithms or techniques used in your implementation.\n   d) Provide a mathematical formulation or pseudo-code snippet that illustrates your approach.\n\n3. Narrative Generation (250-300 words):\n   a) Use your model to generate a short narrative (100-150 words) based on the theme of {t['narrative_theme']}.\n   b) Explain how the generated narrative reflects both the quantum and neurolinguistic aspects of your model.\n   c) Discuss how the integration of {t['quantum_concept']} and {t['neurolinguistic_principle']} influences the narrative structure and content.\n\n4. Narrative Analysis (200-250 words):\n   a) Analyze the generated narrative using your quantum-neurolinguistic model.\n   b) Explain how your model interprets the narrative's structure, meaning, and potential cognitive impact on readers.\n   c) Discuss any unique insights or patterns revealed by your model's analysis.\n\n5. Model Evaluation and Limitations (150-200 words):\n   a) Propose a method to evaluate the performance and validity of your quantum-neurolinguistic model.\n   b) Discuss potential limitations of your approach and suggest ways to address them.\n   c) Compare your model's capabilities to traditional language models and human writers.\n\n6. Future Developments and Implications (150-200 words):\n   a) Suggest two potential extensions or improvements to your model.\n   b) Discuss how your approach might influence future developments in quantum computing, neurolinguistics, or creative writing.\n   c) Explore potential applications of your model in fields such as cognitive science, artificial intelligence, or literary analysis.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, neurolinguistics, and creative writing techniques. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, neurolinguistics, and creative writing techniques.",
            f"The model effectively integrates the quantum concept of {t['quantum_concept']} with the neurolinguistic principle of {t['neurolinguistic_principle']}.",
            "The generated narrative reflects both quantum and neurolinguistic aspects of the model.",
            "The analysis of the generated narrative provides unique insights based on the quantum-neurolinguistic model.",
            "The response is innovative while maintaining scientific plausibility.",
            "The proposed evaluation method and discussion of limitations are thorough and well-reasoned.",
            "The suggested future developments and implications are insightful and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
