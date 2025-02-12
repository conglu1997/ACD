class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "Gallia est omnis divisa in partes tres, quarum unam incolunt Belgae, aliam Aquitani, tertiam qui ipsorum lingua Celtae, nostra Galli appellantur.", "language": "Latin"},
            "2": {"text": "Μῆνιν ἄειδε, θεά, Πηληϊάδεω Ἀχιλῆος οὐλομένην, ἣ μυρί᾽ Ἀχαιοῖς ἄλγε᾽ ἔθηκε, πολλὰς δ᾽ ἰφθίμους ψυχὰς Ἄϊδι προΐαψεν ἡρώων, αὐτοὺς δὲ ἑλώρια τεῦχε κύνεσσιν οἰωνοῖσί τε πᾶσιν", "language": "Ancient Greek"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        language = t["language"]
        return f"""Translate the following ancient text from {language} into modern English. Then, provide a brief historical context explaining the significance of the text and its impact or meaning during the time it was written.

Text: {text}

Submit your response in the following format:
Translation: [Your translation here]
Historical Context: [Your historical context here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should accurately capture the meaning of the ancient text.",
            "The historical context provided should be relevant, accurate, and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
