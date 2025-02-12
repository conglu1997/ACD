import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = ['Indo-European', 'Sino-Tibetan', 'Afroasiatic', 'Austronesian']
        time_periods = ['Ancient (3000-500 BCE)', 'Classical (500 BCE-500 CE)', 'Medieval (500-1500 CE)', 'Early Modern (1500-1800 CE)']
        info_theory_concepts = ['Entropy', 'Mutual Information', 'Kolmogorov Complexity']
        evo_bio_principles = ['Natural Selection', 'Genetic Drift', 'Punctuated Equilibrium']
        
        tasks = [
            {
                'language_family': random.choice(language_families),
                'time_period': random.choice(time_periods),
                'info_theory_concept': random.choice(info_theory_concepts),
                'evo_bio_principle': random.choice(evo_bio_principles)
            },
            {
                'language_family': random.choice(language_families),
                'time_period': random.choice(time_periods),
                'info_theory_concept': random.choice(info_theory_concepts),
                'evo_bio_principle': random.choice(evo_bio_principles)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that applies principles of information theory and evolutionary biology to model and analyze the evolution of linguistic complexity across multiple languages and time periods. Focus on the {t['language_family']} language family during the {t['time_period']}, incorporating the information theory concept of {t['info_theory_concept']} and the evolutionary biology principle of {t['evo_bio_principle']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Outline the key components of your framework for modeling linguistic evolution.
   b) Explain how you integrate information theory and evolutionary biology principles in your model.
   c) Describe how your framework accounts for historical and cultural factors in language change.
   d) Provide a mathematical or formal representation of a core aspect of your framework.

2. Application to Specific Language Family (250-300 words):
   a) Apply your framework to analyze the evolution of complexity in the {t['language_family']} family during the {t['time_period']}.
   b) Discuss how the {t['info_theory_concept']} concept helps quantify linguistic complexity in this context.
   c) Explain how the principle of {t['evo_bio_principle']} might have influenced language evolution in this family and period.

3. Comparative Analysis (200-250 words):
   a) Compare the predicted linguistic evolution in your chosen language family with another major language family.
   b) Discuss any significant differences or similarities in the evolutionary patterns.
   c) Propose hypotheses to explain these differences or similarities.

4. Empirical Predictions (200-250 words):
   a) Derive at least two testable predictions from your framework about linguistic features or changes.
   b) Describe potential methods or data sources for testing these predictions.
   c) Discuss any challenges in empirically validating your model.

5. Implications and Extensions (200-250 words):
   a) Discuss the broader implications of your framework for understanding language evolution and complexity.
   b) Propose an extension of your model to analyze modern linguistic phenomena (e.g., internet language, emojis).
   c) Suggest how your framework might inform approaches in natural language processing or AI language models.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or oversimplifications in your framework.
   b) Propose avenues for future research to address these limitations.
   c) Discuss how advancements in genetics or neuroscience might inform future iterations of your model.

Ensure your response demonstrates a deep understanding of linguistics, information theory, and evolutionary biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, information theory, and evolutionary biology.",
            "The theoretical framework effectively integrates concepts from information theory and evolutionary biology to model linguistic evolution.",
            "The application to the specific language family and time period is well-reasoned and insightful.",
            "The comparative analysis provides meaningful insights into linguistic evolution across different language families.",
            "The empirical predictions are testable and logically derived from the framework.",
            "The discussion of implications and extensions shows creative thinking and broad understanding of potential applications.",
            "The limitations and future directions demonstrate critical thinking and awareness of the framework's boundaries.",
            "The overall response is creative and speculative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits for each section and the overall word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
