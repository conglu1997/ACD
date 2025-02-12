import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            "Ayapaneco",
            "Njerep",
            "Kaixana",
            "Liki",
            "Sarcee",
            "Budukh"
        ]
        neurolinguistic_processes = [
            "Lexical retrieval",
            "Syntactic processing",
            "Phonological encoding",
            "Semantic integration",
            "Pragmatic interpretation",
            "Morphological analysis"
        ]
        return {
            "1": {"language": random.choice(endangered_languages), "process": random.choice(neurolinguistic_processes)},
            "2": {"language": random.choice(endangered_languages), "process": random.choice(neurolinguistic_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that models the neurolinguistic process of {t['process']} in multilingual individuals and applies this knowledge to preserve the endangered language {t['language']}. Your response should include:\n\n1. Neurolinguistic Model (250-300 words):\n   a) Describe the key components of your AI model for {t['process']}.\n   b) Explain how your model incorporates current neuroscientific understanding of this process in multilingual brains.\n   c) Discuss how your model accounts for differences between languages, particularly {t['language']}.\n\n2. AI System Architecture (200-250 words):\n   a) Outline the main components of your AI system and their functions.\n   b) Explain how your system integrates the neurolinguistic model with language preservation techniques.\n   c) Describe any novel algorithms or techniques your system uses for language modeling and preservation.\n\n3. Language Preservation Approach (200-250 words):\n   a) Detail how your AI system would be applied to preserve {t['language']}.\n   b) Explain how your approach addresses specific challenges in preserving this endangered language.\n   c) Discuss how your system ensures cultural context and nuances are maintained.\n\n4. Ethical Considerations (150-200 words):\n   a) Identify potential ethical concerns related to using AI for language preservation.\n   b) Discuss how your system addresses issues of data privacy and cultural sensitivity.\n   c) Propose guidelines for responsible development and use of your AI system.\n\n5. Evaluation and Validation (150-200 words):\n   a) Propose methods to evaluate the effectiveness of your system in preserving {t['language']}.\n   b) Describe how you would measure both linguistic accuracy and cultural appropriateness.\n   c) Discuss the challenges in evaluating such a system and how you'd address them.\n\n6. Future Implications (100-150 words):\n   a) Discuss how your AI system might contribute to our understanding of neurolinguistics and language acquisition.\n   b) Propose two potential applications of your system beyond language preservation.\n\nEnsure your response demonstrates a deep understanding of neurolinguistics, AI technologies, and cultural anthropology. Be creative in your approach while maintaining scientific and ethical rigor. Use appropriate terminology and provide explanations where necessary.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1050-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            "The neurolinguistic model demonstrates a clear understanding of the specified process and its application to multilingual individuals.",
            "The AI system architecture effectively integrates the neurolinguistic model with language preservation techniques.",
            f"The language preservation approach addresses specific challenges related to {t['language']}.",
            "The response demonstrates creativity, scientific plausibility, and interdisciplinary knowledge application.",
            "Ethical considerations and guidelines for responsible AI use are thoroughly addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
