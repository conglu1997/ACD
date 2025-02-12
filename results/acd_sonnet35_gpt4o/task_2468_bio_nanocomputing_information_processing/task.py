import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "ocean microplastic detection",
            "air pollution particulate analysis",
            "soil contamination mapping"
        ]
        medical_diagnostics = [
            "early-stage cancer detection",
            "antibiotic resistance identification",
            "neurodegenerative disease biomarker analysis"
        ]
        dna_computing_principles = [
            "DNA strand displacement",
            "DNA tile assembly",
            "DNA origami"
        ]
        
        return {
            "1": {
                "environmental_challenge": random.choice(environmental_challenges),
                "medical_diagnostic": random.choice(medical_diagnostics),
                "dna_computing_principle": random.choice(dna_computing_principles)
            },
            "2": {
                "environmental_challenge": random.choice(environmental_challenges),
                "medical_diagnostic": random.choice(medical_diagnostics),
                "dna_computing_principle": random.choice(dna_computing_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-nanocomputing system that uses DNA-based information processing to address both an environmental monitoring challenge ({t['environmental_challenge']}) and a medical diagnostic challenge ({t['medical_diagnostic']}). Your system should incorporate the DNA computing principle of {t['dna_computing_principle']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your bio-nanocomputing system.
   b) Explain how DNA-based information processing is integrated into the system.
   c) Detail how the system incorporates the specified DNA computing principle.
   d) Provide a textual description of a schematic representation of your system.

2. Environmental Monitoring Application (250-300 words):
   a) Explain how your system addresses the given environmental challenge.
   b) Describe the DNA-based mechanisms used for detection and data processing.
   c) Discuss the advantages of your approach over traditional monitoring methods.
   d) Address potential challenges and limitations of using bio-nanocomputing for this application.

3. Medical Diagnostic Application (250-300 words):
   a) Detail how your system tackles the specified medical diagnostic challenge.
   b) Explain the DNA-based algorithms or processes used for diagnosis.
   c) Compare the sensitivity and specificity of your system to current diagnostic methods.
   d) Discuss any ethical considerations related to using bio-nanocomputing for medical diagnostics.

4. Information Processing and Analysis (200-250 words):
   a) Describe how information is encoded, processed, and retrieved in your DNA-based system.
   b) Explain any novel data structures or algorithms used in your approach.
   c) Discuss the theoretical information processing capacity of your system.
   d) Address how your system handles potential errors or mutations in DNA sequences.

5. Implementation and Scalability (200-250 words):
   a) Outline the steps required to implement your system in real-world settings.
   b) Discuss challenges in scaling the system for widespread use.
   c) Propose solutions to overcome these challenges.
   d) Consider the cost-effectiveness of your approach compared to existing technologies.

6. Future Prospects and Societal Impact (150-200 words):
   a) Speculate on potential future applications of your bio-nanocomputing system.
   b) Discuss how it might impact healthcare, environmental science, and related fields.
   c) Consider any unintended consequences or ethical dilemmas that might arise.
   d) Suggest areas for further research and development in bio-nanocomputing.

Ensure your response demonstrates a deep understanding of biology, nanotechnology, and information theory. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and considering real-world implications.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly address both the environmental challenge of {t['environmental_challenge']} and the medical diagnostic challenge of {t['medical_diagnostic']}.",
            f"The system should incorporate the DNA computing principle of {t['dna_computing_principle']} in a scientifically plausible manner.",
            "The answer should demonstrate a deep understanding of biology, nanotechnology, and information theory.",
            "The proposed bio-nanocomputing system should be innovative while remaining scientifically grounded.",
            "All six requested sections should be present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
