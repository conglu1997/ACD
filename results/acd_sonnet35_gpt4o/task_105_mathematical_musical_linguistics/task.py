import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "evidentiality",
                "description": "the source of information (direct experience, inference, or hearsay)"
            },
            {
                "feature": "clusivity",
                "description": "distinction between inclusive and exclusive first-person plural pronouns"
            }
        ]
        return {
            "1": random.choice(linguistic_features),
            "2": random.choice(linguistic_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical language based on mathematical principles and use it to encode the linguistic feature of {t['feature']} ({t['description']}). Your task has the following parts:

1. Musical Language Design (4-5 sentences):
   - Describe a system for creating 'musical words' using at least two mathematical principles (e.g., prime numbers, Fibonacci sequence, golden ratio, modular arithmetic).
   - Explain how your system incorporates at least three musical elements (e.g., pitch, rhythm, harmony, timbre, dynamics) to create meaning.
   - Discuss how your system can represent different 'parts of speech' or grammatical functions.

2. Encoding Linguistic Feature (3-4 sentences):
   - Explain how your musical language encodes the linguistic feature of {t['feature']} ({t['description']}).
   - Provide specific examples of how different aspects of this feature would be represented in your musical language.

3. Example 'Sentence' (2-3 sentences):
   - Create a complex 'sentence' in your musical language that demonstrates the linguistic feature and includes at least three 'words'.
   - Describe the sentence using musical notation or a clear textual representation of the musical elements.
   - Provide an English translation of your musical sentence and explain how each part corresponds to the musical representation.

4. Mathematical Analysis (3-4 sentences):
   - Explain the mathematical principles underlying your musical language, including any formulas or algorithms used.
   - Discuss how these principles contribute to the language's ability to encode linguistic information.
   - Provide an example of how changing a mathematical parameter would affect the meaning in your language.

5. Potential Applications (3-4 sentences):
   - Propose an innovative application of your musical language in fields such as cryptography, data compression, cognitive science, or artificial intelligence.
   - Explain how the mathematical and linguistic properties of your system could be advantageous in this application.
   - Describe a potential experiment to test the effectiveness of your system in this application.

6. Limitations and Extensions (2-3 sentences):
   - Discuss two limitations of your musical language system.
   - Propose ways to extend or modify your system to overcome these limitations.

7. Cross-linguistic Implications (2-3 sentences):
   - Discuss how your musical language might influence or be influenced by existing human languages.
   - Speculate on potential cognitive effects of using such a language for communication.

Ensure your response is creative, mathematically sound, and linguistically plausible. Demonstrate a deep understanding of the interconnections between music, mathematics, and linguistics throughout your answer. Organize your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The musical language design incorporates at least two mathematical principles and at least three musical elements",
            f"The system effectively encodes the linguistic feature of {t['feature']} ({t['description']})",
            "A complex example 'sentence' with at least three 'words' is provided with musical notation or clear representation and English translation",
            "The mathematical analysis explains the principles underlying the musical language and includes an example of parameter changes",
            "A potential application of the musical language is proposed with an experimental design",
            "Two limitations of the system are discussed with proposed extensions",
            "Cross-linguistic implications and potential cognitive effects are discussed",
            "The response demonstrates creativity and a deep understanding of music, mathematics, and linguistics",
            "The response is well-organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
