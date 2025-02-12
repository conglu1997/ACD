import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "biological_adaptation": "lotus leaf's water-repellent surface",
                "tech_challenge": "developing self-cleaning solar panels"
            },
            {
                "biological_adaptation": "gecko's adhesive foot pads",
                "tech_challenge": "creating reusable adhesives for space applications"
            },
            {
                "biological_adaptation": "whale's flipper design",
                "tech_challenge": "improving wind turbine efficiency"
            },
            {
                "biological_adaptation": "spider silk's strength and elasticity",
                "tech_challenge": "developing lightweight, high-strength materials for aerospace"
            },
            {
                "biological_adaptation": "butterfly wing's structural color",
                "tech_challenge": "creating energy-efficient color displays"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel technological solution inspired by the {t['biological_adaptation']} to address the challenge of {t['tech_challenge']}. Your response should include the following sections:

1. Biological Inspiration (200-250 words):
   a) Describe the key features and mechanisms of the {t['biological_adaptation']}.
   b) Explain how these features contribute to the organism's survival or function.
   c) Discuss any existing research or applications related to this biological adaptation.

2. Technology Challenge Analysis (150-200 words):
   a) Analyze the key issues and requirements for {t['tech_challenge']}.
   b) Identify the main obstacles that need to be overcome.
   c) Discuss any existing approaches to this challenge and their limitations.

3. Biomimetic Solution Design (250-300 words):
   a) Propose your novel technological solution inspired by the biological adaptation.
   b) Explain how your design mimics or adapts the biological principles.
   c) Describe the key components and mechanisms of your solution.
   d) Include a simple ASCII art diagram illustrating your design.

4. Feasibility and Implementation (200-250 words):
   a) Discuss the potential materials and manufacturing processes for your solution.
   b) Analyze the technical feasibility of your design.
   c) Identify any challenges in scaling or implementing your solution.
   d) Propose methods to overcome these challenges.

5. Performance Analysis (150-200 words):
   a) Predict the potential performance improvements of your solution.
   b) Compare your solution to existing technologies addressing the same challenge.
   c) Discuss any potential limitations or trade-offs of your design.

6. Environmental and Economic Impact (100-150 words):
   a) Analyze the potential environmental benefits or risks of your solution.
   b) Discuss the economic viability and potential market impact of your technology.

7. Future Research Directions (100-150 words):
   a) Propose two areas for further research to enhance or expand your solution.
   b) Suggest a potential collaboration between disciplines that could advance this technology.

Ensure your response demonstrates a deep understanding of both the biological principles and the engineering challenges involved. Be creative in your solution while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['biological_adaptation']} and its relevance to {t['tech_challenge']}.",
            "The proposed solution is innovative and clearly inspired by the biological adaptation.",
            "The design is described in detail, including key components and mechanisms.",
            "The feasibility analysis addresses materials, manufacturing, and implementation challenges.",
            "The performance analysis compares the solution to existing technologies and discusses limitations.",
            "The environmental and economic impacts are thoughtfully considered.",
            "Future research directions are proposed and relevant to advancing the technology.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
