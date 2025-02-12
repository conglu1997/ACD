import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "region": "Southeast Asia",
                "climate_threat": "rising sea levels",
                "resource": "freshwater"
            },
            {
                "region": "Sub-Saharan Africa",
                "climate_threat": "prolonged droughts",
                "resource": "arable land"
            }
        ]
        
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a climate prediction system and use it to make ethical decisions about resource allocation and climate adaptation strategies for {t['region']} facing {t['climate_threat']}. Focus on the allocation of {t['resource']}. Your response should include:

1. Climate Prediction System Design (300-350 words):
   a) Describe the key components of your climate prediction system.
   b) Explain how your system incorporates multiple data sources and modeling techniques.
   c) Discuss how your system accounts for uncertainties and feedback loops in climate systems.
   d) Propose a novel approach to improve the accuracy or efficiency of climate predictions.

2. Scenario Analysis (250-300 words):
   a) Using your prediction system, provide a detailed analysis of the climate scenario for {t['region']}.
   b) Describe the projected impacts of {t['climate_threat']} on the region over the next 50 years.
   c) Identify key vulnerabilities and potential tipping points in the regional climate system.

3. Resource Allocation Strategy (250-300 words):
   a) Propose a strategy for allocating {t['resource']} in response to the predicted climate changes.
   b) Explain how your strategy balances short-term needs with long-term sustainability.
   c) Discuss any innovative technologies or approaches incorporated in your strategy.

4. Ethical Framework (200-250 words):
   a) Develop an ethical framework for making decisions about resource allocation and adaptation strategies.
   b) Explain how your framework addresses issues of justice, equity, and intergenerational responsibility.
   c) Discuss how you resolve potential conflicts between different ethical principles in your decision-making process.

5. Policy Recommendations (200-250 words):
   a) Provide specific policy recommendations for implementing your resource allocation strategy.
   b) Explain how these policies address both climate adaptation and mitigation.
   c) Discuss potential socio-economic impacts of your proposed policies.

6. Uncertainty and Adaptive Management (150-200 words):
   a) Explain how your decision-making process accounts for uncertainties in climate predictions.
   b) Describe an adaptive management approach to adjust strategies as new data becomes available.
   c) Discuss the ethical implications of decision-making under deep uncertainty.

7. Global Implications (150-200 words):
   a) Analyze how your approach to this regional issue could be applied or adapted globally.
   b) Discuss potential international cooperation or conflicts arising from your proposed strategies.
   c) Consider the long-term global consequences of widespread adoption of your approach.

Ensure your response demonstrates a deep understanding of climate science, complex systems modeling, ethical philosophy, and policy analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of climate science, complex systems modeling, ethical reasoning, and policy analysis, particularly in the context of {t['region']} facing {t['climate_threat']}.",
            "The climate prediction system design is innovative, scientifically sound, and addresses uncertainties and complexities in climate modeling.",
            f"The resource allocation strategy for {t['resource']} is well-reasoned, balancing short-term needs with long-term sustainability.",
            "The ethical framework is robust, addressing key principles of justice, equity, and intergenerational responsibility.",
            "Policy recommendations are specific, actionable, and consider both adaptation and mitigation strategies.",
            "The response demonstrates critical thinking about decision-making under uncertainty and proposes a viable adaptive management approach.",
            "The analysis of global implications is insightful and considers potential international dynamics.",
            "The writing is clear, well-structured, uses appropriate technical terminology, and demonstrates a high level of interdisciplinary integration.",
            "The response follows the required format and word count, addressing all specified sections comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
