import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "wave-particle duality",
            "quantum tunneling",
            "uncertainty principle"
        ]
        cultures = [
            "Navajo",
            "Mandarin Chinese",
            "Arabic",
            "Hindi",
            "Swahili"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_concept": random.choice(quantum_concepts),
                "culture": random.choice(cultures)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how the quantum physics concept of {t['quantum_concept']} is expressed in {t['culture']} language and culture, then incorporate this analysis into designing a universal quantum language. Your response should include:

1. Cultural-Linguistic Analysis (250-300 words):
   a) Explain the quantum concept of {t['quantum_concept']} in simple terms.
   b) Research and describe how {t['culture']} language and culture might conceptualize or express this quantum concept.
   c) Identify any unique linguistic features or cultural metaphors that could be relevant.
   d) Discuss challenges in translating this concept accurately into the {t['culture']} worldview.

2. Universal Quantum Language Design (300-350 words):
   a) Propose a method for representing {t['quantum_concept']} in a universal quantum language.
   b) Explain how your design incorporates insights from the {t['culture']} perspective.
   c) Describe the syntax and semantics of your language for this concept.
   d) Provide an example 'sentence' or 'expression' in your universal quantum language that conveys {t['quantum_concept']}.

3. Cross-Cultural Application (200-250 words):
   a) Explain how your universal quantum language could be adapted or translated for use in other cultures.
   b) Discuss potential benefits and challenges of using this language in scientific communication across cultures.
   c) Propose a method for teaching this language to speakers of diverse linguistic backgrounds.

4. Implications and Reflections (150-200 words):
   a) Discuss how this exercise might inform our understanding of the relationship between language, culture, and scientific concepts.
   b) Reflect on any insights gained about the nature of quantum physics through this cultural-linguistic lens.
   c) Consider potential implications for science education and cross-cultural scientific collaboration.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and cultural anthropology. Be creative in your language design while maintaining scientific accuracy. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section. Your total response should be between 900-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the given quantum concept and its cultural-linguistic implications.",
            "The universal quantum language design is creative, logically consistent, and effectively incorporates cultural insights.",
            "The cross-cultural application is well-reasoned and considers diverse linguistic backgrounds.",
            "The implications and reflections show deep thought about the intersection of quantum physics, linguistics, and culture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
