import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_languages = ['English', 'Mandarin', 'Spanish', 'Arabic', 'Russian']
        target_languages = ['Japanese', 'Hindi', 'Swahili', 'French', 'Portuguese']
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise']
        
        task = {
            "source_language": random.choice(source_languages),
            "target_language": random.choice(target_languages),
            "emotion": random.choice(emotions)
        }
        return {"1": task, "2": task}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that translates idiomatic expressions from {t['source_language']} to {t['target_language']} while preserving their emotional and cultural connotations, with a focus on expressions conveying {t['emotion']}. Then, use your system to analyze cross-cultural communication patterns. Your response should include the following sections:\n\n" \
               f"1. System Architecture (300-350 words):\n" \
               f"   a) Describe the key components of your AI system for translating idiomatic expressions.\n" \
               f"   b) Explain how your system integrates linguistic, cultural, and emotional analysis.\n" \
               f"   c) Detail the specific AI techniques and algorithms used in your system.\n" \
               f"   d) Provide a high-level diagram or flowchart of your system architecture (describe it textually).\n\n" \
               f"2. Linguistic and Cultural Analysis (250-300 words):\n" \
               f"   a) Explain how your system analyzes the linguistic structure and cultural context of idiomatic expressions.\n" \
               f"   b) Describe how you handle culture-specific concepts and references.\n" \
               f"   c) Discuss how your system accounts for differences in emotional expression between cultures.\n\n" \
               f"3. Emotional Preservation (250-300 words):\n" \
               f"   a) Detail how your system identifies and quantifies the emotional content of idiomatic expressions.\n" \
               f"   b) Explain your approach to preserving emotional connotations during translation.\n" \
               f"   c) Describe how you handle cases where direct emotional equivalents don't exist in the target language.\n\n" \
               f"4. Translation Process (200-250 words):\n" \
               f"   a) Provide a step-by-step explanation of how your system translates an idiomatic expression.\n" \
               f"   b) Include a specific example of translating an expression related to {t['emotion']} from {t['source_language']} to {t['target_language']}.\n" \
               f"   c) Discuss how your system handles ambiguity and multiple interpretations.\n\n" \
               f"5. Cross-Cultural Communication Analysis (200-250 words):\n" \
               f"   a) Explain how you would use your system to analyze cross-cultural communication patterns.\n" \
               f"   b) Describe potential insights that could be gained from this analysis.\n" \
               f"   c) Discuss how these insights could be applied to improve intercultural understanding.\n\n" \
               f"6. Evaluation and Refinement (200-250 words):\n" \
               f"   a) Propose methods for evaluating the accuracy and effectiveness of your system.\n" \
               f"   b) Describe how you would incorporate user feedback and expert knowledge to refine the system.\n" \
               f"   c) Discuss potential ethical considerations in using AI for idiomatic and emotional translation.\n\n" \
               f"7. Future Developments (150-200 words):\n" \
               f"   a) Suggest two potential improvements or extensions to your system.\n" \
               f"   b) Propose a research question that could further the development of AI systems for cross-cultural communication.\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistics, cultural studies, emotional intelligence, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 1550-1900 words. Include a total word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cultural studies, emotional intelligence, and artificial intelligence.",
            "The AI system design integrates linguistic, cultural, and emotional analysis coherently and innovatively.",
            "The approach to preserving emotional and cultural connotations in idiomatic expression translation is well-explained and plausible.",
            "The cross-cultural communication analysis component is thoughtfully developed and has practical applications.",
            "The evaluation methods, ethical considerations, and future developments are thoroughly addressed.",
            "The response is well-structured, follows the given format with clear headings, and adheres to the word count guidelines.",
            "The proposed system design is original and not based on existing translation systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
