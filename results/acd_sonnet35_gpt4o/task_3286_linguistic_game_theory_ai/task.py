import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Diplomatic Negotiation",
                "context": "International peace talks",
                "objective": "Achieve a mutually beneficial agreement",
                "time_constraint": "48 hours"
            },
            {
                "name": "Corporate Merger",
                "context": "High-stakes business deal",
                "objective": "Maximize company value while ensuring fair terms",
                "time_constraint": "1 week"
            },
            {
                "name": "Hostage Negotiation",
                "context": "Critical law enforcement situation",
                "objective": "Secure the safe release of hostages",
                "time_constraint": "6 hours"
            },
            {
                "name": "Environmental Summit",
                "context": "Global climate change conference",
                "objective": "Reach consensus on emission reduction targets",
                "time_constraint": "2 weeks"
            },
            {
                "name": "Multiparty Coalition Formation",
                "context": "Post-election government formation",
                "objective": "Form a stable coalition government",
                "time_constraint": "72 hours"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that plays a game of strategic communication using principles from game theory and linguistics, then analyze its performance in a {t['name']} scenario with a time constraint of {t['time_constraint']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system integrates game theory principles with linguistic analysis.
   c) Detail the decision-making process your AI uses in the {t['name']} context.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.
   e) Explain how your system manages the {t['time_constraint']} constraint.

2. Linguistic Strategy (200-250 words):
   a) Explain how your system analyzes and generates language in the {t['context']}.
   b) Describe the linguistic features (e.g., pragmatics, implicature) your AI considers.
   c) Discuss how your system adapts its language use to different interlocutors or situations.
   d) Explain how the time constraint affects your system's linguistic choices.

3. Game-Theoretic Approach (200-250 words):
   a) Detail the game-theoretic model your system uses for the {t['name']} scenario.
   b) Explain how your AI calculates utilities and probabilities in this context.
   c) Describe any novel algorithms or techniques used to optimize your AI's strategy.
   d) Discuss how the {t['time_constraint']} constraint is incorporated into your game-theoretic model.

4. Performance Analysis (150-200 words):
   a) Propose a method to evaluate your AI's performance in the {t['name']} scenario.
   b) Describe potential metrics for measuring success in achieving the objective to {t['objective']}.
   c) Discuss how you would compare your AI's performance to human negotiators.
   d) Explain how the time constraint affects performance evaluation.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in using AI for strategic communication in {t['context']}.
   b) Propose guidelines for responsible development and use of such AI systems.
   c) Discuss the implications of AI-driven negotiations on human decision-making processes.
   d) Address any ethical concerns related to the time-constrained nature of the task.

6. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Describe how these developments could enhance performance or address current limitations.
   c) Discuss the broader implications of advanced AI systems in strategic communication.
   d) Explore potential advancements in managing time constraints in AI-driven negotiations.

Ensure your response demonstrates a deep understanding of game theory, linguistics, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and practical plausibility. Address all aspects of the task, including time management strategies.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the {t['name']} scenario in the context of {t['context']} with the {t['time_constraint']} constraint.",
            "The system architecture integrates game theory principles with linguistic analysis and addresses time management.",
            "The linguistic strategy considers relevant features such as pragmatics and implicature, and adapts to the time constraint.",
            "The game-theoretic approach is well-explained, appropriate for the scenario, and incorporates the time constraint.",
            "The performance analysis proposal is thorough, includes relevant metrics, and considers the impact of the time constraint.",
            "Ethical considerations are thoughtfully discussed, including those related to the time-constrained nature of the task.",
            "Future developments are proposed and their implications are explored, including advancements in managing time constraints.",
            "The response demonstrates a deep understanding of game theory, linguistics, AI system design, and time management in strategic communication.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The response is creative while maintaining scientific and practical plausibility.",
            "The response includes a high-level diagram or pseudocode illustrating the system's architecture.",
            "The response explicitly addresses time management strategies throughout the different sections.",
            "The total response is between 1000-1300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
