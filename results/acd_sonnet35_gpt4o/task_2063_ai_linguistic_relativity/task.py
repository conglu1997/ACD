import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Hopi",
                "feature": "Lack of grammatical tense markers",
                "concept": "Time perception"
            },
            {
                "name": "Guugu Yimithirr",
                "feature": "Absolute spatial reference system",
                "concept": "Spatial cognition"
            }
        ]
        return {
            "1": {"language": random.choice(languages)},
            "2": {"language": random.choice(languages)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        language = t['language']
        return f"""Design experiments to test the Sapir-Whorf hypothesis using large language models, focusing on the {language['name']} language and its {language['feature']}. Your task is to:

1. Experimental Design (300-350 words):
   a) Propose two experiments that could reveal whether an AI model trained exclusively on {language['name']} exhibits cognitive biases related to {language['concept']} compared to models trained on languages without this feature.
   b) For each experiment, describe the methodology, including control groups, stimuli, and measurement techniques.
   c) Explain how your experiments account for potential confounding variables.

2. AI Model Architecture (250-300 words):
   a) Describe the architecture of the AI models you would use for these experiments.
   b) Explain how you would modify existing language model architectures to accommodate the unique features of {language['name']}.
   c) Discuss any challenges in training models on languages with limited available data and how you would address them.

3. Linguistic Analysis (200-250 words):
   a) Analyze how the {language['feature']} of {language['name']} might influence the model's understanding and generation of language related to {language['concept']}.
   b) Provide specific examples of how this linguistic feature could manifest in the model's outputs.
   c) Discuss potential implications for natural language understanding and generation in AI systems.

4. Cognitive Implications (200-250 words):
   a) Explore the potential cognitive implications if your experiments show significant effects of linguistic relativity in AI models.
   b) Discuss how these findings might inform our understanding of human cognition and language processing.
   c) Consider the philosophical implications for AI consciousness and the nature of thought.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns or limitations of using AI models to study linguistic relativity.
   b) Discuss how these experiments might impact our approach to developing multilingual AI systems.
   c) Propose safeguards or guidelines for responsible research in this area.

Ensure your response demonstrates a deep understanding of psycholinguistics, AI technologies, and experimental design. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific rigor.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Experimental Design:') on a new line, followed by your response for that section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively, with each section meeting the specified word count range.",
            f"The experimental designs are tailored to test linguistic relativity in AI models trained on {t['language']['name']}, with clear methodologies and consideration of confounding variables.",
            "The proposed AI model architecture demonstrates understanding of language model design and adaptation for specific linguistic features, including strategies for handling limited data.",
            f"The linguistic analysis shows deep understanding of how {t['language']['feature']} might influence the model's processing of {t['language']['concept']}, with specific examples provided.",
            "The discussion of cognitive implications demonstrates interdisciplinary thinking and considers broader impacts on AI, cognitive science, and philosophy.",
            "The ethical considerations are thoughtful and relevant to the proposed research, including suggestions for responsible development of multilingual AI systems.",
            "The overall response shows creativity, scientific rigor, and interdisciplinary integration of psycholinguistics, AI, and cognitive science.",
            "The response is properly formatted with clear headings for each section as specified in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
