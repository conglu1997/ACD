import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                'problem': 'energy-efficient building cooling',
                'biological_inspiration': 'termite mounds',
                'industry': 'architecture'
            },
            {
                'problem': 'water purification in resource-scarce areas',
                'biological_inspiration': 'mangrove roots',
                'industry': 'environmental engineering'
            }
        ]
        return {str(i+1): task for i, task in enumerate(challenges)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic solution for {t['problem']} inspired by {t['biological_inspiration']}. Your response should include:

1. Biological Analysis (200-250 words):
   - Describe the relevant biological system ({t['biological_inspiration']}) and its key features.
   - Explain how this system addresses a challenge similar to {t['problem']}.
   - Identify the specific mechanisms or principles that could be applied to the engineering problem.

2. Biomimetic Solution Design (250-300 words):
   - Propose a detailed design for your biomimetic solution to {t['problem']}.
   - Explain how your design incorporates the biological principles identified earlier.
   - Describe the key components and their functions in your solution.
   - Include a simple diagram or schematic of your design (describe it textually).

3. Comparative Analysis (200-250 words):
   - Compare your biomimetic solution to existing conventional solutions for {t['problem']}.
   - Discuss potential advantages and disadvantages of your approach.
   - Analyze how your solution might impact sustainability and efficiency in the {t['industry']} industry.

4. Implementation Strategy (200-250 words):
   - Outline a strategy for developing and implementing your biomimetic solution.
   - Identify potential challenges in the development process and propose ways to address them.
   - Discuss any ethical considerations or potential unintended consequences of your solution.

5. Future Implications (150-200 words):
   - Speculate on how your biomimetic solution might evolve or be adapted for other applications.
   - Discuss the potential long-term impact of biomimetic approaches in the {t['industry']} industry.
   - Propose a related area of research that could further enhance biomimetic solutions in this field.

Ensure your response demonstrates a deep understanding of both the biological system and the engineering principles involved. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific and engineering plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a thorough analysis of {t['biological_inspiration']} and its relevance to {t['problem']}.",
            "The biomimetic solution design is detailed, innovative, and clearly incorporates biological principles.",
            f"The solution is compared to conventional approaches for {t['problem']} with a thoughtful analysis of advantages and disadvantages.",
            "A realistic implementation strategy is provided, addressing potential challenges and ethical considerations.",
            f"The response discusses future implications and potential evolution of the solution in the {t['industry']} industry.",
            "The overall response demonstrates a deep understanding of biomimicry, engineering principles, and the specific problem domain."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
