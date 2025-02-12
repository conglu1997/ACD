import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organisms = [
            {
                "name": "Tardigrade",
                "environment": "extreme conditions",
                "unique_feature": "cryptobiosis"
            },
            {
                "name": "Mantis Shrimp",
                "environment": "coral reefs",
                "unique_feature": "complex visual system"
            },
            {
                "name": "Slime Mold",
                "environment": "forest floors",
                "unique_feature": "decentralized intelligence"
            },
            {
                "name": "Gecko",
                "environment": "vertical surfaces",
                "unique_feature": "adhesive toe pads"
            }
        ]
        return {str(i+1): org for i, org in enumerate(random.sample(organisms, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic robot inspired by the {t['name']}, which is known for its ability to survive in {t['environment']} and its {t['unique_feature']}. Your task is to create a detailed design for a robot that incorporates the key biological features of this organism and applies them to solve real-world problems.

Your response should include:

1. Biological Analysis (200-250 words):
   a) Describe the key biological features of the {t['name']} that are relevant to your robot design.
   b) Explain how these features enable the organism to thrive in its environment.
   c) Discuss any unique capabilities or adaptations that make this organism particularly interesting for biomimetic design.

2. Robot Design (250-300 words):
   a) Provide a detailed description of your biomimetic robot's structure and components.
   b) Explain how your design incorporates and adapts the biological features of the {t['name']}.
   c) Describe the materials and technologies you would use to replicate these biological features.
   d) Include a brief description of the robot's control system and any AI components.

3. Functionality and Applications (200-250 words):
   a) Describe the primary functions of your biomimetic robot.
   b) Explain how the robot's design enables it to perform these functions effectively.
   c) Propose at least two specific real-world applications for your robot.
   d) Discuss any advantages your biomimetic design offers over traditional robotic approaches.

4. Technical Challenges and Solutions (150-200 words):
   a) Identify at least three major technical challenges in implementing your design.
   b) Propose potential solutions or areas for further research to address these challenges.
   c) Discuss any trade-offs made in your design and justify your decisions.

5. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to the development and deployment of your biomimetic robot.
   b) Discuss the potential impact of your robot on society, industry, or the environment.
   c) Propose guidelines for the responsible development and use of biomimetic robots.

Ensure your response demonstrates a deep understanding of both biological systems and robotics principles. Be creative in your approach while maintaining scientific and engineering plausibility. Use appropriate technical terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design should be clearly inspired by the {t['name']} and incorporate its {t['unique_feature']}",
            "The response should include all required sections: Biological Analysis, Robot Design, Functionality and Applications, Technical Challenges and Solutions, and Ethical and Societal Implications",
            "The biomimetic robot design should be innovative, scientifically plausible, and demonstrate a clear understanding of both biological and robotic principles",
            "The response should propose realistic applications and address potential challenges in implementation",
            "The analysis of ethical and societal implications should be thoughtful and comprehensive"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
