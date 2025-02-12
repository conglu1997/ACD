import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "brain_region": "Broca's area",
                "language": "Sumerian"
            },
            {
                "quantum_principle": "entanglement",
                "brain_region": "Wernicke's area",
                "language": "Linear A"
            },
            {
                "quantum_principle": "tunneling",
                "brain_region": "angular gyrus",
                "language": "Etruscan"
            },
            {
                "quantum_principle": "quantum coherence",
                "brain_region": "inferior frontal gyrus",
                "language": "Ainu"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired model of language processing in the brain, then use it to analyze and generate text in an extinct or endangered language. This task assesses the ability to integrate advanced concepts from quantum physics, neuroscience, and linguistics to push the boundaries of our understanding of language and cognition.

1. Quantum-Cognitive Model (300-350 words):
   a) Describe a model that integrates the quantum principle of {t['quantum_principle']} with neural processes in the {t['brain_region']}.
   b) Explain how this integration might enhance our understanding of language processing.
   c) Propose a novel mechanism by which quantum effects could influence neural computation in language tasks.
   d) Include a diagram or detailed description of your model's architecture.

2. Linguistic Application (250-300 words):
   a) Apply your model to analyze the structure and features of the {t['language']} language.
   b) Explain how your quantum-cognitive approach reveals new insights about this language.
   c) Discuss any challenges in applying your model to an extinct or endangered language.

3. Text Generation (250-300 words):
   a) Use your model to generate a short text (2-3 sentences) in {t['language']}.
   b) Provide a translation and explanation of the generated text.
   c) Describe how the quantum aspects of your model influenced the text generation process.
   d) Explain how you ensured the generated text is consistent with known features of the language.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-cognitive model to traditional neurolinguistic models.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose an experiment to test the validity of your model against classical approaches.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of your model for our understanding of cognition and language.
   b) Propose two potential applications of your model in fields such as language preservation or AI-assisted translation.
   c) Suggest future research directions to further develop and validate your quantum-cognitive linguistic model.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Within each section, use lettered subheadings (a, b, c, etc.) to organize your thoughts. Your total response should be between 1200-1450 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum principle of {t['quantum_principle']} and its potential application to neural processes in the {t['brain_region']}.",
            f"The model is applied effectively to analyze and generate text in the {t['language']} language, with clear explanations of the process and outcomes.",
            f"The generated text in {t['language']} is consistent with known features of the language and not simply made up or nonsensical.",
            "The comparative analysis and proposed experiment show a thorough understanding of both quantum-inspired and traditional neurolinguistic approaches.",
            "The implications and future directions discussed are innovative and scientifically plausible.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology from quantum physics, neuroscience, and linguistics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
