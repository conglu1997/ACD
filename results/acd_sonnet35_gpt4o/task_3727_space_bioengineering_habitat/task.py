import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "resource": "oxygen",
                "environmental_factor": "radiation",
                "martian_condition": "dust storms"
            },
            {
                "resource": "food",
                "environmental_factor": "low gravity",
                "martian_condition": "extreme temperature fluctuations"
            },
            {
                "resource": "water",
                "environmental_factor": "low atmospheric pressure",
                "martian_condition": "perchlorates in soil"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bioengineered habitat for long-term human survival on Mars, focusing on sustainable {t['resource']} production, protection against {t['environmental_factor']}, and addressing the challenge of {t['martian_condition']}. Your design should integrate synthetic biology, materials science, and environmental engineering principles. Provide your response in the following format:

1. Habitat Overview (250-300 words):
   a) Describe the overall structure and key components of your bioengineered Mars habitat.
   b) Explain how your design addresses the challenges of {t['resource']} production, {t['environmental_factor']} protection, and {t['martian_condition']}.
   c) Discuss how synthetic biology is incorporated into the habitat's core systems.
   d) Provide a visual representation of your habitat design using ASCII art or a detailed textual description of a diagram. Include labels for key components.

2. Bioengineered Systems (300-350 words):
   a) Detail the specific bioengineered organisms or systems designed for {t['resource']} production.
   b) Explain the genetic modifications or synthetic biological processes involved.
   c) Describe how these systems interact with the habitat's overall environment.
   d) Discuss potential risks and mitigation strategies for using engineered organisms in a closed system.
   e) Explain how your bioengineered systems address the challenge of {t['martian_condition']}.

3. Materials Science Integration (200-250 words):
   a) Describe novel materials used in your habitat's construction, focusing on {t['environmental_factor']} protection.
   b) Explain how these materials interact with or support the bioengineered systems.
   c) Discuss any self-repairing or adaptive properties of the materials used.
   d) Analyze how your materials science solutions contribute to managing {t['martian_condition']}.

4. Environmental Engineering (200-250 words):
   a) Explain how your habitat maintains a stable internal environment suitable for both humans and engineered organisms.
   b) Describe systems for waste management, water recycling, and atmospheric regulation.
   c) Discuss how the habitat adapts to external environmental changes on Mars, particularly {t['martian_condition']}.
   d) Propose an energy generation and management system for your habitat.

5. Long-term Sustainability and Scalability (150-200 words):
   a) Analyze the long-term viability of your bioengineered habitat design.
   b) Discuss potential challenges in maintaining the system over decades.
   c) Propose strategies for ensuring the habitat's resilience and adaptability.
   d) Explain how your design could be scaled up to support a growing Martian colony.

6. Ethical Considerations and Human Factors (150-200 words):
   a) Discuss ethical implications of using synthetic biology for Mars colonization.
   b) Address concerns about potential environmental impact on Mars.
   c) Consider the psychological effects on inhabitants living in a bioengineered environment.
   d) Propose measures to ensure the well-being and safety of the habitat's human occupants.

7. Earth Applications and Future Developments (100-150 words):
   a) Suggest how technologies developed for your Mars habitat could be applied to solve challenges on Earth.
   b) Discuss potential benefits and risks of adapting these technologies for terrestrial use.
   c) Propose future research directions to enhance the capabilities of your bioengineered habitat design.

Ensure your response demonstrates a deep understanding of synthetic biology, materials science, and environmental engineering. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses {t['resource']} production using bioengineered systems.",
            f"The design includes protection against {t['environmental_factor']}.",
            f"The habitat addresses the challenge of {t['martian_condition']}.",
            "The response includes a visual representation or detailed description of the habitat design.",
            "The design considers long-term sustainability and scalability.",
            "The response discusses ethical implications and human factors.",
            "The submission suggests Earth applications and future research directions."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
