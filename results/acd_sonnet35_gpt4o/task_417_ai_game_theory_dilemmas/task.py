import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "AI Resource Allocation",
                "context": "Two AI systems managing limited computational resources",
                "game_theory_concept": "Nash Equilibrium",
                "cognitive_bias": "Sunk Cost Fallacy"
            },
            {
                "scenario": "Autonomous Vehicle Ethics",
                "context": "Multiple self-driving cars navigating a complex traffic situation",
                "game_theory_concept": "Pareto Optimality",
                "cognitive_bias": "Framing Effect"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a strategic decision-making scenario based on the following parameters:

Scenario: {t['scenario']}
Context: {t['context']}
Game Theory Concept: {t['game_theory_concept']}
Cognitive Bias: {t['cognitive_bias']}

Your task is to:

1. Scenario Design (200-250 words):
   a) Develop a detailed scenario involving AI agents in the given context.
   b) Clearly define the choices available to each AI agent and the potential outcomes.
   c) Explain how the specified game theory concept applies to this scenario.

2. AI Decision Analysis (200-250 words):
   a) Analyze how rational AI agents would approach this scenario using game-theoretic principles.
   b) Discuss how the introduction of the specified cognitive bias might alter AI decision-making.
   c) Propose a potential resolution or equilibrium state for the scenario.

3. Ethical Implications (150-200 words):
   a) Discuss the ethical considerations arising from this scenario.
   b) Analyze how different ethical frameworks (e.g., utilitarianism, deontology) might approach this dilemma.
   c) Propose an ethically-guided decision-making protocol for AI agents in this scenario.

4. Human-AI Interaction (150-200 words):
   a) Discuss how human decision-makers might respond differently to this scenario compared to AI agents.
   b) Analyze potential challenges in aligning AI decision-making with human values and preferences.
   c) Propose a method for improving human-AI cooperation in similar scenarios.

5. Future Implications (100-150 words):
   a) Speculate on how this type of scenario might evolve as AI systems become more advanced.
   b) Discuss potential societal impacts of widespread AI decision-making in similar contexts.
   c) Propose a research question or experiment to further explore the implications of your analysis.

Ensure your response demonstrates a deep understanding of game theory, cognitive psychology, and AI ethics. Be creative in your scenario design while maintaining logical consistency and plausibility. Use appropriate terminology and provide clear explanations throughout your analysis.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed scenario design incorporating the given context and game theory concept",
            "The AI decision analysis applies game-theoretic principles and discusses the impact of the specified cognitive bias",
            "Ethical implications are thoroughly discussed, including different ethical frameworks",
            "The human-AI interaction section compares human and AI decision-making and proposes improvements",
            "Future implications are speculated upon, including societal impacts and research questions",
            "The response demonstrates a deep understanding of game theory, cognitive psychology, and AI ethics",
            "The analysis is creative while maintaining logical consistency and plausibility",
            "Appropriate terminology is used throughout the response",
            "The response is well-structured with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
