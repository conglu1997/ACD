import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "Mandarin Chinese",
                "linguistic_phenomenon": "Tonal distinctions",
                "qualia_aspect": "Auditory experience",
                "example_input": "mā (mother) vs. má (hemp) vs. mǎ (horse) vs. mà (scold)"
            },
            {
                "language": "American Sign Language",
                "linguistic_phenomenon": "Spatial grammar",
                "qualia_aspect": "Visual-spatial experience",
                "example_input": "JOHN GIVE BOOK TO MARY (with appropriate spatial arrangement)"
            },
            {
                "language": "Pirahã",
                "linguistic_phenomenon": "Absence of number words",
                "qualia_aspect": "Conceptual experience",
                "example_input": "hói (small amount/size) vs. hoí (larger amount/size)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes linguistic qualia - the subjective, conscious experiences associated with language use - for {t['language']}, focusing on the linguistic phenomenon of {t['linguistic_phenomenon']} and the qualia aspect of {t['qualia_aspect']}. Your response should include:

1. Theoretical Framework (200-250 words):
   a) Explain the concept of linguistic qualia and its relevance to AI and cognitive science.
   b) Describe the specific linguistic phenomenon in the given language and its associated qualia.
   c) Discuss current theories or research related to this type of linguistic experience.
   d) Propose a hypothesis about how this linguistic phenomenon might influence cognitive processing.

2. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating linguistic qualia.
   b) Explain how your system models the specific linguistic phenomenon and qualia aspect.
   c) Detail how the system integrates linguistic, cognitive, and phenomenological principles.
   d) Propose a novel method or algorithm for simulating the given linguistic qualia.
   e) Provide a brief pseudocode or flowchart description of a key component in your system.
   f) Explain how your system handles the subjective nature of qualia while maintaining scientific rigor.

3. Simulation and Analysis Process (200-250 words):
   a) Outline the step-by-step process for simulating the linguistic qualia in your AI system.
   b) Describe how you would analyze and interpret the simulated qualia.
   c) Explain how your system differentiates between simulated qualia and mere information processing.
   d) Propose a method for validating the accuracy of your system's qualia simulation.
   e) Provide a concrete example of how your system would process and analyze the following linguistic input: {t['example_input']}

4. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for our understanding of language, consciousness, and AI.
   b) Propose two novel applications of your linguistic qualia simulator in fields such as linguistics, cognitive science, or AI development.
   c) Explain how your system could contribute to the study of linguistic relativity or cross-cultural communication.
   d) Discuss potential challenges in applying your system to real-world scenarios.
   e) Explore possible cross-linguistic implications of your system for studying qualia in different languages.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in simulating and analyzing subjective linguistic experiences.
   b) Discuss the implications of attributing qualia-like experiences to AI systems.
   c) Propose guidelines for the responsible development and use of linguistic qualia simulators.
   d) Address potential misuse or misinterpretation of your system's outputs.

6. Limitations and Future Directions (100-150 words):
   a) Acknowledge key limitations of your current AI system.
   b) Suggest potential improvements or extensions to address these limitations.
   c) Propose a future research direction that builds on your linguistic qualia simulator.
   d) Discuss how your system might evolve to handle more complex linguistic phenomena.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology from these fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        word_count = len(submission.split())
        if word_count < 1000 or word_count > 1300:
            return 0.0
        criteria = [
            f"The response accurately explains linguistic qualia and its relevance to the {t['linguistic_phenomenon']} in {t['language']}",
            f"The AI system design clearly addresses how it simulates and analyzes the {t['qualia_aspect']} of the given linguistic phenomenon",
            "The response proposes a novel method or algorithm for simulating the given linguistic qualia",
            "A brief pseudocode or flowchart description of a key system component is provided",
            "The simulation and analysis process is well-defined, plausible, and includes a concrete example using the provided linguistic input",
            "The response discusses meaningful implications and applications of the linguistic qualia simulator, including cross-linguistic implications",
            "Ethical considerations are thoughtfully addressed, including guidelines for responsible use and potential misuse",
            "The answer demonstrates interdisciplinary knowledge of linguistics, cognitive science, and AI",
            "The proposed system is innovative yet scientifically grounded, with clear acknowledgment of limitations and future directions",
            f"The response includes a specific analysis of the example input: {t['example_input']}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
