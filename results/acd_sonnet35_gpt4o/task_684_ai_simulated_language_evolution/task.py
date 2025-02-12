import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "initial_language": "Proto-Indo-European",
                "time_span": "5000 years",
                "environmental_factor": "Geographic isolation",
                "social_factor": "Technological advancements"
            },
            {
                "initial_language": "Proto-Austronesian",
                "time_span": "3000 years",
                "environmental_factor": "Climate change",
                "social_factor": "Cultural exchange through trade"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a simulation of language evolution using AI, starting with {t['initial_language']} and evolving over {t['time_span']}. Consider the effects of {t['environmental_factor']} and {t['social_factor']} on the language's development. Your response should include:

1. Initial Language Description (100-150 words):
   Provide a brief overview of the key linguistic features of {t['initial_language']}, including phonology, morphology, syntax, and semantics.

2. Simulation Model Design (200-250 words):
   a) Describe the AI model or algorithm you would use to simulate language evolution.
   b) Explain how your model incorporates {t['environmental_factor']} and {t['social_factor']}.
   c) Discuss how your model handles different aspects of language change (e.g., phonological shifts, grammaticalization, semantic drift).

3. Evolutionary Trajectory (250-300 words):
   Describe the simulated evolution of the language over {t['time_span']}, including:
   a) Major changes in phonology, morphology, syntax, and semantics.
   b) The emergence of new linguistic features or the loss of existing ones.
   c) How these changes relate to the environmental and social factors.

4. Daughter Languages (150-200 words):
   Propose two hypothetical daughter languages that could have evolved from your simulation. Briefly describe their key features and how they differ from each other and the original language.

5. Linguistic Analysis (200-250 words):
   Analyze the plausibility of your simulated language evolution. Discuss how it aligns with or differs from known patterns of historical linguistics. Provide justifications for any unusual or unexpected developments.

6. Model Evaluation (150-200 words):
   a) Propose a method to evaluate the accuracy and realism of your language evolution simulation.
   b) Discuss potential limitations of your model and how they might be addressed in future iterations.

7. Interdisciplinary Implications (100-150 words):
   Discuss how this type of AI-driven language evolution simulation could contribute to fields such as historical linguistics, anthropology, or cognitive science.

Ensure your response demonstrates a deep understanding of linguistic principles, evolutionary processes, and AI modeling techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate linguistic terminology throughout your response.

Format your answer with clear headings for each section. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic principles and evolutionary processes.",
            "The simulation model is well-designed and incorporates the given environmental and social factors.",
            "The evolutionary trajectory and daughter languages are plausible and creatively developed.",
            "The linguistic analysis shows critical thinking and justification for the simulated changes.",
            "The proposed evaluation method and discussion of limitations are thoughtful and relevant.",
            "The interdisciplinary implications are insightful and well-reasoned.",
            "The response uses appropriate linguistic terminology and maintains scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
