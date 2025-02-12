import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            {"lang1": "Mandarin", "lang2": "English"},
            {"lang1": "Spanish", "lang2": "Arabic"},
            {"lang1": "Hindi", "lang2": "Japanese"},
            {"lang1": "Swahili", "lang2": "Russian"}
        ]
        return {
            "1": random.choice(language_pairs),
            "2": random.choice(language_pairs)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and manipulates neural representations of language to facilitate seamless code-switching between {t['lang1']} and {t['lang2']}. Your response should include:

1. Neural Representation (250-300 words):
   a) Describe how your AI system models the neural representations of {t['lang1']} and {t['lang2']}.
   b) Explain how these representations capture linguistic features such as syntax, semantics, and phonology.
   c) Discuss how your model accounts for the differences and similarities between the two languages.

2. Code-Switching Mechanism (300-350 words):
   a) Outline the key components of your AI system that enable code-switching.
   b) Explain how your system identifies appropriate moments for code-switching in natural language.
   c) Describe the process by which your system transitions between neural representations of the two languages.
   d) Discuss how your system maintains coherence and meaning during code-switching.

3. Training and Data (200-250 words):
   a) Describe the type and amount of data your system would need for training.
   b) Explain your approach to data collection and preprocessing, considering the specific challenges of {t['lang1']} and {t['lang2']}.
   c) Discuss any potential biases in your training data and how you would address them.

4. Neurolinguistic Grounding (250-300 words):
   a) Explain how your AI system's architecture and functioning relate to current neuroscientific understanding of bilingual language processing.
   b) Discuss any novel hypotheses about bilingual cognition that your system might generate or test.
   c) Propose an experiment that could validate your system's neural model using human participants.

5. Applications and Implications (200-250 words):
   a) Suggest two novel applications of your system beyond simple translation or interpretation.
   b) Discuss the potential impact of your system on fields such as education, global communication, and cognitive science.
   c) Address any ethical considerations related to privacy, cultural preservation, and potential misuse of the technology.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your current system design.
   b) Propose two ways to extend or improve your system in future iterations.
   c) Suggest a research question that could be explored using your system as a foundation.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence.",
            "The AI system design is innovative, scientifically plausible, and addresses the specific challenges of code-switching between the given language pair.",
            "The neural representation model and code-switching mechanism are well-explained and grounded in current scientific knowledge.",
            "The response considers ethical implications and potential applications of the technology.",
            "The answer is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
