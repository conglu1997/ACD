import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        proto_indo_european = {
            "descendant_1": {"name": "Latin", "words": ["pater", "mater", "frater", "ignis", "novus", "duo"]},
            "descendant_2": {"name": "Ancient Greek", "words": ["pater", "meter", "phrater", "pugmai", "neos", "duo"]},
            "descendant_3": {"name": "Sanskrit", "words": ["pitar", "matar", "bhratar", "agni", "nava", "dva"]},
            "modern_phrase": "The new fire burns brightly"
        }
        
        proto_austronesian = {
            "descendant_1": {"name": "Tagalog", "words": ["mata", "apat", "bato", "bulan", "isda", "langit"]},
            "descendant_2": {"name": "Hawaiian", "words": ["maka", "ha", "pohaku", "mahina", "i'a", "lani"]},
            "descendant_3": {"name": "Maori", "words": ["mata", "wha", "kowhatu", "marama", "ika", "rangi"]},
            "modern_phrase": "Four fish swim under the moon"
        }
        
        tasks = [proto_indo_european, proto_austronesian]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to reconstruct a hypothetical proto-language based on the given descendant languages, then use it to translate a modern phrase. Follow these steps:\n\n" \
               f"1. Analyze the provided words from three descendant languages: {t['descendant_1']['name']}, {t['descendant_2']['name']}, and {t['descendant_3']['name']}.\n" \
               f"2. Reconstruct the proto-forms for each of the given words. Explain your reasoning for each reconstruction, considering sound changes and patterns across the descendant languages.\n" \
               f"3. Based on your reconstructions, propose a name for this proto-language and briefly describe its hypothetical historical and geographical context.\n" \
               f"4. Using your reconstructed proto-language, translate the modern phrase: \"{t['modern_phrase']}\" into the proto-language. Explain your translation process and any assumptions you made.\n" \
               f"5. Discuss how this proto-language might have evolved into the given descendant languages, providing at least two examples of possible sound changes or grammatical shifts.\n\n" \
               f"Provide your response in the following format:\n" \
               f"1. Proto-language Reconstruction (300-350 words)\n" \
               f"2. Proto-language Name and Context (100-150 words)\n" \
               f"3. Modern Phrase Translation (200-250 words)\n" \
               f"4. Language Evolution Discussion (200-250 words)\n\n" \
               f"Ensure your response demonstrates a deep understanding of historical linguistics, sound change patterns, and language evolution. Be creative in your reconstructions while maintaining linguistic plausibility. Your total response should be between 800-1000 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes plausible reconstructions for all given words, with clear explanations for each.",
            "The proposed proto-language name and historical context are creative and linguistically plausible.",
            "The translation of the modern phrase into the proto-language is logical and consistent with the reconstructions.",
            "The discussion of language evolution includes at least two specific examples of sound changes or grammatical shifts.",
            "The response demonstrates a deep understanding of historical linguistics and language evolution principles.",
            "The submission adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
