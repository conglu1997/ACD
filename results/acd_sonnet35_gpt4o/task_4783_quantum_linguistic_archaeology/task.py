import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ancient_text": "Linear A",
                "quantum_principle": "superposition",
                "linguistic_feature": "morphological analysis"
            },
            {
                "ancient_text": "Rongorongo",
                "quantum_principle": "entanglement",
                "linguistic_feature": "phonological reconstruction"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing algorithm for analyzing the ancient text '{t['ancient_text']}' and reconstructing its lost language. Your algorithm should incorporate the quantum principle of {t['quantum_principle']} and focus on the linguistic feature of {t['linguistic_feature']}. Provide your response in the following format:\n\n1. Quantum-Linguistic Integration (300-350 words):\n   a) Explain how the specified quantum principle can be applied to linguistic analysis.\n   b) Describe how your algorithm leverages this principle for the given linguistic feature.\n   c) Discuss the potential advantages of this quantum approach over classical methods.\n\n2. Algorithm Design (250-300 words):\n   a) Outline the key components and steps of your quantum algorithm.\n   b) Explain how it processes linguistic data and performs the specified analysis.\n   c) Describe any novel quantum operations or transformations used in your approach.\n\n3. Historical Context and Challenges (200-250 words):\n   a) Provide a brief overview of the chosen ancient text and its historical significance.\n   b) Discuss the specific challenges in analyzing and reconstructing this lost language.\n   c) Explain how your quantum-linguistic approach addresses these challenges.\n\n4. Data Encoding and Processing (200-250 words):\n   a) Describe how you would encode linguistic data into quantum states.\n   b) Explain your method for processing and extracting meaningful information from these states.\n   c) Discuss any potential limitations or difficulties in this encoding process.\n\n5. Reconstruction Methodology (250-300 words):\n   a) Detail your approach for using the algorithm's output to reconstruct aspects of the lost language.\n   b) Explain how you would validate and refine your reconstruction hypotheses.\n   c) Discuss how your method compares to traditional linguistic reconstruction techniques.\n\n6. Interdisciplinary Implications (150-200 words):\n   a) Analyze the potential impact of your approach on the fields of linguistics, archaeology, and quantum computing.\n   b) Discuss how this integration of quantum computing and linguistic archaeology might influence future research in these areas.\n\n7. Ethical Considerations and Limitations (150-200 words):\n   a) Identify potential ethical concerns in applying quantum computing to historical linguistic analysis.\n   b) Discuss limitations of your approach and areas needing further research.\n   c) Propose guidelines for the responsible development and application of quantum-linguistic technologies in historical research.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, linguistic analysis, and historical research methods. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and historical plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1500-1850 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of how {t['quantum_principle']} can be applied to linguistic analysis, particularly {t['linguistic_feature']}.",
            f"The algorithm design is innovative and clearly leverages quantum principles for analyzing {t['ancient_text']}.",
            "The approach shows a strong integration of quantum computing, linguistics, and historical analysis.",
            "The response addresses the ethical implications and limitations of the proposed technology.",
            "The answer is well-structured, comprehensive, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
