import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "source_language": "Mandarin Chinese",
                "target_language": "English",
                "ethical_concern": "preserving cultural nuances in idiomatic expressions",
                "quantum_principle": "quantum superposition",
                "example_phrase": "马马虎虎 (mǎmǎhūhū)"
            },
            "2": {
                "source_language": "Arabic",
                "target_language": "Spanish",
                "ethical_concern": "maintaining gender neutrality across different gender systems",
                "quantum_principle": "quantum entanglement",
                "example_phrase": "على راسي (ala rasi)"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum circuit for word vector similarity analysis in a cross-cultural language translation system. Your circuit should analyze word vectors from {t['source_language']} to aid translation to {t['target_language']}, focusing on the ethical concern of {t['ethical_concern']}. Incorporate the quantum principle of {t['quantum_principle']} in your design.

Background:
- Quantum circuits use quantum gates to manipulate qubits, which can exist in superposition states.
- Word vectors are numerical representations of words in a high-dimensional space, where similar words have similar vectors.
- {t['quantum_principle']} allows quantum systems to exist in multiple states simultaneously, enabling parallel processing of information.

Example: In quantum computing, we could represent a word's meaning using superposition. For instance, the word "bank" could be represented as a superposition of "financial institution" and "river edge" states.

Your response should include the following sections:

1. Circuit Design (300-350 words):
   a) Describe the overall structure of your quantum circuit for word vector similarity analysis.
   b) Explain how it incorporates {t['quantum_principle']} into its design.
   c) Detail the following components of your circuit:
      - Input encoding: How word vectors are encoded into quantum states.
      - Similarity measurement: How the circuit computes similarity between word vectors.
      - Output decoding: How the quantum state is converted back to classical information.
   d) Provide a visual representation of your circuit (use ASCII art or Unicode characters).
   e) Include a simple pseudocode or algorithm sketch for a key part of your circuit.

2. Quantum-Semantic Integration (200-250 words):
   a) Explain how your circuit represents and processes word vector information.
   b) Describe how it measures semantic similarity between words or phrases.
   c) Provide an example of how your circuit would process the phrase: "{t['example_phrase']}"

3. Ethical Considerations (200-250 words):
   a) Analyze how your circuit addresses the ethical concern of {t['ethical_concern']}.
   b) Discuss potential unintended consequences and propose mitigation strategies.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum circuit to classical word vector similarity methods.
   b) Discuss potential advantages and limitations of your approach.

5. Implementation Challenges (150-200 words):
   a) Discuss challenges in implementing your circuit on current quantum hardware.
   b) Propose strategies to overcome these challenges.

Ensure your response demonstrates a deep understanding of quantum computing principles, word vector representations, and ethical reasoning. Be creative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a quantum circuit for word vector similarity analysis for {t['source_language']} to {t['target_language']} translation.",
            f"The circuit design must incorporate {t['quantum_principle']} and address the ethical concern of {t['ethical_concern']}.",
            "The response must include all five required sections: Circuit Design, Quantum-Semantic Integration, Ethical Considerations, Comparative Analysis, and Implementation Challenges.",
            "The circuit design must describe input encoding, similarity measurement, and output decoding components.",
            "The circuit design must include a visual representation and a simple pseudocode or algorithm sketch.",
            "The response must demonstrate understanding of quantum computing principles and word vector representations.",
            f"The response must provide an example of how the circuit would process the phrase: \"{t['example_phrase']}\".",
            "The ethical implications must be discussed with proposed mitigation strategies for potential issues.",
            "The comparative analysis must offer insights on advantages and limitations compared to classical methods.",
            "The implementation challenges section must discuss realistic issues with current quantum hardware and propose plausible solutions.",
            "The total response should be between 1000-1250 words, with each section adhering to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
