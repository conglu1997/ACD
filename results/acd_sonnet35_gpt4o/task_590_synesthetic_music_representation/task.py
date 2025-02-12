import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_element": "harmony",
                "visual_domain": "color",
                "cognitive_aspect": "emotional valence"
            },
            {
                "musical_element": "rhythm",
                "visual_domain": "shape",
                "cognitive_aspect": "attention"
            },
            {
                "musical_element": "melody",
                "visual_domain": "motion",
                "cognitive_aspect": "memory"
            },
            {
                "musical_element": "timbre",
                "visual_domain": "texture",
                "cognitive_aspect": "sensory integration"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Synesthesia is a perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in another sensory or cognitive pathway. In this task, you will design a synesthetic system for representing {t['musical_element']} visually using {t['visual_domain']}, taking into account the cognitive aspect of {t['cognitive_aspect']}. Then, use your system to analyze an existing musical piece and generate a novel composition. Your task has the following parts:

1. Synesthetic System Design (200-300 words):
   a) Explain how your system represents {t['musical_element']} using {t['visual_domain']}.
   b) Describe how your system incorporates the cognitive aspect of {t['cognitive_aspect']}.
   c) Provide examples of how at least three specific musical features are visually represented.
   d) Discuss how your system might enhance or alter music perception and cognition.

2. Musical Analysis (200-250 words):
   a) Choose a well-known musical piece and analyze its {t['musical_element']} using your synesthetic system.
   b) Provide a visual representation of your analysis (use ASCII art or a detailed text description).
      If using ASCII art, ensure it is at least 10 lines long and uses a variety of characters.
      If using a text description, provide a detailed, step-by-step explanation of the visual elements.
   c) Explain how your visual representation reveals patterns or structures in the music that might not be immediately apparent through traditional notation or auditory perception.

3. Novel Composition Generation (200-250 words):
   a) Use your synesthetic system to generate a novel musical composition.
   b) Describe the composition in terms of both its musical features and its visual representation.
   c) Explain how the cognitive aspect of {t['cognitive_aspect']} influenced your compositional choices.

4. Cognitive and Perceptual Implications (150-200 words):
   a) Discuss how your synesthetic system might affect music learning and memory.
   b) Explain potential benefits and drawbacks of using this system for music education or music therapy.
   c) Propose an experiment to test the cognitive effects of your synesthetic music representation system.

5. AI and Music Generation (200-250 words):
   a) Describe how an AI model could be trained to use your synesthetic system for music analysis and generation.
   b) Discuss potential challenges in implementing this system in AI and propose solutions.
   c) Explain how AI-generated music using this system might differ from traditional AI music generation methods.
   d) Discuss potential ethical implications of using AI for music generation with this system, including issues of authorship, creativity, and cultural appropriation.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and AI. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 950-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive science, and AI",
            f"The synesthetic system effectively represents {t['musical_element']} using {t['visual_domain']}",
            f"The system incorporates the cognitive aspect of {t['cognitive_aspect']} in a meaningful way",
            "The musical analysis reveals patterns or structures not immediately apparent in traditional notation",
            "The visual representation is detailed and follows the specified guidelines",
            "The novel composition generation demonstrates creative use of the synesthetic system",
            "The response discusses cognitive and perceptual implications of the system with scientific plausibility",
            "The AI implementation proposal is well-reasoned and addresses potential challenges",
            "The response includes a thoughtful discussion of ethical implications"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
