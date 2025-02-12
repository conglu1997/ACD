import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_languages = ['English', 'Mandarin Chinese', 'Arabic', 'Spanish', 'Russian', 'Hindi']
        target_languages = ['Japanese', 'French', 'Swahili', 'Portuguese', 'German', 'Korean']
        conceptual_domains = ['Time', 'Emotions', 'Power', 'Life', 'Knowledge', 'Morality']
        
        tasks = {}
        for i in range(1, 3):
            source = random.choice(source_languages)
            target = random.choice([lang for lang in target_languages if lang != source])
            domain = random.choice(conceptual_domains)
            tasks[str(i)] = {
                'source_language': source,
                'target_language': target,
                'conceptual_domain': domain
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of simulating and analyzing cross-linguistic conceptual metaphors, then use it to generate novel metaphors in {t['target_language']} based on {t['source_language']} input, focusing on the conceptual domain of {t['conceptual_domain']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your AI system for cross-linguistic metaphor simulation and generation.\n   b) Explain how your system processes and represents conceptual metaphors from different languages.\n   c) Detail how your system handles the cultural and linguistic nuances specific to {t['source_language']} and {t['target_language']}.\n   d) Discuss any novel AI techniques or algorithms used in your system.\n\n2. Conceptual Metaphor Analysis (250-300 words):\n   a) Explain how your system identifies and analyzes conceptual metaphors in the domain of {t['conceptual_domain']} in {t['source_language']}.\n   b) Describe the process of mapping these metaphors to potential equivalents in {t['target_language']}.\n   c) Discuss how your system handles cases where direct metaphorical equivalents don't exist between the languages.\n\n3. Novel Metaphor Generation (250-300 words):\n   a) Detail the process by which your system generates novel metaphors in {t['target_language']}.\n   b) Explain how the system ensures the generated metaphors are culturally appropriate and meaningful in {t['target_language']}.\n   c) Provide an example of a novel metaphor your system might generate for the concept of {t['conceptual_domain']} in {t['target_language']}, based on a {t['source_language']} input.\n\n4. Evaluation and Validation (200-250 words):\n   a) Propose a method for evaluating the quality and cultural relevance of the generated metaphors.\n   b) Discuss potential challenges in assessing the effectiveness of cross-linguistic metaphor generation.\n   c) Suggest how native speakers and linguistic experts could be involved in the validation process.\n\n5. Ethical and Cultural Considerations (150-200 words):\n   a) Discuss potential ethical implications of using AI for cross-cultural metaphor generation.\n   b) Address concerns about cultural appropriation or misrepresentation.\n   c) Propose guidelines for responsible use of this technology in linguistic and cultural studies.\n\n6. Future Implications and Applications (150-200 words):\n   a) Speculate on how this technology might impact fields such as translation, cross-cultural communication, and cognitive linguistics.\n   b) Suggest potential applications of your system beyond metaphor generation (e.g., language learning, cultural studies).\n   c) Propose areas for future research or improvement in AI-driven cross-linguistic analysis.\n\nEnsure your response demonstrates a deep understanding of cognitive linguistics, natural language processing, and cultural knowledge integration. Use appropriate terminology from relevant fields, providing clear explanations where necessary. Be creative in your approach while maintaining scientific and cultural plausibility.\n\nFormat your response with clear headings for each main section (numbered 1-6) and use lettered subheadings (a, b, c, etc.) within each section as outlined above. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, natural language processing, and cultural knowledge integration.",
            "The proposed AI system is innovative, coherent, and technically plausible.",
            "The conceptual metaphor analysis shows sensitivity to linguistic and cultural differences between the source and target languages.",
            "The novel metaphor generation process is well-detailed and addresses cultural appropriateness.",
            "The evaluation and validation methods are thoughtfully considered and include native speaker involvement.",
            "Ethical and cultural considerations are thoroughly addressed.",
            "The response is well-structured, using the required headings and subheadings.",
            "All required sections are thoroughly addressed.",
            "The response is creative while maintaining scientific and cultural plausibility.",
            "The total word count is between 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
