import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "species": "Leafcutter ants",
                "environment": "Tropical rainforest",
                "disaster": "Wildfire"
            },
            {
                "species": "Emperor penguins",
                "environment": "Antarctic ice shelf",
                "disaster": "Ice shelf collapse"
            },
            {
                "species": "African elephants",
                "environment": "Savanna",
                "disaster": "Drought"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired swarm intelligence system for environmental monitoring and disaster response, based on the collective behavior of {t['species']} in a {t['environment']} environment, specifically addressing the potential disaster of {t['disaster']}. Your response should include the following sections:

1. Biological Inspiration (250-300 words):
   a) Describe the relevant collective behaviors and adaptations of {t['species']}.
   b) Explain how these behaviors contribute to the species' survival and efficiency in their natural habitat.
   c) Analyze how these behaviors could be applied to environmental monitoring and disaster response.

2. Swarm Robotics Design (300-350 words):
   a) Propose a design for individual swarm robots inspired by {t['species']}, including sensors, actuators, and communication mechanisms.
   b) Describe the swarm algorithms and decision-making processes based on the species' collective behavior.
   c) Provide a mathematical or algorithmic representation of a key aspect of the swarm behavior (e.g., movement patterns, communication protocol, or decision-making process).
   d) Explain how the swarm would navigate and operate in the {t['environment']} environment.
   e) Include a diagram or schematic representation of your swarm robotics system (describe it textually).

3. Environmental Monitoring Capabilities (200-250 words):
   a) Detail how your swarm system would monitor key environmental parameters in the {t['environment']}.
   b) Explain how the swarm would process and communicate collected data.
   c) Describe how the system could detect early signs of a potential {t['disaster']}.

4. Disaster Response Protocol (250-300 words):
   a) Outline the swarm's response strategy in the event of a {t['disaster']}.
   b) Explain how the swarm would adapt its behavior and communication during the disaster.
   c) Describe how the swarm would interact with other disaster response systems or personnel.

5. Ethical and Environmental Considerations (150-200 words):
   a) Discuss potential ecological impacts of deploying your swarm system in the {t['environment']}.
   b) Address ethical considerations related to biomimicry and the use of swarm intelligence in disaster scenarios.
   c) Propose guidelines for responsible development and deployment of your system.

6. Limitations and Future Development (200-250 words):
   a) Discuss potential limitations or challenges of your proposed system.
   b) Suggest how these limitations could be addressed in future iterations.
   c) Propose two potential improvements or extensions to your system for future development.
   d) Suggest an experiment to validate the effectiveness of your swarm intelligence system.

Ensure your response demonstrates a deep understanding of biology, robotics, environmental science, and emergency management. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered exactly as above (1. Biological Inspiration, 2. Swarm Robotics Design, etc.). Include the word count for each section in parentheses at the end of the section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of the collective behavior of {t['species']} and how it can be applied to swarm robotics",
            f"The swarm robotics design should be well-suited for operation in a {t['environment']} environment",
            f"The system should have clear capabilities for environmental monitoring and responding to a {t['disaster']} scenario",
            "The response should show interdisciplinary integration of biology, robotics, environmental science, and emergency management",
            "The ethical and environmental considerations should be thoughtfully addressed",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response should include a mathematical or algorithmic representation of a key aspect of the swarm behavior",
            "The response should discuss potential limitations or challenges of the proposed system",
            "The response should include all required sections with appropriate word counts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
