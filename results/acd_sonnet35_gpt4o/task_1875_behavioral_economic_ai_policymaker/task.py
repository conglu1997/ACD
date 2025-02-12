import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        policy_areas = ['healthcare', 'education', 'environmental protection', 'taxation']
        cognitive_biases = ['anchoring', 'framing effect', 'loss aversion', 'status quo bias']
        economic_principles = ['incentive structures', 'game theory', 'behavioral nudges', 'market failures']
        
        tasks = {
            "1": {
                "policy_area": random.choice(policy_areas),
                "cognitive_bias": random.choice(cognitive_biases),
                "economic_principle": random.choice(economic_principles)
            },
            "2": {
                "policy_area": random.choice(policy_areas),
                "cognitive_bias": random.choice(cognitive_biases),
                "economic_principle": random.choice(economic_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates behavioral economics principles and cognitive biases to create and evaluate public policies, then analyze its decision-making process and potential societal impacts. Focus on the policy area of {t['policy_area']}, incorporate the cognitive bias of {t['cognitive_bias']}, and apply the economic principle of {t['economic_principle']}.

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI policymaking system.
   b) Explain how your system incorporates behavioral economics principles and cognitive biases.
   c) Detail how the system integrates the specified economic principle into its decision-making process.
   d) Include a brief textual description of a visual representation of your system architecture (e.g., a flowchart or block diagram).

2. Policy Generation and Evaluation (200-250 words):
   a) Explain the process by which your AI system generates policy proposals in the given policy area.
   b) Describe how the system evaluates the potential impacts of these policies.
   c) Discuss how the specified cognitive bias is accounted for in policy generation and evaluation.

3. Decision-Making Analysis (200-250 words):
   a) Analyze how your AI system makes decisions, comparing it to human policymakers.
   b) Explain how the system balances multiple, potentially conflicting objectives.
   c) Discuss any novel approaches your system uses to overcome limitations in traditional policymaking.

4. Ethical Considerations and Bias Mitigation (150-200 words):
   a) Identify potential ethical issues arising from using AI in policymaking.
   b) Propose safeguards to ensure the AI system's decisions are fair and unbiased.
   c) Discuss how to maintain human oversight and accountability in AI-assisted policymaking.

5. Simulation and Testing (150-200 words):
   a) Propose a method to simulate and test your AI system's performance in real-world scenarios.
   b) Describe key metrics you would use to evaluate the system's effectiveness.
   c) Explain how you would validate the system's outputs against expert human judgment.

6. Societal Impact Analysis (150-200 words):
   a) Discuss potential positive and negative societal impacts of implementing your AI policymaking system.
   b) Analyze how it might change the nature of governance and citizen participation.
   c) Propose guidelines for responsible deployment of AI in public policy decisions.

Ensure your response demonstrates a deep understanding of behavioral economics, cognitive psychology, and artificial intelligence. Use appropriate terminology from these fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of behavioral economics, cognitive psychology, and artificial intelligence.",
            "The AI system architecture is well-described and integrates the specified economic principle and cognitive bias.",
            "The policy generation and evaluation process is clearly explained and incorporates the given policy area.",
            "The decision-making analysis shows a thoughtful comparison between the AI system and human policymakers.",
            "Ethical considerations and bias mitigation strategies are thoroughly addressed.",
            "The simulation and testing method is well-designed and includes relevant evaluation metrics.",
            "The societal impact analysis is comprehensive and balanced.",
            "The response is creative and innovative while maintaining scientific and ethical rigor.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
