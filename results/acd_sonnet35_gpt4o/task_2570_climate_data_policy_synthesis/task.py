import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "rising sea levels",
            "biodiversity loss",
            "extreme weather events",
            "agricultural disruption",
            "urban heat islands",
            "water scarcity"
        ]
        data_types = [
            "satellite imagery",
            "weather station records",
            "ocean temperature and acidity measurements",
            "greenhouse gas emission data",
            "biodiversity surveys",
            "socioeconomic indicators"
        ]
        policy_domains = [
            "energy sector",
            "transportation",
            "urban planning",
            "agriculture and food systems",
            "industrial emissions",
            "ecosystem conservation"
        ]
        
        tasks = {
            "1": {
                "challenge": random.choice(environmental_challenges),
                "data_type": random.choice(data_types),
                "policy_domain": random.choice(policy_domains)
            },
            "2": {
                "challenge": random.choice(environmental_challenges),
                "data_type": random.choice(data_types),
                "policy_domain": random.choice(policy_domains)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze complex climate data sets, identify trends and patterns, and propose evidence-based policy recommendations to address the environmental challenge of {t['challenge']}. Focus on using {t['data_type']} and develop policy recommendations for the {t['policy_domain']}.

Your response should include the following sections:

1. Data Analysis (300-350 words):
   a) Describe the key characteristics of the {t['data_type']} you would analyze for this challenge.
   b) Explain your approach to processing and analyzing this data, including any specific techniques or algorithms you would use.
   c) Identify three key trends or patterns you would expect to find in the data related to {t['challenge']}.
   d) Discuss any limitations or potential biases in the data and how you would address them.

2. Environmental Impact Assessment (250-300 words):
   a) Based on your data analysis, assess the current and projected impacts of {t['challenge']} on the environment and society.
   b) Describe how these impacts specifically relate to the {t['policy_domain']}.
   c) Identify any feedback loops or cascading effects that could exacerbate the problem.
   d) Discuss the uncertainty in your assessment and how you would communicate this to policymakers.

3. Policy Recommendations (300-350 words):
   a) Propose three specific, evidence-based policy recommendations for the {t['policy_domain']} to address {t['challenge']}.
   b) For each recommendation, explain:
      - The scientific rationale based on your data analysis
      - The expected environmental and societal benefits
      - Potential challenges or barriers to implementation
   c) Discuss how your recommendations balance short-term and long-term goals.

4. Implementation Strategy (200-250 words):
   a) Outline a step-by-step plan to implement your most promising policy recommendation.
   b) Identify key stakeholders and explain how you would engage them in the policy process.
   c) Propose a method for monitoring and evaluating the effectiveness of the policy over time.

5. Interdisciplinary Considerations (200-250 words):
   a) Discuss how your analysis and recommendations integrate knowledge from climate science, data analytics, and policy studies.
   b) Explain how insights from other relevant fields (e.g., economics, sociology, ecology) could enhance your approach.
   c) Propose a novel interdisciplinary research question that emerges from your analysis.

6. Ethical Implications (150-200 words):
   a) Identify potential ethical issues arising from your data analysis or policy recommendations.
   b) Discuss how these ethical considerations might influence policy implementation.
   c) Propose guidelines for ensuring ethical use of climate data in policymaking.

Ensure your response demonstrates a deep understanding of climate science, data analysis techniques, and policy formulation. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific rigor and practical feasibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, data analysis techniques, and policy formulation.",
            "The data analysis approach is well-explained and appropriate for the given data type and environmental challenge.",
            "The environmental impact assessment is comprehensive and considers complex interactions and uncertainties.",
            "Policy recommendations are specific, evidence-based, and relevant to the given policy domain.",
            "The implementation strategy is practical and considers stakeholder engagement and policy evaluation.",
            "The response effectively integrates knowledge from multiple disciplines and proposes a novel interdisciplinary research question.",
            "Ethical implications are thoughtfully considered and addressed.",
            "The overall response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
