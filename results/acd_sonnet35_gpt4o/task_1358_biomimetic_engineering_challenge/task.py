import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "biological_system": "Spider silk production",
                "engineering_problem": "Creating strong, lightweight materials for aerospace applications"
            },
            {
                "biological_system": "Photosynthesis in plants",
                "engineering_problem": "Developing more efficient solar energy capture and storage systems"
            },
            {
                "biological_system": "Whale fin hydrodynamics",
                "engineering_problem": "Improving the efficiency of wind turbine blades"
            }
        ]
        return {str(i+1): challenge for i, challenge in enumerate(random.sample(challenges, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the biological system of {t['biological_system']} and design a biomimetic solution to the engineering problem of {t['engineering_problem']}. Your response should include the following sections:

1. Biological System Analysis (200-250 words):
   a) Describe the key features and mechanisms of {t['biological_system']}.
   b) Explain how these features contribute to the system's efficiency or effectiveness.
   c) Identify specific aspects that could be relevant to solving the engineering problem.

2. Biomimetic Solution Design (250-300 words):
   a) Propose an innovative solution to {t['engineering_problem']} inspired by {t['biological_system']}.
   b) Explain how your solution mimics or adapts the biological system's features.
   c) Describe the key components and mechanisms of your proposed solution.
   d) Include a simple diagram or sketch of your design (use ASCII art).

3. Feasibility and Scalability Analysis (200-250 words):
   a) Discuss the technical feasibility of implementing your solution.
   b) Analyze potential challenges in scaling up the solution for practical applications.
   c) Propose strategies to overcome these challenges.

4. Sustainability Assessment (150-200 words):
   a) Evaluate the environmental impact of your proposed solution.
   b) Compare its sustainability to existing solutions for the engineering problem.
   c) Suggest improvements to enhance the solution's overall sustainability.

5. Interdisciplinary Connections (150-200 words):
   a) Identify two fields of study, other than biology and engineering, that could contribute to refining or implementing your solution.
   b) Explain how insights from these fields could be integrated into your design.

6. Future Research Directions (100-150 words):
   a) Propose two specific research questions or experiments to further develop your biomimetic solution.
   b) Explain how answering these questions could lead to improvements in your design.

Ensure your response demonstrates a deep understanding of both the biological system and the engineering problem. Be creative in your solution while maintaining scientific and engineering plausibility. Your total response should be between 1050-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the biological system and its relevance to the engineering problem",
            "The proposed biomimetic solution is innovative, well-explained, and plausibly addresses the engineering problem",
            "The feasibility and scalability analysis is comprehensive and identifies realistic challenges and solutions",
            "The sustainability assessment critically evaluates the environmental impact of the proposed solution",
            "The interdisciplinary connections are relevant and well-justified",
            "The future research directions are specific and have the potential to meaningfully improve the proposed solution",
            "The response includes all required sections and falls within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
