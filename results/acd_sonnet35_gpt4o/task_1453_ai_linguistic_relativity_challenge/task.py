import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_feature": "Grammatical gender",
                "cognitive_domain": "Object perception",
                "ai_application": "Image captioning"
            },
            {
                "linguistic_feature": "Evidentiality markers",
                "cognitive_domain": "Source reliability assessment",
                "ai_application": "Fake news detection"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a series of experiments to test the linguistic relativity hypothesis in AI language models, focusing on the linguistic feature of {t['linguistic_feature']} and its potential influence on {t['cognitive_domain']}. Consider implications for {t['ai_application']} systems. Your response should include:

1. Experimental Design (300-350 words):
   a) Describe 2-3 experiments to test how {t['linguistic_feature']} in training data might influence an AI model's performance in tasks related to {t['cognitive_domain']}.
   b) Explain your hypothesis, methodology, and expected results for each experiment.
   c) Discuss how you would control for confounding variables and ensure the validity of your results.

2. AI Model Analysis (200-250 words):
   a) Analyze potential biases that might emerge in AI models trained on languages with different {t['linguistic_feature']} systems.
   b) Discuss how these biases could impact the performance and fairness of {t['ai_application']} systems.
   c) Propose methods to detect and mitigate these biases in AI development.

3. Cross-linguistic AI Development (200-250 words):
   a) Suggest approaches for developing AI systems that can handle multiple languages with varying {t['linguistic_feature']} systems.
   b) Discuss the challenges and potential solutions for creating linguistically flexible AI models.
   c) Explain how this flexibility might enhance or hinder performance in {t['ai_application']}.

4. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of linguistic relativity in AI, particularly for {t['ai_application']}.
   b) Propose ethical guidelines for developing and deploying linguistically diverse AI systems.
   c) Address potential societal impacts of AI systems that may perpetuate or challenge linguistic biases.

5. Future Research Directions (150-200 words):
   a) Suggest 2-3 future research questions that arise from your experiments and analysis.
   b) Explain how answering these questions could advance our understanding of linguistic relativity in AI and improve {t['ai_application']} systems.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide clear explanations. Be creative in your experimental design and analysis while maintaining scientific rigor and plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['linguistic_feature']} and its potential influence on {t['cognitive_domain']}.",
            f"The experimental designs are creative, well-structured, and relevant to testing linguistic relativity in AI for {t['ai_application']}.",
            "The analysis of AI biases and proposed mitigation strategies are insightful and well-reasoned.",
            "The ethical considerations are comprehensive and show a nuanced understanding of the implications of linguistic relativity in AI development.",
            "The suggested future research directions are innovative and have the potential to advance the field significantly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
