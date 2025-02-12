import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_process': 'spatial reasoning',
                'environmental_context': 'underwater exploration',
                'soft_robotic_feature': 'variable stiffness tentacles'
            },
            {
                'cognitive_process': 'tactile learning',
                'environmental_context': 'object manipulation in microgravity',
                'soft_robotic_feature': 'electroactive polymer skin'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a soft robotic system that demonstrates principles of embodied cognition, focusing on the cognitive process of {t['cognitive_process']} in the context of {t['environmental_context']}. Your system should incorporate {t['soft_robotic_feature']} as a key feature. Analyze the implications of your design for artificial intelligence and cognitive science. Provide your response in the following format:

1. Soft Robotic System Design (300-350 words):
   a) Describe the overall structure and components of your soft robotic system.
   b) Explain how you've incorporated {t['soft_robotic_feature']} into your design.
   c) Discuss how your system is adapted for {t['environmental_context']}.
   d) Include a simple diagram or schematic representation of your system (using ASCII art or a clear textual description).

2. Embodied Cognition Implementation (250-300 words):
   a) Explain how your system demonstrates embodied cognition principles for {t['cognitive_process']}.
   b) Describe the specific mechanisms by which the physical structure and properties of your soft robot influence its cognitive processes.
   c) Discuss how the interaction between the robot's body and its environment contributes to its cognitive capabilities.

3. Artificial Intelligence Integration (200-250 words):
   a) Describe the AI system or algorithms that control your soft robot.
   b) Explain how the AI system interacts with the physical embodiment of the robot.
   c) Discuss any novel AI approaches or architectures necessitated by the embodied, soft robotic design.

4. Cognitive Science Implications (200-250 words):
   a) Analyze how your soft robotic system might inform or challenge current theories in cognitive science.
   b) Discuss potential insights your system could provide into human or animal cognition.
   c) Propose an experiment using your system that could test a hypothesis about embodied cognition.

5. Challenges and Future Directions (150-200 words):
   a) Identify key technical or theoretical challenges in implementing your system.
   b) Suggest potential solutions or areas for future research to address these challenges.
   c) Discuss how advancements in soft robotics and embodied AI could impact future cognitive architectures.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of developing embodied AI systems with advanced cognitive capabilities.
   b) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of embodied cognition, soft robotics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words, not including the system diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of embodied cognition principles and their application to {t['cognitive_process']}.",
            f"The soft robotic system design effectively incorporates {t['soft_robotic_feature']} and is well-adapted for {t['environmental_context']}.",
            "The AI integration is innovative and well-explained, showing clear interaction with the robot's physical embodiment.",
            "The cognitive science implications are thoughtfully analyzed, with a plausible experiment proposed.",
            "Challenges and future directions are realistically identified and discussed.",
            "Ethical considerations are thoroughly addressed with responsible guidelines proposed.",
            "The response demonstrates creativity and interdisciplinary knowledge integration throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
