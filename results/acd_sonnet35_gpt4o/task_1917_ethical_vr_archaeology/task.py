import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "site": "Ancient Mayan Temple Complex",
                "artifact": "Jade Death Mask",
                "ethical_dilemma": "Local community claims ownership vs. museum acquisition"
            },
            {
                "site": "Submerged Bronze Age Settlement",
                "artifact": "Intact Wooden Boat",
                "ethical_dilemma": "Preservation in situ vs. excavation for study"
            },
            {
                "site": "Neolithic Cave Paintings",
                "artifact": "Undeciphered Symbolic Inscriptions",
                "ethical_dilemma": "Use of AI for interpretation vs. traditional archaeological methods"
            },
            {
                "site": "Roman Colosseum",
                "artifact": "Gladiator Remains",
                "ethical_dilemma": "Public display vs. respectful reburial"
            },
            {
                "site": "Viking Burial Mound",
                "artifact": "Golden Crown with Precious Gems",
                "ethical_dilemma": "Full excavation vs. partial sampling to preserve site integrity"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality (VR) system for archaeological exploration of the {t['site']}, focusing on the discovery and ethical handling of the {t['artifact']}. Your system should incorporate an ethical decision-making scenario related to the following dilemma: {t['ethical_dilemma']}.

Your response should include the following sections:

1. VR System Architecture (250-300 words):
   a) Describe the key components of your VR system for archaeological exploration.
   b) Explain how users interact with the virtual environment and artifacts.
   c) Discuss how you incorporate realistic archaeological practices into the VR experience.
   d) Include a simple ASCII art diagram or clear textual description of your system's architecture.

2. Archaeological Site Simulation (200-250 words):
   a) Detail how you recreate the {t['site']} in virtual reality.
   b) Explain how you balance historical accuracy with user experience.
   c) Describe how the {t['artifact']} is integrated into the VR environment.

3. Ethical Dilemma Implementation (250-300 words):
   a) Explain how you present the ethical dilemma ({t['ethical_dilemma']}) within the VR experience.
   b) Describe the decision-making process users go through when confronting this dilemma.
   c) Discuss how you ensure users understand the cultural and ethical implications of their choices.

4. Educational Value and Learning Outcomes (200-250 words):
   a) Analyze the potential educational benefits of your VR archaeological system.
   b) Propose specific learning outcomes related to archaeological practices and ethical decision-making.
   c) Suggest how this system could be used in formal educational settings or public outreach programs.

5. Ethical Considerations of VR Use in Archaeology (150-200 words):
   a) Discuss potential ethical issues arising from the use of VR in archaeological research and education.
   b) Propose guidelines for the responsible development and use of VR in archaeology.

6. Future Developments and Research Directions (150-200 words):
   a) Suggest two potential enhancements or extensions to your VR archaeological system.
   b) Propose a research study to evaluate the effectiveness of your system in promoting ethical decision-making in archaeology.

Ensure your response demonstrates a deep understanding of virtual reality technology, archaeological practices, and ethical considerations in cultural heritage management. Be innovative in your approach while maintaining scientific and historical accuracy. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of VR technology and its application to archaeological exploration of {t['site']}.",
            f"The proposed system effectively incorporates the ethical dilemma related to {t['ethical_dilemma']}.",
            "The VR system architecture is well-described and includes realistic archaeological practices.",
            "The ethical decision-making process is clearly explained and integrated into the VR experience.",
            "The response addresses the educational value and potential learning outcomes of the VR system.",
            "Ethical considerations of using VR in archaeology are thoughtfully discussed.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
