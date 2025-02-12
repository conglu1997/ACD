import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "synesthesia_type": "grapheme-color",
                "application": "creative writing",
                "target_language": "English"
            },
            "2": {
                "synesthesia_type": "lexical-gustatory",
                "application": "language learning",
                "target_language": "Mandarin Chinese"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates {t['synesthesia_type']} synesthesia for language processing and generation, focusing on its application in {t['application']} for {t['target_language']}. Your response should include the following sections:

1. Synesthesia Simulation (250-300 words):
   a) Explain the chosen type of synesthesia and its neurological basis.
   b) Describe how your AI system models this type of synesthesia.
   c) Discuss any assumptions or simplifications in your model compared to human synesthesia.
   d) Provide a simple diagram or pseudocode snippet illustrating a key aspect of your synesthesia simulation.

2. Language Processing Integration (200-250 words):
   a) Explain how your synesthetic AI system processes and represents language.
   b) Describe any novel language processing techniques enabled by the synesthetic approach.
   c) Discuss how your system handles the specific features of the target language.

3. Application in {t['application']} (200-250 words):
   a) Describe how your synesthetic AI system is applied to the specified domain.
   b) Provide a concrete example of the system in use, including input and output.
   c) Analyze potential benefits and challenges of this application.

4. Comparative Analysis (150-200 words):
   a) Compare your synesthetic AI approach to traditional methods in the chosen application.
   b) Discuss potential advantages and limitations of your system.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns or societal impacts of simulating synesthesia in AI.
   b) Propose guidelines for responsible development and use of synesthetic AI systems.
   c) Discuss potential implications for understanding human cognition and perception.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your synesthetic AI system.
   b) Briefly describe how these extensions could enhance its capabilities or applications.

Ensure your response demonstrates a deep understanding of synesthesia, linguistics, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of {t['synesthesia_type']} synesthesia and how it is modeled in the AI system",
            "The language processing integration is well-described and considers the specific features of the target language",
            f"The application in {t['application']} is clearly explained with a concrete example",
            "A thorough comparative analysis is provided, discussing advantages and limitations",
            "Ethical considerations and societal impacts are thoughtfully addressed",
            "Two relevant future research directions are suggested with clear explanations",
            "The response demonstrates deep understanding of synesthesia, linguistics, and AI systems",
            "The proposed system is creative while remaining scientifically and technologically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
