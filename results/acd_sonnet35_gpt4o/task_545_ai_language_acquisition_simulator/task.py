import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_stages = [
            "Babbling and first words",
            "Two-word combinations",
            "Simple sentences and grammar",
            "Complex sentences and advanced grammar"
        ]
        
        linguistic_features = [
            "Phonological development",
            "Semantic acquisition",
            "Syntactic rule learning",
            "Pragmatic skills development"
        ]
        
        cognitive_principles = [
            "Statistical learning",
            "Social interaction and imitation",
            "Neural plasticity and critical periods",
            "Embodied cognition"
        ]
        
        return {
            "1": {
                "stage": random.choice(language_stages),
                "feature": random.choice(linguistic_features),
                "principle": random.choice(cognitive_principles)
            },
            "2": {
                "stage": random.choice(language_stages),
                "feature": random.choice(linguistic_features),
                "principle": random.choice(cognitive_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical AI system that simulates the human language acquisition stage of {t['stage']}, focusing on the linguistic feature of {t['feature']} and incorporating the cognitive principle of {t['principle']}. Your response should include:\n\n" \
               f"1. System Architecture (200-250 words):\n" \
               f"   a) Describe the key components of your AI language acquisition system.\n" \
               f"   b) Explain how these components interact to facilitate language learning.\n" \
               f"   c) Discuss how your system incorporates the specified cognitive principle.\n\n" \
               f"2. Learning Process (200-250 words):\n" \
               f"   a) Outline the steps your AI system would take to acquire language skills at the given stage.\n" \
               f"   b) Explain how your system develops the specified linguistic feature.\n" \
               f"   c) Describe any specific algorithms or techniques your system would use.\n\n" \
               f"3. Comparison to Human Development (150-200 words):\n" \
               f"   a) Compare your AI system's language acquisition process to human language development.\n" \
               f"   b) Identify similarities and differences between AI and human learning at this stage.\n\n" \
               f"4. Challenges and Solutions (150-200 words):\n" \
               f"   a) Discuss potential challenges in implementing your system.\n" \
               f"   b) Propose innovative solutions to these challenges.\n\n" \
               f"5. Ethical Considerations (100-150 words):\n" \
               f"   Analyze potential ethical implications of developing AI systems that mimic human language acquisition.\n\n" \
               f"Ensure your response is creative, scientifically grounded, and demonstrates a deep understanding of both language acquisition theories and AI learning processes. Use clear headings for each section of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified language acquisition stage, linguistic feature, and cognitive principle.",
            "The proposed AI system architecture is innovative and coherently integrates concepts from developmental psychology and neurolinguistics.",
            "The learning process description is detailed and logically incorporates the specified cognitive principle.",
            "The comparison between AI and human language acquisition is insightful and well-reasoned.",
            "Challenges and proposed solutions are realistic and demonstrate creative problem-solving.",
            "Ethical considerations are thoughtfully analyzed and relevant to the context of AI language acquisition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
