import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "organism": "Giant isopod",
                "environment": "Abyssal plain",
                "adaptation_focus": "Pressure resistance"
            },
            {
                "organism": "Anglerfish",
                "environment": "Mesopelagic zone",
                "adaptation_focus": "Bioluminescence"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic robot inspired by the {t['organism']}, capable of adapting its morphology and behavior to the {t['environment']} with a focus on {t['adaptation_focus']}. Your response should include the following sections:

1. Biological Inspiration (200-250 words):
   a) Describe the key characteristics of the {t['organism']} relevant to its survival in deep-sea environments.
   b) Explain how these characteristics inform your robot design, particularly in relation to {t['adaptation_focus']}.
   c) Discuss any challenges in translating biological features into robotic systems.

2. Robot Design (300-350 words):
   a) Provide a detailed description of your biomimetic robot's structure and components.
   b) Explain how your design incorporates adaptive features for {t['adaptation_focus']}.
   c) Describe the materials and fabrication techniques you would use, considering deep-sea conditions.
   d) Include a simple diagram or ASCII art representation of your robot design.

3. Adaptive Mechanisms (250-300 words):
   a) Explain the specific mechanisms that allow your robot to adapt to changing conditions in the {t['environment']}.
   b) Describe how these mechanisms relate to the {t['adaptation_focus']}.
   c) Discuss any novel approaches or technologies you've incorporated into your design.

4. Control Systems and AI (200-250 words):
   a) Describe the control systems and AI algorithms used in your robot.
   b) Explain how these systems enable autonomous operation and decision-making in the deep-sea environment.
   c) Discuss any machine learning approaches used for environmental adaptation.

5. Environmental Interaction (200-250 words):
   a) Explain how your robot interacts with and senses its environment in the {t['environment']}.
   b) Describe any specific behaviors or strategies your robot employs for navigation, foraging, or self-preservation.
   c) Discuss how your robot minimizes its environmental impact.

6. Potential Applications (150-200 words):
   a) Propose two potential applications for your biomimetic robot in deep-sea exploration or research.
   b) Explain how these applications could advance our understanding of deep-sea ecosystems.

7. Ethical Considerations and Future Improvements (150-200 words):
   a) Discuss any ethical considerations related to deploying biomimetic robots in natural ecosystems.
   b) Propose two potential improvements or extensions to your robot design.
   c) Suggest a research question that could be explored using an advanced version of your biomimetic robot.

Ensure your response demonstrates a deep understanding of marine biology, robotics, materials science, and environmental adaptation. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words, not including the headings."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design effectively incorporates biomimetic features inspired by the {t['organism']}.",
            f"The robot's adaptive mechanisms for {t['adaptation_focus']} are well-explained and plausible.",
            f"The response demonstrates a deep understanding of the challenges posed by the {t['environment']}.",
            "The control systems and AI algorithms are appropriate for autonomous deep-sea operation.",
            "The proposed applications and ethical considerations are thoughtfully addressed.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The explanation is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
