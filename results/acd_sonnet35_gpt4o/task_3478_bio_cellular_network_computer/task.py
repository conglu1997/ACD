import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        computational_problems = [
            {"problem": "protein folding prediction", "domain": "structural biology"},
            {"problem": "climate model simulation", "domain": "environmental science"},
            {"problem": "cryptographic key generation", "domain": "cybersecurity"},
            {"problem": "optimization of supply chain logistics", "domain": "operations research"},
            {"problem": "drug interaction prediction", "domain": "pharmacology"}
        ]
        return {
            "1": random.choice(computational_problems),
            "2": random.choice(computational_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biological computing system using cellular communication networks and apply it to solve the complex computational problem of {t['problem']} in the domain of {t['domain']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your bio-cellular network computer.
   b) Explain how cellular communication mechanisms are used for information processing.
   c) Detail any novel biological or synthetic components incorporated in your design.
   d) Include a high-level diagram or flowchart of your system's architecture (describe it textually).

2. Information Encoding and Processing (250-300 words):
   a) Explain how information is encoded in your biological system.
   b) Describe the mechanisms for information transmission and processing between cells.
   c) Discuss how your system handles error correction and noise reduction.

3. Problem-Specific Implementation (300-350 words):
   a) Outline how your bio-cellular network computer approaches the given computational problem.
   b) Describe any specific adaptations or optimizations for the problem domain.
   c) Compare the potential advantages of your biological approach to traditional computing methods for this problem.

4. Scalability and Performance Analysis (250-300 words):
   a) Discuss the scalability of your system for larger or more complex problems.
   b) Analyze the theoretical performance capabilities of your bio-cellular network computer.
   c) Propose methods for benchmarking your system against traditional computers.

5. Ethical and Safety Considerations (200-250 words):
   a) Discuss potential biosafety concerns related to your system and how they can be addressed.
   b) Explore ethical implications of using engineered biological systems for computation.
   c) Propose guidelines for responsible development and use of bio-cellular network computers.

6. Future Developments and Applications (200-250 words):
   a) Suggest potential improvements or extensions to your bio-cellular network computer.
   b) Discuss how advances in this field might impact computing, biology, and related disciplines.
   c) Propose two novel applications of bio-cellular network computers beyond the given problem.

Ensure your response demonstrates a deep understanding of cellular biology, information theory, and complex systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses all six sections related to the bio-cellular network computer design for {t['problem']}.",
            "The proposed system architecture is innovative and scientifically plausible.",
            "The explanation demonstrates a deep understanding of cellular biology, information theory, and complex systems.",
            "The problem-specific implementation is well-thought-out and relevant to the given computational problem.",
            "The analysis of scalability, performance, and ethical considerations is thorough and insightful.",
            "The discussion of future developments and applications is creative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
