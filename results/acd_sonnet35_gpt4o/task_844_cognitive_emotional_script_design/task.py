import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        experiences = [
            "falling in love for the first time",
            "overcoming a significant personal challenge",
            "experiencing a profound loss",
            "having a sudden realization that changes one's worldview"
        ]
        
        tasks = {
            "1": {"experience": random.choice(experiences)},
            "2": {"experience": random.choice(experiences)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel writing system that encodes linguistic, emotional, and cognitive information, then use it to transcribe and analyze the complex human experience of {t['experience']}. Your task has the following parts:

1. Writing System Design (250-300 words):
   a) Describe your writing system, explaining how it incorporates linguistic, emotional, and cognitive elements.
   b) Provide examples of how basic concepts are represented in your system.
   c) Explain how your system can represent complex, multi-layered human experiences.

2. Cognitive and Emotional Encoding Justification (150-200 words):
   a) Explain how your writing system reflects or respects current understanding of cognitive and emotional processes.
   b) Discuss any advantages or unique features of your system for representing human experiences.

3. Experience Transcription (200-250 words):
   a) Transcribe the given experience ({t['experience']}) using your writing system.
   b) Provide a detailed explanation of your transcription, highlighting how different aspects of the experience are encoded.

4. Analysis and Interpretation (200-250 words):
   a) Analyze the transcribed experience, extracting insights about the linguistic, emotional, and cognitive aspects of the experience.
   b) Discuss how your writing system reveals layers of meaning that might not be apparent in traditional writing systems.

5. AI Application (150-200 words):
   a) Propose how an AI system could be designed to read and interpret texts written in your script.
   b) Discuss potential applications of such an AI system in fields like psychology, anthropology, or human-computer interaction.

6. Reflection (100-150 words):
   Discuss the potential implications of your writing system for understanding human cognition, emotion, and communication.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and emotional intelligence. Be creative in your system design while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section and use paragraphs for readability. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a novel writing system that encodes linguistic, emotional, and cognitive information.",
            "The writing system is logically consistent, clearly explained, and genuinely reflects current understanding of cognitive and emotional processes.",
            "The given experience is transcribed using the new writing system, with a detailed explanation provided.",
            "The analysis extracts meaningful insights about the linguistic, emotional, and cognitive aspects of the experience.",
            "The proposed AI application is plausible and demonstrates understanding of AI capabilities.",
            "The reflection provides insightful discussion on the implications of the writing system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
