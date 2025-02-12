import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dna_bases = ['A', 'T', 'C', 'G']
        quantum_properties = ['superposition', 'entanglement', 'tunneling']
        genetic_applications = ['gene editing', 'protein folding prediction', 'epigenetic modification']
        medical_fields = ['oncology', 'neurology', 'immunology']
        
        return {
            "1": {
                "dna_base": random.choice(dna_bases),
                "quantum_property": random.choice(quantum_properties),
                "genetic_application": random.choice(genetic_applications),
                "medical_field": random.choice(medical_fields)
            },
            "2": {
                "dna_base": random.choice(dna_bases),
                "quantum_property": random.choice(quantum_properties),
                "genetic_application": random.choice(genetic_applications),
                "medical_field": random.choice(medical_fields)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical DNA-based quantum computing system for genetic engineering, focusing on the DNA base {t['dna_base']}, utilizing the quantum property of {t['quantum_property']}, and applying it to {t['genetic_application']}. Then, analyze its potential applications in personalized medicine, specifically in the field of {t['medical_field']}. Your response should include:\n\n1. Quantum-DNA Interface (200-250 words):\n   a) Explain how the chosen DNA base can be used as a qubit.\n   b) Describe how the specified quantum property is leveraged in your system.\n   c) Propose a method for manipulating and reading the quantum state of the DNA-based qubits.\n\n2. Genetic Engineering Application (200-250 words):\n   a) Detail how your system would be applied to the specified genetic engineering task.\n   b) Discuss the advantages of your quantum approach over classical methods.\n   c) Address potential challenges and limitations of your approach.\n\n3. Personalized Medicine Integration (150-200 words):\n   a) Explain how your system could be applied in the specified medical field.\n   b) Describe a specific scenario where it could improve patient outcomes.\n   c) Discuss how it might change current medical practices in this field.\n\n4. Ethical Considerations (100-150 words):\n   a) Identify potential ethical issues arising from this technology.\n   b) Discuss how these issues might be addressed or mitigated.\n   c) Propose guidelines for responsible development and use of this technology.\n\n5. Future Implications (100-150 words):\n   a) Speculate on how this technology might evolve in the next 20-30 years.\n   b) Discuss potential societal impacts beyond medicine.\n   c) Propose a novel application of this technology in another field.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, genetics, and medical science. Be creative and innovative while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 750-1000 words.\n\nYour response will be evaluated based on the depth of understanding shown, the innovation and plausibility of your proposed system, the thoroughness of your discussion on applications and ethical considerations, and the clarity and structure of your writing."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, genetics, and medical science.",
            "The proposed DNA-based quantum computing system is innovative, plausible, and well-explained.",
            "The genetic engineering application and personalized medicine integration are thoroughly discussed and scientifically sound.",
            "Ethical considerations are thoughtfully analyzed and future implications are creatively explored.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        result = eval_with_llm_judge(instructions, submission, criteria)
        return 1.0 if result else 0.0
