import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_principles = [
            "Phonology",
            "Syntax",
            "Semantics",
            "Pragmatics"
        ]
        musical_elements = [
            "Melody",
            "Harmony",
            "Rhythm",
            "Timbre"
        ]
        applications = [
            "Music Therapy",
            "Language Acquisition",
            "Cognitive Enhancement",
            "Cross-Cultural Communication"
        ]
        
        tasks = {}
        for i in range(1, 3):
            principle = random.choice(linguistic_principles)
            element = random.choice(musical_elements)
            application = random.choice(applications)
            tasks[str(i)] = {"principle": principle, "element": element, "application": application}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel musical language based on the linguistic principle of {t['principle']}, focusing on the musical element of {t['element']}. Then, analyze its potential application in {t['application']}. Your response should include:\n\n1. Language Design (250-300 words):\n   a) Describe the key features of your musical language.\n   b) Explain how it incorporates the specified linguistic principle.\n   c) Detail how the chosen musical element is utilized in your language.\n   d) Provide a simple notational system or visual representation of your language.\n\n2. Linguistic Analysis (200-250 words):\n   a) Analyze how your musical language relates to natural language structures.\n   b) Discuss any novel linguistic insights that arise from your design.\n   c) Compare and contrast your language with existing musical notation systems.\n\n3. Cognitive Science Implications (200-250 words):\n   a) Explore how your musical language might be processed by the human brain.\n   b) Discuss potential cognitive benefits or challenges of using this language.\n   c) Propose an experiment to test the cognitive effects of your language.\n\n4. Application Analysis (200-250 words):\n   a) Describe how your musical language could be applied to {t['application']}.\n   b) Provide a specific example or case study of its use in this context.\n   c) Discuss potential benefits and limitations of using your language in this application.\n\n5. Future Developments (150-200 words):\n   a) Suggest two potential extensions or modifications to your musical language.\n   b) Propose a research question that arises from your design.\n   c) Discuss ethical considerations related to the development and use of your language.\n\nEnsure your response demonstrates a deep understanding of linguistics, music theory, and cognitive science. Be creative in your design while maintaining scientific plausibility. Use appropriate terminology from all relevant fields."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, music theory, and cognitive science",
            "The musical language design is creative, novel, and scientifically plausible",
            "The analysis of linguistic principles, cognitive implications, and practical applications is thorough and insightful",
            "The response includes all required sections with appropriate length and detail",
            "The proposed notational system or visual representation is clear and well-explained",
            "The response uses appropriate terminology from all relevant fields"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
