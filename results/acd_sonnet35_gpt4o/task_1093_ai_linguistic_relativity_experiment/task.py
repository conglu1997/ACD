import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "Mandarin Chinese",
            "Hopi",
            "Pirahã",
            "Russian",
            "Guugu Yimithirr"
        ]
        cognitive_domains = [
            "color perception",
            "time perception",
            "spatial reasoning",
            "numerical cognition",
            "gender perception"
        ]
        return {
            "1": {"language": random.choice(languages), "domain": random.choice(cognitive_domains)},
            "2": {"language": random.choice(languages), "domain": random.choice(cognitive_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an experiment to test the Sapir-Whorf hypothesis using AI language models, focusing on {t['language']} and its potential influence on {t['domain']}. Your response should include:

1. Background (200-250 words):
   a) Briefly explain the Sapir-Whorf hypothesis and its relevance to AI language models.
   b) Describe the key linguistic features of {t['language']} that might influence {t['domain']}.
   c) Discuss any existing research or theories about how {t['language']} might affect cognition in the domain of {t['domain']}.

2. Experimental Design (300-350 words):
   a) Outline a detailed experimental setup to test how an AI model trained on {t['language']} might exhibit different cognitive patterns in {t['domain']} compared to models trained on other languages.
   b) Describe the control group and variables you would use in your experiment.
   c) Explain how you would isolate the effects of language from other potential influencing factors.
   d) Propose specific tasks or problems related to {t['domain']} that the AI models would need to solve as part of the experiment.

3. Data Analysis and Interpretation (200-250 words):
   a) Describe the methods you would use to analyze the experimental results.
   b) Explain how you would determine if any observed differences are statistically significant.
   c) Discuss potential confounding factors and how you would account for them in your analysis.

4. Implications for AI Cognition (250-300 words):
   a) Discuss how the results of your experiment might inform our understanding of AI cognition and language processing.
   b) Explore the potential implications for developing more culturally aware and linguistically diverse AI systems.
   c) Consider how this research might contribute to the debate on AI consciousness and the nature of machine understanding.

5. Ethical Considerations (150-200 words):
   a) Discuss any ethical implications of using AI models to study linguistic relativity.
   b) Address potential biases in your experimental design and how they might be mitigated.
   c) Consider the broader societal implications of your research findings.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific rigor and plausibility. Use clear headings for each section and number your paragraphs for easy reference."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of the Sapir-Whorf hypothesis and its potential application to AI language models.",
            f"The experimental design should be well-thought-out and specifically tailored to test the influence of {t['language']} on {t['domain']}.",
            "The proposed data analysis methods should be appropriate and scientifically sound.",
            "The discussion of implications for AI cognition should be insightful and demonstrate an understanding of current debates in AI research.",
            "The response should address ethical considerations and potential biases in a thoughtful manner.",
            "All five requested sections should be present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
