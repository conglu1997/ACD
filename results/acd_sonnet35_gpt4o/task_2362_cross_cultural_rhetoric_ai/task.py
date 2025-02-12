import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        rhetorical_devices = [
            {
                "device": "Chiasmus",
                "description": "A rhetorical device where the second part of an expression is balanced against the first, with key elements reversed",
                "example": "Ask not what your country can do for you, ask what you can do for your country"
            },
            {
                "device": "Anaphora",
                "description": "The repetition of a word or phrase at the beginning of successive clauses or sentences",
                "example": "I have a dream that one day... I have a dream that one day..."
            }
        ]
        cultures = ["Ancient Greek", "Modern American", "Classical Chinese", "Contemporary Indian"]
        return {
            "1": {"rhetorical_device": random.choice(rhetorical_devices), "source_culture": random.choice(cultures), "target_culture": random.choice(cultures)},
            "2": {"rhetorical_device": random.choice(rhetorical_devices), "source_culture": random.choice(cultures), "target_culture": random.choice(cultures)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating the rhetorical device of {t['rhetorical_device']['device']} across different cultures, specifically translating from {t['source_culture']} culture to {t['target_culture']} culture. Your system should be able to identify this device in text from the source culture, understand its persuasive impact, and generate an equivalent or analogous device in the target culture.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system integrates linguistic analysis, cultural knowledge, and text generation.
   c) Discuss any novel features that make your system particularly suited for cross-cultural rhetorical analysis and generation.

2. Rhetorical Device Analysis (200-250 words):
   a) Explain how your system identifies and analyzes the {t['rhetorical_device']['device']} in {t['source_culture']} texts.
   b) Describe the linguistic features and cultural context your system considers in this analysis.
   c) Discuss how your system evaluates the persuasive impact of the device in the source culture.

3. Cross-Cultural Translation (250-300 words):
   a) Detail the process by which your system translates the rhetorical device from {t['source_culture']} to {t['target_culture']} culture.
   b) Explain how your system accounts for differences in linguistic structures and cultural values between the two cultures.
   c) Provide an example of how your system might translate a specific instance of {t['rhetorical_device']['device']} between these cultures.

4. Text Generation (200-250 words):
   a) Describe how your system generates new text incorporating the translated rhetorical device in the target culture.
   b) Explain how your system ensures the generated text is culturally appropriate and persuasive.
   c) Discuss any mechanisms for maintaining the original intent and impact of the rhetorical device.

5. Training and Data (150-200 words):
   a) Explain the types of data your system would need for training.
   b) Describe your approach to acquiring or generating this data.
   c) Discuss any challenges in obtaining diverse and representative data for different cultures.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to cross-cultural rhetorical analysis and generation.
   b) Discuss how your system addresses concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for the responsible development and use of such AI systems.

7. Evaluation and Future Work (150-200 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your system's rhetorical device translations.
   b) Suggest areas for future research or improvement in cross-cultural rhetorical AI.
   c) Discuss potential applications of your system beyond academic or literary analysis.

Ensure your response demonstrates a deep understanding of linguistics, cultural studies, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of the rhetorical device {t['rhetorical_device']['device']} and its use in both {t['source_culture']} and {t['target_culture']} cultures.",
            "The proposed AI system architecture is well-designed and integrates linguistic analysis, cultural knowledge, and text generation effectively.",
            "The cross-cultural translation process is clearly explained and accounts for linguistic and cultural differences.",
            "The text generation approach is creative and ensures cultural appropriateness.",
            "Ethical considerations are thoroughly addressed, including concerns about cultural appropriation.",
            "The evaluation methods and future work suggestions are insightful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
