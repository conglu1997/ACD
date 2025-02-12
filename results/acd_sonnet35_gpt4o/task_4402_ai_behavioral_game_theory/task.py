import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "game": "Ultimatum Game",
                "bias": "Loss Aversion",
                "context": "Corporate Negotiation"
            },
            {
                "game": "Prisoner's Dilemma",
                "bias": "Overconfidence Effect",
                "context": "International Diplomacy"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        game_explanations = {
            "Ultimatum Game": "a two-player game where one player proposes a division of a sum of money, and the other player can either accept or reject the offer",
            "Prisoner's Dilemma": "a game where two players must decide whether to cooperate or defect, with payoffs structured so that mutual cooperation is collectively optimal, but individual defection is personally optimal"
        }
        bias_explanations = {
            "Loss Aversion": "the tendency to prefer avoiding losses over acquiring equivalent gains",
            "Overconfidence Effect": "the tendency to overestimate one's own abilities or chances of success"
        }
        return f"Design an AI system capable of modeling, predicting, and participating in the {t['game']} ({game_explanations[t['game']]}) while incorporating the cognitive bias of {t['bias']} ({bias_explanations[t['bias']]}). The system should be applied to the context of {t['context']}. Your response should include the following sections:\n\n1. AI System Architecture (300-350 words):\n   a) Describe the key components of your AI system for modeling and participating in the specified game theory scenario.\n   b) Explain how your system incorporates principles of behavioral economics and the specified cognitive bias.\n   c) Detail any novel algorithms or techniques used to handle strategic decision-making.\n   d) Include a high-level diagram or flowchart of your system's architecture (describe it textually).\n\n2. Game Theory Implementation (250-300 words):\n   a) Explain how your AI system models and represents the {t['game']}.\n   b) Describe the strategy or decision-making process your AI uses in this game.\n   c) Discuss how the system adapts its strategy based on opponent behavior and game outcomes.\n\n3. Behavioral Economics Integration (250-300 words):\n   a) Detail how your AI system incorporates the {t['bias']} into its decision-making process.\n   b) Explain how this integration affects the AI's performance in the game.\n   c) Discuss any challenges in modeling human-like biases in an AI system.\n\n4. Contextual Application (200-250 words):\n   a) Describe how your AI system would be applied in the context of {t['context']}.\n   b) Provide a specific example scenario and explain how your AI would behave.\n   c) Discuss the potential benefits and risks of using your AI system in this context.\n\n5. Performance Evaluation (200-250 words):\n   a) Propose a method for evaluating your AI system's performance in the game theory scenario.\n   b) Describe how you would measure the system's ability to model human-like behavior and biases.\n   c) Suggest benchmarks or baseline comparisons for your system.\n\n6. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical issues arising from the use of your AI system in real-world scenarios.\n   b) Propose guidelines for the responsible development and deployment of such systems.\n   c) Consider the implications of AI systems that can exploit human cognitive biases.\n\n7. Future Developments and Challenges (150-200 words):\n   a) Identify key challenges in further developing AI systems for behavioral game theory.\n   b) Suggest potential improvements or extensions to your system.\n   c) Discuss how advances in this area might contribute to our understanding of human decision-making and economic behavior.\n\nEnsure your response demonstrates a deep understanding of game theory, behavioral economics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and logical plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. AI System Architecture:') on a new line, followed by your response for that section. Your total response should be between 1500-1850 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['game']}, {t['bias']}, and their application in {t['context']}.",
            "The AI system architecture is well-designed and incorporates principles of behavioral economics and game theory.",
            "The integration of the specified cognitive bias into the AI's decision-making process is clearly explained and plausible.",
            "The contextual application of the AI system is well-thought-out and includes a specific, relevant example.",
            "The proposed performance evaluation method is comprehensive and addresses both game theory performance and human-like behavior modeling.",
            "Ethical considerations are thoroughly discussed, including responsible development guidelines and potential implications.",
            "The response includes creative and scientifically plausible ideas for future developments in AI behavioral game theory.",
            "The response adheres to the specified format, including all required sections and word count limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
