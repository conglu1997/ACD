import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_areas = [
            {
                "name": "Broca's area",
                "function": "Speech production and language processing"
            },
            {
                "name": "Wernicke's area",
                "function": "Language comprehension and semantic processing"
            }
        ]
        linguistic_aspects = [
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Phonology"
        ]
        return {
            "1": {
                "brain_area": random.choice(brain_areas),
                "linguistic_aspect": random.choice(linguistic_aspects)
            },
            "2": {
                "brain_area": random.choice(brain_areas),
                "linguistic_aspect": random.choice(linguistic_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that decodes neural activity from {t['brain_area']['name']} (primarily responsible for {t['brain_area']['function']}) and generates coherent, contextually appropriate language output, with a focus on the linguistic aspect of {t['linguistic_aspect']}. Your task has the following components:

1. Neural Decoding Architecture (250-300 words):
   a) Describe the key components of your neural decoding system.
   b) Explain how it processes and interprets neural signals from the specified brain area.
   c) Discuss any novel techniques or algorithms you incorporate for improved accuracy.
   d) Address how your system handles the variability in neural activity across individuals.

2. Language Generation Model (200-250 words):
   a) Detail the architecture of your language generation model.
   b) Explain how it integrates the decoded neural information to produce language output.
   c) Describe how your model specifically addresses the given linguistic aspect.
   d) Discuss any mechanisms for ensuring coherence and contextual appropriateness.

3. Integration and Optimization (200-250 words):
   a) Explain how the neural decoding and language generation components are integrated.
   b) Describe any feedback mechanisms between the two systems.
   c) Discuss how your system optimizes for real-time performance.
   d) Address potential challenges in maintaining the connection between neural activity and generated language.

4. Evaluation and Testing (150-200 words):
   a) Propose a method for evaluating the accuracy and naturalness of the generated language.
   b) Describe an experiment to test your system's performance across different linguistic contexts.
   c) Discuss how you would validate that the output truly reflects the individual's intended communication.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss the ethical implications of a system that can 'read' and generate thoughts.
   b) Address potential privacy concerns and propose safeguards.
   c) Explain the limitations of your system and any potential risks of misinterpretation.

6. Future Developments and Applications (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Propose an innovative application of this technology beyond basic communication.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word limits provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and AI principles.",
            "The proposed system integrates neural decoding and language generation in a novel and plausible way.",
            "The design specifically addresses the given brain area and linguistic aspect.",
            "The evaluation method and experiment design are well-thought-out and appropriate.",
            "Ethical considerations and limitations are thoroughly discussed.",
            "The proposed future developments and applications are innovative and relevant.",
            "The response is well-structured, clear, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
