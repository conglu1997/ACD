import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "field": "Quantum Biology",
                "hypothesis": "Quantum entanglement plays a significant role in avian magnetoreception and influences migratory patterns across multiple generations",
                "constraint": "Experiments must be non-invasive, conducted on live birds, and span at least three generations"
            },
            {
                "field": "Astrobiology",
                "hypothesis": "Certain extremophiles can survive in simulated Martian atmospheric conditions and potentially terraform their immediate environment",
                "constraint": "Experiments must be conducted within a budget of $500,000, completed within 18 months, and include a small-scale simulation of Martian soil composition"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an innovative scientific experiment to test the following hypothesis in the field of {t['field']}:

Hypothesis: {t['hypothesis']}

Constraint: {t['constraint']}

Your task is to create a detailed experimental design that addresses this hypothesis while adhering to the given constraint. Your response should include:

1. Experimental Design (250-300 words):
   a) Outline the key components of your experimental setup.
   b) Describe the methods and procedures you would use to test the hypothesis.
   c) Explain how your design addresses the given constraint.
   d) Discuss any novel techniques or technologies you would employ.

2. Data Collection and Analysis (200-250 words):
   a) Describe the types of data you would collect.
   b) Explain your proposed data analysis methods.
   c) Discuss how you would interpret different possible outcomes.

3. Potential Challenges and Solutions (150-200 words):
   a) Identify at least two potential challenges in implementing your experiment.
   b) Propose solutions or workarounds for these challenges.

4. Ethical Considerations (100-150 words):
   a) Discuss any ethical implications of your experimental design.
   b) Propose safeguards or guidelines to address these ethical concerns.

5. Interdisciplinary Connections (150-200 words):
   a) Explain how your experiment integrates knowledge from at least two other scientific disciplines.
   b) Discuss how these connections enhance the validity or impact of your experiment.

6. Potential Impact and Future Directions (150-200 words):
   a) Describe the potential scientific impact if your hypothesis is supported.
   b) Suggest two follow-up studies that could build on your experimental results.

Ensure your response is creative yet grounded in scientific principles. Use appropriate scientific terminology and provide explanations where necessary. Your total response should be between 1000-1300 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The experimental design is innovative and scientifically sound",
            "The proposed methods effectively test the given hypothesis",
            "The design adheres to the specified constraint",
            "The response addresses all required sections (Experimental Design, Data Collection and Analysis, Potential Challenges and Solutions, Ethical Considerations, Interdisciplinary Connections, Potential Impact and Future Directions)",
            "The experiment integrates knowledge from multiple scientific disciplines",
            "The response demonstrates a strong understanding of experimental design principles and creative problem-solving",
            "Ethical implications are thoughtfully considered and addressed",
            "The potential impact and future directions are well-reasoned and scientifically relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
