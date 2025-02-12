import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "descendant_languages": [
                    {"name": "Arpitan", "words": ["fèna", "cârro", "montâgne", "nêt"]},
                    {"name": "Gascon", "words": ["hemna", "car", "montanha", "net"]},
                    {"name": "Provençal", "words": ["frema", "char", "montanha", "nuech"]}
                ],
                "meanings": ["woman", "cart", "mountain", "night"],
                "historical_context": "These languages descended from Vulgar Latin in the 9th century CE in what is now southern France.",
                "modern_concept": "smartphone"
            },
            "2": {
                "descendant_languages": [
                    {"name": "Icelandic", "words": ["vatn", "faðir", "móðir", "fiskur"]},
                    {"name": "Norwegian", "words": ["vann", "far", "mor", "fisk"]},
                    {"name": "Swedish", "words": ["vatten", "far", "mor", "fisk"]}
                ],
                "meanings": ["water", "father", "mother", "fish"],
                "historical_context": "These languages descended from Old Norse in the 9th century CE in Scandinavia.",
                "modern_concept": "internet"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a historical linguist tasked with reconstructing a proto-language and using it creatively. Your task has the following steps:

1. Proto-language Reconstruction (200-250 words):
   a) Analyze the given descendant languages: {', '.join([lang['name'] for lang in t['descendant_languages']])}
   b) Reconstruct the proto-words for: {', '.join(t['meanings'])}
   c) Explain your reconstruction process, including any sound changes you identify.
   d) Consider the historical context: {t['historical_context']}

2. Grammar Sketch (100-150 words):
   Propose basic grammatical features of the proto-language based on your reconstruction and historical knowledge.

3. Modern Concept Translation (100-150 words):
   a) Create a word or phrase in your reconstructed proto-language for the modern concept: {t['modern_concept']}
   b) Explain your reasoning and any cultural implications.

4. Language Evolution Hypothesis (150-200 words):
   Hypothesize how your proto-language might have evolved differently under alternative historical circumstances.

Ensure your response demonstrates a deep understanding of historical linguistics, creative problem-solving, and interdisciplinary thinking. Be innovative in your approach while maintaining linguistic plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes reconstructed proto-words for all given meanings.",
            "The reconstruction process is explained with reference to sound changes.",
            "A basic grammar sketch of the proto-language is provided.",
            "A word or phrase for the given modern concept is created in the proto-language.",
            "A hypothesis about alternative language evolution is presented."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
