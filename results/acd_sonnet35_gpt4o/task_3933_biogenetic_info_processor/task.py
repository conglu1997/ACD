import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "DNA replication",
            "Transcription",
            "Translation",
            "Gene regulation"
        ]
        data_analysis_problems = [
            "Anomaly detection in financial transactions",
            "Prediction of protein folding structures",
            "Analysis of social network dynamics",
            "Climate pattern forecasting"
        ]
        information_theory_concepts = [
            "Shannon entropy",
            "Mutual information",
            "Error correction",
            "Data compression"
        ]
        
        tasks = [
            {
                "biological_process": random.choice(biological_processes),
                "data_analysis_problem": random.choice(data_analysis_problems),
                "information_theory_concept": random.choice(information_theory_concepts)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired information processing system that mimics {t['biological_process']} to solve the complex data analysis problem of {t['data_analysis_problem']}, while incorporating the information theory concept of {t['information_theory_concept']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your bio-inspired information processing system.
   b) Explain how your system mimics {t['biological_process']} in its design and function.
   c) Detail how you've incorporated {t['information_theory_concept']} into your system.
   d) Provide a high-level diagram of your system architecture (describe it textually).

2. Biological-Computational Mapping (250-300 words):
   a) Explain how specific elements of {t['biological_process']} are translated into computational processes.
   b) Describe any novel algorithms or data structures inspired by this biological process.
   c) Discuss how this bio-inspired approach differs from traditional computing methods.

3. Application to {t['data_analysis_problem']} (300-350 words):
   a) Describe how your system would approach solving {t['data_analysis_problem']}.
   b) Explain the specific advantages your bio-inspired system offers for this problem.
   c) Discuss any potential limitations or challenges in applying your system to this problem.
   d) Provide an example of how your system would process a small dataset related to this problem.

4. Information Theoretic Analysis (200-250 words):
   a) Analyze your system's performance using the concept of {t['information_theory_concept']}.
   b) Explain how this analysis provides insights into your system's efficiency or effectiveness.
   c) Discuss how your bio-inspired approach might optimize information processing compared to traditional methods.

5. Comparative Analysis (200-250 words):
   a) Compare your bio-inspired system to a traditional approach for solving {t['data_analysis_problem']}.
   b) Discuss potential advantages and limitations of your approach.
   c) Analyze how closely your system might approximate or improve upon biological information processing.

6. Ethical Implications and Societal Impact (200-250 words):
   a) Discuss potential ethical concerns related to using bio-inspired systems for data analysis.
   b) Explore how your system might impact privacy, decision-making, or other societal issues.
   c) Propose guidelines for the responsible development and use of bio-inspired information processing systems.

7. Future Developments (150-200 words):
   a) Suggest two potential advancements or applications of your bio-inspired system.
   b) Discuss how progress in molecular biology or information theory might further enhance your system.
   c) Propose a research agenda to address current limitations in bio-inspired computing.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific biological process of {t['biological_process']}, the data analysis problem of {t['data_analysis_problem']}, and the information theory concept of {t['information_theory_concept']}",
            "The design should clearly integrate principles from molecular biology, information theory, and artificial intelligence",
            "The response should include all required sections: System Architecture, Biological-Computational Mapping, Application to the data analysis problem, Information Theoretic Analysis, Comparative Analysis, Ethical Implications and Societal Impact, and Future Developments",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response should demonstrate a deep understanding of molecular biology, information theory, and artificial intelligence",
            "The discussion should be creative while addressing potential challenges, limitations, and ethical implications"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
