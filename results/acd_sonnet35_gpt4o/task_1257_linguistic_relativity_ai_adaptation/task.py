import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages_features = [
            ('Hopi', 'Time perception'),
            ('Guugu Yimithirr', 'Spatial reasoning'),
            ('Pirahã', 'Numerical cognition'),
            ('Russian', 'Color categorization'),
            ('Japanese', 'Politeness levels')
        ]
        
        tasks = {}
        selected_pairs = random.sample(languages_features, 2)
        for i, (language, feature) in enumerate(selected_pairs, 1):
            tasks[str(i)] = {
                'language': language,
                'linguistic_feature': feature
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the concept of linguistic relativity in the context of AI language models, focusing on the {t['language']} language and its unique approach to {t['linguistic_feature']}. Then, design an AI system that can adapt its cognitive processes based on this linguistic feature. Provide your response in the following format and adhere to the specified word counts:\n\n" \
               f"1. Linguistic Analysis (200-250 words):\n" \
               f"   a) Explain how {t['language']} approaches {t['linguistic_feature']}.\n" \
               f"   b) Discuss how this approach might influence cognition according to the linguistic relativity hypothesis.\n" \
               f"   c) Compare this with how English or another widely-spoken language approaches the same feature.\n\n" \
               f"2. AI Model Design (250-300 words):\n" \
               f"   a) Propose an AI language model architecture that can adapt its cognitive processes based on the {t['linguistic_feature']} feature of {t['language']}.\n" \
               f"   b) Explain how your model would represent and process information differently when operating in {t['language']} mode versus English mode.\n" \
               f"   c) Describe the key components and mechanisms that allow your model to switch between different linguistic-cognitive frameworks.\n\n" \
               f"3. Potential Applications (150-200 words):\n" \
               f"   a) Suggest three potential applications or benefits of an AI system that can adapt its cognition based on linguistic features.\n" \
               f"   b) Explain how each application might advance our understanding of the relationship between language, thought, and AI.\n\n" \
               f"4. Ethical Considerations (150-200 words):\n" \
               f"   a) Discuss potential ethical implications of developing AI systems that can adopt different linguistic-cognitive frameworks.\n" \
               f"   b) Consider issues such as bias, cultural preservation, and the potential for misuse or misunderstanding.\n\n" \
               f"5. Experimental Design (200-250 words):\n" \
               f"   a) Propose an experiment to test whether your AI model truly adopts different cognitive processes when operating in different language modes.\n" \
               f"   b) Describe the methodology, including control conditions and measurable outcomes.\n" \
               f"   c) Predict potential results and explain their implications for the linguistic relativity hypothesis and AI development.\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistic relativity, the specified language and linguistic feature, and current AI language model architectures. Be innovative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistic relativity and how {t['language']} approaches {t['linguistic_feature']}.",
            "The linguistic analysis accurately compares the approach of the given language to English or another widely-spoken language.",
            "The proposed AI model design is innovative, well-explained, and plausible given current AI technologies.",
            "The AI model design clearly explains how it would adapt its cognitive processes based on the given linguistic feature.",
            "The potential applications are creative, well-reasoned, and show a clear understanding of the implications of linguistic relativity for AI.",
            "The ethical considerations are thoughtful and comprehensive, addressing relevant issues in AI development and cultural implications.",
            "The experimental design is well-structured, with clear methodology and predictions that logically follow from the proposed model.",
            "The response integrates concepts from linguistics, cognitive science, and AI in a sophisticated manner.",
            "The writing is clear, well-organized, and follows the requested format and word counts.",
            "The total word count is between 950-1200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
