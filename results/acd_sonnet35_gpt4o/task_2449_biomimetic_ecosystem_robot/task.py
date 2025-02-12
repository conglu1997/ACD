import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "coral reef",
            "rainforest",
            "arctic tundra",
            "grassland savanna"
        ]
        biological_inspirations = [
            "jellyfish",
            "hummingbird",
            "polar bear",
            "termite"
        ]
        restoration_focuses = [
            "pollination",
            "seed dispersal",
            "soil quality improvement",
            "invasive species control"
        ]
        tasks = [
            {
                'ecosystem': random.choice(ecosystems),
                'biological_inspiration': random.choice(biological_inspirations),
                'restoration_focus': random.choice(restoration_focuses)
            },
            {
                'ecosystem': random.choice(ecosystems),
                'biological_inspiration': random.choice(biological_inspirations),
                'restoration_focus': random.choice(restoration_focuses)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic robot for ecosystem monitoring and restoration, inspired by the {t['biological_inspiration']}, to operate in a {t['ecosystem']} environment with a focus on {t['restoration_focus']}. Your response should include the following sections:

1. Biomimetic Design (250-300 words):
   a) Describe the key features of your robot inspired by the {t['biological_inspiration']}.
   b) Explain how these features are advantageous for operating in a {t['ecosystem']} environment.
   c) Discuss any novel materials or structures used in your robot's design.

2. Locomotion and Adaptation (200-250 words):
   a) Detail the locomotion method(s) of your robot, explaining how they are suited to the {t['ecosystem']}.
   b) Describe how your robot adapts to different terrains or conditions within the ecosystem.
   c) Explain any energy harvesting or conservation mechanisms incorporated into the design.

3. Sensing and Data Collection (200-250 words):
   a) List and describe the types of sensors your robot uses for ecosystem monitoring.
   b) Explain how these sensors work together to create a comprehensive picture of ecosystem health.
   c) Discuss any unique data collection methods inspired by the {t['biological_inspiration']}.

4. AI and Decision Making (200-250 words):
   a) Describe the AI system that governs your robot's behavior and decision-making.
   b) Explain how the AI processes sensor data to identify ecosystem issues and determine appropriate actions.
   c) Discuss how the AI balances monitoring tasks with {t['restoration_focus']} activities.

5. Ecosystem Restoration Capabilities (250-300 words):
   a) Detail how your robot performs {t['restoration_focus']} in the {t['ecosystem']}.
   b) Describe any tools or mechanisms the robot uses for this restoration work.
   c) Explain how the robot minimizes its own impact on the ecosystem while performing its tasks.

6. Swarm Coordination (if applicable) (150-200 words):
   a) If your robot is designed to work in a swarm, explain the coordination mechanisms.
   b) Discuss how individual robots communicate and share data.
   c) Describe how the swarm collectively makes decisions about ecosystem interventions.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of deploying your robot in natural ecosystems.
   b) Address any limitations of your design and suggest areas for future improvement.
   c) Propose guidelines for the responsible use of biomimetic robots in ecosystem management.

Ensure your response demonstrates a deep understanding of biology, robotics, AI, and environmental science. Be innovative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biology, robotics, AI, and environmental science.",
            f"The biomimetic design effectively incorporates features inspired by the {t['biological_inspiration']}.",
            f"The robot's design and capabilities are well-suited to the {t['ecosystem']} environment.",
            f"The ecosystem restoration approach focusing on {t['restoration_focus']} is well-developed and plausible.",
            "The AI system for decision-making and ecosystem monitoring is comprehensively described.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
