import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Navajo",
                "family": "Na-Dené",
                "speakers": "170,000",
                "sample_phrase": "Yá'át'ééh",
                "meaning": "Hello"
            },
            {
                "name": "Aymara",
                "family": "Aymaran",
                "speakers": "1,700,000",
                "sample_phrase": "Kamisaki",
                "meaning": "How are you?"
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(languages)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic encryption system for the {t['name']} language (language family: {t['family']}, approximately {t['speakers']} speakers) and analyze its potential applications in secure communication and language preservation. Your task has the following components:

1. Encryption System Design (300-350 words):
   a) Describe the key features of your quantum-inspired linguistic encryption system.
   b) Explain how your system incorporates principles from quantum computing (e.g., superposition, entanglement) and linguistics.
   c) Detail how your system encodes and encrypts linguistic elements (e.g., phonemes, morphemes, syntax).
   d) Provide an example of how the phrase "{t['sample_phrase']}" (meaning: "{t['meaning']}") would be encrypted using your system.

2. Quantum-Linguistic Integration (250-300 words):
   a) Analyze how quantum principles enhance the security and efficiency of your linguistic encryption.
   b) Discuss any challenges in reconciling quantum concepts with linguistic structures.
   c) Explain how your system accounts for unique features of the {t['name']} language.

3. Secure Communication Applications (200-250 words):
   a) Propose two novel applications of your encryption system for secure communication.
   b) Explain how these applications might benefit the {t['name']} speaking community.
   c) Discuss potential advantages over classical encryption methods.

4. Language Preservation Aspects (200-250 words):
   a) Analyze how your system could contribute to the preservation of the {t['name']} language.
   b) Discuss how quantum-inspired encryption might protect against linguistic data loss or corruption.
   c) Propose a method for using your system in documenting and archiving the language.

5. Ethical and Societal Implications (200-250 words):
   a) Identify potential ethical concerns related to the development and use of your encryption system.
   b) Discuss the societal impact of introducing quantum-linguistic encryption to the {t['name']} community.
   c) Propose guidelines for the responsible development and use of such systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum-linguistic encryption system.
   b) Propose a research question that bridges your system with another scientific field not mentioned in the task.
   c) Discuss how this interdisciplinary approach might lead to new insights in language technology or quantum computing.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and cryptography. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words. Include a brief summary (100-150 words) at the end, highlighting the key innovations and potential impacts of your quantum-linguistic encryption system."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The encryption system design must clearly incorporate principles from both quantum computing and linguistics, with a specific example using the provided phrase.",
            "The response should demonstrate a deep understanding of the challenges in integrating quantum concepts with linguistic structures, particularly for the specified language.",
            "The proposed applications for secure communication should be innovative, feasible, and clearly beneficial to the specified language community.",
            "The language preservation aspects should show a thoughtful consideration of how the technology could protect and document the language, with specific methods proposed.",
            "The ethical and societal implications should be thoroughly analyzed, showing an understanding of potential impacts on the language community and proposing responsible guidelines.",
            "The future research directions should demonstrate creative thinking about potential interdisciplinary connections and advancements, with a clear research question proposed.",
            "The overall response should exhibit high-level interdisciplinary thinking and creativity in approaching the complex problem of quantum-linguistic encryption, while maintaining scientific plausibility.",
            "The response should follow the specified format, including all required sections and a summary, and fall within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
