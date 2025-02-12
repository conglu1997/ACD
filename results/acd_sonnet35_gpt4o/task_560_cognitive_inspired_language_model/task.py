import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_theory': 'Connectionist models',
                'language_aspect': 'Morphological processing',
                'target_language': 'English',
                'example_phenomenon': 'Past tense formation (e.g., regular vs. irregular verbs)'
            },
            {
                'cognitive_theory': 'Usage-based theory',
                'language_aspect': 'Syntax acquisition',
                'target_language': 'Mandarin Chinese',
                'example_phenomenon': 'Word order in complex sentences'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design, implement, and analyze a novel language model based on cognitive theories of language acquisition and processing. Your task focuses on {t['cognitive_theory']} applied to {t['language_aspect']} in {t['target_language']}, with a specific focus on {t['example_phenomenon']}. Provide your response in the following structured format:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['cognitive_theory']} and how they relate to language acquisition and processing.
   b) Describe how these principles can be applied to model {t['language_aspect']} in {t['target_language']}, particularly for {t['example_phenomenon']}.
   c) Discuss any specific challenges or considerations for this combination of theory, language aspect, and target language.

2. Model Design (300-350 words):
   a) Propose a detailed architecture for your cognitive-inspired language model.
   b) Explain how each component of your model relates to the principles of {t['cognitive_theory']}.
   c) Describe the input and output representations of your model, using {t['example_phenomenon']} as an example.
   d) Outline the learning algorithm or process your model would use.
   e) Include a high-level pseudocode or diagram of your model's architecture and processing flow.

3. Implementation and Output (200-250 words):
   a) Describe how you would implement your model computationally.
   b) Explain any simplifications or assumptions made in the implementation.
   c) Provide a concrete example of input data for {t['example_phenomenon']} and the expected output from your model, explaining how it demonstrates the model's cognitive-inspired nature.

4. Evaluation and Analysis (250-300 words):
   a) Propose specific methods to evaluate your model's performance in modeling {t['language_aspect']} in {t['target_language']}, focusing on {t['example_phenomenon']}.
   b) Compare your model's expected behavior to human language acquisition and processing patterns, using {t['example_phenomenon']} as a case study.
   c) Discuss potential insights your model could provide about cognitive processes in language learning and use.
   d) Analyze limitations of your model and propose future improvements.

5. Broader Implications (150-200 words):
   a) Discuss how your cognitive-inspired model could influence the development of AI language models.
   b) Explore potential applications of your model in fields such as language education, speech therapy, or natural language processing.
   c) Consider ethical implications of using cognitive-inspired models in AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your model design while maintaining scientific plausibility and grounding in established theories. Use appropriate technical terminology and provide clear explanations.

Format your response with clear headings for each section, and number your paragraphs within each section for easy reference. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['cognitive_theory']} and its application to {t['language_aspect']} in {t['target_language']}, with a clear focus on {t['example_phenomenon']}.",
            "The proposed model design is innovative, well-explained, and grounded in the chosen cognitive theory, with clear connections to the example phenomenon.",
            "The implementation description includes a concrete example of input and output for the specified phenomenon, effectively illustrating the model's cognitive-inspired nature.",
            "The evaluation and analysis section provides specific methods for assessing the model and insightful comparisons between the model and human language processing, using the example phenomenon as a case study.",
            "The discussion of broader implications shows a nuanced understanding of the potential impacts and applications of cognitive-inspired AI models in relevant fields."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
