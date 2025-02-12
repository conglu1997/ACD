import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'sense': 'touch',
                'culture_pair': ('Japanese', 'Brazilian'),
                'concept': 'trust'
            },
            {
                'sense': 'taste',
                'culture_pair': ('Indian', 'Swedish'),
                'concept': 'success'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model capable of generating and interpreting metaphors based on sensory experiences across different cultures. Focus on the following parameters:

Sense: {t['sense']}
Culture Pair: {t['culture_pair'][0]} and {t['culture_pair'][1]}
Concept to Express: {t['concept']}

Your task:

1. Sensory-Linguistic Mapping (250-300 words):
   a) Explain how the given sense is typically experienced and described in each culture.
   b) Discuss any cultural differences in the perception or expression of this sense.
   c) Describe how your model would represent and process sensory information in relation to language.
   d) Provide at least one example of a sensory experience unique to each culture and how it might be linguistically expressed.

2. Metaphor Generation Mechanism (300-350 words):
   a) Design a mechanism for your model to generate metaphors using the given sense to express the specified concept.
   b) Explain how your model incorporates cultural knowledge to create culturally appropriate metaphors.
   c) Provide two example metaphors for each culture, explaining the generation process and cultural significance.
   d) Describe how your model ensures diversity in metaphor generation within each culture.

3. Cross-Cultural Interpretation (250-300 words):
   a) Describe how your model would interpret metaphors from one culture in the context of the other.
   b) Discuss potential challenges in cross-cultural metaphor interpretation and how your model addresses them.
   c) Provide an example of cross-cultural metaphor interpretation using your model, including:
      - An original metaphor from Culture A
      - Its interpretation in Culture B
      - An explanation of any meaning lost or gained in the interpretation

4. Model Architecture (200-250 words):
   a) Outline the key components of your language model's architecture.
   b) Explain how it integrates sensory, linguistic, and cultural information.
   c) Discuss any novel aspects of your model that differ from traditional language models.
   d) Provide a simple diagram or flowchart of your model's architecture (describe it textually).

5. Evaluation and Ethical Considerations (200-250 words):
   a) Propose a method to evaluate the effectiveness and cultural sensitivity of your model.
   b) Discuss potential biases or ethical concerns in cross-cultural metaphor generation and interpretation.
   c) Suggest guidelines for responsible development and use of such models.
   d) Describe a potential experiment to test your model's performance across multiple cultures and senses.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and cultural anthropology. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Include specific examples and scenarios throughout your response. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the relationship between sensory experiences and language across the specified cultures.",
            "The proposed model shows innovative approaches to generating and interpreting culturally-specific metaphors for the given sense and concept.",
            "The explanation of the model's architecture and mechanisms is clear, detailed, and scientifically plausible.",
            "The response addresses challenges in cross-cultural interpretation and proposes thoughtful solutions, with concrete examples.",
            "The evaluation method and ethical considerations are well-reasoned, comprehensive, and specific to the cross-cultural sensory metaphor task.",
            "The overall response showcases interdisciplinary knowledge and creative problem-solving in linguistics, cognitive science, and AI.",
            "The response includes the required number of examples and scenarios, demonstrating the model's capability in generating diverse, culturally-appropriate metaphors.",
            "The proposed experiment for testing the model's performance is well-designed and addresses multiple cultures and senses."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
