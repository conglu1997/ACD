import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "English"),
            ("Arabic", "Spanish"),
            ("Russian", "Japanese"),
            ("Hindi", "French")
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Inferior frontal gyrus"
        ]
        return {
            "1": {
                "languages": random.choice(language_pairs),
                "focus_region": random.choice(brain_regions)
            },
            "2": {
                "languages": random.choice(language_pairs),
                "focus_region": random.choice(brain_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) for real-time language translation from {t['languages'][0]} to {t['languages'][1]}, with a particular focus on neural activity in {t['focus_region']}. Your response should include:

1. Neurolinguistic Foundation (200-250 words):
   a) Explain the role of {t['focus_region']} in language processing.
   b) Describe how neural activity patterns in this region might differ between {t['languages'][0]} and {t['languages'][1]} speakers.
   c) Discuss any challenges specific to this language pair in terms of neural representation.

2. BCI Design (250-300 words):
   a) Propose a detailed design for your BCI, including its components and how they interact.
   b) Explain how your BCI would capture and interpret neural signals from {t['focus_region']}.
   c) Describe the signal processing and machine learning techniques your BCI would use to translate between the two languages.
   d) Address how your design handles the specific challenges of this language pair.

3. Implementation and Ethical Considerations (200-250 words):
   a) Discuss potential methods for training the BCI system.
   b) Address challenges in implementing this technology, including issues of invasiveness and long-term use.
   c) Analyze ethical implications, including privacy concerns and potential misuse.

4. Speculative Applications (150-200 words):
   a) Propose two novel applications of your BCI beyond simple translation.
   b) Explain how these applications could impact fields such as education, cross-cultural communication, or cognitive enhancement.

5. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research that could enhance your BCI design.
   b) Explain how these research directions could address current limitations in neurolinguistics or BCI technology.

Ensure your response demonstrates a deep understanding of neurolinguistics, BCI technology, and the specific challenges of the given language pair. Be creative and innovative in your design while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the role of {t['focus_region']} in language processing and how it relates to {t['languages'][0]} and {t['languages'][1]}.",
            "The BCI design is innovative, detailed, and scientifically plausible.",
            "The implementation challenges and ethical considerations are thoroughly addressed.",
            "The speculative applications are creative and well-reasoned.",
            "The proposed future research directions are relevant and have the potential to advance the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
