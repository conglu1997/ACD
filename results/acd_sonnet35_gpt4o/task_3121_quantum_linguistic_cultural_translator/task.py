import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'source_culture': 'Inuit',
                'target_culture': 'Maasai',
                'concept': 'relationship with nature',
                'quantum_principle': 'superposition'
            },
            '2': {
                'source_culture': 'Ancient Greek',
                'target_culture': 'Modern Japanese',
                'concept': 'concept of time',
                'quantum_principle': 'entanglement'
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that translates the cultural concept of '{t['concept']}' from {t['source_culture']} culture to {t['target_culture']} culture, utilizing the quantum principle of {t['quantum_principle']}. Your response should include the following sections:

1. Quantum-Cultural Framework (250-300 words):
   a) Explain how the chosen quantum principle ({t['quantum_principle']}) can be applied to represent cultural concepts.
   b) Describe how your system would encode cultural information using quantum states.
   c) Discuss the advantages of using quantum computing for this task over classical methods.

2. Cultural Analysis (200-250 words):
   a) Analyze the concept of '{t['concept']}' in both {t['source_culture']} and {t['target_culture']} cultures.
   b) Identify key differences and similarities in how these cultures perceive and express this concept.
   c) Explain how these cultural nuances would be represented in your quantum system.
   (Hint: Consider how the {t['source_culture']} culture might view {t['concept']} in terms of their traditional practices, and compare this to the {t['target_culture']} perspective.)

3. Quantum Algorithm Design (250-300 words):
   a) Propose a quantum algorithm for translating the cultural concept, including key quantum operations.
   b) Explain how your algorithm leverages {t['quantum_principle']} to capture and convey nuanced meanings.
   c) Describe the quantum circuit or operations involved in your translation process.
   d) Include a simple diagram or pseudocode representation of your quantum algorithm.
   e) Briefly discuss the computational advantages of your quantum approach.

4. Linguistic Integration (200-250 words):
   a) Explain how your quantum system interfaces with natural language processing.
   b) Describe the process of converting linguistic input into quantum states and vice versa.
   c) Discuss challenges in preserving semantic and pragmatic meaning across languages.

5. Output and Interpretation (150-200 words):
   a) Provide an example output of your system translating the concept of '{t['concept']}' from {t['source_culture']} to {t['target_culture']} culture.
   b) Explain how to interpret the quantum state output in terms of cultural understanding.
   c) Discuss potential ambiguities or uncertainties in the translation and how they are represented.

6. Evaluation, Limitations, and Ethical Considerations (200-250 words):
   a) Propose methods for evaluating the accuracy and cultural sensitivity of your quantum translation system.
   b) Discuss potential limitations of your quantum-cultural translation system and suggest areas for future improvement.
   c) Analyze ethical implications of using quantum computing for cultural translation.
   d) Address potential biases and how to mitigate them in your system.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theory, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Cite relevant literature to support your proposed quantum-cultural framework and algorithm design. Use in-text citations in the format (Author, Year) and provide a brief bibliography at the end of your response.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']} and its application to cultural concept translation.",
            f"The cultural analysis shows insight into both {t['source_culture']} and {t['target_culture']} perspectives on {t['concept']}.",
            "The proposed quantum algorithm applies quantum principles to cultural translation in a plausible manner.",
            "The linguistic integration addresses challenges in cross-linguistic and cross-cultural communication.",
            "The example output and interpretation demonstrate how the system would work in practice.",
            "Limitations, ethical considerations, and evaluation methods are discussed with specific examples.",
            "Relevant literature is cited to support the proposed quantum-cultural framework and algorithm design.",
            "The response meets the specified word count requirements for each section and overall (1250-1550 words)."
        ]
        word_count = len(submission.split())
        if word_count < 1250 or word_count > 1550:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0