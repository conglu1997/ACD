import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scripts = [
            {
                "name": "Lumerian",
                "era": "Bronze Age",
                "region": "Mediterranean",
                "known_symbols": [
                    ("☼", "sun"),
                    ("☽", "moon"),
                    ("△", "mountain"),
                    ("○", "city"),
                    ("⚔", "war")
                ],
                "unknown_text": "☼△○☽⚔○△☼☽△⍟☼○△⍟☽⚔△"
            },
            {
                "name": "Zephyrian",
                "era": "Classical Antiquity",
                "region": "Central Asia",
                "known_symbols": [
                    ("♠", "earth"),
                    ("♥", "water"),
                    ("♣", "fire"),
                    ("♦", "air"),
                    ("⚭", "unity")
                ],
                "unknown_text": "♠♥⚭♣♦♥♠♣⚭♦♠☸♠♥♦☸♣⚭♥"
            }
        ]
        return {
            "1": random.choice(scripts),
            "2": random.choice(scripts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a linguist specializing in ancient languages. Your task is to decipher a newly discovered text written in the ancient {t['name']} script from the {t['era']} in the {t['region']} region. Your goal is to propose a plausible translation and explain your decipherment process.

Known information:
1. The following symbols have been reliably translated:
   {', '.join([f'{symbol} = {meaning}' for symbol, meaning in t['known_symbols']])}
2. The unknown text to be deciphered is: {t['unknown_text']}
3. Scholars suspect that this language may have a specific grammatical structure or word order, but this is yet to be confirmed.

Your task has three parts:

1. Analysis and Decipherment (300-350 words):
   a) Describe the patterns you observe in the unknown text.
   b) Propose a hypothesis about the structure of the {t['name']} language based on the known symbols and the unknown text.
   c) Suggest a possible grammatical structure or word order based on your observations.
   d) Propose a writing system classification (logographic, syllabic, alphabetic, or a combination) and justify your choice.
   e) Describe your step-by-step approach to deciphering the unknown symbols and potential grammatical structure.
   f) Provide a tentative translation for the unknown symbol(s), explaining your reasoning.

2. Historical and Cultural Context (200-250 words):
   a) Based on the era and region, suggest possible historical and cultural factors that might influence the content and structure of the text.
   b) Explain how this context might help in deciphering the unknown symbols and understanding the potential grammatical structure.
   c) Draw parallels with known ancient writing systems from similar eras or regions.

3. Proposed Translation and Analysis (250-300 words):
   a) Offer a plausible translation of the entire text, including your interpretation of its grammatical structure.
   b) Explain the significance of your translation in the historical and cultural context you proposed.
   c) Discuss any remaining ambiguities or alternative interpretations.
   d) Compare and contrast the {t['name']} script with at least one known ancient writing system, discussing how this comparison informs your understanding of the script.

Ensure your response demonstrates a deep understanding of linguistic principles, historical context, and logical reasoning. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a thorough analysis of the unknown text, a plausible hypothesis about the structure of the {t['name']} language, and a justified writing system classification.",
            "The decipherment process is logical, well-explained, and applies appropriate linguistic principles or techniques.",
            f"The historical and cultural context provided is relevant to the {t['era']} and {t['region']} and offers insights that aid in understanding the script.",
            "The proposed translation is plausible and consistent with the known symbols and the hypothesized language structure.",
            "The response demonstrates creativity and critical thinking in approaching the decipherment task.",
            "The analysis of the translation's significance considers the historical and cultural context.",
            "The comparison with a known ancient writing system is meaningful and informs the understanding of the {t['name']} script.",
            "The response acknowledges and discusses any remaining ambiguities or alternative interpretations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
