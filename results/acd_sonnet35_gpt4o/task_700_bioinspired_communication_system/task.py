import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                "name": "Quorum Sensing",
                "description": "A process by which bacteria communicate and coordinate behavior based on population density"
            },
            {
                "name": "Bioluminescence",
                "description": "The production and emission of light by living organisms"
            }
        ]
        information_theory_concepts = [
            {
                "name": "Channel Capacity",
                "description": "The maximum rate at which information can be transmitted over a communication channel"
            },
            {
                "name": "Error Correction",
                "description": "Methods to detect and correct errors in transmitted data"
            }
        ]
        return {
            "1": {
                "bio_process": random.choice(biological_processes),
                "info_theory": random.choice(information_theory_concepts)
            },
            "2": {
                "bio_process": random.choice(biological_processes),
                "info_theory": random.choice(information_theory_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system inspired by the biological process of {t['bio_process']['name']} and the information theory concept of {t['info_theory']['name']}. Your response should include:

1. System Overview (200-250 words):
   a) Describe the key components and functionality of your communication system.
   b) Explain how it incorporates principles from {t['bio_process']['name']} ({t['bio_process']['description']}).
   c) Detail how it utilizes the concept of {t['info_theory']['name']} ({t['info_theory']['description']}).

2. Technical Design (250-300 words):
   a) Provide a detailed technical description of your system's architecture.
   b) Explain the data encoding and transmission processes.
   c) Describe any novel algorithms or protocols developed for this system.

3. Advantages and Limitations (200-250 words):
   a) Discuss the potential advantages of your system over conventional communication methods.
   b) Analyze any limitations or challenges in implementing this system.
   c) Propose solutions to overcome these limitations.

4. Practical Applications (150-200 words):
   a) Suggest at least two practical applications for your communication system.
   b) Explain how these applications leverage the unique features of your design.

5. Future Developments (150-200 words):
   a) Propose potential future enhancements or extensions to your system.
   b) Discuss how emerging technologies might impact the evolution of your design.

Ensure your response demonstrates a deep understanding of both biological processes and information theory principles. Be creative in your system design while maintaining scientific plausibility and technical feasibility. Use appropriate terminology and provide clear explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively.",
            f"The communication system design clearly incorporates principles from {t['bio_process']['name']} and {t['info_theory']['name']}.",
            "The technical design is detailed, innovative, and scientifically plausible.",
            "The analysis of advantages, limitations, and practical applications is thorough and well-reasoned.",
            "The response demonstrates a deep understanding of both biological processes and information theory principles.",
            "The proposed system is creative and original, showing interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
