import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conlangs = [
            {
                "name": "Ithkuil",
                "sample": "Eqatëns âñžarödh akçiëla'ň eqatrîl öttüas êqut âñžaršš.",
                "explanation": "Ithkuil is a highly complex language designed for precise expression. It uses a combination of consonant clusters, diacritics, and complex morphology to convey nuanced meanings. Each syllable can carry multiple layers of information, including tense, aspect, mood, and case.",
                "translation": "The child's face suddenly became pale upon seeing the stranger.",
                "challenge": "Create a new sentence in Ithkuil expressing a complex emotion, such as 'bittersweet nostalgia' or 'anticipatory dread'."
            },
            {
                "name": "Lojban",
                "sample": "mi fanva fi lo jbobau fi lo glibau",
                "explanation": "Lojban is a logical language designed to be unambiguous. It uses predicate structure and particles to precisely define relationships between concepts. Words are divided into content words (brivla) and structure words (cmavo). The language aims to eliminate syntactic ambiguity.",
                "translation": "I translate from Lojban to English.",
                "challenge": "Create a Lojban sentence describing a conditional statement, such as 'If it rains tomorrow, I will stay home.'"
            }
        ]
        conlang_params = [
            {
                "base": "Create a language based on mathematical operations. Each word should represent a mathematical concept or operation.",
                "rules": [
                    "Use basic arithmetic operations as verb tenses (e.g., addition for present, multiplication for past)",
                    "Represent nouns as prime numbers",
                    "Use mathematical functions for adjectives (e.g., square root for 'essential', exponential for 'growing')",
                    "Incorporate the concept of 'zero' as negation"
                ],
                "feature": "Include a system of evidentiality (indicating the source of information) using mathematical notation."
            },
            {
                "base": "Design a language using only typographical symbols and punctuation marks",
                "rules": [
                    "Each symbol represents a basic concept (e.g., @ for 'at', ? for 'question')",
                    "Combinations of symbols create more complex meanings",
                    "The size of symbols indicates emphasis or intensity",
                    "The orientation of symbols (e.g., rotated or mirrored) changes the meaning"
                ],
                "feature": "Incorporate an aspect system that distinguishes between perfective and imperfective actions using symbol modifications."
            }
        ]
        return {
            "1": random.choice(conlangs),
            "2": random.choice(conlang_params)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "sample" in t:
            return f"Analyze the following sample of the constructed language {t['name']}:\n\nSample: {t['sample']}\nExplanation: {t['explanation']}\nTranslation: {t['translation']}\n\nBased on this analysis, {t['challenge']}\n\nProvide your response in the following format:\n1. Brief analysis of the language structure (3-4 sentences)\n2. Your created sentence\n3. English translation of your sentence\n4. Detailed explanation of how your creation fits the language's rules (at least 3 points)\n5. Rationale for your analysis and creation (3-4 sentences)"
        else:
            return f"Design a complex constructed language (conlang) based on the following parameters:\n\nBase concept: {t['base']}\nRules:\n- {t['rules'][0]}\n- {t['rules'][1]}\n- {t['rules'][2]}\n- {t['rules'][3]}\nAdditional feature: {t['feature']}\n\nProvide your response in the following format:\n1. Explanation of your language's structure (5-6 sentences)\n2. Brief 'grammar guide' explaining the basic rules of your language (4-5 points)\n3. Five example words or phrases with their meanings\n4. One complete sentence in your language\n5. English translation of your sentence\n6. Detailed explanation of how your language follows each of the given rules and incorporates the additional feature\n7. Rationale for your language design choices (4-5 sentences)\n8. Translate the following English sentence into your conlang: 'The curious scientist observed the unexpected phenomenon with great interest.'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "sample" in t:
            criteria = [
                "The analysis demonstrates a clear and accurate understanding of the given conlang's complex structure and rules, including specific features mentioned in the explanation.",
                "The created sentence follows the conlang's rules consistently and expresses the required complex emotion or concept.",
                "The explanation clearly justifies how the created sentence adheres to the language's structure, providing at least 3 specific points of adherence to the rules.",
                "The rationale shows depth of thought in analyzing and applying the language rules, considering the language's unique features and the challenges of expressing complex concepts."
            ]
        else:
            criteria = [
                "The created language follows all given rules consistently and incorporates the additional linguistic feature in a logical and creative manner.",
                "The 'grammar guide' provides a clear and comprehensive overview of the language's basic rules.",
                "The example words, phrases, and sentences demonstrate creativity, complexity, and logical consistency within the language system.",
                "The explanation clearly justifies how the language adheres to each given rule and incorporates the additional feature, with specific examples.",
                "The rationale demonstrates thoughtful consideration in the language design process, explaining the choices made in creating the language's structure and how it achieves the goals of the base concept.",
                "The translation of the given English sentence into the conlang is consistent with the established rules and structure of the created language."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
