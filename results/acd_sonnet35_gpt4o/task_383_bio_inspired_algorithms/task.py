import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "photosynthesis",
            "neural plasticity",
            "immune response",
            "cellular respiration",
            "DNA replication",
            "protein folding",
            "symbiosis",
            "bioluminescence"
        ]
        computational_problems = [
            "resource allocation",
            "pattern recognition",
            "data compression",
            "network optimization",
            "anomaly detection",
            "predictive modeling",
            "multi-objective optimization",
            "adaptive learning"
        ]
        return {
            "1": {
                "biological_process": random.choice(biological_processes),
                "computational_problem": random.choice(computational_problems)
            },
            "2": {
                "biological_process": random.choice(biological_processes),
                "computational_problem": random.choice(computational_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel and original bio-inspired algorithm based on the biological process of {t['biological_process']} and apply it to solve the computational problem of {t['computational_problem']}. Your task has the following parts:

1. Biological Process Analysis (150-200 words):
   a) Explain the key mechanisms and principles of {t['biological_process']}.
   b) Identify the aspects of this process that could be relevant to algorithm design.

2. Algorithm Design (250-300 words):
   a) Describe your bio-inspired algorithm, explaining how it mimics or draws inspiration from {t['biological_process']}.
   b) Outline the main steps of the algorithm using pseudocode or a flowchart.
   c) Explain how your algorithm addresses the problem of {t['computational_problem']}.
   d) Highlight the innovative aspects of your algorithm that distinguish it from existing approaches.

3. Implementation Considerations (150-200 words):
   a) Discuss potential challenges in implementing your algorithm.
   b) Propose solutions or workarounds for these challenges.
   c) Suggest appropriate data structures or programming paradigms for implementation.

4. Performance Analysis (200-250 words):
   a) Analyze the theoretical time and space complexity of your algorithm.
   b) Compare its expected performance to existing algorithms for {t['computational_problem']}.
   c) Discuss any trade-offs between biological accuracy and computational efficiency.

5. Broader Implications (150-200 words):
   a) Explore potential applications of your algorithm beyond {t['computational_problem']}.
   b) Discuss how this bio-inspired approach might contribute to the field of bioinformatics or computational biology.
   c) Propose an experiment to test the effectiveness of your algorithm in a real-world scenario.

Ensure your response demonstrates a deep understanding of both the biological process and the computational problem. Be creative and original in your algorithm design while maintaining scientific plausibility. Your total response should be between 900-1150 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['biological_process']} and its relevance to algorithm design.",
            f"The algorithm design must be clearly inspired by {t['biological_process']} and address {t['computational_problem']}.",
            "The algorithm must be presented in pseudocode or flowchart format.",
            "The algorithm design must demonstrate originality and innovation.",
            "Implementation challenges and solutions must be discussed.",
            "The response must include a theoretical analysis of time and space complexity.",
            "The algorithm's performance must be compared to existing algorithms for the given problem.",
            "The response must explore broader implications and potential applications of the bio-inspired algorithm.",
            "The overall response must demonstrate creativity, scientific plausibility, and interdisciplinary knowledge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
