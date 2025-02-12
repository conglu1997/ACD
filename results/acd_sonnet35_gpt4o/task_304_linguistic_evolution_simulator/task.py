import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "English",
                "time_frame": "200 years",
                "environmental_factor": "Increased global connectivity"
            },
            {
                "language": "Mandarin Chinese",
                "time_frame": "100 years",
                "environmental_factor": "Rapid technological advancement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulation of language evolution for {t['language']} over the next {t['time_frame']}, incorporating linguistic, cognitive, and environmental factors, with a focus on the impact of {t['environmental_factor']}. Your task has the following parts:

1. Simulation Model Design (250-300 words):
   a) Describe the key components of your language evolution simulation model.
   b) Explain how your model incorporates linguistic theories, cognitive factors, and environmental influences.
   c) Detail how you represent and track changes in vocabulary, grammar, and phonology.
   d) Explain how your model accounts for the specified environmental factor.

2. Cognitive and Social Factors (200-250 words):
   a) Discuss how your model incorporates cognitive processes such as memory, learning, and social cognition.
   b) Explain how social factors like group dynamics and cultural transmission are simulated.
   c) Describe how individual variations in language use are modeled and how they contribute to overall language change.

3. Predictive Analysis (200-250 words):
   a) Based on your simulation, predict 3-5 specific changes that might occur in {t['language']} over the next {t['time_frame']}.
   b) For each prediction, explain the linguistic, cognitive, and environmental factors that contribute to this change.
   c) Discuss any potential new linguistic features that might emerge as a result of these changes.

4. Model Validation (150-200 words):
   a) Propose a method to validate your simulation model using historical language data.
   b) Discuss potential limitations of your model and how they might affect the accuracy of your predictions.

5. Implications for AI and Cognitive Science (150-200 words):
   a) Discuss how your simulation model could inform the development of more adaptive and culturally aware AI language models.
   b) Explain how insights from your model might contribute to our understanding of human cognition and language processing.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and complex systems modeling. Be creative in your approach while grounding your ideas in established theories and principles. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The simulation model design effectively incorporates linguistic, cognitive, and environmental factors.",
            "The discussion of cognitive and social factors demonstrates a deep understanding of their role in language evolution.",
            "The predictive analysis provides specific, well-reasoned predictions based on the simulation model.",
            "The model validation proposal is scientifically sound and addresses potential limitations.",
            "The implications for AI and cognitive science are insightful and well-explained.",
            "The overall response demonstrates strong interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
