class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"site": "The Parthenon is a former temple on the Athenian Acropolis, Greece, dedicated to the goddess Athena. It was built in the 5th century BC during the height of the Athenian empire. The structure is renowned for its Doric columns, intricate sculptures, and its role as an enduring symbol of Ancient Greece and Athenian democracy."},
            "2": {"site": "Machu Picchu is a 15th-century Inca citadel located in the Eastern Cordillera of southern Peru. It was built in the classical Inca style, with polished dry-stone walls. The site includes more than 150 buildings ranging from baths and houses to temples and sanctuaries, and is divided into an urban sector and an agricultural sector."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to describe and visualize the historical site based on the provided textual information. Ensure your description includes key features, historical context, and spatial arrangement. Use the text to reconstruct a visual representation of the site as clearly as possible.

Site Information: {t['site']}

Provide your response in plain text format. Your response should include:
1. A detailed description of the site, including key features and historical context.
2. A visual reconstruction in text format, describing the spatial arrangement and layout of the site."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include key features, historical context, and spatial arrangement.",
            "The visual reconstruction should be clear and accurate based on the provided text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
