import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            "Tardigrade (Water Bear)",
            "Bombardier Beetle",
            "Mantis Shrimp",
            "Leafcutter Ant",
            "Hagfish",
            "Axolotl"
        ]
        real_world_problems = [
            "Deep-sea exploration",
            "Disaster response and search-and-rescue",
            "Sustainable agriculture",
            "Medical diagnostics and treatment",
            "Environmental monitoring and conservation",
            "Space exploration"
        ]
        return {
            "1": {
                "biological_system": random.choice(biological_systems),
                "problem": random.choice(real_world_problems)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "problem": random.choice(real_world_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel biomimetic robot inspired by the {t['biological_system']} to address the real-world problem of {t['problem']}. Your response should include:

1. Biological System Analysis (200-250 words):
   a) Describe the key characteristics and adaptations of the {t['biological_system']}.
   b) Explain how these features make it suitable for inspiring a solution to {t['problem']}.
   c) Discuss any challenges in mimicking this biological system in a robotic form.

2. Robot Design (300-350 words):
   a) Propose a detailed design for your biomimetic robot, including its structure, materials, and key components.
   b) Explain how your design incorporates and adapts the biological features of the {t['biological_system']}.
   c) Describe the robot's locomotion, sensing, and control systems.
   d) Include a simple diagram or schematic representation of your proposed robot (describe it textually).

3. Functional Mechanisms (200-250 words):
   a) Explain how your robot would function to address {t['problem']}.
   b) Describe any novel mechanisms or technologies required for your design.
   c) Discuss potential challenges in implementing these mechanisms and propose solutions.

4. Performance Analysis (200-250 words):
   a) Predict the performance capabilities of your robot in addressing {t['problem']}.
   b) Compare your biomimetic approach to traditional robotic solutions for this problem.
   c) Discuss any limitations of your design and potential areas for improvement.

5. Broader Applications (150-200 words):
   a) Propose two additional applications for your biomimetic robot beyond {t['problem']}.
   b) Explain how the robot's design could be adapted for these applications.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to the development and deployment of your biomimetic robot.
   b) Propose guidelines for responsible use of this technology.
   c) Address any potential environmental impacts of your robot.

7. Future Research Directions (100-150 words):
   a) Suggest areas for further research to enhance your biomimetic robot design.
   b) Propose one novel research question that arises from your design.

Ensure your response demonstrates a deep understanding of biology, robotics, and the specific problem domain. Be creative and innovative in your approach while maintaining scientific and engineering plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified biological system and its potential applications to robotics.",
            "The robot design is innovative, coherent, and effectively incorporates biomimetic principles.",
            "The functional mechanisms and performance analysis are well-reasoned and plausible.",
            "The proposed broader applications are creative and demonstrate the versatility of the design.",
            "Ethical considerations and environmental impacts are thoughtfully addressed.",
            "The suggested future research directions are novel and relevant.",
            "The overall response is well-structured, coherent, and demonstrates strong interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
