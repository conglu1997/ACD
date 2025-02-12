import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genomic_features = ['SNP analysis', 'Gene expression profiling', 'Epigenetic markers', 'Structural variations']
        medical_applications = ['Cancer diagnosis', 'Drug response prediction', 'Rare disease identification', 'Aging-related disorders']
        
        tasks = {
            "1": {
                "genomic_feature": random.choice(genomic_features),
                "medical_application": random.choice(medical_applications)
            },
            "2": {
                "genomic_feature": random.choice(genomic_features),
                "medical_application": random.choice(medical_applications)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum machine learning system for advanced genomic analysis, focusing on {t['genomic_feature']}, and propose novel applications in personalized medicine, specifically addressing {t['medical_application']}. Your response should include:

1. Quantum Genomic AI Architecture (300-350 words):
   a) Describe the key components of your quantum machine learning system for genomic analysis.
   b) Explain how quantum computing principles are integrated into your AI architecture.
   c) Detail how your system processes and analyzes genomic data, particularly for {t['genomic_feature']}.
   d) Include a high-level diagram or pseudocode illustrating the system's architecture (describe it textually).

2. Quantum Advantage in Genomics (250-300 words):
   a) Explain how your quantum AI system provides advantages over classical machine learning approaches in genomic analysis.
   b) Discuss specific quantum algorithms or techniques used in your system and their benefits.
   c) Quantify the expected improvement in performance or efficiency, if possible.

3. Application to {t['medical_application']} (300-350 words):
   a) Describe how your quantum genomic AI system would be applied to {t['medical_application']}.
   b) Explain the specific genomic features or patterns your system would analyze for this application.
   c) Discuss potential breakthroughs or novel insights your system might uncover.
   d) Propose a step-by-step process for using your system in a clinical setting.

4. Data Management and Privacy (200-250 words):
   a) Explain how your system handles large-scale genomic data sets.
   b) Discuss data privacy and security measures, considering the sensitive nature of genomic information.
   c) Describe any quantum encryption techniques used to protect patient data.

5. Ethical Implications and Societal Impact (200-250 words):
   a) Discuss ethical considerations related to using quantum AI for genomic analysis and personalized medicine.
   b) Address potential societal impacts, both positive and negative, of your proposed system.
   c) Suggest guidelines for responsible development and use of quantum genomic AI technologies.

6. Future Directions and Challenges (200-250 words):
   a) Identify potential limitations or challenges in implementing your quantum genomic AI system.
   b) Propose two future research directions that could enhance the capabilities of your system.
   c) Discuss how advancements in quantum computing might influence the evolution of your system.

Ensure your response demonstrates a deep understanding of quantum computing, genomics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, genomics, and artificial intelligence.",
            "The proposed quantum genomic AI system is innovative and scientifically plausible.",
            "The application to the specified medical field is well-explained and shows potential for significant impact.",
            "The discussion of ethical implications and societal impact is thoughtful and comprehensive.",
            "The response addresses all required sections and adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
