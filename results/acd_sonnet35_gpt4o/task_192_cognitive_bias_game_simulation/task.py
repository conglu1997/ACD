import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_bias': 'anchoring bias',
                'bias_description': 'The tendency to rely too heavily on the first piece of information encountered when making decisions.',
                'game_scenario': 'negotiation',
                'num_agents': 3
            },
            {
                'cognitive_bias': 'confirmation bias',
                'bias_description': 'The tendency to search for, interpret, favor, and recall information in a way that confirms one\'s preexisting beliefs or hypotheses.',
                'game_scenario': 'stock market trading',
                'num_agents': 5
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multi-agent AI system that simulates {t['cognitive_bias']} in a {t['game_scenario']} scenario with {t['num_agents']} agents. {t['cognitive_bias'].capitalize()} is defined as: {t['bias_description']}

Your task has four parts:

1. System Design (300-350 words):
   - Describe the components and architecture of your multi-agent AI system.
   - Explain how you model {t['cognitive_bias']} in the agents' decision-making processes.
   - Outline the key features of the {t['game_scenario']} scenario and how it interacts with the cognitive bias.

2. Agent Behavior Analysis (250-300 words):
   - Analyze how the simulated {t['cognitive_bias']} affects the agents' behavior in the {t['game_scenario']} scenario.
   - Discuss any emerging patterns or unexpected outcomes in the multi-agent interaction.
   - Compare the biased agents' behavior to hypothetical unbiased agents in the same scenario.

3. Game-Theoretic Implications (250-300 words):
   - Examine the game-theoretic implications of introducing {t['cognitive_bias']} into the {t['game_scenario']} scenario.
   - Discuss how the bias affects strategic decision-making and overall system dynamics.
   - Propose a method to quantify the impact of the bias on the game's outcome.

4. Ethical Considerations and Real-World Applications (200-250 words):
   - Discuss potential ethical implications of simulating cognitive biases in AI systems.
   - Propose two real-world applications where your system could provide valuable insights.
   - Suggest one potential improvement or extension to your system for future research.

Ensure your response demonstrates a deep understanding of cognitive science, game theory, and AI system design. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response as follows:

System Design:
[Your design description]

Agent Behavior Analysis:
[Your analysis]

Game-Theoretic Implications:
[Your discussion]

Ethical Considerations and Real-World Applications:
[Your considerations and applications]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a multi-agent AI system simulating {t['cognitive_bias']} in a {t['game_scenario']} scenario.",
            f"The system design and analysis demonstrate a deep understanding of {t['cognitive_bias']} and its effects on decision-making.",
            f"The response analyzes the behavior of {t['num_agents']} agents and discusses emerging patterns in their interactions.",
            "The submission examines game-theoretic implications and proposes a method to quantify the bias's impact.",
            "Ethical considerations and real-world applications are thoughtfully discussed.",
            "The response shows creativity and plausibility in the system design and analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
