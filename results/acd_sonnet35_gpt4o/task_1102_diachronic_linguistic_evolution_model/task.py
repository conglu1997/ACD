import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_aspects = [
            {
                "aspect": "Phonological changes",
                "cognitive_factor": "Perceptual biases",
                "social_factor": "Language contact",
                "environmental_factor": "Geographic isolation"
            },
            {
                "aspect": "Semantic shift",
                "cognitive_factor": "Metaphorical thinking",
                "social_factor": "Technological advancements",
                "environmental_factor": "Climate change"
            }
        ]
        return {
            "1": random.choice(language_aspects),
            "2": random.choice(language_aspects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a computational model simulating the evolution of a language over time, focusing on {t['aspect']}. Your model should incorporate the cognitive factor of {t['cognitive_factor']}, the social factor of {t['social_factor']}, and the environmental factor of {t['environmental_factor']}. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the key components of your computational model for language evolution.
   b) Explain how your model simulates changes in {t['aspect']} over time.
   c) Detail how the model incorporates the given cognitive, social, and environmental factors.
   d) Discuss any novel aspects of your model that differentiate it from existing approaches in historical linguistics or language evolution modeling.

2. Simulation Process (200-250 words):
   a) Outline the steps your model would take to simulate language evolution over time.
   b) Provide an example of how the model might represent a specific change in {t['aspect']}.
   c) Explain how the model accounts for interactions between the given factors in driving language change.
   d) Describe how your model handles the balance between random variation and directed change in language evolution.

3. Theoretical Grounding (200-250 words):
   a) Explain the key linguistic and cognitive theories underlying your model.
   b) Discuss how your model incorporates or challenges existing theories of language change.
   c) Describe any assumptions or simplifications made in translating these theories to a computational framework.

4. Predictive Analysis (150-200 words):
   a) Describe a specific prediction your model would make about the evolution of {t['aspect']}.
   b) Explain the reasoning behind this prediction based on your model's architecture and underlying principles.
   c) Propose a method to test this prediction against historical linguistic data or future language changes.

5. Model Evaluation (150-200 words):
   a) Discuss potential methods for validating your model against empirical data on language evolution.
   b) Identify possible limitations of your model and suggest ways to address them.
   c) Explain how your model could be extended or improved in future iterations.

6. Interdisciplinary Implications (100-150 words):
   a) Discuss how your model could contribute to our understanding of human cognition, social dynamics, or environmental influences on culture.
   b) Propose potential applications of your model in fields such as historical linguistics, cognitive science, or artificial intelligence.

7. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using such a model in research or policy-making.
   b) Consider issues such as language preservation, linguistic diversity, and the potential for misuse in language planning.
   c) Propose guidelines for the responsible use and interpretation of your model's results.

Ensure your response demonstrates a deep understanding of historical linguistics, cognitive science, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the language aspect of {t['aspect']} and incorporate the cognitive factor of {t['cognitive_factor']}, the social factor of {t['social_factor']}, and the environmental factor of {t['environmental_factor']}.",
            "The proposed model must be logically coherent and demonstrate a clear understanding of language evolution processes.",
            "The submission must include all seven required elements as specified in the instructions, with each section adequately addressing its respective topics.",
            "The model description must be creative and propose novel ideas while remaining grounded in established linguistic and cognitive theories.",
            "The explanation of how the model simulates language change must be scientifically plausible and well-reasoned.",
            "The response must demonstrate a deep understanding of historical linguistics, cognitive science, and computational modeling.",
            "The predictive analysis and proposed validation methods must be thoughtful and demonstrate an understanding of empirical research in linguistics.",
            "The discussion of interdisciplinary implications and ethical considerations must be insightful and demonstrate awareness of broader impacts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
