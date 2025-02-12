class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phrase": "Schadenfreude",
                "source_language": "German",
                "target_language": "English",
                "context": "This German term is often used to describe a feeling experienced by people when they take pleasure in someone else's misfortune. It is a compound of two words: 'Schaden' meaning 'harm' and 'Freude' meaning 'joy'."
            },
            "2": {
                "phrase": "Ikigai",
                "source_language": "Japanese",
                "target_language": "English",
                "context": "A Japanese concept that refers to something that gives a person a sense of purpose, a reason for living. It is often associated with the intersection of what you love, what you are good at, what the world needs, and what you can be paid for."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        phrase = t["phrase"]
        source_language = t["source_language"]
        target_language = t["target_language"]
        context = t["context"]
        return f"""Translate the following culturally specific phrase from {source_language} to {target_language} and explain its meaning and cultural context. Phrase: {phrase}\n
Context: {context}\n
Submit your translation and explanation as a plain text string in the following format: 'Translation: [Your translation]\nExplanation: [Your explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should be accurate and culturally appropriate.", "The explanation should clearly describe the meaning and cultural context of the phrase."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
