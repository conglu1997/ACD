import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "challenge": "Urban loneliness in megacities",
                "culture1": "Ancient Greek city-states",
                "culture2": "Modern Japanese society",
                "historical_period": "Industrial Revolution"
            },
            {
                "challenge": "Sustainable food production in arid regions",
                "culture1": "Native American Pueblo communities",
                "culture2": "Ancient Egyptian civilization",
                "historical_period": "Age of Exploration"
            },
            {
                "challenge": "Intergenerational knowledge transfer",
                "culture1": "Polynesian wayfinding traditions",
                "culture2": "European Renaissance guilds",
                "historical_period": "Information Age"
            },
            {
                "challenge": "Equitable access to healthcare",
                "culture1": "Traditional Chinese medicine",
                "culture2": "Scandinavian welfare systems",
                "historical_period": "Post-World War II era"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an innovative solution to address the societal challenge of {t['challenge']} by synthesizing elements from {t['culture1']} and {t['culture2']}, while also incorporating relevant insights from the {t['historical_period']}. Your response should include:

1. Problem Analysis (200-250 words):
   a) Analyze the root causes and current impacts of the given societal challenge.
   b) Discuss how this challenge manifests in contemporary society.
   c) Identify key stakeholders and their perspectives on the issue.

2. Cultural Synthesis (250-300 words):
   a) Describe relevant aspects of {t['culture1']} and {t['culture2']} that could inform a solution.
   b) Explain how these cultural elements address similar challenges or values.
   c) Discuss any potential conflicts or synergies between the two cultures' approaches.

3. Historical Insight (150-200 words):
   a) Analyze how the {t['historical_period']} relates to the current challenge.
   b) Identify lessons or cautionary tales from this period that could inform your solution.

4. Innovative Solution (300-350 words):
   a) Present your proposed solution, clearly explaining how it synthesizes elements from the given cultures and historical period.
   b) Describe how your solution addresses the root causes identified in the problem analysis.
   c) Explain the potential social, economic, and cultural impacts of your solution.
   d) Discuss how your solution balances innovation with cultural sensitivity and historical awareness.

5. Implementation Strategy (200-250 words):
   a) Outline a step-by-step plan for implementing your solution.
   b) Address potential challenges and resistance to implementation.
   c) Propose methods for measuring the success and impact of your solution.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications or unintended consequences of your solution.
   b) Propose guidelines for ensuring cultural respect and avoiding cultural appropriation in the implementation of your solution.
   c) Address how your solution might impact different socioeconomic groups.

Ensure your response demonstrates a deep understanding of the given cultures, historical period, and contemporary societal challenges. Use appropriate terminology and provide explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and practical feasibility.

Format your response with clear headings for each section and include the word count for each section in parentheses at the end of the section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly address the societal challenge of {t['challenge']}.",
            f"The proposed solution must meaningfully and creatively incorporate elements from both {t['culture1']} and {t['culture2']}.",
            f"The solution must demonstrate relevant and insightful applications of knowledge from the {t['historical_period']}.",
            "The response must include all six required sections as specified in the instructions, with each section adequately addressing its respective topics and meeting the specified word count range.",
            "The proposed solution must be innovative, culturally sensitive, and demonstrate a clear understanding of how diverse cultural elements can be synthesized to address contemporary challenges.",
            "The implementation strategy must be well-thought-out, realistic, and address potential challenges and methods for measuring success.",
            "The response must demonstrate a deep understanding of the given cultures, historical period, and contemporary societal challenges, showing evidence of thorough research and critical thinking.",
            "The ethical considerations must be thoughtful, comprehensive, and demonstrate an understanding of potential unintended consequences, cultural sensitivities, and impacts on different socioeconomic groups.",
            "The overall response must be well-structured, coherent, and demonstrate a high level of interdisciplinary thinking and problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
