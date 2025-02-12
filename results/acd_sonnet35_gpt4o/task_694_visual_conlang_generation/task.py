class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "base_shape": "triangle",
                "color_system": "RGB",
                "grammatical_feature": "aspect",
                "text_to_translate": "The sun will rise tomorrow."
            },
            "2": {
                "base_shape": "circle",
                "color_system": "CMYK",
                "grammatical_feature": "evidentiality",
                "text_to_translate": "I heard that it might rain later."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a visual constructed language (conlang) and use it to translate a given text. Your task has the following parts:

1. Visual Conlang Design (250-300 words):
   a) Create a visual language system using {t['base_shape']} as the base shape and the {t['color_system']} color system.
   b) Explain how your visual language represents different parts of speech (nouns, verbs, adjectives, etc.).
   c) Describe how your language incorporates the grammatical feature of {t['grammatical_feature']}.
   d) Provide examples of at least 5 basic symbols in your language and their meanings. Describe each symbol in detail, including its shape, color, and any modifications to the base shape.

2. Translation (100-150 words):
   a) Translate the following text into your visual language: "{t['text_to_translate']}"
   b) Provide a detailed description of your translation, explaining how each visual element corresponds to the original text.
   c) Describe any challenges you encountered in the translation process and how you addressed them.

3. Visual Language Analysis (200-250 words):
   a) Analyze the strengths and limitations of your visual language compared to traditional written languages.
   b) Discuss how your visual conlang might be processed differently by the human brain compared to written or spoken languages.
   c) Explain how your visual language could be used to represent complex abstract concepts.

4. AI and Visual Language Processing (200-250 words):
   a) Propose a method for training an AI model to understand and generate text in your visual language.
   b) Discuss potential applications of your visual language in human-AI interaction or data visualization.
   c) Explain how principles from your visual conlang could be applied to improve existing visual programming languages or icon-based user interfaces.

5. Linguistic and Cognitive Implications (150-200 words):
   a) Discuss how your visual language challenges or supports linguistic theories about language universals.
   b) Explore the potential cognitive effects of using a primarily visual language for communication.
   c) Propose an experiment to test whether using your visual language affects spatial reasoning or other cognitive abilities.

Ensure your response demonstrates creativity, logical consistency, and a deep understanding of linguistics, visual design, and artificial intelligence. Use clear, concise language and provide detailed visual descriptions where necessary. Do not create or embed actual images; instead, describe visual elements textually.

Format your response with clear headings for each section, and include a 'Visual Representations' section at the end to describe the visual elements of your conlang and translation in a structured, text-based format.

Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a detailed and coherent design for a visual conlang based on the given parameters, including clear descriptions of at least 5 basic symbols.",
            "The translation of the given text is logical, well-explained, and includes detailed descriptions of the visual elements used.",
            "The analysis of the visual language is insightful and considers both strengths and limitations, with specific examples.",
            "The discussion of AI applications and visual language processing is well-reasoned, innovative, and includes concrete examples or scenarios.",
            "The exploration of linguistic and cognitive implications demonstrates a deep understanding of relevant theories and proposes a plausible, detailed experiment.",
            "The response includes a structured 'Visual Representations' section that clearly describes the visual elements of the conlang and translation.",
            "The overall response is creative, logically consistent, and demonstrates interdisciplinary knowledge without creating or embedding actual images."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
