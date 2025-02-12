import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "environment": "Deep ocean trenches",
                "challenges": ["Extreme pressure", "Low light conditions", "Corrosive salt water"],
                "inspiration": "Bioluminescent deep-sea creatures"
            },
            {
                "environment": "Volcanic active zones",
                "challenges": ["Extreme heat", "Toxic gases", "Unstable terrain"],
                "inspiration": "Extremophile microorganisms"
            },
            {
                "environment": "Arctic tundra",
                "challenges": ["Extreme cold", "Limited energy sources", "Rapidly changing seasons"],
                "inspiration": "Hibernating mammals"
            },
            {
                "environment": "Martian surface",
                "challenges": ["Low atmospheric pressure", "Radiation exposure", "Dust storms"],
                "inspiration": "Extremophile bacteria"
            }
        ]
        return {
            "1": random.choice(environments),
            "2": random.choice(environments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic robot capable of adapting its physical structure and behavior to the extreme environment of {t['environment']}. Your design should integrate principles from materials science, evolutionary biology, and artificial intelligence to create a highly adaptable and resilient system. Address the following points in your response:

1. Robot Design (300-350 words):
   a) Describe the overall structure and key components of your biomimetic robot.
   b) Explain how your design addresses the specific challenges of {', '.join(t['challenges'])}.
   c) Detail how your robot incorporates biomimetic features inspired by {t['inspiration']}.
   d) Discuss any novel materials or structures you've incorporated into your design.

2. Adaptive Mechanisms (250-300 words):
   a) Explain the mechanisms that allow your robot to adapt its physical structure to the environment.
   b) Describe how your robot modifies its behavior based on environmental conditions.
   c) Discuss how principles of evolutionary biology inform your robot's adaptive capabilities.

3. AI and Control Systems (250-300 words):
   a) Outline the AI architecture that governs your robot's decision-making and adaptation processes.
   b) Explain how your robot learns from and responds to its environment.
   c) Describe any novel algorithms or computational approaches used in your design.

4. Energy and Resource Management (200-250 words):
   a) Describe how your robot manages energy in the extreme environment.
   b) Explain any self-maintenance or self-repair capabilities of your robot.
   c) Discuss how your robot might gather or process resources from its environment.

5. Potential Applications and Ethical Considerations (200-250 words):
   a) Propose two potential applications for your adaptive biomimetic robot beyond its primary environment.
   b) Discuss any ethical implications or potential misuses of this technology.
   c) Suggest guidelines for the responsible development and deployment of such robots.

6. Future Developments (150-200 words):
   a) Propose an innovative extension or improvement to your design.
   b) Discuss how this technology might evolve in the next 20 years.
   c) Suggest a potential breakthrough in another field that could significantly enhance adaptive biomimetic robotics.

Ensure your response demonstrates a deep understanding of robotics, materials science, evolutionary biology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of robotics, materials science, evolutionary biology, and artificial intelligence.",
            f"The robot design effectively addresses the specific challenges of {', '.join(t['challenges'])}.",
            f"The design incorporates biomimetic features inspired by {t['inspiration']}.",
            "The adaptive mechanisms are well-explained and grounded in principles of evolutionary biology.",
            "The AI architecture and control systems are clearly described and innovative.",
            "The energy and resource management strategies are appropriate for the extreme environment.",
            "The potential applications and ethical considerations are thoughtfully discussed.",
            "The response is well-structured, creative, and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
