import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        game_theory_concepts = [
            "Prisoner's Dilemma",
            "Ultimatum Game",
            "Public Goods Game",
            "Trust Game"
        ]
        psychological_biases = [
            "Loss Aversion",
            "Anchoring Effect",
            "Framing Effect",
            "Social Proof"
        ]
        economic_contexts = [
            "Resource Allocation",
            "Market Competition",
            "Risk Management",
            "Negotiation"
        ]
        
        return {
            "1": {
                "game_theory_concept": random.choice(game_theory_concepts),
                "psychological_bias": random.choice(psychological_biases),
                "economic_context": random.choice(economic_contexts)
            },
            "2": {
                "game_theory_concept": random.choice(game_theory_concepts),
                "psychological_bias": random.choice(psychological_biases),
                "economic_context": random.choice(economic_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a complex behavioral economics experiment that investigates human decision-making in strategic social situations. Your experiment should incorporate the following elements:

1. Game Theory Concept: {t['game_theory_concept']}
2. Psychological Bias: {t['psychological_bias']}
3. Economic Context: {t['economic_context']}

Your response should include the following sections:

1. Experimental Design (300-350 words):
   a) Describe the overall structure of your experiment, including participant roles and interactions.
   b) Explain how you've incorporated the specified game theory concept, psychological bias, and economic context.
   c) Detail the key variables you'll measure and how they relate to decision-making processes.
   d) Outline any control conditions or comparative scenarios in your experiment.

2. Hypotheses and Predictions (200-250 words):
   a) State 2-3 specific hypotheses that your experiment aims to test.
   b) For each hypothesis, provide a clear prediction and the reasoning behind it.
   c) Explain how these hypotheses relate to broader theories in behavioral economics or social psychology.

3. Methodology and Procedure (250-300 words):
   a) Describe the step-by-step procedure of your experiment, including any instructions given to participants.
   b) Explain any deception used in the experiment and justify its necessity.
   c) Detail the methods you'll use to collect and analyze data, including any statistical tests.
   d) Discuss how you'll control for potential confounding variables.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in your experimental design.
   b) Explain how you'll address these issues, including informed consent and debriefing procedures.
   c) Discuss any potential long-term implications of participation in your experiment.

5. Potential Applications and Implications (200-250 words):
   a) Discuss how the results of your experiment could inform real-world policies or practices.
   b) Explain potential applications in fields such as marketing, public policy, or organizational behavior.
   c) Consider any limitations in generalizing the results of your experiment to real-world situations.

6. Future Research Directions (100-150 words):
   a) Propose two follow-up studies that could build on your experiment's findings.
   b) Explain how these studies would address any limitations or unanswered questions from your original experiment.

Ensure your response demonstrates a deep understanding of behavioral economics, game theory, and social psychology. Use appropriate terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific rigor and ethical standards.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The experiment design clearly incorporates the game theory concept of {t['game_theory_concept']}, the psychological bias of {t['psychological_bias']}, and the economic context of {t['economic_context']}.",
            "The response demonstrates a deep understanding of behavioral economics, game theory, and social psychology principles.",
            "The experimental design is innovative, scientifically rigorous, and ethically sound.",
            "The hypotheses, methodology, and analysis plans are clearly explained and logically connected.",
            "The response considers potential real-world applications and implications of the research.",
            "The proposed future research directions are relevant and build meaningfully on the original experiment."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
