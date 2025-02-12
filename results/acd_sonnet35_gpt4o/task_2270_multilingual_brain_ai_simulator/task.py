import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "English"),
            ("Spanish", "Arabic"),
            ("French", "Japanese"),
            ("German", "Russian")
        ]
        cognitive_processes = [
            "executive function",
            "working memory",
            "cognitive flexibility",
            "attention control"
        ]
        linguistic_phenomena = [
            "code-switching",
            "syntactic transfer",
            "lexical borrowing",
            "phonological interference"
        ]
        return {
            "1": {
                "language_pair": random.choice(language_pairs),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            },
            "2": {
                "language_pair": random.choice(language_pairs),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates multilingual language acquisition and processing in the human brain, focusing on the language pair {t['language_pair'][0]} and {t['language_pair'][1]}. Then, use this system to predict and analyze cross-linguistic influence and cognitive advantages related to {t['cognitive_process']} in multilingual individuals, with a specific focus on the linguistic phenomenon of {t['linguistic_phenomenon']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI system for simulating multilingual language processing.\n   b) Explain how your system models the interaction between the two specified languages in the brain.\n   c) Detail how your system incorporates current neuroscientific understanding of bilingualism and language acquisition.\n   d) Propose a novel feature that enhances the system's ability to model the specified cognitive process.\n\n2. Language Acquisition Simulation (200-250 words):\n   a) Explain how your system simulates the acquisition of the specified language pair.\n   b) Describe how the system accounts for age of acquisition, proficiency levels, and learning contexts.\n   c) Discuss any challenges in modeling simultaneous vs. sequential bilingualism and how you addressed them.\n\n3. Cross-linguistic Influence Analysis (200-250 words):\n   a) Detail how your system predicts and analyzes the specified linguistic phenomenon between the two languages.\n   b) Explain how this phenomenon might manifest differently depending on the direction of influence (L1 to L2 or vice versa).\n   c) Propose a method to validate your system's predictions against empirical data from human bilinguals.\n\n4. Cognitive Advantage Modeling (200-250 words):\n   a) Describe how your system models the potential cognitive advantages in the specified cognitive process for bilinguals of your language pair.\n   b) Explain how these advantages might be influenced by factors such as language proficiency, age of acquisition, and frequency of use.\n   c) Discuss any potential cognitive costs your system predicts and how they interact with the advantages.\n\n5. Neural Network Implementation (150-200 words):\n   a) Propose a neural network architecture that could implement your multilingual processing model.\n   b) Explain how this architecture captures the unique aspects of bilingual language processing and the specified cognitive process.\n   c) Discuss any novel or unconventional neural network components necessitated by your model.\n\n6. Practical Applications (100-150 words):\n   a) Suggest potential applications of your system in fields such as education, cognitive therapy, or artificial intelligence.\n   b) Discuss how your system could inform language policy or bilingual education strategies.\n\n7. Ethical Considerations and Limitations (100-150 words):\n   a) Identify potential ethical issues related to simulating and predicting cognitive processes in bilinguals.\n   b) Discuss limitations of your approach and potential biases in the system.\n   c) Propose guidelines for the responsible use of such AI systems in research and applied contexts.\n\nEnsure your response demonstrates a deep understanding of psycholinguistics, cognitive neuroscience, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words.\n\nAdditional Requirements:\n1. Include at least one relevant citation or reference to current research in each section.\n2. Provide a simple diagram or pseudocode snippet in the Neural Network Implementation section to illustrate your proposed architecture.\n3. In the Cognitive Advantage Modeling section, include a hypothetical data point or scenario that your system would analyze.\n\nYour response will be evaluated based on the depth of knowledge demonstrated, the innovativeness and plausibility of your proposed system, and the clarity and coherence of your explanations."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of psycholinguistics, cognitive neuroscience, and artificial intelligence as they relate to bilingualism and language acquisition.",
            "The proposed system architecture is innovative, coherent, and effectively integrates current neuroscientific understanding of bilingualism.",
            "The explanation of language acquisition simulation and cross-linguistic influence analysis is thorough and scientifically plausible.",
            "The cognitive advantage modeling demonstrates a nuanced understanding of the potential benefits and costs of bilingualism, including a relevant hypothetical scenario.",
            "The proposed neural network implementation is well-reasoned and includes a clear diagram or pseudocode snippet.",
            "The discussion of practical applications and ethical considerations shows awareness of the broader implications of this research.",
            "The response is well-structured, clear, and adheres to the specified word limits for each section.",
            "Each section includes at least one relevant citation or reference to current research."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
