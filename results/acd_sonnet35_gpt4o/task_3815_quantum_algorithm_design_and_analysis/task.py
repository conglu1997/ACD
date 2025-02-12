import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        computational_problems = [
            "protein folding prediction",
            "climate model optimization",
            "cryptographic code breaking",
            "financial market simulation"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        return {
            str(i+1): {
                'problem': random.choice(computational_problems),
                'principle': random.choice(quantum_principles)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm to solve the computational problem of {t['problem']}, emphasizing the use of the quantum principle of {t['principle']}. Then, analyze its potential impact on various scientific and technological fields. Your response should include:

1. Algorithm Design (300-350 words):
   a) Provide a name for your quantum algorithm.
   b) Explain the key steps of your algorithm, using appropriate quantum computing terminology.
   c) Describe how your algorithm specifically utilizes {t['principle']} to address {t['problem']}.
   d) Compare your approach to classical computing methods for solving this problem.
   e) Include a high-level pseudocode or quantum circuit diagram to illustrate your algorithm (describe it textually).

2. Theoretical Analysis (250-300 words):
   a) Analyze the theoretical time and space complexity of your algorithm.
   b) Discuss any quantum advantages your algorithm provides over classical methods.
   c) Identify potential limitations or challenges in implementing your algorithm on current or near-future quantum hardware.

3. Interdisciplinary Applications (200-250 words):
   a) Propose three potential applications of your algorithm in different scientific or technological domains.
   b) Explain how each application could benefit from the unique features of your quantum approach.
   c) Discuss any modifications or extensions needed to adapt your algorithm for these applications.

4. Societal and Economic Impact (200-250 words):
   a) Analyze the potential societal impacts of widespread adoption of your quantum algorithm.
   b) Discuss possible economic implications, including potential disruptions to existing industries.
   c) Consider any ethical concerns that might arise from the use of your algorithm.

5. Future Research Directions (150-200 words):
   a) Propose two potential improvements or extensions to your quantum algorithm.
   b) Suggest a research experiment to test the efficiency or applicability of your algorithm.
   c) Discuss how advancements in quantum hardware might affect the implementation of your algorithm.

Ensure your response demonstrates a deep understanding of quantum computing principles, algorithmic design, and interdisciplinary applications. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, following the structure outlined above. Your total response should be between 1100-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their application to the given problem",
            "The proposed quantum algorithm is novel, well-explained, and plausibly addresses the specified computational problem",
            "The analysis of the algorithm's impact on various fields is thorough and insightful",
            "The response shows creativity and speculative thinking while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
