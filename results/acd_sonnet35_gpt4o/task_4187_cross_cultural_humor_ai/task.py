import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        humor_types = [
            "Wordplay",
            "Situational comedy",
            "Sarcasm",
            "Absurdism",
            "Self-deprecation"
        ]
        cultures = [
            "American",
            "British",
            "Japanese",
            "Indian",
            "Nigerian"
        ]
        cognitive_aspects = [
            "Incongruity resolution",
            "Superiority theory",
            "Relief theory",
            "Benign violation theory",
            "Script-based semantic theory of humor"
        ]
        
        tasks = {}
        for i in range(1, 3):
            humor_type = random.choice(humor_types)
            culture_pair = random.sample(cultures, 2)
            cognitive_aspect = random.choice(cognitive_aspects)
            tasks[str(i)] = {
                "humor_type": humor_type,
                "culture_1": culture_pair[0],
                "culture_2": culture_pair[1],
                "cognitive_aspect": cognitive_aspect
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of understanding, analyzing, and generating humor across different cultures, focusing on linguistic and cognitive aspects of humor comprehension and production. Your system should specifically address {t['humor_type']} as a form of humor, compare its perception and generation between {t['culture_1']} and {t['culture_2']} cultures, and incorporate the cognitive aspect of {t['cognitive_aspect']} in its modeling of humor. Your response should include the following sections:\n\n1. Theoretical Foundation (250-300 words):\n   a) Explain the linguistic and cognitive principles underlying {t['humor_type']}.\n   b) Discuss how {t['cognitive_aspect']} contributes to humor comprehension and generation.\n   c) Compare and contrast how {t['humor_type']} is perceived and used in {t['culture_1']} and {t['culture_2']} cultures.\n\n2. AI System Architecture (300-350 words):\n   a) Describe the key components of your AI system for cross-cultural humor analysis and generation.\n   b) Explain how your system incorporates linguistic, cultural, and cognitive models of humor.\n   c) Detail how the system processes and generates {t['humor_type']} across different cultures.\n   d) Provide a high-level diagram or flowchart of your system's architecture (describe it textually).\n\n3. Humor Analysis Process (250-300 words):\n   a) Explain how your AI system would analyze and interpret instances of {t['humor_type']} from {t['culture_1']} and {t['culture_2']} cultures.\n   b) Describe the features or elements the system would consider in its analysis.\n   c) Discuss how the system accounts for cultural context and cognitive aspects in its interpretation.\n\n4. Humor Generation Process (250-300 words):\n   a) Detail the step-by-step process your AI system would use to generate {t['humor_type']} that is appropriate and effective in both {t['culture_1']} and {t['culture_2']} cultures.\n   b) Explain how the system ensures cultural sensitivity and relevance in its generated humor.\n   c) Provide an example of how your system might generate a humorous instance that works in both cultures.\n\n5. Evaluation and Validation (200-250 words):\n   a) Propose methods to evaluate the effectiveness of your AI system in analyzing and generating cross-cultural humor.\n   b) Describe experiments or studies to validate the system's performance against human judges from different cultures.\n   c) Discuss potential challenges in evaluating humor across cultures and how you would address them.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss ethical implications of using AI systems to analyze and generate culturally-sensitive humor.\n   b) Address potential risks of misunderstanding or offense when dealing with cross-cultural humor.\n   c) Propose guidelines for responsible development and use of humor-generating AI systems.\n\n7. Future Directions and Applications (150-200 words):\n   a) Suggest potential applications of your cross-cultural humor AI system in fields such as education, diplomacy, or entertainment.\n   b) Propose two future research directions that could enhance the system's capabilities or expand its cultural range.\n   c) Discuss how advancements in this field might impact our understanding of human cognition and cross-cultural communication.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, cultural studies, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, cultural studies, and artificial intelligence as they relate to humor",
            f"The AI system design effectively addresses {t['humor_type']} and compares its perception between {t['culture_1']} and {t['culture_2']} cultures",
            f"The system incorporates the cognitive aspect of {t['cognitive_aspect']} in its modeling of humor",
            "The proposed AI architecture is innovative, plausible, and well-explained",
            "The humor analysis and generation processes are detailed and account for cultural differences",
            "The evaluation methods and ethical considerations are thoughtfully addressed",
            "The response includes all required sections with appropriate length and detail"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
