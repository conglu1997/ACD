import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_area": "Broca's area",
                "musical_element": "Rhythm",
                "cognitive_process": "Syntactic processing"
            },
            {
                "language_area": "Wernicke's area",
                "musical_element": "Melody",
                "cognitive_process": "Semantic processing"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates between natural language and musical patterns, focusing on the relationship between {t['language_area']} and {t['musical_element']}, emphasizing the cognitive process of {t['cognitive_process']}. Then, use this system to solve a problem and analyze its cognitive implications. Your response should include:

1. System Design (300-350 words):
   a) Explain how your AI system models the function of {t['language_area']} in language processing.
   b) Describe how it relates this to {t['musical_element']} in music cognition.
   c) Outline the key components and processes of your system, focusing on {t['cognitive_process']}.
   d) Provide a specific example of how the system would translate a simple sentence into a musical pattern (or vice versa). Use a clear notation or description for the musical pattern, such as a simplified musical score, rhythm notation, or detailed verbal description.
   e) Describe at least one novel algorithm or technique your system uses to bridge linguistic and musical elements.

2. Neurolinguistic Basis (200-250 words):
   a) Discuss current understanding of how {t['language_area']} functions in human language processing, citing at least one recent study.
   b) Explain how your AI system's design reflects or extends this understanding to musical cognition.
   c) Propose a testable hypothesis about how your system might inform or challenge current neurolinguistic theories.

3. Problem Solving Application (250-300 words):
   a) Present a specific, complex problem that your system could address (e.g., language learning for individuals with specific cognitive impairments, or generating emotionally resonant music from text).
   b) Describe in detail how your system would approach and solve this problem, including any preprocessing steps and output interpretation.
   c) Explain how the solution leverages the neurolinguistic principles and musical elements in your system.
   d) Provide a concrete example of the system's input and output for this problem, demonstrating its effectiveness.

4. Cognitive Implications Analysis (200-250 words):
   a) Analyze how using this system might affect human cognitive processes related to language and music, considering both potential benefits and risks.
   b) Discuss potential implications for our understanding of {t['cognitive_process']} in both language and music, referencing relevant cognitive theories.
   c) Consider how this system might reveal new insights about the relationship between language and music in human cognition, proposing at least one novel research question it could help address.

5. Ethical Considerations and Future Research (150-200 words):
   a) Discuss potential ethical implications of a system that translates between language and music based on neurolinguistic principles, including privacy concerns and potential for misuse.
   b) Propose specific guidelines for responsible development and use of such systems, addressing issues of transparency and accountability.
   c) Suggest a detailed experiment or study to further explore the capabilities or limitations of your system, including methodology and expected outcomes.

Ensure your response demonstrates a deep understanding of neurolinguistics, music cognition, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system that translates between natural language and musical patterns, focusing on {t['language_area']} and {t['musical_element']}, with a novel algorithm or technique described",
            f"The system design and problem-solving application demonstrate a clear emphasis on {t['cognitive_process']}, with detailed explanations of the processes involved",
            "The response provides specific, concrete examples, including a clear representation of a language-to-music or music-to-language translation",
            "The analysis shows a deep understanding of neurolinguistics, music cognition, and AI, with references to current research and theories",
            "The response includes creative and plausible ideas while maintaining scientific integrity, proposing testable hypotheses and novel research questions",
            "Ethical considerations are thoughtfully addressed, with specific guidelines proposed for responsible development and use",
            "The suggested future research includes a detailed experimental design with clear methodology and expected outcomes"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
