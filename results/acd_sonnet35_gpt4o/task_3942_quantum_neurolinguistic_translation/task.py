import random
from typing import List, Optional

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_language": "English",
                "target_language": "Japanese",
                "linguistic_features": ["tense", "aspect"],
                "example_words": [
                    "walk (present)", "walked (past)",
                    "歩く(aruku, present)", "歩いた(aruita, past)",
                    "is walking (present progressive)", "has walked (present perfect)",
                    "歩いている(aruite iru, present progressive)", "歩いてしまった(aruite shimatta, present perfect)"
                ]
            },
            {
                "source_language": "Spanish",
                "target_language": "Mandarin",
                "linguistic_features": ["number", "classifier"],
                "example_words": [
                    "gato (singular)", "gatos (plural)",
                    "猫(māo, singular)", "猫们(māomen, plural)",
                    "un gato (a cat)", "una mesa (a table)",
                    "一只猫(yī zhī māo, a cat)", "一张桌子(yī zhāng zhuōzi, a table)"
                ]
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum circuit for translating the linguistic features of {' and '.join(t['linguistic_features'])} from {t['source_language']} to {t['target_language']} using principles of neurolinguistics. Use the provided example words as a basis for your design:
{', '.join(t['example_words'])}

Your response should include the following sections:

1. Quantum Circuit Design (250-300 words):
   a) Describe the overall structure of your quantum circuit for translating the specified linguistic features.
   b) Explain how you encode each linguistic feature into qubit states.
   c) Detail at least three quantum gates used and their purpose in the translation process.
   d) Include an ASCII diagram of your quantum circuit, showing at least 4 qubits and 3 quantum gates.

2. Neurolinguistic Integration (200-250 words):
   a) Explain which neurolinguistic principles you've incorporated into your quantum circuit design.
   b) Describe how your circuit mimics neural pathways involved in processing the specified linguistic features.
   c) Discuss how your approach accounts for differences in these features between {t['source_language']} and {t['target_language']}.

3. Translation Process (200-250 words):
   a) Outline the step-by-step process of translating the linguistic features using your quantum circuit.
   b) Explain how the circuit handles at least two of the provided example words.
   c) Discuss any challenges in generalizing this approach to other words or phrases not in the example set.

4. Advantages and Limitations (150-200 words):
   a) Analyze potential quantum advantages in translating these linguistic features.
   b) Discuss at least two limitations of your approach and possible ways to address them.

5. Real-world Application (100-150 words):
   a) Propose one potential real-world application of your quantum neurolinguistic translation system.
   b) Briefly discuss the societal impact and ethical considerations of implementing such a system.

Ensure your response demonstrates understanding of quantum computing, neurolinguistics, and translation concepts. Use appropriate technical terminology and provide clear explanations.

Include at least one equation using LaTeX notation to represent a key concept in your quantum circuit design.

Provide a pseudocode snippet (5-8 lines) illustrating a core quantum operation in your circuit, such as a custom gate for linguistic feature translation.

Format your response with clear headings for each section, numbered as above. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all 5 sections outlined in the instructions.",
            f"The quantum circuit design targets the translation of {' and '.join(t['linguistic_features'])} from {t['source_language']} to {t['target_language']}.",
            "An ASCII diagram of the quantum circuit is included, showing at least 4 qubits and 3 quantum gates.",
            "The design incorporates relevant neurolinguistic principles and explains their integration into the quantum circuit.",
            "The response includes at least one relevant equation using LaTeX notation.",
            "A pseudocode snippet (5-8 lines) illustrating a core quantum operation is provided.",
            "The explanation demonstrates how the circuit handles at least two specific example words from the provided set.",
            "The response proposes one potential real-world application and briefly discusses its societal and ethical implications.",
            "The total response is between 900-1150 words.",
            "The response demonstrates understanding of quantum computing, neurolinguistics, and translation concepts, while being innovative and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
