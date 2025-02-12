import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_areas = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm"
        ]
        tasks = [
            {"language_area": area, "musical_element": element}
            for area, element in zip(language_areas, musical_elements)
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates brain activity in {t['language_area']} into musical compositions, focusing on the musical element of {t['musical_element']}. This task requires integrating knowledge from neuroscience, linguistics, music theory, and artificial intelligence.

Your task has the following parts:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for brain activity-to-music translation.
   b) Explain how it incorporates current understanding of {t['language_area']} and its role in language processing.
   c) Detail how the system will capture and interpret relevant brain activity.
   d) Discuss how the system will generate musical output focusing on {t['musical_element']}.

2. Neurolinguistic-Musical Interface (250-300 words):
   a) Explain how your system translates neural data into musical parameters.
   b) Describe the mapping between linguistic features and {t['musical_element']}.
   c) Discuss challenges in this translation process and how you address them.

3. AI Algorithm Design (250-300 words):
   a) Propose a machine learning algorithm for generating music based on neural input.
   b) Explain how this algorithm incorporates both neurolinguistic and musical theory principles.
   c) Describe how the algorithm ensures musical coherence and aesthetic quality.

4. Example Output (200-250 words):
   a) Provide a detailed description of a potential musical output from your system, based on a specific linguistic input of your choice.
   b) Explain how this output reflects the neural activity, linguistic features, and musical element.

5. Applications and Implications (250-300 words):
   a) Discuss potential applications of your system in fields such as neuroscience, linguistics, music therapy, and brain-computer interfaces.
   b) Explore ethical considerations and potential misuses of this technology.
   c) Speculate on how this technology might impact our understanding of language, music, and cognition.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Your total response should be between 1250-1500 words. Please structure your answer with clear headings for each of the five main sections, and use subheadings for each sub-task where applicable."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture demonstrates a clear understanding of {t['language_area']} and its role in language processing, and how it relates to {t['musical_element']}",
            f"The neurolinguistic-musical interface provides a plausible mapping between linguistic features and {t['musical_element']}, addressing potential challenges",
            "The AI algorithm design incorporates principles from both neurolinguistics and music theory, ensuring musical coherence",
            "The example output demonstrates a creative and plausible translation of neural activity to music, with clear explanations",
            "The response explores diverse applications, thoughtful ethical considerations, and potential impacts of the technology on multiple fields",
            "The submission demonstrates comprehensive interdisciplinary knowledge and innovative problem-solving across neuroscience, linguistics, music theory, and AI"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
