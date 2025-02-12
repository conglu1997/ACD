import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "coral reefs",
            "rainforests",
            "arctic tundra",
            "urban ecosystems"
        ]
        biomimetic_inspirations = [
            "jellyfish",
            "hummingbirds",
            "tardigrades",
            "slime molds"
        ]
        ai_capabilities = [
            "swarm intelligence",
            "adaptive learning",
            "predictive modeling",
            "multi-agent cooperation"
        ]
        restoration_tasks = [
            "pollutant filtration",
            "seed dispersal",
            "microclimate regulation",
            "invasive species control"
        ]
        
        tasks = [
            {
                "environment": random.choice(environments),
                "biomimetic_inspiration": random.choice(biomimetic_inspirations),
                "ai_capability": random.choice(ai_capabilities),
                "restoration_task": random.choice(restoration_tasks)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic robot with embedded AI for environmental monitoring and ecosystem restoration in {t['environment']}, inspired by {t['biomimetic_inspiration']}, utilizing {t['ai_capability']} for {t['restoration_task']}. Then, analyze its potential impact and ethical implications. Your response should include:

1. Robot Design (300-350 words):
   a) Describe the physical structure and key features of your biomimetic robot, explaining how it mimics {t['biomimetic_inspiration']}.
   b) Explain how the robot's design is suited for operating in {t['environment']}.
   c) Detail the sensors and actuators that enable the robot to perform {t['restoration_task']}.
   d) Include a basic schematic or diagram of your robot design.

2. AI System Integration (250-300 words):
   a) Explain how {t['ai_capability']} is implemented in your robot's AI system.
   b) Describe how the AI system processes environmental data and makes decisions.
   c) Discuss how the AI enables the robot to adapt to changing conditions in {t['environment']}.

3. Environmental Monitoring and Restoration (250-300 words):
   a) Detail how your robot performs {t['restoration_task']} in {t['environment']}.
   b) Explain the environmental data collected by the robot and how it's used.
   c) Discuss potential challenges and solutions for long-term deployment in {t['environment']}.

4. Ecological Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative impacts of your robot on {t['environment']}.
   b) Discuss how the robot's activities might affect local flora and fauna.
   c) Propose methods to mitigate any potential negative ecological consequences.

5. Ethical Implications (200-250 words):
   a) Identify and discuss at least three ethical concerns raised by the deployment of your robot.
   b) Analyze potential unintended consequences of using biomimetic AI robots for ecosystem restoration.
   c) Propose guidelines for the responsible development and use of such technologies.

6. Future Developments and Applications (150-200 words):
   a) Suggest two potential improvements or extensions to your robot design.
   b) Discuss how this technology could be applied to other environmental challenges.

Ensure your response demonstrates a deep understanding of robotics, AI, biology, and environmental science. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use subheadings (a, b, c, etc.) as outlined above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must describe a biomimetic robot inspired by {t['biomimetic_inspiration']} for use in {t['environment']}",
            f"The AI system must incorporate {t['ai_capability']} for {t['restoration_task']}",
            "The design should be scientifically plausible and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration",
            "Ethical implications must be thoughtfully considered",
            "The ecological impact analysis should be thorough and balanced",
            "Future developments and applications should be relevant and well-justified",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1350-1650 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
