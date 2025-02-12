import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            {
                "organism": "Slime mold",
                "process": "Network optimization",
                "domain": "Transportation and logistics"
            },
            {
                "organism": "Honeybees",
                "process": "Swarm intelligence",
                "domain": "Distributed computing"
            },
            {
                "organism": "Octopus",
                "process": "Distributed cognition",
                "domain": "Robotics and adaptive control"
            },
            {
                "organism": "Tardigrade",
                "process": "Cryptobiosis",
                "domain": "Data storage and preservation"
            }
        ]
        return {
            "1": random.choice(biological_inspirations),
            "2": random.choice(biological_inspirations)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Biomimicry in AI involves drawing inspiration from biological systems to develop innovative technological solutions. Your task is to design a novel AI system inspired by the {t['organism']}'s {t['process']} for applications in {t['domain']}. Your response should be well-structured, using clear headings for each section and adhering to the specified word ranges.

1. Biological Inspiration (200-300 words):
   a) Describe the key features of the {t['organism']}'s {t['process']}.
   b) Explain how these features contribute to the organism's survival or efficiency.
   c) Discuss any existing research or applications that have drawn inspiration from this biological process.

2. AI System Design (300-400 words):
   a) Outline the architecture of your biomimetic AI system, including its main components and their interactions.
   b) Explain how your system mimics or incorporates the key features of the {t['organism']}'s {t['process']}.
   c) Describe the algorithms or mechanisms that enable your system to function, using pseudo-code or high-level descriptions where appropriate.
   d) Discuss how your system improves upon or differs from traditional approaches in {t['domain']}.

3. Application Analysis (200-300 words):
   a) Propose at least two specific applications of your biomimetic AI system in {t['domain']}.
   b) Analyze the potential benefits and limitations of your system for each application.
   c) Compare your system's expected performance to existing solutions in the field.

4. Environmental and Ethical Implications (150-250 words):
   a) Discuss how your biomimetic AI system might contribute to environmental sustainability.
   b) Analyze any potential ethical concerns or unintended consequences of implementing your system.
   c) Propose guidelines or safeguards to ensure responsible development and use of your technology.

5. Future Research Directions (100-200 words):
   a) Suggest two potential research projects that could further develop or expand upon your biomimetic AI system.
   b) Briefly describe the goals and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of both biological processes and AI principles. Be creative in your design while maintaining scientific plausibility. Your total response should be between 950-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['organism']}'s {t['process']} and its relevance to {t['domain']}.",
            "The AI system design should be innovative, well-explained, and demonstrate a clear connection to the biological inspiration.",
            "The application analysis should include at least two specific, well-reasoned applications with benefits and limitations discussed.",
            "Environmental and ethical implications must be thoughtfully considered, including potential concerns and proposed safeguards.",
            "Future research directions should be relevant and demonstrate potential for advancing the field.",
            "The overall response should be well-structured, adhere to the word ranges, and demonstrate interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
