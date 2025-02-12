import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = [
            'Indo-European', 'Sino-Tibetan', 'Niger-Congo', 'Austronesian',
            'Afroasiatic', 'Dravidian', 'Turkic', 'Uralic'
        ]
        linguistic_features = [
            'word order', 'case marking', 'gender system', 'tense-aspect-mood',
            'evidentiality', 'phonological inventory', 'tone system'
        ]
        information_theory_concepts = [
            'entropy', 'mutual information', 'Kolmogorov complexity',
            'channel capacity', 'data compression'
        ]
        
        return {
            "1": {
                "source_family": random.choice(language_families),
                "target_family": random.choice([f for f in language_families if f != "source_family"]),
                "linguistic_feature": random.choice(linguistic_features),
                "info_theory_concept": random.choice(information_theory_concepts)
            },
            "2": {
                "source_family": random.choice(language_families),
                "target_family": random.choice([f for f in language_families if f != "source_family"]),
                "linguistic_feature": random.choice(linguistic_features),
                "info_theory_concept": random.choice(information_theory_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel machine translation system optimized for translating between languages from the {t['source_family']} family to the {t['target_family']} family. Your system should focus on handling the linguistic feature of {t['linguistic_feature']} and incorporate the information theory concept of {t['info_theory_concept']}. Your task has the following components:\n\n" \
               f"1. System Architecture (250-300 words):\n" \
               f"   a) Describe the key components of your machine translation system.\n" \
               f"   b) Explain how it addresses the specific challenges of translating between the given language families.\n" \
               f"   c) Detail how your system incorporates the specified linguistic feature and information theory concept.\n\n" \
               f"2. Linguistic Analysis (200-250 words):\n" \
               f"   a) Compare and contrast how the specified linguistic feature is typically expressed in the source and target language families.\n" \
               f"   b) Explain how your system would handle these differences in translation.\n" \
               f"   c) Discuss any linguistic universals or typological patterns that your system leverages.\n\n" \
               f"3. Information Theory Application (200-250 words):\n" \
               f"   a) Explain how the specified information theory concept is applied in your translation system.\n" \
               f"   b) Describe how this application improves the translation process or output.\n" \
               f"   c) Discuss any trade-offs or challenges in implementing this concept.\n\n" \
               f"4. Translation Process (250-300 words):\n" \
               f"   a) Provide a step-by-step explanation of how your system would translate a complex sentence.\n" \
               f"   b) Include an example sentence in a specific source language, and show how it would be processed and translated.\n" \
               f"   c) Highlight how your system handles ambiguities or culture-specific concepts.\n\n" \
               f"5. Evaluation and Implications (200-250 words):\n" \
               f"   a) Propose a method to evaluate the effectiveness of your translation system, particularly in handling the specified linguistic feature.\n" \
               f"   b) Discuss how your approach could contribute to the field of machine translation and linguistic typology.\n" \
               f"   c) Address any ethical considerations or potential biases in your system.\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistic typology, information theory, and machine translation principles. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic typology, particularly regarding the specified language families and linguistic feature.",
            f"The system effectively incorporates the information theory concept of {t['info_theory_concept']}.",
            "The translation process is clearly explained with a plausible example.",
            "The proposed evaluation method is appropriate and well-reasoned.",
            "The response addresses ethical considerations and potential biases.",
            "The solution is creative while maintaining scientific plausibility.",
            "The response is well-structured and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
