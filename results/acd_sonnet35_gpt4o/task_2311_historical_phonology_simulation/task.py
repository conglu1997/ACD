import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "language_family": "Indo-European",
                "time_span": "3000 years",
                "focus_area": "Consonant shifts"
            },
            "2": {
                "language_family": "Sino-Tibetan",
                "time_span": "2000 years",
                "focus_area": "Tonal development"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model to simulate the evolution of phonological systems in {t['language_family']} languages over a period of {t['time_span']}, with a focus on {t['focus_area']}. Your response should include the following sections:

1. Model Architecture (250-300 words):
   a) Describe the key components of your computational model.
   b) Explain how your model incorporates principles of historical linguistics.
   c) Detail how machine learning algorithms are integrated into your model.
   d) Include a simple diagram or flowchart of your model's architecture.

2. Phonological Representation (200-250 words):
   a) Explain how you represent phonemes and phonological features in your model.
   b) Describe how your model accounts for phonotactic constraints.
   c) Discuss any novel approaches to phonological representation in your model.

3. Historical Processes Simulation (250-300 words):
   a) Describe how your model simulates specific phonological changes (e.g., assimilation, dissimilation, lenition).
   b) Explain how you model the spread of phonological changes across a language community.
   c) Discuss how your model handles the interaction between different phonological processes.
   d) Provide at least two specific examples of phonological changes your model can simulate, relevant to the given language family.

4. Machine Learning Integration (200-250 words):
   a) Explain which machine learning algorithms you use and why.
   b) Describe how your model learns from historical data to predict future changes.
   c) Discuss any novel machine learning techniques specific to your model.

5. Language Contact and Borrowing (150-200 words):
   a) Explain how your model accounts for language contact and borrowing.
   b) Describe any specific mechanisms for simulating the effects of linguistic borrowing on phonological systems.
   c) Discuss the challenges in modeling these phenomena and how your approach addresses them.

6. Validation and Testing (150-200 words):
   a) Propose a method to validate your model against known historical changes.
   b) Describe how you would test your model's predictive capabilities.
   c) Discuss the challenges in evaluating the accuracy of long-term language evolution predictions.

7. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your model.
   b) Suggest improvements or extensions to address these limitations.
   c) Propose a novel research question that could be explored using your model.

Ensure your response demonstrates a deep understanding of historical linguistics, computational modeling, and machine learning. Use appropriate terminology and provide clear explanations. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical linguistics principles",
            "The computational model is well-designed and incorporates machine learning algorithms appropriately",
            "The approach to simulating phonological changes is scientifically plausible and innovative",
            "The model's architecture is clearly explained and includes all required components",
            "The response addresses the specific language family and focus area provided in the task",
            "The validation and testing methods proposed are appropriate and well-reasoned",
            "The limitations and future directions discussed show critical thinking and insight",
            "Specific examples of phonological changes relevant to the given language family are provided",
            "The model's approach to language contact and borrowing is well-explained and plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
