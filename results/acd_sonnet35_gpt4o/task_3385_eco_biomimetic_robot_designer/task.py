import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "Coral reef",
            "Rainforest canopy",
            "Deep sea hydrothermal vent",
            "Arctic tundra"
        ]
        conservation_tasks = [
            "Pollution monitoring",
            "Biodiversity assessment",
            "Climate change impact tracking",
            "Invasive species detection"
        ]
        
        tasks = {}
        for i in range(1, 3):
            ecosystem = random.choice(ecosystems)
            task = random.choice(conservation_tasks)
            tasks[str(i)] = {
                "ecosystem": ecosystem,
                "conservation_task": task
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic robot inspired by the {t['ecosystem']} ecosystem to perform {t['conservation_task']}. Then, analyze its potential impact on scientific research and environmental preservation. Your response should include the following sections:

1. Robot Design (300-350 words):
   a) Describe the overall structure and key components of your biomimetic robot.
   b) Explain which specific organisms or biological systems from the {t['ecosystem']} inspired your design.
   c) Detail how your robot's features are adapted to the ecosystem and its conservation task.
   d) Discuss any novel materials or technologies required for your robot's functionality.
   e) Include a brief description of a diagram representing your robot's design.

2. Biomimetic Systems (250-300 words):
   a) Explain how your robot mimics biological systems for locomotion in the {t['ecosystem']}.
   b) Describe how your robot's sensory systems are inspired by organisms in this ecosystem.
   c) Detail any other biomimetic features that enhance your robot's performance or adaptability.
   d) Discuss how biomimicry in your design improves upon traditional robotic approaches.

3. Conservation Task Implementation (200-250 words):
   a) Explain how your robot performs {t['conservation_task']} in the {t['ecosystem']}.
   b) Describe the data collection and processing methods used by your robot.
   c) Discuss any challenges specific to this ecosystem and task, and how your design addresses them.
   d) Explain how your robot minimizes its environmental impact while performing its task.

4. Scientific Research Potential (200-250 words):
   a) Identify three potential scientific research applications for your biomimetic robot.
   b) Explain how your robot could advance our understanding of the {t['ecosystem']}.
   c) Discuss how the data collected by your robot could contribute to broader environmental research.

5. Environmental Impact Analysis (200-250 words):
   a) Analyze the potential positive impacts of your robot on environmental preservation.
   b) Discuss any potential negative consequences of deploying your robot in the ecosystem.
   c) Propose guidelines for the ethical use of your robot in environmental research and conservation.
   d) Explain how your robot's design mitigates potential harm to the ecosystem.

6. Future Developments and Challenges (150-200 words):
   a) Suggest two potential improvements or extensions to your biomimetic robot design.
   b) Discuss the scalability of your approach to other ecosystems or conservation tasks.
   c) Identify any technological or ecological challenges that need to be overcome for widespread deployment.

Ensure your response demonstrates a deep understanding of robotics, biology, environmental science, and conservation practices. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering real-world constraints and ethical implications.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['ecosystem']} and how to perform {t['conservation_task']} within it",
            "The biomimetic robot design is innovative yet scientifically plausible",
            "The explanation of how the robot performs its conservation task is clear and well-reasoned",
            "The analysis of scientific research potential and environmental impact is thorough and insightful",
            "The response shows strong interdisciplinary knowledge integration across robotics, biology, and environmental science"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
