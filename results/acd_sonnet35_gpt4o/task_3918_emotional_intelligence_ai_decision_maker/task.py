import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "Nuclear disarmament negotiations between two historically hostile nations",
            "Climate change mitigation agreement between developed and developing countries",
            "Trade dispute resolution between major economic powers",
            "Peacekeeping mission deployment in a conflict-ridden region",
            "Global pandemic response coordination among nations with varying resources"
        ]
        emotional_factors = [
            "national pride",
            "historical grievances",
            "fear of economic loss",
            "public opinion pressure",
            "leadership ego"
        ]
        return {
            "1": {"scenario": random.choice(scenarios), "emotional_factor": random.choice(emotional_factors)},
            "2": {"scenario": random.choice(scenarios), "emotional_factor": random.choice(emotional_factors)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that incorporates principles of emotional intelligence into its decision-making process, then apply it to the following geopolitical negotiation scenario: {t['scenario']}. Your system should particularly account for the emotional factor of {t['emotional_factor']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they integrate emotional intelligence principles.
   b) Explain how your system models and processes emotional factors in decision-making.
   c) Detail any novel algorithms or approaches used to balance emotional and rational inputs.
   d) Include a high-level diagram or flowchart of your system's architecture (describe it textually).

2. Emotional Intelligence Integration (250-300 words):
   a) Explain how your system recognizes and interprets emotional cues in the given scenario.
   b) Describe how it incorporates the specified emotional factor into its decision-making process.
   c) Discuss how your system manages potential conflicts between emotional and logical considerations.

3. Scenario Analysis and Decision-Making (300-350 words):
   a) Apply your AI system to the given geopolitical negotiation scenario.
   b) Provide a step-by-step breakdown of how your system would approach the negotiation.
   c) Explain key decision points and how emotional intelligence influences the choices made.
   d) Describe the expected outcome and how it differs from a purely rational approach.

4. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of using AI with emotional intelligence in geopolitical negotiations.
   b) Address potential biases or limitations in your system's approach to emotional factors.
   c) Propose safeguards or guidelines for the responsible use of emotionally intelligent AI in sensitive scenarios.

5. Evaluation and Refinement (200-250 words):
   a) Propose metrics to evaluate your system's performance in the given scenario.
   b) Describe how you would refine and improve your system based on these evaluations.
   c) Discuss potential challenges in scaling this approach to different types of negotiations or decision-making scenarios.

Ensure your response demonstrates a deep understanding of emotional intelligence, artificial intelligence, and geopolitical dynamics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section. Your total response should be between 1250-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of emotional intelligence principles and their application to AI decision-making.",
            "The proposed AI system architecture is well-designed and clearly explained, with a logical integration of emotional factors.",
            "The scenario analysis shows a nuanced application of the AI system, balancing emotional and rational considerations effectively.",
            "Ethical implications are thoroughly discussed, with thoughtful proposals for responsible use of emotionally intelligent AI.",
            "The evaluation and refinement section provides concrete, relevant metrics and improvement strategies.",
            "The response is well-structured, follows the specified format, and falls within the given word count range.",
            "The proposed system and its application demonstrate creativity and innovation while maintaining scientific plausibility.",
            "The response specifically addresses the given scenario and emotional factor, showing an understanding of their unique challenges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
