import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "spatial reasoning",
            "temporal perception",
            "decision making",
            "emotional regulation",
            "abstract thinking",
            "memory formation"
        ]
        linguistic_features = [
            "phonology",
            "morphology",
            "syntax",
            "semantics",
            "pragmatics"
        ]
        return {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of creating and analyzing constructed languages (conlangs) that influence cognitive processes. Then, use this system to generate a conlang that specifically targets the cognitive process of {t['cognitive_process']} through its {t['linguistic_feature']}. Your response should include:\n\n1. AI System Design (300-350 words):\n   a) Describe the key components and architecture of your AI conlang engineering system.\n   b) Explain how your system incorporates principles from cognitive science, linguistics, and AI.\n   c) Detail how the system generates and analyzes conlangs to influence specific cognitive processes.\n   d) Discuss any novel algorithms or techniques used in your design.\n\n2. Conlang Generation (250-300 words):\n   a) Use your AI system to generate a conlang that targets {t['cognitive_process']} through its {t['linguistic_feature']}.\n   b) Provide a detailed description of the conlang's relevant features and structures.\n   c) Explain how these features are designed to influence the specified cognitive process.\n   d) Include examples of words, phrases, or sentences in the conlang with their English translations.\n\n3. Cognitive Impact Analysis (250-300 words):\n   a) Analyze how the generated conlang might influence {t['cognitive_process']}.\n   b) Discuss potential short-term and long-term effects on speakers' cognitive abilities.\n   c) Compare the expected cognitive impact to that of natural languages with similar features.\n   d) Propose experiments to measure the conlang's effect on {t['cognitive_process']}.\n\n4. Ethical Considerations (150-200 words):\n   a) Discuss ethical implications of designing languages to influence cognitive processes.\n   b) Address potential risks and benefits of using such conlangs in various contexts.\n   c) Propose guidelines for responsible development and use of cognitive-enhancing conlangs.\n\n5. Practical Applications (150-200 words):\n   a) Suggest potential real-world applications for conlangs designed to enhance {t['cognitive_process']}.\n   b) Discuss how these applications could advance research or technology in cognitive science, education, or therapy.\n   c) Explore potential challenges in implementing these applications.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your conlang design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1100-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence, especially in relation to {t['cognitive_process']} and {t['linguistic_feature']}.",
            "The AI system design is innovative, well-explained, and plausibly integrates principles from multiple disciplines.",
            f"The generated conlang effectively targets {t['cognitive_process']} through its {t['linguistic_feature']}, with clear examples and explanations.",
            "The cognitive impact analysis is thorough, considering both short-term and long-term effects, and proposes valid experiments.",
            "Ethical considerations are thoughtfully addressed, with balanced discussion of risks and benefits.",
            "Practical applications are creative, relevant, and well-reasoned.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0