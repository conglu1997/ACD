import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Autonomous Vehicle Dilemma",
                "context": "An autonomous vehicle must decide between two harmful outcomes in an unavoidable accident.",
                "behavioral_bias": "Loss aversion",
                "game_theory_concept": "Nash equilibrium"
            },
            {
                "scenario": "AI-Driven Resource Allocation",
                "context": "An AI system must allocate limited medical resources during a pandemic.",
                "behavioral_bias": "Present bias",
                "game_theory_concept": "Pareto efficiency"
            },
            {
                "scenario": "Algorithmic Trading Ethics",
                "context": "An AI trading system must balance profit maximization with market stability and fairness.",
                "behavioral_bias": "Overconfidence effect",
                "game_theory_concept": "Prisoner's dilemma"
            },
            {
                "scenario": "AI Content Moderation",
                "context": "An AI system must balance free speech with protection from harmful content on a social media platform.",
                "behavioral_bias": "Confirmation bias",
                "game_theory_concept": "Tragedy of the commons"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes ethical decision-making in the scenario of {t['scenario']}, incorporating principles of behavioral economics and game theory. Your system should specifically address the behavioral bias of {t['behavioral_bias']} and apply the game theory concept of {t['game_theory_concept']}. Consider the following context: {t['context']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating ethical decision-making.
   b) Explain how your system integrates principles from behavioral economics and game theory.
   c) Discuss any novel algorithms or techniques used in your ethical reasoning process.
   d) Include a simple diagram or flowchart illustrating the system's architecture (use ASCII art).

2. Ethical Framework Integration (250-300 words):
   a) Explain how your system incorporates ethical principles into its decision-making process.
   b) Describe how you balance utilitarian and deontological approaches in your ethical framework.
   c) Discuss how your system handles conflicts between different ethical considerations.

3. Behavioral Economics Implementation (200-250 words):
   a) Explain how your system models and accounts for {t['behavioral_bias']}.
   b) Describe how this behavioral bias influences the ethical decision-making process in your scenario.
   c) Discuss any challenges in implementing this behavioral aspect and how you address them.

4. Game Theory Application (200-250 words):
   a) Explain how your system applies the concept of {t['game_theory_concept']} to the given scenario.
   b) Describe how game theory informs the ethical decision-making process in your system.
   c) Provide an example of how this game theory concept might lead to unexpected or counterintuitive outcomes.

5. Simulation and Analysis (250-300 words):
   a) Describe a specific simulation your system would run for the given scenario.
   b) Explain the key variables and parameters your simulation would consider.
   c) Analyze the potential outcomes and ethical implications of your simulation.
   d) Discuss how your system would evaluate and rank different ethical decisions.

6. Limitations and Ethical Considerations (200-250 words):
   a) Discuss the limitations of your AI system in making ethical decisions.
   b) Address potential biases or unfairness that might arise from your system's approach.
   c) Propose safeguards or oversight mechanisms to ensure responsible use of your system.
   d) Reflect on the broader implications of using AI for ethical decision-making in economic contexts.

Ensure your response demonstrates a deep understanding of AI ethics, behavioral economics, and game theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI ethics, behavioral economics, and game theory.",
            "The proposed system effectively integrates ethical decision-making with behavioral economics and game theory principles.",
            "The system architecture is well-designed and clearly explained.",
            "The response addresses the specific behavioral bias and game theory concept mentioned in the prompt.",
            "The simulation and analysis section provides insightful and plausible outcomes.",
            "The response acknowledges limitations and ethical considerations of the proposed system.",
            "The writing is clear, well-structured, and adheres to the specified format and word count."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))