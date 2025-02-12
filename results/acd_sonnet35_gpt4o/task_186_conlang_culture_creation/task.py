class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "environment": "Desert planet with two moons",
                "cultural_focus": "Time perception"
            },
            "2": {
                "environment": "Underwater civilization in a gas giant's moon",
                "cultural_focus": "Social hierarchy"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a constructed language (conlang) and design a fictional culture for a civilization living in the following environment: {t['environment']}. Your conlang and culture should particularly emphasize the concept of {t['cultural_focus']}.

        1. Conlang Basics (150-200 words):
           a) Describe the phonology (sound system) of your language.
           b) Explain its basic grammatical structure (e.g., word order, case system).
           c) Provide a unique linguistic feature that reflects the environment or cultural focus.

        2. Lexicon (100-150 words):
           a) Create 5 words in your conlang related to the environment or cultural focus.
           b) Provide their pronunciation, meaning, and etymology.

        3. Cultural Integration (200-250 words):
           a) Explain how the language reflects and shapes the culture's perception of {t['cultural_focus']}.
           b) Describe a cultural practice or tradition that is deeply tied to a linguistic feature of your conlang.

        4. Sapir-Whorf Thought Experiment (150-200 words):
           Propose a unique way of thinking or perceiving the world that speakers of this language might have due to its structure, relating to the linguistic relativity hypothesis.

        5. Translation Challenge:
           Translate the following English sentence into your conlang, then back-translate it, explaining any cultural or linguistic nuances:
           "In our world, understanding transcends the boundaries of time and space."

        6. Anthropological Analysis (100-150 words):
           Discuss how studying this fictional language and culture could provide insights into real-world linguistic and cultural phenomena.

        Format your response using clear headings for each section. Be creative while ensuring internal consistency in your language and cultural design.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            "The conlang demonstrates a coherent phonology, grammar, and unique linguistic features.",
            "The lexicon includes 5 words with pronunciation, meaning, and etymology.",
            "The cultural integration section clearly links language features to cultural concepts.",
            "The Sapir-Whorf thought experiment presents a plausible and creative idea.",
            "The translation challenge is completed with a reasonable explanation of nuances.",
            "The anthropological analysis provides insightful connections to real-world phenomena.",
            "The overall response shows creativity, internal consistency, and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
