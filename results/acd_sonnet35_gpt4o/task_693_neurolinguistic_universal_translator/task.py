import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "source_language": "Human (English)",
                "target_language": "Dolphin echolocation patterns",
                "context": "Marine biology research"
            },
            {
                "source_language": "Alien mathematical symbols",
                "target_language": "Human (Mandarin Chinese)",
                "context": "First contact scenario"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical universal translation system based on neurolinguistic principles, capable of real-time translation between {t['source_language']} and {t['target_language']} in the context of {t['context']}. Your response should include the following sections:

1. System Architecture (200-250 words):
   a) Describe the key components of your universal translator.
   b) Explain how it integrates neurolinguistic principles.
   c) Discuss any novel technologies or theoretical concepts it employs.

2. Translation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system would translate between the given languages.
   b) Address any unique challenges posed by the specific language pair and context.
   c) Explain how your system handles non-verbal or non-human communication elements.

3. Neurolinguistic Basis (150-200 words):
   a) Discuss the neurolinguistic theories or models your system is based on.
   b) Explain how these principles are implemented in your translation process.
   c) Describe any assumptions made about the neural basis of language across species or forms of communication.

4. Cultural and Ethical Considerations (150-200 words):
   a) Analyze potential cultural implications of using such a universal translator.
   b) Discuss ethical concerns related to privacy, consent, and potential misuse.
   c) Propose guidelines for responsible development and use of this technology.

5. Limitations and Future Improvements (100-150 words):
   a) Identify current limitations of your proposed system.
   b) Suggest potential areas for future research and development.

6. Interdisciplinary Implications (100-150 words):
   a) Discuss how your universal translator might impact fields such as linguistics, neuroscience, and artificial intelligence.
   b) Propose novel research questions that arise from the development of this technology.

Ensure your response demonstrates a deep understanding of neurolinguistics, translation technologies, and the specific challenges posed by the given language pair and context. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed system architecture that integrates neurolinguistic principles for translating between {t['source_language']} and {t['target_language']}",
            f"The translation process is clearly explained, addressing the unique challenges of the {t['context']} scenario",
            "The neurolinguistic basis of the system is well-explained and scientifically plausible",
            "Cultural and ethical considerations are thoroughly discussed with specific examples",
            "Limitations and future improvements are identified and explained",
            "Interdisciplinary implications are discussed with novel research questions proposed",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of neurolinguistics, translation technologies, and artificial intelligence"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
