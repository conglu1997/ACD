import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        color_stimuli = [
            {'color': 'Red', 'wavelength': '620-750 nm'},
            {'color': 'Blue', 'wavelength': '450-495 nm'},
            {'color': 'Green', 'wavelength': '495-570 nm'},
            {'color': 'Yellow', 'wavelength': '570-590 nm'}
        ]
        musical_elements = [
            {'element': 'Pitch', 'description': 'The highness or lowness of a sound'},
            {'element': 'Rhythm', 'description': 'The pattern of regular or irregular pulses in music'},
            {'element': 'Harmony', 'description': 'The combination of simultaneously sounded musical notes'},
            {'element': 'Timbre', 'description': 'The character or quality of a musical sound'}
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'color_stimulus': random.choice(color_stimuli),
                'musical_element': random.choice(musical_elements)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system that translates neural activity associated with the perception of {t['color_stimulus']['color']} (wavelength: {t['color_stimulus']['wavelength']}) into musical compositions, focusing on the musical element of {t['musical_element']['element']} ({t['musical_element']['description']}). Your task has the following parts:

1. Neural Interface Design (250-300 words):
   a) Describe the key components of your BCI system for detecting color-related neural activity.
   b) Explain how your system isolates and interprets neural signals associated with {t['color_stimulus']['color']} perception.
   c) Discuss any novel technologies or techniques your system employs to enhance signal detection and processing.
   d) Address potential challenges in distinguishing color-specific neural activity from other visual processing.

2. Color-to-Music Translation Algorithm (250-300 words):
   a) Describe your algorithm for translating color-related neural signals into musical parameters, focusing on {t['musical_element']['element']}.
   b) Explain how your algorithm accounts for variations in neural responses to color across individuals.
   c) Discuss how your system maintains musical coherence and aesthetic quality in the generated compositions.
   d) Provide a simplified pseudocode or flowchart of your translation algorithm.

3. Neuroscientific Basis (200-250 words):
   a) Explain the neurological basis for your color-to-music translation, citing relevant research in color perception and synesthesia.
   b) Discuss how your system might affect or interact with existing neural pathways related to color perception and musical processing.
   c) Propose a hypothesis about how prolonged use of your system might influence a user's natural color perception or musical abilities.

4. Music Theory Integration (200-250 words):
   a) Describe how your system incorporates principles of music theory in its composition process.
   b) Explain how the properties of {t['color_stimulus']['color']} (e.g., wavelength, intensity) are mapped to specific aspects of {t['musical_element']['element']}.
   c) Discuss how your system ensures the generated music adheres to established musical conventions while remaining novel and color-inspired.

5. Practical Application and Experimentation (200-250 words):
   a) Propose an experiment to test the effectiveness and consistency of your color-to-music translation system.
   b) Describe how you would measure and evaluate the 'synesthetic accuracy' of the generated music.
   c) Suggest potential applications of your system in fields such as art therapy, music composition, or cognitive enhancement.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of artificially inducing synesthetic experiences.
   b) Address concerns about altering natural cognitive processes through prolonged use of the BCI system.
   c) Propose guidelines for responsible development and use of neural-based creative technologies.
   d) Suggest future research directions or expansions of your system, such as incorporating other sensory modalities.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Your total response should be between 1250-1550 words.

Format your response with clear headings for each section, as follows:

1. Neural Interface Design:
   [Your content here]

2. Color-to-Music Translation Algorithm:
   [Your content here]

3. Neuroscientific Basis:
   [Your content here]

4. Music Theory Integration:
   [Your content here]

5. Practical Application and Experimentation:
   [Your content here]

6. Ethical Considerations and Future Directions:
   [Your content here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Neural Interface Design effectively addresses the detection of neural activity related to {t['color_stimulus']['color']} perception.",
            f"The Color-to-Music Translation Algorithm clearly explains how {t['color_stimulus']['color']} perception is translated into {t['musical_element']['element']}.",
            "The Neuroscientific Basis section demonstrates a deep understanding of color perception and synesthesia research.",
            f"The Music Theory Integration effectively explains how {t['color_stimulus']['color']} properties are mapped to {t['musical_element']['element']}.",
            "The Practical Application and Experimentation section proposes a well-designed experiment to test the system's effectiveness.",
            "Ethical Considerations and Future Directions are thoughtfully addressed with relevant guidelines proposed.",
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence.",
            "The ideas presented are creative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
