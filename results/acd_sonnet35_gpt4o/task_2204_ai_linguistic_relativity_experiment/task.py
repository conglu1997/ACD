import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "Mandarin Chinese",
            "Hopi",
            "Russian",
            "Pirahã"
        ]
        cognitive_domains = [
            "Perception of time",
            "Spatial reasoning",
            "Color discrimination",
            "Numerical cognition"
        ]
        tasks = {
            "1": {"language": random.choice(languages), "cognitive_domain": random.choice(cognitive_domains)},
            "2": {"language": random.choice(languages), "cognitive_domain": random.choice(cognitive_domains)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an experiment to test the linguistic relativity hypothesis using large language models trained on different languages, and analyze the implications for AI cognition and cross-cultural communication. Focus on the language {t['language']} and the cognitive domain of {t['cognitive_domain']}.

Your response should include the following sections:

1. Experimental Design (300-350 words):
   a) Describe the setup of your experiment, including the language models to be used and how they will be compared.
   b) Explain how you will isolate the effects of language on the chosen cognitive domain.
   c) Detail the specific tasks or prompts you will use to test the language models.
   d) Discuss how you will control for confounding variables.

2. Linguistic Analysis (250-300 words):
   a) Analyze the key features of {t['language']} relevant to {t['cognitive_domain']}.
   b) Compare these features to English or another widely-used language in AI.
   c) Hypothesize how these linguistic differences might affect cognitive processing in the language models.

3. Implementation and Methodology (200-250 words):
   a) Outline the steps to implement your experiment using existing AI technologies.
   b) Describe the data collection and analysis methods you will use.
   c) Explain how you will measure and quantify the language models' performance in the chosen cognitive domain.

4. Expected Results and Interpretation (200-250 words):
   a) Predict potential outcomes of your experiment.
   b) Explain how different results would support or challenge the linguistic relativity hypothesis.
   c) Discuss the implications of your findings for AI cognition and development.

5. Implications for Cross-Cultural AI (150-200 words):
   a) Analyze how your experiment's results could impact the development of culturally-aware AI systems.
   b) Discuss potential applications in improving cross-cultural communication through AI.
   c) Address ethical considerations in applying these findings to real-world AI systems.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your experimental design.
   b) Suggest improvements or extensions to your study.
   c) Propose future research questions that arise from your experiment.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI language models. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific rigor. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed experiment to test the linguistic relativity hypothesis using language models",
            f"The experimental design focuses on the specified language ({t['language']}) and cognitive domain ({t['cognitive_domain']})",
            "The linguistic analysis demonstrates a deep understanding of the relevant features of the specified language",
            "The implementation and methodology are clearly explained and feasible with current AI technologies",
            "The expected results and interpretation show a nuanced understanding of the linguistic relativity hypothesis",
            "The implications for cross-cultural AI are thoughtfully analyzed",
            "Limitations and future directions are adequately addressed",
            "The response demonstrates interdisciplinary knowledge of linguistics, cognitive science, and AI",
            "The proposed experiment is innovative while maintaining scientific rigor",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
