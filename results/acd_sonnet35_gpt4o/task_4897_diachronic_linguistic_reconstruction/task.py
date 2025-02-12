import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_family": "Zephyrian",
                "daughter_languages": [
                    {"name": "Aurorian", "words": ["solara", "lunith", "stellar", "noctis", "aethera"]},
                    {"name": "Borealis", "words": ["solir", "lunan", "steren", "noxen", "aether"]},
                    {"name": "Crepuscular", "words": ["solor", "lunus", "astrum", "noctum", "aetherium"]}
                ],
                "meanings": ["sun", "moon", "star", "night", "sky"],
                "text_to_translate": "The night sky was filled with stars as the moon rose."
            },
            {
                "language_family": "Terralian",
                "daughter_languages": [
                    {"name": "Montanese", "words": ["petra", "arbor", "aqua", "ignis", "ventus"]},
                    {"name": "Plainspeech", "words": ["ston", "tre", "watr", "fyr", "wynd"]},
                    {"name": "Coastlang", "words": ["lithos", "dendron", "hydor", "pyros", "anemoi"]}
                ],
                "meanings": ["stone", "tree", "water", "fire", "wind"],
                "text_to_translate": "The wind whispered through the trees near the water."
            }
        ]
        return {"1": random.choice(tasks), "2": random.choice(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the evolution of the fictional {t['language_family']} language family and reconstruct its proto-language. Then, use your reconstruction to translate a given text. Follow these steps:

1. Language Family Analysis (200-250 words):
   a) Examine the provided daughter languages: {', '.join([lang['name'] for lang in t['daughter_languages']])}
   b) Identify phonological and morphological patterns across the languages.
   c) Propose at least three sound change rules that explain the differences between the languages.
   d) Discuss any apparent semantic shifts or grammatical changes.

2. Proto-Language Reconstruction (150-200 words):
   a) Reconstruct the proto-forms for the given words in the {t['language_family']} proto-language.
   b) Explain your reasoning for each reconstruction, citing the patterns and rules you identified.
   c) Propose a name for the proto-language.

3. Additional Vocabulary (100-150 words):
   a) Based on your understanding of the language family, create three additional words in the proto-language.
   b) Provide their meanings and explain how they might have evolved in each daughter language.

4. Translation Task (150-200 words):
   a) Translate the following text into your reconstructed proto-language:
      "{t['text_to_translate']}"
   b) Explain your translation choices, including any assumptions about grammar or syntax.
   c) Describe how this sentence might be realized in each of the daughter languages.

5. Comparative Linguistic Analysis (150-200 words):
   a) Compare the {t['language_family']} family to a real-world language family.
   b) Discuss similarities and differences in patterns of change and diversification.
   c) Hypothesize about the cultural or historical factors that might have influenced the evolution of the {t['language_family']} family.

Ensure your response demonstrates a deep understanding of historical linguistics principles, sound change patterns, and creative application of linguistic knowledge. Use appropriate terminology and provide clear explanations for your reasoning throughout the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of historical linguistics principles and sound change patterns.",
            "The proto-language reconstruction is logically consistent and well-explained.",
            "The translation into the proto-language is coherent and aligns with the proposed reconstruction.",
            "The comparative analysis shows insightful connections between the fictional and real-world language families.",
            "The response is creative while maintaining linguistic plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
