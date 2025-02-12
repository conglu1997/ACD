import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                'environmental_challenge': 'Ocean acidification',
                'ecosystem_focus': 'Coral reefs',
                'policy_area': 'Carbon emissions reduction'
            },
            {
                'environmental_challenge': 'Deforestation',
                'ecosystem_focus': 'Amazon rainforest',
                'policy_area': 'Sustainable agriculture'
            },
            {
                'environmental_challenge': 'Arctic sea ice loss',
                'ecosystem_focus': 'Polar ecosystems',
                'policy_area': 'Climate change mitigation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(challenges, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulation system that models global ecosystem interactions and allows for testing of environmental policies, then use it to propose and evaluate solutions for {t['environmental_challenge']}. Focus on the {t['ecosystem_focus']} ecosystem and consider policies related to {t['policy_area']}. Your response should include the following sections:

1. Simulation System Design (300-350 words):
   a) Describe the key components and structure of your global ecosystem simulation system.
   b) Explain how your system models complex interactions between different environmental factors.
   c) Detail how the system incorporates and tests various environmental policies.
   d) Discuss any novel algorithms or data sources used in your simulation.

2. {t['ecosystem_focus']} Ecosystem Model (250-300 words):
   a) Describe how your simulation specifically models the {t['ecosystem_focus']} ecosystem.
   b) Explain the key variables and interactions considered in this ecosystem model.
   c) Discuss how your model accounts for both short-term and long-term changes in the ecosystem.

3. Policy Testing Framework (250-300 words):
   a) Explain how your system allows for the input and testing of environmental policies.
   b) Describe the metrics used to evaluate policy effectiveness.
   c) Discuss how the system accounts for potential unintended consequences of policies.

4. {t['environmental_challenge']} Solution Proposal (300-350 words):
   a) Use your simulation system to propose a set of policies to address {t['environmental_challenge']}.
   b) Explain the rationale behind your proposed policies.
   c) Provide at least one quantitative prediction from your simulation on the effects of these policies.
   d) Discuss any trade-offs or potential negative consequences of your proposed solution.

5. Comparative Policy Analysis (200-250 words):
   a) Compare your proposed solution to at least two alternative policy approaches.
   b) Use your simulation to quantitatively evaluate the effectiveness of each approach.
   c) Discuss the strengths and weaknesses of each policy set.

6. Implementation and Monitoring (150-200 words):
   a) Propose a plan for implementing your recommended policies.
   b) Describe how you would monitor the real-world effects of these policies.
   c) Explain how you would update your simulation based on observed results.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss any ethical implications of using simulations to guide environmental policy.
   b) Address potential limitations or biases in your simulation system.
   c) Propose guidelines for the responsible use of ecosystem simulations in policy-making.

Ensure your response demonstrates a deep understanding of environmental science, data analysis, and policy-making. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1600-1950 words. Include at least one quantitative prediction or analysis in your response, and use scientific terminology throughout, providing explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of environmental science, data analysis, and policy-making, particularly in relation to the specified environmental challenge and ecosystem.",
            "The proposed simulation system is well-designed, innovative, and plausibly models complex global ecosystem interactions.",
            "The policy testing framework and solution proposal are well-thought-out and demonstrate an understanding of the complexities involved in environmental policy-making.",
            "The comparative policy analysis shows critical thinking and a nuanced understanding of policy trade-offs.",
            "The implementation, monitoring, and ethical considerations sections demonstrate foresight and responsible thinking about the use of simulations in policy-making.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The response includes at least one quantitative prediction or analysis and uses appropriate scientific terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
