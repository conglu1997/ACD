import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "environment": "Low-gravity lunar surface",
                "challenge": "Efficient movement in reduced gravity with loose regolith",
                "inspiration": "Kangaroo locomotion"
            },
            {
                "environment": "Dense jungle canopy",
                "challenge": "3D navigation and movement through complex branch structures",
                "inspiration": "Gibbon brachiation"
            },
            {
                "environment": "Turbulent ocean currents",
                "challenge": "Stability and propulsion in dynamic fluid environments",
                "inspiration": "Cuttlefish propulsion"
            },
            {
                "environment": "Martian sand dunes",
                "challenge": "Locomotion on loose, shifting granular media",
                "inspiration": "Sidewinder snake movement"
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a framework for an embodied AI system capable of learning and adapting its locomotion strategies in the following environment: {t['environment']}. Your system should address the specific challenge of {t['challenge']} and draw inspiration from {t['inspiration']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your embodied AI system, including sensors, actuators, and processing units.
   b) Explain how your system integrates principles from robotics, physics, machine learning, and biomechanics.
   c) Discuss any novel algorithms or techniques used in your system.
   d) Include a simple diagram or flowchart illustrating the system's architecture.

2. Learning and Adaptation Mechanism (250-300 words):
   a) Explain how your system learns and adapts its locomotion strategies to the given environment.
   b) Describe the role of reinforcement learning, evolutionary algorithms, or other relevant techniques in your system.
   c) Discuss how your system balances exploration and exploitation in learning new locomotion strategies.

3. Biomimetic Design Elements (200-250 words):
   a) Analyze the locomotion strategy of the specified biological inspiration ({t['inspiration']}).
   b) Explain how you've incorporated key elements of this biological system into your AI design.
   c) Discuss any challenges in translating biological principles to artificial systems and how you've addressed them.

4. Physical Modeling and Simulation (250-300 words):
   a) Describe your approach to modeling the physical environment and the AI system's interactions with it.
   b) Explain how you account for the specific challenges of the given environment in your physical model.
   c) Discuss any novel simulation techniques or tools you've employed to test and refine your system.

5. Performance Evaluation (200-250 words):
   a) Propose specific metrics to evaluate your system's performance in the given environment.
   b) Describe experiments or scenarios to test your system's adaptability and efficiency.
   c) Discuss how you would compare your system's performance to existing robotic locomotion systems.

6. Ethical Considerations and Potential Applications (150-200 words):
   a) Discuss potential ethical issues related to the development and deployment of adaptive, embodied AI systems.
   b) Explore potential real-world applications of your system beyond the specific environment given.
   c) Propose guidelines for responsible development and use of this technology.

7. Limitations and Future Work (150-200 words):
   a) Discuss potential limitations or challenges of your proposed system.
   b) Suggest areas for future research or improvements to address these limitations.

Ensure your response demonstrates a deep understanding of robotics, physics, machine learning, and biomechanics. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Include at least 5 relevant citations to support your scientific claims and design choices. Use a consistent citation format throughout your response.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for an embodied AI system capable of adapting its locomotion in {t['environment']}",
            f"The system effectively addresses the challenge of {t['challenge']}",
            f"The design incorporates clear inspiration from {t['inspiration']}",
            "The system architecture integrates principles from robotics, physics, machine learning, and biomechanics",
            "The learning and adaptation mechanism is well-explained and scientifically plausible",
            "The biomimetic design elements are thoughtfully incorporated and analyzed",
            "The physical modeling and simulation approach is detailed and appropriate for the given environment",
            "The performance evaluation metrics and experiments are well-designed and relevant",
            "Ethical considerations are thoughtfully addressed",
            "Limitations and future work are discussed comprehensively",
            "The response demonstrates deep understanding of robotics, physics, machine learning, and biomechanics through appropriate use of technical terminology and clear explanations",
            "At least 5 relevant citations are included and properly formatted",
            "The writing is clear, well-structured, adheres to the specified format, and falls within the 1500-1850 word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
