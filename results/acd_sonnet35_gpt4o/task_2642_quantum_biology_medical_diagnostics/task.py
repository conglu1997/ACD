import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        diseases = [
            {
                "name": "Alzheimer's disease",
                "biological_target": "Amyloid-beta protein aggregation",
                "quantum_effect": "Quantum tunneling"
            },
            {
                "name": "Cancer",
                "biological_target": "DNA mutations",
                "quantum_effect": "Quantum entanglement"
            },
            {
                "name": "Parkinson's disease",
                "biological_target": "Alpha-synuclein protein misfolding",
                "quantum_effect": "Quantum coherence"
            },
            {
                "name": "Diabetes",
                "biological_target": "Glucose metabolism",
                "quantum_effect": "Quantum superposition"
            },
            {
                "name": "Cardiovascular disease",
                "biological_target": "Atherosclerotic plaque formation",
                "quantum_effect": "Quantum electron tunneling"
            },
            {
                "name": "Multiple sclerosis",
                "biological_target": "Myelin sheath degradation",
                "quantum_effect": "Quantum spin effects"
            }
        ]
        return {
            "1": random.choice(diseases),
            "2": random.choice(diseases)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum biology-based diagnostic system for early detection of {t['name']}, focusing on {t['biological_target']} and utilizing the quantum effect of {t['quantum_effect']}. Your response should include:\n\n1. Quantum Biological Mechanism (200-250 words):\n   a) Explain how the specified quantum effect could be involved in the biological process related to the disease.\n   b) Describe a hypothetical quantum biological mechanism that could be exploited for early disease detection.\n   c) Discuss any current scientific evidence or theories that support your proposed mechanism.\n\n2. Diagnostic System Design (250-300 words):\n   a) Outline the key components of your quantum biology-based diagnostic system.\n   b) Explain how your system would detect and measure the relevant quantum effects in biological samples.\n   c) Describe how your system would process and interpret the quantum biological data to diagnose the disease.\n   d) Discuss any potential advantages of your system over conventional diagnostic methods.\n\n3. Technical Challenges and Solutions (200-250 words):\n   a) Identify at least three major technical challenges in implementing your diagnostic system.\n   b) Propose innovative solutions to these challenges, explaining the scientific principles behind each solution.\n   c) Discuss any limitations of your proposed solutions and potential areas for future research.\n\n4. Clinical Application (150-200 words):\n   a) Describe how your quantum biology-based diagnostic system would be used in a clinical setting.\n   b) Explain the potential impact of your system on early disease detection and patient outcomes.\n   c) Discuss any ethical considerations related to the use of quantum biological diagnostics.\n\n5. Interdisciplinary Implications (150-200 words):\n   a) Discuss how your proposed system could contribute to our understanding of quantum effects in biological systems.\n   b) Explain potential implications of your work for other fields, such as quantum computing or drug development.\n   c) Propose a novel research direction that could emerge from the development of quantum biological diagnostics.\n\nEnsure your response demonstrates a deep understanding of both quantum mechanics and biology, as well as their potential interactions in living systems. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section (e.g., '1. Quantum Biological Mechanism', '2. Diagnostic System Design', etc.). Your total response should be between 950-1200 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of how {t['quantum_effect']} could be involved in {t['biological_target']} related to {t['name']}.",
            "The proposed quantum biology-based diagnostic system is innovative, scientifically plausible, and clearly described.",
            "At least three major technical challenges are identified, and innovative solutions are proposed with scientific principles explained.",
            "The clinical application, potential impact, and ethical considerations are thoroughly discussed.",
            "The interdisciplinary implications and potential for future research are well-explained and show originality.",
            "The response shows a deep understanding of both quantum mechanics and biology, using appropriate terminology and providing clear explanations for complex concepts.",
            "The response follows the required format with clear headings for each section.",
            "The response is between 950-1200 words in length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
