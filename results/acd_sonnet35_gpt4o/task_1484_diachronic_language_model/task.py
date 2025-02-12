import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Latin', 'Chinese']
        time_periods = ['Ancient', 'Medieval', 'Early Modern', 'Contemporary']
        analysis_tasks = [
            'Analyze phonological changes',
            'Trace semantic shift in key words',
            'Examine syntactic evolution'
        ]
        
        tasks = {}
        for i in range(2):
            lang = random.choice(languages)
            period1, period2 = random.sample(time_periods, 2)
            analysis = random.choice(analysis_tasks)
            tasks[str(i+1)] = {
                'language': lang,
                'start_period': period1,
                'end_period': period2,
                'analysis_task': analysis
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a diachronic language model for {t['language']} that can generate text from the {t['start_period']} period to the {t['end_period']} period. Then, use this model to {t['analysis_task']}.

A diachronic language model is a computational model that captures the historical development and changes in a language over time, allowing for the analysis and generation of text from different historical periods.

Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your diachronic language model.
   b) Explain how your model incorporates historical linguistic knowledge.
   c) Discuss how your model handles the transition between different time periods.
   d) Describe the training data and process you would use for this model.

2. Implementation Details (250-300 words):
   a) Provide a high-level pseudocode for the main algorithm of your model.
   b) Explain how you handle challenges specific to diachronic modeling (e.g., sparse data for older periods).
   c) Describe any pre-processing or post-processing steps necessary for your model.

3. Text Generation (200-250 words):
   a) Generate a short text sample (2-3 sentences) for both the {t['start_period']} and {t['end_period']} periods of {t['language']}.
   b) Explain the key linguistic features that distinguish these samples.
   c) Discuss how your model ensures historical accuracy in the generated texts.

4. Language Evolution Analysis (250-300 words):
   a) Use your model to {t['analysis_task']} in {t['language']} between the {t['start_period']} and {t['end_period']} periods.
   b) Provide specific examples of linguistic changes identified by your model.
   c) Explain how these changes reflect broader historical or cultural shifts.

5. Evaluation and Limitations (200-250 words):
   a) Propose a method to evaluate the historical accuracy of your model's outputs.
   b) Discuss potential biases or limitations in your approach.
   c) Suggest ways to improve or extend your model for future research.

6. Interdisciplinary Applications (150-200 words):
   a) Propose two potential applications of your diachronic language model in fields outside of linguistics.
   b) Explain how these applications could contribute to research or practical problems in those fields.

Ensure your response demonstrates a deep understanding of historical linguistics, natural language processing, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical linguistics, natural language processing, and machine learning.",
            "The proposed diachronic language model is innovative, well-designed, and scientifically plausible.",
            f"The model successfully generates text samples for both the {t['start_period']} and {t['end_period']} periods of {t['language']}.",
            f"The language evolution analysis effectively {t['analysis_task']} between the specified time periods.",
            "The response includes thoughtful evaluation methods, discusses limitations, and proposes interdisciplinary applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
