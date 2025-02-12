import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "problem": "Energy-efficient building cooling",
                "biological_inspiration": "Termite mounds",
                "constraint": "Must reduce energy consumption by at least 30%"
            },
            {
                "problem": "Water purification in resource-scarce areas",
                "biological_inspiration": "Mangrove roots",
                "constraint": "Must be low-cost and require minimal maintenance"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic solution for {t['problem']}, inspired by {t['biological_inspiration']}. Your solution must {t['constraint']}. Provide your response in the following format:

1. Biological System Analysis (200-250 words):
   a) Describe the key features and mechanisms of {t['biological_inspiration']} relevant to {t['problem']}.
   b) Explain how these features contribute to efficiency or effectiveness in nature.

2. Biomimetic Solution Design (300-350 words):
   a) Present your biomimetic solution, detailing its structure and function.
   b) Explain how your design mimics or adapts the biological system's key features.
   c) Describe how your solution addresses {t['problem']} and meets the constraint.
   d) Include a simple diagram or schematic of your design (use ASCII art or a text-based description).

3. Engineering Principles (200-250 words):
   a) Discuss the core engineering principles utilized in your solution.
   b) Explain how these principles interact with the biomimetic aspects of your design.
   c) Address any potential challenges in implementing your solution and how they might be overcome.

4. Performance Analysis (250-300 words):
   a) Predict the performance of your biomimetic solution in addressing {t['problem']}.
   b) Compare your solution to existing technologies or methods for {t['problem']}.
   c) Discuss how your solution meets or exceeds the given constraint.
   d) Identify any potential limitations or drawbacks of your approach.

5. Sustainability and Scalability (150-200 words):
   a) Analyze the environmental impact and sustainability of your solution.
   b) Discuss the potential for scaling your solution for wider implementation.
   c) Address any ethical considerations related to your biomimetic design.

6. Future Developments (150-200 words):
   a) Propose two potential improvements or extensions to your biomimetic solution.
   b) Suggest how your approach could be applied to other engineering challenges.
   c) Discuss the broader implications of your biomimetic solution for the field of sustainable engineering.

Ensure your response demonstrates a deep understanding of both the biological system and relevant engineering principles. Be creative in your approach while maintaining scientific and engineering plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the biological system and its relevance to the engineering problem.",
            "The biomimetic solution is creative, well-designed, and effectively addresses the given problem and constraint.",
            "The explanation of engineering principles is accurate and shows how they integrate with the biomimetic aspects.",
            "The performance analysis is insightful and provides a meaningful comparison to existing technologies.",
            "The discussion of sustainability, scalability, and future developments is thoughtful and relevant.",
            "The overall response shows a high level of interdisciplinary knowledge integration and problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
