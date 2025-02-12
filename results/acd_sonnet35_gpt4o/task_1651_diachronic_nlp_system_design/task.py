import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_periods = [
            "Ancient Greece (5th century BCE)",
            "Medieval Europe (12th century CE)",
            "Renaissance Italy (15th century CE)",
            "Victorian England (19th century CE)"
        ]
        
        linguistic_features = [
            "Semantic shift",
            "Syntactic change",
            "Lexical borrowing",
            "Pragmatic evolution"
        ]
        
        nlp_techniques = [
            "Word embeddings",
            "Attention mechanisms",
            "Transfer learning",
            "Unsupervised learning"
        ]
        
        return {
            "1": {
                "source_period": random.choice(time_periods),
                "target_period": "Modern day (21st century CE)",
                "linguistic_feature": random.choice(linguistic_features),
                "nlp_technique": random.choice(nlp_techniques)
            },
            "2": {
                "source_period": random.choice(time_periods),
                "target_period": "Modern day (21st century CE)",
                "linguistic_feature": random.choice(linguistic_features),
                "nlp_technique": random.choice(nlp_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical Natural Language Processing (NLP) system capable of translating and analyzing texts from {t['source_period']} to {t['target_period']}, with a focus on {t['linguistic_feature']}. Your system should incorporate {t['nlp_technique']} as a key component. Your response should include:\n\n" \
               f"1. System Architecture (250-300 words):\n" \
               f"   a) Describe the main components of your NLP system.\n" \
               f"   b) Explain how your system incorporates {t['nlp_technique']}.\n" \
               f"   c) Detail how your system addresses {t['linguistic_feature']} between the two time periods.\n\n" \
               f"2. Historical and Linguistic Analysis (200-250 words):\n" \
               f"   a) Discuss the key linguistic differences between {t['source_period']} and {t['target_period']}.\n" \
               f"   b) Analyze how {t['linguistic_feature']} manifests in texts from these periods.\n" \
               f"   c) Explain the cultural factors that contribute to these linguistic changes.\n\n" \
               f"3. Translation and Analysis Process (200-250 words):\n" \
               f"   a) Describe step-by-step how your system would translate a text from {t['source_period']} to {t['target_period']}.\n" \
               f"   b) Explain how your system would analyze and account for {t['linguistic_feature']}.\n" \
               f"   c) Provide an example of how your system might handle a specific linguistic challenge.\n\n" \
               f"4. Evaluation and Limitations (150-200 words):\n" \
               f"   a) Propose a method for evaluating the accuracy and effectiveness of your system.\n" \
               f"   b) Discuss potential limitations or challenges in your approach.\n" \
               f"   c) Suggest ways to address these limitations in future iterations.\n\n" \
               f"5. Interdisciplinary Applications (150-200 words):\n" \
               f"   a) Discuss potential applications of your system in fields such as history, literature, or cultural studies.\n" \
               f"   b) Propose an innovative way your system could be used to gain new insights into historical texts or language evolution.\n\n" \
               f"Ensure your response demonstrates a deep understanding of both historical linguistics and modern NLP techniques. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of historical linguistics and modern NLP techniques.",
            "The proposed NLP system architecture is innovative and coherently integrates the specified NLP technique.",
            "The historical and linguistic analysis shows deep understanding of language evolution and cultural factors.",
            "The translation and analysis process is well-explained and addresses the specified linguistic feature.",
            "The evaluation method and limitations discussion show critical thinking and awareness of challenges in the field.",
            "The interdisciplinary applications proposed are creative and demonstrate the potential impact of the system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
