import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "Superposition",
                "linguistic_phenomenon": "Lexical ambiguity",
                "languages": ["English", "Mandarin Chinese"],
                "example_word": "bank",
                "example_sentence": "I went to the bank."
            },
            {
                "quantum_concept": "Entanglement",
                "linguistic_phenomenon": "Semantic coherence",
                "languages": ["Arabic", "Spanish"],
                "example_word": "سلام",
                "example_sentence": "أَلْقَى السَّلَامَ"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model for language processing that incorporates the quantum mechanical concept of {t['quantum_concept']} to explain the linguistic phenomenon of {t['linguistic_phenomenon']}. Then, apply this model to analyze and generate text in {t['languages'][0]} and {t['languages'][1]}. Your response should include:

1. Quantum Cognitive Model (300-350 words):
   a) Explain how {t['quantum_concept']} can be applied to model {t['linguistic_phenomenon']}.
   b) Describe the key components and mechanisms of your quantum cognitive language model.
   c) Discuss how your model differs from classical approaches to language processing.
   d) Include a mathematical formulation of your model using appropriate quantum notation (e.g., Dirac notation, density matrices). Explain each component of your equations.

2. Linguistic Analysis (250-300 words):
   a) Apply your model to analyze {t['linguistic_phenomenon']} in {t['languages'][0]} and {t['languages'][1]}.
   b) Compare and contrast how your model explains this phenomenon in both languages.
   c) Provide specific examples from each language to illustrate your analysis. Consider the example word "{t['example_word']}" and sentence "{t['example_sentence']}" in your analysis.

3. Text Generation (200-250 words):
   a) Describe how your model would generate text exhibiting {t['linguistic_phenomenon']} in both languages.
   b) Provide a short example of generated text in each language, explaining how it demonstrates the phenomenon.
   c) Discuss any challenges in adapting your model for text generation across different languages.

4. Empirical Predictions (200-250 words):
   a) Propose testable predictions derived from your quantum cognitive language model.
   b) Describe an experiment to validate these predictions, including methodology and expected results.
   c) Discuss how the results would support or challenge your model compared to classical approaches.

5. Implications and Future Directions (200-250 words):
   a) Analyze the implications of your model for our understanding of language processing and cognition.
   b) Discuss potential applications in natural language processing, machine translation, or cognitive science.
   c) Propose future research directions to extend or refine your quantum cognitive language model.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of applying quantum-inspired models to human language and cognition.
   b) Address potential misuse or misinterpretation of your model's outputs.
   c) Propose guidelines for responsible development and application of quantum cognitive language models.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and linguistics. Be innovative in your approach while maintaining scientific rigor. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed quantum cognitive model incorporating {t['quantum_concept']} to explain {t['linguistic_phenomenon']}",
            f"The model is applied to analyze and generate text in both {t['languages'][0]} and {t['languages'][1]}",
            "The response demonstrates deep understanding of quantum mechanics, cognitive science, and linguistics",
            "The proposed model and analysis are innovative while maintaining scientific rigor",
            "Ethical considerations are thoughtfully addressed",
            f"The example word '{t['example_word']}' and sentence '{t['example_sentence']}' are incorporated into the analysis"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
