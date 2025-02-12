class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species = [
            {
                "name": "Luminous Cephalopods",
                "characteristics": "Bioluminescent skin for communication, distributed neural network, ability to change shape and color rapidly, underwater habitat"
            },
            {
                "name": "Crystalline Hive-Mind",
                "characteristics": "Silicon-based lifeform, communicates through vibrations and light refraction, collective consciousness, no individual bodies"
            }
        ]
        import random
        return {
            "1": random.choice(species),
            "2": random.choice(species)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language system for the {t['name']} species. Their key characteristics are: {t['characteristics']}.

        Your task is to:

        1. Language System Design (300-350 words):
           a) Describe the fundamental elements of the language (e.g., phonemes, morphemes, syntax) and how they relate to the species' characteristics.
           b) Explain how the language conveys complex ideas, taking into account the species' unique cognitive and physical traits.
           c) Provide examples of basic communication units (equivalent to words or phrases) in this language.

        2. Grammar and Syntax (200-250 words):
           a) Outline the basic grammatical rules of the language.
           b) Explain how sentence structure works in this language.
           c) Describe any unique linguistic features that arise from the species' characteristics.

        3. Concept Translation (150-200 words):
           Translate the concept of 'time' into this language. Explain:
           a) How the species might perceive time given their characteristics.
           b) How this perception is reflected in the language.
           c) Provide an example 'sentence' in this language expressing a complex temporal idea.

        4. Cultural and Cognitive Implications (200-250 words):
           a) Discuss how this language might shape the species' culture and cognitive processes.
           b) Explain any challenges humans might face in learning or understanding this language.
           c) Propose a method for facilitating communication between humans and this species.

        Ensure your response is creative yet grounded in linguistic principles and the given species characteristics. Use appropriate terminology and provide clear explanations of your design choices.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language system design is comprehensive and clearly relates to the species' characteristics.",
            "The grammar and syntax explanation is logical and consistent with the species' traits.",
            "The concept of 'time' is translated creatively and appropriately for the species.",
            "The cultural and cognitive implications are thoughtfully explored.",
            "The response demonstrates a deep understanding of linguistic principles and creative language design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
