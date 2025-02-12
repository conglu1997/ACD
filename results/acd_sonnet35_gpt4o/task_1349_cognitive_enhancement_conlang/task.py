import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_abilities = [
            "working memory",
            "abstract reasoning",
            "pattern recognition",
            "spatial visualization",
            "cognitive flexibility"
        ]
        return {
            "1": {"ability": random.choice(cognitive_abilities)},
            "2": {"ability": random.choice(cognitive_abilities)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a constructed language (conlang) aimed at enhancing {t['ability']}. Your response should include:\n\n" + \
               "1. Conlang Design (300-350 words):\n" + \
               "   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.\n" + \
               "   b) Explain how these features are specifically designed to enhance {t['ability']}.\n" + \
               "   c) Provide examples of words or sentences in your conlang, with translations.\n" + \
               "   d) Discuss any unique writing system or script associated with your conlang.\n\n" + \
               "2. Cognitive Enhancement Analysis (250-300 words):\n" + \
               "   a) Analyze how your conlang might enhance {t['ability']}.\n" + \
               "   b) Explain the theoretical basis for your analysis, citing relevant research in linguistics and cognitive science.\n" + \
               "   c) Discuss potential limitations or drawbacks of your conlang.\n\n" + \
               "3. Learning and Usage (200-250 words):\n" + \
               "   a) Describe how one would go about learning your conlang.\n" + \
               "   b) Explain how regular use of your conlang might affect cognitive processes over time.\n" + \
               "   c) Discuss potential applications of your conlang in education or therapy.\n\n" + \
               "4. Experimental Design (250-300 words):\n" + \
               "   a) Propose an experiment to test the effects of your conlang on {t['ability']}.\n" + \
               "   b) Describe the methodology, including participant selection, experimental procedure, and measurement techniques.\n" + \
               "   c) Discuss potential confounding variables and how you would control for them.\n\n" + \
               "5. Ethical Considerations and Future Directions (150-200 words):\n" + \
               "   a) Discuss any ethical implications of using a conlang for cognitive enhancement.\n" + \
               "   b) Propose two potential future research directions related to cognitive enhancement conlangs.\n\n" + \
               "Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and experimental design. " + \
               "Be creative in your conlang design while maintaining scientific plausibility. " + \
               "Your total response should be between 1150-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate word counts.",
            "The conlang design is well-explained, innovative, and clearly aimed at enhancing the specified cognitive ability.",
            "The cognitive enhancement analysis demonstrates a deep understanding of both linguistics and cognitive science.",
            "The learning and usage section provides practical insights into the application of the conlang.",
            "The experimental design is well-thought-out and scientifically sound.",
            "The response addresses ethical considerations and future directions thoughtfully.",
            "The overall response demonstrates creativity, interdisciplinary knowledge integration, and analytical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
