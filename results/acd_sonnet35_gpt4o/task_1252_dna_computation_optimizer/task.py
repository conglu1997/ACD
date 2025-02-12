import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        optimization_problems = [
            {
                "problem": "traveling salesman problem",
                "application": "logistics and supply chain optimization"
            },
            {
                "problem": "protein folding prediction",
                "application": "drug discovery and personalized medicine"
            },
            {
                "problem": "maximum cut problem",
                "application": "network design and VLSI circuit layout"
            },
            {
                "problem": "job shop scheduling",
                "application": "manufacturing process optimization"
            }
        ]
        return {
            "1": random.choice(optimization_problems),
            "2": random.choice(optimization_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a DNA-based computation system to solve the {t['problem']}, and analyze its potential applications in {t['application']}. Your response should include:

1. DNA Computation System Design (250-300 words):
   a) Describe the key components of your DNA-based computation system.
   b) Explain how DNA molecules are used to represent and process information in your system.
   c) Detail the encoding scheme for representing the {t['problem']} using DNA sequences.
   d) Outline the main steps of your DNA algorithm for solving the optimization problem.

2. Molecular Biology Techniques (200-250 words):
   a) Discuss the specific molecular biology techniques used in your system (e.g., PCR, gel electrophoresis, DNA synthesis).
   b) Explain how these techniques contribute to the computation process.
   c) Address any potential biological limitations or challenges in implementing your system.

3. Computational Analysis (200-250 words):
   a) Analyze the computational complexity of your DNA-based algorithm.
   b) Compare the efficiency of your system to traditional electronic computing methods for solving the {t['problem']}.
   c) Discuss any novel computational properties or advantages offered by your DNA-based approach.

4. Application to {t['application']} (200-250 words):
   a) Explain how your DNA computation system could be applied to {t['application']}.
   b) Describe the potential benefits and challenges of using DNA computation in this field.
   c) Propose a specific use case and discuss its potential impact.

5. Scalability and Future Prospects (150-200 words):
   a) Discuss the scalability of your DNA computation system for larger problem instances.
   b) Propose potential improvements or extensions to your system.
   c) Speculate on future applications of DNA computation beyond the current problem domain.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to DNA-based computation.
   b) Propose guidelines for responsible development and use of this technology.

7. Summary (50-100 words):
   Provide a brief summary of your DNA computation system, its key advantages, and its potential impact on solving the {t['problem']} and its application to {t['application']}.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and computational complexity. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing practical considerations.

Your total response should be between 1150-1500 words. Please include a word count at the end of your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of DNA-based computation and molecular biology techniques.",
            "The DNA computation system design is innovative, well-explained, and scientifically plausible.",
            "The computational analysis shows a clear understanding of algorithmic complexity and comparison with traditional methods.",
            "The application to the specified field is thoughtful and demonstrates potential real-world impact.",
            "Ethical considerations are addressed comprehensively and responsibly.",
            "The summary effectively encapsulates the key points of the proposed system and its potential impact."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
