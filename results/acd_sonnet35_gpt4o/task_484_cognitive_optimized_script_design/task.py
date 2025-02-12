import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "script_purpose": "rapid information processing",
                "target_language": "English",
                "cognitive_constraint": "working memory limitations"
            },
            {
                "script_purpose": "emotional expression enhancement",
                "target_language": "Mandarin Chinese",
                "cognitive_constraint": "visual processing speed"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel writing system optimized for {t['script_purpose']} that balances human cognitive processing and machine recognition for {t['target_language']}, considering the cognitive constraint of {t['cognitive_constraint']}. Your task is to:

1. Script Design (300-350 words):
   a) Describe the key features of your writing system, explaining how they address the given script purpose and cognitive constraint.
   b) Provide examples of at least 5 characters or symbols in your script, explaining their design rationale.
   c) Explain how your script optimizes for both human readability and machine recognition.

2. Cognitive Science Analysis (200-250 words):
   a) Analyze how your script design aligns with principles of cognitive science, particularly in relation to the specified cognitive constraint.
   b) Discuss potential cognitive benefits and challenges for users learning and using this script.

3. Machine Learning Considerations (200-250 words):
   a) Explain how your script design facilitates efficient machine recognition and processing.
   b) Describe potential challenges in implementing OCR (Optical Character Recognition) for your script and propose solutions.

4. Practical Implementation (200-250 words):
   a) Propose a method for teaching this script to human learners, considering cognitive science principles.
   b) Describe how this script could be integrated into existing digital communication systems.
   c) Discuss potential societal impacts of adopting this script for the target language.

5. Comparative Analysis (150-200 words):
   Compare and contrast your script with existing writing systems for the target language, highlighting advantages and potential drawbacks of your design.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and machine learning principles. Be creative in your design while maintaining scientific plausibility and practical considerations.

Format your response using clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The script design clearly addresses the purpose of {t['script_purpose']} and considers the cognitive constraint of {t['cognitive_constraint']}.",
            f"The response includes at least 5 example characters or symbols for {t['target_language']} with explanations of their design rationale.",
            "The analysis demonstrates a deep understanding of cognitive science principles and their application to script design.",
            "The submission explains how the script optimizes for both human readability and machine recognition.",
            "The response includes a thoughtful discussion of practical implementation and potential societal impacts.",
            "The comparative analysis provides meaningful insights into the advantages and drawbacks of the new script compared to existing systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
