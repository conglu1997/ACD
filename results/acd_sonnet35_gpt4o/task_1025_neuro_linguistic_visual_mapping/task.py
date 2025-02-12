import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_structure": "garden path sentences",
                "neurolinguistic_theory": "serial vs. parallel processing",
                "visual_style": "abstract geometric shapes"
            },
            {
                "linguistic_structure": "center-embedded clauses",
                "neurolinguistic_theory": "working memory limitations",
                "visual_style": "interconnected networks"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets abstract visual representations of {t['linguistic_structure']} based on the neurolinguistic theory of {t['neurolinguistic_theory']}. Your system should use {t['visual_style']} as its primary visual language. Your response should include:

1. Theoretical Foundation (200-250 words):
   a) Explain the key characteristics of {t['linguistic_structure']} and their significance in language processing.
   b) Describe the neurolinguistic theory of {t['neurolinguistic_theory']} and its relevance to {t['linguistic_structure']}.
   c) Discuss how {t['visual_style']} can be used to represent linguistic and cognitive processes.

2. AI System Architecture (250-300 words):
   a) Design an AI system that can generate and interpret visual representations of {t['linguistic_structure']}.
   b) Describe the key components of your system and their functions.
   c) Explain how your system incorporates insights from the theory of {t['neurolinguistic_theory']}.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.

3. Visual Representation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system would generate a visual representation for a given example of {t['linguistic_structure']}.
   b) Describe any novel algorithms or techniques used in this process.
   c) Explain how your visual representation captures both the linguistic structure and the cognitive processes involved.

4. Interpretation and Analysis (200-250 words):
   a) Describe how your system would interpret and analyze a given visual representation.
   b) Explain how it would extract linguistic information from the visual elements.
   c) Discuss how your system could identify potential processing difficulties or ambiguities in the linguistic structure.

5. Evaluation and Applications (150-200 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your system.
   b) Discuss potential applications in fields such as language education, cognitive science research, or natural language processing.
   c) Consider how your system might be extended to handle other linguistic phenomena or neurolinguistic theories.

Ensure your response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of {t['linguistic_structure']} and {t['neurolinguistic_theory']}",
            f"The AI system design should effectively incorporate {t['visual_style']} to represent linguistic structures",
            "The visual representation process should be clearly explained and scientifically plausible",
            "The interpretation and analysis section should demonstrate how linguistic information can be extracted from visual elements",
            "The response should show creativity and interdisciplinary knowledge integration"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
