import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "neural_signal": "alpha waves",
                "emotional_state": "anxiety",
                "musical_element": "rhythm"
            },
            {
                "neural_signal": "beta waves",
                "emotional_state": "depression",
                "musical_element": "harmony"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates personalized music therapy based on real-time neural feedback, focusing on {t['neural_signal']} to address {t['emotional_state']}, with emphasis on manipulating {t['musical_element']}. Your response should include:

1. Neurofeedback Integration (250-300 words):
   a) Describe how your AI system interprets {t['neural_signal']} in real-time.
   b) Explain the correlation between {t['neural_signal']} and {t['emotional_state']}.
   c) Detail how your system translates neural signals into musical parameters.

2. AI Music Generation (250-300 words):
   a) Outline the AI architecture for generating adaptive music therapy.
   b) Explain how your system manipulates {t['musical_element']} based on neural feedback.
   c) Describe any novel algorithms or techniques used in your music generation process.

3. Music Theory Application (200-250 words):
   a) Discuss how principles of music theory inform your system's composition process.
   b) Explain how manipulating {t['musical_element']} can influence {t['emotional_state']}.
   c) Provide an example of a musical pattern your system might generate and its intended effect.

4. Therapeutic Efficacy (200-250 words):
   a) Propose methods to evaluate the therapeutic effectiveness of your AI-generated music.
   b) Describe how your system adapts to individual patient responses over time.
   c) Discuss potential limitations of your approach and how you'd address them.

5. Ethical Considerations (150-200 words):
   a) Analyze potential ethical issues in using AI for music therapy.
   b) Discuss privacy concerns related to collecting and using neural data.
   c) Propose guidelines for responsible development and use of your system.

6. Future Implications (150-200 words):
   a) Discuss how your system might contribute to our understanding of music cognition and emotional regulation.
   b) Propose two potential applications of your system beyond mental health therapy.
   c) Suggest a research question that could further explore the intersection of neuroscience, AI, and music therapy.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and AI. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and AI, integrating these fields effectively.",
            "The AI system design is innovative, plausible, and addresses the specific neural signal, emotional state, and musical element given in the task.",
            "The explanation of how neural feedback is interpreted and translated into musical parameters is clear and scientifically grounded.",
            "The response includes a thoughtful discussion of ethical considerations and proposes responsible guidelines for system use.",
            "The answer provides a comprehensive analysis of the system's potential therapeutic efficacy and limitations.",
            "The response explores future implications and potential applications of the technology beyond its primary use case.",
            "The submission is well-structured, following the required format and word count, and addresses all specified sections comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
