class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "mathematical_principle": "Fibonacci sequence",
                "cultural_aspect": "Spiritual practices"
            },
            "2": {
                "mathematical_principle": "Prime numbers",
                "cultural_aspect": "Social hierarchy"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical system based on the mathematical principle of {t['mathematical_principle']} and design a culture around it, focusing on how this system influences {t['cultural_aspect']}. Your task has the following parts:

        1. Musical System Design (200-250 words):
           a) Explain how you incorporate {t['mathematical_principle']} into your musical system.
           b) Describe the basic elements of your musical system (e.g., scales, rhythms, harmony).
           c) Provide a unique feature of your system that directly relates to the mathematical principle.

        2. Composition Example (100-150 words):
           a) Describe a short musical piece in your system.
           b) Explain how it exemplifies the mathematical principle and your system's unique features.

        3. Cultural Integration (200-250 words):
           a) Explain how your musical system shapes the culture's approach to {t['cultural_aspect']}.
           b) Describe a cultural practice or tradition that is deeply tied to a feature of your musical system.

        4. Mathematical-Musical Thought Experiment (150-200 words):
           Propose a unique way of thinking or perceiving the world that members of this culture might have due to their musical-mathematical system.

        5. Notational System (100-150 words):
           a) Design a basic notational system for your music.
           b) Provide an example of how a simple melody would be written in this system.

        6. Comparative Analysis (100-150 words):
           Discuss how studying this fictional musical system and culture could provide insights into real-world mathematical and cultural phenomena.

        Format your response using clear headings for each section. Be creative while ensuring internal consistency in your musical system and cultural design.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            "The musical system demonstrates a coherent integration of the specified mathematical principle.",
            "The composition example clearly illustrates the unique features of the musical system.",
            "The cultural integration section logically connects the musical system to the specified cultural aspect.",
            "The mathematical-musical thought experiment presents a plausible and creative idea.",
            "The notational system is coherent and clearly explained with an example.",
            "The comparative analysis provides insightful connections to real-world phenomena.",
            "The overall response shows creativity, internal consistency, and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
