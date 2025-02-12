import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_aspect": "syntax",
                "developmental_stage": "early childhood (2-4 years)",
                "neural_process": "statistical learning"
            },
            {
                "language_aspect": "semantics",
                "developmental_stage": "middle childhood (5-8 years)",
                "neural_process": "conceptual mapping"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics human neural processes for language acquisition, focusing on {t['language_aspect']} during the {t['developmental_stage']} stage and incorporating the neural process of {t['neural_process']}. Your response should include:

1. Neurolinguistic Foundation (200-250 words):
   a) Explain the key principles of {t['language_aspect']} acquisition during the {t['developmental_stage']} stage.
   b) Describe how {t['neural_process']} contributes to language learning in the human brain.
   c) Discuss relevant neural structures and their roles in this specific aspect of language acquisition.

2. AI System Architecture (250-300 words):
   a) Propose a novel AI architecture that models the neural processes involved in {t['language_aspect']} acquisition.
   b) Describe at least four key components of your AI system and their interactions.
   c) Explain how your system incorporates {t['neural_process']} in its learning mechanisms.
   d) Discuss how your architecture reflects the developmental patterns observed in {t['developmental_stage']}.

3. Learning Algorithm (200-250 words):
   a) Outline a learning algorithm for your AI system that mimics human {t['language_aspect']} acquisition.
   b) Explain how this algorithm integrates principles from neurolinguistics and developmental psychology.
   c) Describe how your algorithm would process and learn from input data.

4. Data Requirements and Processing (150-200 words):
   a) Specify the types of data your AI system would need to learn {t['language_aspect']}.
   b) Explain how this data would be preprocessed to mimic the input received by children during {t['developmental_stage']}.
   c) Discuss any ethical considerations in data collection or use for this purpose.

5. Evaluation Metrics (150-200 words):
   a) Propose metrics to evaluate your AI system's language acquisition progress.
   b) Explain how these metrics align with developmental milestones in human language acquisition.
   c) Discuss potential challenges in comparing AI language acquisition to human language acquisition.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your proposed AI system.
   b) Discuss how these limitations reflect current gaps in our understanding of human language acquisition.
   c) Suggest areas for future research that could improve the biological plausibility of AI language learning systems.

Ensure your response demonstrates a deep understanding of neurolinguistics, developmental psychology, and AI system design. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Aim for a total response between 1100-1400 words. Format your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response focuses on {t['language_aspect']} acquisition during the {t['developmental_stage']} stage.",
            f"The AI system incorporates {t['neural_process']} in its design and learning mechanisms.",
            "The proposed AI architecture demonstrates a clear understanding of relevant neurolinguistic principles.",
            "The learning algorithm effectively mimics human language acquisition processes.",
            "The response covers all six required sections with appropriate detail and coherence.",
            "The proposed evaluation metrics align well with human developmental milestones.",
            "The limitations and future directions section shows critical thinking about the challenges in this field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
