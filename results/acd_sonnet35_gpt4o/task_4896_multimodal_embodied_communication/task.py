import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "setting": "Emergency Room",
                "context": "Triage and patient communication",
                "challenge": "Language barrier with a critically ill patient"
            },
            {
                "setting": "International Business Negotiation",
                "context": "High-stakes deal closure",
                "challenge": "Navigating cultural differences in communication styles"
            }
        ]
        communication_modes = [
            "Verbal language",
            "Facial expressions",
            "Gestures",
            "Proxemics",
            "Touch"
        ]
        return {
            "1": {"scenario": random.choice(scenarios), "modes": random.sample(communication_modes, 3)},
            "2": {"scenario": random.choice(scenarios), "modes": random.sample(communication_modes, 3)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and generates multimodal communication strategies for embodied agents in complex social scenarios. Your system should integrate verbal and non-verbal cues with physical actions. Apply your system to the following scenario:

Setting: {t['scenario']['setting']}
Context: {t['scenario']['context']}
Challenge: {t['scenario']['challenge']}

Your system should incorporate the following communication modes:
{', '.join(t['modes'])}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling and generating multimodal communication strategies.
   b) Explain how your system integrates insights from cognitive science, linguistics, and robotics.
   c) Detail how your system models the interaction between different communication modes.
   d) Discuss any novel AI algorithms or approaches used in your system.
   e) Provide a simple diagram or flowchart of your system's architecture (described textually).

2. Multimodal Integration (250-300 words):
   a) Explain how your system combines and coordinates the specified communication modes.
   b) Describe how your system accounts for the interdependencies between different modes.
   c) Discuss how your approach addresses the challenges of timing and synchronization in multimodal communication.

3. Scenario Analysis and Strategy Generation (250-300 words):
   a) Analyze the given scenario, identifying key challenges and opportunities for effective communication.
   b) Describe the step-by-step process your system would follow to generate a communication strategy.
   c) Provide an example of a multimodal communication sequence your system might generate for this scenario.

4. Embodied Cognition and Physical Actions (200-250 words):
   a) Explain how your system incorporates principles of embodied cognition.
   b) Describe how physical actions are integrated into the communication strategy.
   c) Discuss any challenges in modeling the physical aspects of communication for embodied agents.

5. Adaptive Learning and Context Sensitivity (200-250 words):
   a) Explain how your system adapts its communication strategies based on feedback and changing context.
   b) Describe any machine learning techniques used to improve performance over time.
   c) Discuss how your system handles unexpected or novel situations in the given scenario.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to AI-generated multimodal communication strategies.
   b) Discuss any limitations of your approach, particularly in complex social scenarios.
   c) Propose guidelines for the responsible development and use of such AI systems in real-world applications.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, robotics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, robotics, and artificial intelligence",
            "The AI system design effectively integrates multiple communication modes and addresses the given scenario",
            "The approach is innovative while maintaining scientific plausibility",
            "The response adequately covers all required sections with appropriate depth",
            "Ethical considerations and limitations are thoughtfully discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
