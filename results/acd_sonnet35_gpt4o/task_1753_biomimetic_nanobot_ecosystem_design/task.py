import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "ocean",
            "soil",
            "atmosphere"
        ]
        contaminants = [
            "microplastics",
            "heavy metals",
            "greenhouse gases"
        ]
        biomimetic_inspirations = [
            "bacteria",
            "fungi",
            "plankton"
        ]
        return {
            "1": {
                "environment": random.choice(environments),
                "contaminant": random.choice(contaminants),
                "inspiration": random.choice(biomimetic_inspirations)
            },
            "2": {
                "environment": random.choice(environments),
                "contaminant": random.choice(contaminants),
                "inspiration": random.choice(biomimetic_inspirations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic nanobot ecosystem for environmental remediation in the {t['environment']}, targeting {t['contaminant']} contamination. Your design should be inspired by {t['inspiration']}. Provide your response in the following format:

1. Nanobot Design (300-350 words):
   a) Describe the structure and function of your nanobots, explaining how they mimic {t['inspiration']}.
   b) Explain how the nanobots detect, interact with, and remediate {t['contaminant']}.
   c) Discuss any novel features that allow the nanobots to operate effectively in the {t['environment']}.
   d) Provide a conceptual diagram or detailed description of your nanobot's key components and mechanisms.

2. Ecosystem Dynamics (250-300 words):
   a) Explain how your nanobots interact with each other and their environment to form an ecosystem.
   b) Describe the life cycle of your nanobots, including replication, energy acquisition, and end-of-life processes.
   c) Discuss how your nanobot ecosystem maintains balance and adapts to changing environmental conditions.

3. Environmental Impact Analysis (250-300 words):
   a) Analyze the potential positive and negative impacts of your nanobot ecosystem on the {t['environment']}.
   b) Discuss how your system avoids unintended ecological consequences.
   c) Propose methods for monitoring and controlling the nanobot population.

4. Remediation Efficiency (200-250 words):
   a) Estimate the theoretical efficiency of your nanobot ecosystem in remediating {t['contaminant']}.
   b) Compare your system's efficiency to current remediation technologies.
   c) Propose a method for measuring and optimizing remediation performance in real-world conditions.

5. Ethical and Societal Implications (200-250 words):
   a) Discuss potential ethical concerns related to releasing engineered nanobots into the environment.
   b) Analyze possible societal impacts of widespread adoption of your technology.
   c) Propose guidelines for responsible development, testing, and deployment of nanobot ecosystems.

6. Future Developments and Applications (150-200 words):
   a) Suggest two potential improvements or extensions to your nanobot ecosystem design.
   b) Discuss how your approach might be adapted to other environmental challenges.
   c) Speculate on the long-term implications of this technology for environmental management and restoration.

Ensure your response demonstrates a deep understanding of biology, nanotechnology, and ecology. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biology, nanotechnology, and ecology.",
            "The nanobot design is innovative, well-explained, and scientifically plausible.",
            "The ecosystem dynamics are thoroughly described and ecologically sound.",
            "The environmental impact analysis is comprehensive and considers both positive and negative effects.",
            "The remediation efficiency estimation is well-reasoned and compared to existing technologies.",
            "Ethical and societal implications are thoughtfully addressed.",
            "Future developments and applications are creative and plausible.",
            "The response effectively integrates the specified environment, contaminant, and biological inspiration.",
            "Technical terminology is used appropriately and complex concepts are clearly explained.",
            "The response is within the specified word count range (1350-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
