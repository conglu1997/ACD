import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "deep sea",
            "extreme desert",
            "arctic tundra",
            "high altitude mountain",
            "volcanic region",
            "dense urban megacity",
            "low gravity extraterrestrial"
        ]
        challenges = [
            "energy efficiency",
            "waste management",
            "structural integrity",
            "resource scarcity",
            "extreme temperature regulation",
            "atmospheric pressure adaptation",
            "radiation protection"
        ]
        inspirations = [
            "coral reefs",
            "cacti",
            "polar bears",
            "mountain goats",
            "tardigrades",
            "mycelium networks",
            "spider silk"
        ]
        tasks = [
            {
                "environment": random.choice(environments),
                "challenge": random.choice(challenges),
                "inspiration": random.choice(inspirations)
            } for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an innovative architectural solution for a human settlement in a {t['environment']} environment, addressing the key challenge of {t['challenge']}. Your design should incorporate biomimetic principles inspired by {t['inspiration']}. Provide your response in the following format:

1. Conceptual Overview (200-250 words):
   a) Describe the overall concept of your architectural design.
   b) Explain how it addresses the specific challenges of the {t['environment']} environment.
   c) Discuss how your design incorporates biomimetic principles inspired by {t['inspiration']}.

2. Structural Design (200-250 words):
   a) Detail the key structural elements of your design.
   b) Explain how these elements contribute to the overall stability and functionality of the structure.
   c) Describe any novel materials or construction techniques you propose to use.

3. Environmental Systems (200-250 words):
   a) Outline the systems designed to manage {t['challenge']} in your structure.
   b) Explain how these systems are integrated into the overall architectural design.
   c) Discuss the efficiency and sustainability of these systems.

4. Biomimetic Features (150-200 words):
   a) Identify specific features of your design directly inspired by {t['inspiration']}.
   b) Explain how these biomimetic elements enhance the structure's functionality or efficiency.
   c) Discuss any challenges in adapting biological principles to architectural design.

5. Human Factors (150-200 words):
   a) Describe how your design accommodates human comfort and well-being in the extreme environment.
   b) Discuss any unique features that address psychological needs of inhabitants.
   c) Explain how your design balances functionality with aesthetic considerations.

6. Scalability and Adaptability (100-150 words):
   a) Discuss the potential for scaling your design to accommodate larger populations.
   b) Explain how your design could be adapted to other extreme environments.

7. Potential Challenges and Solutions (100-150 words):
   a) Identify two potential challenges or limitations of your design.
   b) Propose innovative solutions or areas for further research to address these challenges.

Ensure your response demonstrates a deep understanding of architectural principles, environmental engineering, and biomimicry. Be creative and innovative in your approach while maintaining scientific and engineering plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design effectively addresses the challenges of the {t['environment']} environment.",
            f"The solution incorporates biomimetic principles inspired by {t['inspiration']} in a meaningful and innovative way.",
            f"The proposed systems for managing {t['challenge']} are well-integrated and efficient.",
            "The design demonstrates a balance between functionality, sustainability, and human factors.",
            "The response shows a deep understanding of architectural principles and environmental engineering.",
            "The proposed solution is creative and innovative while maintaining scientific and engineering plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
