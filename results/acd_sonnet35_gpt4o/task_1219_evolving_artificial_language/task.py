import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        constraints = [
            {
                "phonetic": "Limited to 15 distinct phonemes",
                "syntactic": "Subject-Object-Verb word order",
                "semantic": "No distinction between nouns and verbs"
            },
            {
                "phonetic": "Tonal language with 3 tones",
                "syntactic": "Verb-Subject-Object word order",
                "semantic": "Evidentiality markers required for all statements"
            }
        ]
        return {
            "1": random.choice(constraints),
            "2": random.choice(constraints)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language with the following constraints:

Phonetic: {t['phonetic']}
Syntactic: {t['syntactic']}
Semantic: {t['semantic']}

Your task has the following components:

1. Language Design (300-350 words):
   a) Describe the basic structure and rules of your artificial language, adhering to the given constraints.
   b) Provide at least 5 grammatical rules that govern your language.
   c) Provide examples of at least 5 words or phrases in your language, with their meanings, grammatical explanations, and IPA notation. Each example should be 20-30 words long.
   d) Explain how your language's structure might influence the thought patterns of its speakers.

2. Evolutionary Simulation (250-300 words):
   a) Propose a method to simulate the evolution of your language over 1000 years.
   b) Describe three significant changes that might occur in your language over this time period.
   c) Explain the linguistic principles or social factors that could drive these changes.

3. Cognitive Implications (200-250 words):
   a) Analyze how the unique features of your language might affect cognitive processes such as memory, perception, or problem-solving.
   b) Compare these effects to those observed in natural languages with similar features.
   c) Propose an experiment to test one of your hypotheses about the cognitive effects of your language.

4. Communication Efficiency (150-200 words):
   a) Evaluate the efficiency of your language for communication compared to natural languages.
   b) Discuss any trade-offs between expressiveness and simplicity in your language design.
   c) Suggest one way to optimize your language for more efficient communication.

5. Practical Application (100-150 words):
   a) Propose an innovative real-world application for your artificial language or the insights gained from its design.
   b) Explain how this application could benefit a field outside of linguistics (e.g., AI, cognitive science, or intercultural communication).

Ensure your response demonstrates a deep understanding of linguistic principles, language evolution, and cognitive science. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1000-1250 words.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic principles and their application in language design.",
            "The language design includes at least 5 grammatical rules and 5 examples with IPA notation.",
            "The evolutionary simulation and cognitive implications are logically derived and scientifically plausible.",
            "The analysis of communication efficiency and practical application shows creative and interdisciplinary thinking.",
            "The artificial language design adheres to the given constraints while demonstrating creativity and coherence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
