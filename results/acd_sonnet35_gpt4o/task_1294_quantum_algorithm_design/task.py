import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        computational_problems = [
            "graph coloring",
            "protein folding simulation",
            "cryptographic key distribution",
            "optimization of financial portfolios",
            "machine learning model training"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum tunneling",
            "quantum annealing"
        ]
        return {
            "1": {
                "problem": random.choice(computational_problems),
                "principle": random.choice(quantum_principles)
            },
            "2": {
                "problem": random.choice(computational_problems),
                "principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a novel quantum algorithm for {t['problem']}, incorporating the quantum principle of {t['principle']}. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe the overall structure and steps of your quantum algorithm.
   b) Explain how your algorithm leverages {t['principle']} to address {t['problem']}.
   c) Provide a high-level pseudocode or quantum circuit diagram of your algorithm.
   d) Discuss how your algorithm differs from classical approaches to this problem.

2. Quantum Mechanics Analysis (200-250 words):
   a) Explain the quantum mechanical principles underlying your algorithm.
   b) Discuss how {t['principle']} contributes to the algorithm's potential advantage.
   c) Analyze potential quantum effects or phenomena that could impact your algorithm's performance.

3. Complexity Analysis (150-200 words):
   a) Provide a theoretical analysis of your algorithm's time and space complexity.
   b) Compare the complexity of your quantum algorithm to the best known classical algorithm for {t['problem']}.
   c) Discuss any potential speedup or efficiency gains.

4. Implementation Considerations (200-250 words):
   a) Describe the quantum hardware requirements for implementing your algorithm.
   b) Discuss potential challenges in realizing your algorithm on current or near-term quantum devices.
   c) Propose methods to mitigate errors or decoherence effects in your implementation.

5. Potential Applications (150-200 words):
   a) Propose two novel real-world applications of your quantum algorithm.
   b) Explain how these applications could benefit from the quantum speedup or other advantages.
   c) Discuss any potential societal or economic impacts of these applications.

6. Future Research Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your quantum algorithm.
   b) Propose a novel research question that could be explored using your algorithm as a foundation.

Ensure your response demonstrates a deep understanding of quantum computing principles, algorithmic design, and the specific problem domain. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and the specified quantum principle.",
            "The algorithm design is novel, well-structured, and clearly explained.",
            "The quantum mechanics analysis is accurate and insightful.",
            "The complexity analysis is thorough and compares the quantum approach to classical methods.",
            "Implementation considerations are realistic and address current challenges in quantum computing.",
            "Proposed applications are innovative and well-reasoned.",
            "Future research directions are promising and build upon the proposed algorithm.",
            "The response is well-organized, adheres to the specified format, and meets the word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
