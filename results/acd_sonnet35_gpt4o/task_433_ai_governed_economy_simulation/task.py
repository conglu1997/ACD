import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Resource Allocation",
                "constraint": "Limited renewable resources",
                "behavioral_bias": "Loss aversion"
            },
            {
                "scenario": "Labor Market",
                "constraint": "Skill-based job matching",
                "behavioral_bias": "Overconfidence effect"
            },
            {
                "scenario": "Financial Markets",
                "constraint": "Information asymmetry",
                "behavioral_bias": "Herding behavior"
            },
            {
                "scenario": "Public Goods Distribution",
                "constraint": "Free-rider problem",
                "behavioral_bias": "Present bias"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical economic system governed by AI agents, focusing on the scenario of {t['scenario']}. Address the following points:

1. System Design (200-250 words):
   Describe the key components of your AI-governed economic system, explaining how AI agents make decisions and interact. Detail how the system addresses the constraint: {t['constraint']} and incorporates the behavioral bias: {t['behavioral_bias']}.

2. Game Theory Analysis (200-250 words):
   Identify a key strategic interaction within your system. Model this as a game with players, strategies, and payoffs. Analyze the equilibrium state(s) and explain how AI governance influences these. Include a simple numerical example (e.g., a 2x2 payoff matrix).

3. Economic Efficiency (150-200 words):
   Define efficiency criteria for your system. Analyze potential inefficiencies, especially those arising from the behavioral bias. Propose AI governance mechanisms to improve efficiency.

4. Ethical Considerations (100-150 words):
   Discuss two potential ethical issues in your AI-governed system and propose safeguards or guidelines to address them.

5. Comparative Analysis (150-200 words):
   Compare your AI-governed system to traditional human-governed economies. Identify two advantages and two disadvantages of your system. Speculate on its potential evolution.

Ensure your response demonstrates understanding of economic principles, game theory, behavioral economics, and AI capabilities. Be creative while maintaining logical consistency. Use appropriate terminology and provide clear explanations.

Format your response with clear headings for each section. Your total response should be between 800-1050 words.

Note: You will be evaluated on addressing all sections, incorporating the given constraint and bias, providing a well-defined game theory analysis with an example, demonstrating understanding of relevant fields, creativity, logical consistency, terminology use, and word count adherence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five sections as specified in the instructions.",
            "The system design incorporates the given constraint and behavioral bias.",
            "The game theory analysis includes a well-defined game with players, strategies, payoffs, and a numerical example.",
            "The response demonstrates understanding of economic principles, game theory, behavioral economics, and AI capabilities.",
            "The response is creative while maintaining logical consistency and plausibility.",
            "The response uses appropriate terminology and provides clear explanations of concepts.",
            "The total response is between 800-1050 words."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
