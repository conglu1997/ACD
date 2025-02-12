import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scripts = [
            {
                "script": "Devanagari",
                "language": "Hindi",
                "color_palette": ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#800000", "#008000", "#000080", "#808000", "#800080", "#008080"]
            },
            {
                "script": "Arabic",
                "language": "Arabic",
                "color_palette": ["#FFA500", "#800080", "#008000", "#FF0000", "#0000FF", "#FFFF00", "#FFC0CB", "#A52A2A", "#00FFFF", "#FF00FF", "#808080", "#000000"]
            }
        ]
        return {
            "1": scripts[0],
            "2": scripts[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates grapheme-color synaesthesia for the {t['script']} script used in the {t['language']} language. Your system should process and generate text while associating specific colors with each grapheme. Use the following color palette for your associations: {', '.join(t['color_palette'])}.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for simulating grapheme-color synaesthesia.
   b) Explain how it incorporates principles from neuroscience and cognitive psychology.
   c) Detail the key components, including input processing, color association, and text generation modules.
   d) Discuss any novel machine learning techniques or algorithms used in your design.

2. Synaesthetic Mapping (250-300 words):
   a) Explain how your system creates and maintains consistent color associations for each grapheme in the {t['script']} script.
   b) Describe how these associations are used in both text processing and generation.
   c) Discuss how your system handles potential conflicts or ambiguities in color mapping.

3. Language Processing and Generation (250-300 words):
   a) Detail how your AI processes input text in the {t['language']} language, taking into account the synaesthetic color associations.
   b) Explain how the system generates new text while maintaining consistent color associations.
   c) Describe any techniques used to ensure the generated text is coherent and contextually appropriate.

4. Cognitive Implications (200-250 words):
   a) Discuss how your system's synaesthetic processing might influence language understanding or production.
   b) Speculate on potential cognitive effects of using this system for language learning or text analysis.
   c) Compare your artificial synaesthesia model to known properties of natural synaesthesia in humans.

5. Evaluation and Testing (200-250 words):
   a) Propose methods for evaluating the consistency and effectiveness of your system's synaesthetic associations.
   b) Describe experiments to test whether the system's text processing and generation are influenced by color associations in ways similar to human synaesthetes.
   c) Suggest how you would validate the system's output with actual synaesthetes who use the {t['script']} script.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss potential applications of your AI system in fields such as linguistics, psychology, or education.
   b) Address any ethical concerns related to simulating cognitive phenomena like synaesthesia.
   c) Explore how this technology could be used to enhance cross-modal sensory experiences in art or communication.

Ensure your response demonstrates a deep understanding of synaesthesia, the {t['script']} script, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system architecture is well-described and incorporates principles from neuroscience and cognitive psychology, specifically for {t['script']} script.",
            "The approach to synaesthetic mapping is comprehensive and addresses challenges specific to grapheme-color associations.",
            f"The language processing and generation methods effectively handle the {t['language']} language while maintaining synaesthetic associations.",
            "The cognitive implications of the system are thoroughly explored and compared to natural synaesthesia.",
            "The evaluation and testing methods are sound and address the challenges of validating artificial synaesthesia.",
            "Ethical considerations and potential applications are thoughtfully discussed.",
            "The response demonstrates a deep understanding of synaesthesia, cognitive science, and artificial intelligence.",
            "The proposed solutions are innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
