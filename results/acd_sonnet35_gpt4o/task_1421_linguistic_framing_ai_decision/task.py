import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        framing_scenarios = [
            {
                "scenario": "Medical Treatment",
                "frame_a": "This treatment has a 70% survival rate",
                "frame_b": "This treatment has a 30% mortality rate"
            },
            {
                "scenario": "Economic Policy",
                "frame_a": "This policy will result in 95% employment",
                "frame_b": "This policy will result in 5% unemployment"
            },
            {
                "scenario": "Environmental Initiative",
                "frame_a": "This initiative will preserve 80% of the forest",
                "frame_b": "This initiative will allow logging in 20% of the forest"
            },
            {
                "scenario": "Public Safety Measure",
                "frame_a": "This measure will make 90% of neighborhoods safer",
                "frame_b": "This measure will leave 10% of neighborhoods at current risk levels"
            }
        ]
        return {
            "1": random.choice(framing_scenarios),
            "2": random.choice(framing_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the effects of linguistic framing on decision-making processes, focusing on the scenario: {t['scenario']}. Then, analyze its implications for AI ethics and human-AI interaction. Your response should include the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating framing effects.
   b) Explain how these components interact to process linguistic input and generate decisions.
   c) Detail how your system models the cognitive processes involved in framing effects.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Framing Simulation (200-250 words):
   a) Explain how your system would process and respond to the two frames:
      Frame A: "{t['frame_a']}"
      Frame B: "{t['frame_b']}"
   b) Describe the expected differences in decision outcomes for each frame.
   c) Discuss how your system accounts for individual differences in susceptibility to framing effects.
   d) Provide a specific example of how your AI system would make a decision in this scenario, demonstrating the impact of framing.

3. Cognitive Modeling (200-250 words):
   a) Detail how your system models the cognitive mechanisms underlying framing effects.
   b) Explain how your model incorporates relevant theories from cognitive science and linguistics.
   c) Discuss any simplifications or assumptions made in your cognitive model.
   d) Propose a novel approach to improving the cognitive modeling of framing effects in AI systems.

4. Ethical Implications (200-250 words):
   a) Analyze the ethical implications of an AI system susceptible to framing effects.
   b) Discuss potential consequences of framing-induced biases in AI decision-making.
   c) Propose guidelines for the responsible development and use of such AI systems.
   d) Explore a potential scenario where framing effects in AI could lead to unintended negative consequences.

5. Human-AI Interaction (150-200 words):
   a) Explain how awareness of framing effects in AI could impact human-AI interaction.
   b) Discuss potential benefits and risks of AI systems that can recognize and respond to framing.
   c) Propose a method for transparently communicating an AI system's susceptibility to framing.
   d) Suggest a novel approach to mitigating the impact of framing effects in human-AI interactions.

6. Evaluation and Future Work (150-200 words):
   a) Propose a method to evaluate your system's performance in simulating framing effects.
   b) Discuss limitations of your current model and areas for future improvement.
   c) Suggest potential applications of your system in AI research or practical domains.
   d) Propose a novel research direction that could emerge from your work on framing effects in AI.

Ensure your response demonstrates a deep understanding of linguistic framing, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Each section should adhere to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic framing and its effects on decision-making.",
            "The AI system design is creative, plausible, and well-explained, with a clear architecture and example of decision-making.",
            "The cognitive modeling component incorporates relevant theories, is scientifically grounded, and proposes a novel approach to improving modeling of framing effects.",
            "The ethical implications are thoroughly analyzed, considering multiple perspectives and exploring potential negative consequences.",
            "The discussion on human-AI interaction is insightful, considers both benefits and risks, and suggests a novel approach to mitigating framing effects.",
            "The evaluation proposal, future work suggestions, and proposed novel research direction are relevant, well-reasoned, and innovative.",
            "The response is well-structured, using appropriate terminology and clear explanations for complex concepts.",
            "The total response falls within the 1150-1450 word range, with each section adhering to the specified word count."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
