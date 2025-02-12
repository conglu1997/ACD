import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        bio_inspirations = [
            {
                "biological_system": "Neural networks in the human brain",
                "computing_paradigm": "Neuromorphic computing"
            },
            {
                "biological_system": "DNA information storage",
                "computing_paradigm": "DNA-based data storage and processing"
            },
            {
                "biological_system": "Bacterial quorum sensing",
                "computing_paradigm": "Swarm computing"
            },
            {
                "biological_system": "Plant root networks",
                "computing_paradigm": "Distributed edge computing"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(bio_inspirations, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical bio-inspired computing system based on {t['biological_system']}, implementing the computing paradigm of {t['computing_paradigm']}. Your task is to create a detailed proposal for this system, analyze its potential applications, and explore the ethical implications of its development and use.

Provide your response in the following format:

1. System Design (250-300 words):
   a) Describe the key components and functionalities of your bio-inspired computing system.
   b) Explain how it mimics or incorporates principles from {t['biological_system']}.
   c) Detail how the system implements the {t['computing_paradigm']} paradigm.
   d) Propose a novel feature that enhances the system's capabilities or efficiency.
   e) Include a simple ASCII art diagram illustrating the key components and their interactions.

2. Technical Analysis (200-250 words):
   a) Compare your system's potential performance to current computing technologies.
   b) Identify any technical challenges in realizing this system and propose potential solutions.
   c) Discuss how this system might integrate with or enhance existing computing infrastructure.

3. Potential Applications (200-250 words):
   a) Propose three innovative applications for your bio-inspired computing system.
   b) Explain how each application leverages the unique features of your system.
   c) Discuss the potential societal or scientific impact of these applications.

4. Ethical Implications (250-300 words):
   a) Identify and analyze at least three potential ethical concerns raised by your system.
   b) Discuss how these concerns might affect different stakeholders in society.
   c) Propose guidelines or safeguards to address these ethical issues.
   d) Explore any potential dual-use scenarios and their ethical ramifications.

5. Future Directions (150-200 words):
   a) Suggest potential advancements or iterations for your system.
   b) Discuss how your system might evolve alongside other emerging technologies.
   c) Propose a research agenda to further develop and refine your bio-inspired computing paradigm.

6. Interdisciplinary Reflection (100-150 words):
   Reflect on how this bio-inspired computing system demonstrates the intersection of biology, computer science, and ethics. Discuss any insights or novel perspectives gained from this interdisciplinary approach.

Ensure your response demonstrates a deep understanding of both biological systems and computing principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical considerations.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should design a computing system inspired by {t['biological_system']} and implement {t['computing_paradigm']}",
            "The system design should be creative, scientifically plausible, and clearly explained, including an ASCII art diagram",
            "The technical analysis should demonstrate understanding of both biological and computational principles",
            "The potential applications should be innovative and leverage the unique features of the proposed system",
            "The ethical implications should be thoroughly explored, considering multiple perspectives and proposing concrete guidelines",
            "The response should demonstrate interdisciplinary thinking, combining biology, computer science, and ethics",
            "The future directions should propose plausible advancements and a coherent research agenda",
            "The interdisciplinary reflection should provide insightful connections between biology, computer science, and ethics",
            "The response should adhere to the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
