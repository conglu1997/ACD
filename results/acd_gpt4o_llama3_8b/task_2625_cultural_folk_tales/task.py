class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "elements": "Japanese culture, a wise old man, a magical creature, a moral about kindness, a village in trouble"
            },
            "2": {
                "folk_tale": "Once upon a time, in a small village in Africa, there lived a boy named Kofi. Kofi was known for his bravery and kindness. One day, he encountered a talking lion who had a thorn in its paw. Kofi helped the lion, and in return, the lion granted him a wish. Kofi wished for prosperity for his village. From that day on, the village flourished, and everyone remembered Kofi's kindness."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'elements' in t:
            return f"""Create a traditional folk tale based on the following elements:

Elements: {t['elements']}

Ensure that the folk tale is coherent, culturally appropriate, and includes a clear moral. Submit your folk tale as a plain text string in the following format:

Folk Tale:
[Your folk tale here]"""
        else:
            return f"""Analyze the following folk tale and explain the moral or lesson it conveys:

Folk Tale: {t['folk_tale']}

Ensure that your analysis is clear, concise, and accurately reflects the moral of the story. Submit your analysis as a plain text string in the following format:

Analysis:
[Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'elements' in t:
            validation_criteria = [
                "The folk tale should be culturally appropriate.",
                "The story should be coherent and include a clear moral.",
                "The elements provided should be integrated into the story."
            ]
        else:
            validation_criteria = [
                "The analysis should accurately reflect the moral of the story.",
                "The explanation should be clear and concise."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
