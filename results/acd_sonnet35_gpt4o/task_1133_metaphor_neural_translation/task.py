import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "metaphor_domain": "Time concepts",
                "example_metaphor": "Time is a flowing river",
                "cultural_context": "In Japanese culture, time is often viewed as a continuous flow, while in Brazilian culture, time is more flexible and event-based."
            },
            "2": {
                "source_culture": "Inuit",
                "target_culture": "Maasai",
                "metaphor_domain": "Emotional states",
                "example_metaphor": "Anger is fire in the belly",
                "cultural_context": "Inuit culture emphasizes emotional control in harsh environments, while Maasai culture values expressive displays of emotion, especially in warrior traditions."
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture for translating metaphors from {t['source_culture']} culture to {t['target_culture']} culture, focusing on the domain of {t['metaphor_domain']}. Your task is to create a system that can understand and translate metaphors while preserving their cultural significance and emotional impact. Consider the example metaphor: "{t['example_metaphor']}" and the following cultural context: {t['cultural_context']}

Your response should include:

1. Conceptual Framework (200-250 words):
   a) Explain the key challenges in cross-cultural metaphor translation.
   b) Discuss how cognitive linguistics theories can inform your approach.
   c) Describe how you will incorporate cultural context into your model.

2. Neural Network Architecture (250-300 words):
   a) Design a detailed neural network architecture for this task.
   b) Explain each component of your architecture and its function.
   c) Describe how your architecture addresses the specific challenges of metaphor translation.
   d) Include a diagram of your architecture (using ASCII art or a clear textual description).

3. Data Representation (150-200 words):
   a) Explain how you will represent metaphors, cultural context, and linguistic features as inputs to your network.
   b) Describe any pre-processing steps required for your input data.
   c) Discuss how your data representation captures the nuances of metaphorical language.

4. Training Process (150-200 words):
   a) Outline the training process for your neural network.
   b) Describe the type and source of data you would use for training.
   c) Explain any specific techniques you would employ to handle the complexities of metaphor translation.

5. Evaluation Metrics (100-150 words):
   a) Propose at least three specific metrics to evaluate the performance of your metaphor translation system.
   b) Explain how these metrics capture both linguistic accuracy and cultural appropriateness.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for cross-cultural metaphor translation.
   b) Address issues such as cultural appropriation, misrepresentation, and the role of human expertise.

7. Limitations and Future Work (100-150 words):
   a) Identify at least two limitations of your proposed system.
   b) Suggest directions for future research to improve cross-cultural metaphor translation.

Ensure your response demonstrates a deep understanding of neural network architectures, cognitive linguistics, and cultural studies. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Conceptual Framework:') followed by your response for that section. Adhere strictly to the word limits provided for each section.

Your total response should be between 1050-1400 words, not including the architecture diagram. The architecture diagram should be included as a separate, clearly labeled section after the main text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neural network architectures, cognitive linguistics, and cultural studies, using appropriate technical terminology.",
            "The proposed neural network architecture is innovative, detailed, and specifically designed for cross-cultural metaphor translation, with a clear explanation of each component's function.",
            "The approach effectively incorporates cognitive linguistics theories and the provided cultural context in a meaningful way.",
            "The data representation and training process are well-explained, appropriate for the task, and address the complexities of metaphor translation.",
            "At least three specific evaluation metrics are proposed, capturing both linguistic accuracy and cultural appropriateness.",
            "Ethical considerations are thoroughly addressed, including potential issues of cultural appropriation, misrepresentation, and the role of human expertise.",
            "The response includes a clear, labeled diagram or description of the neural network architecture as a separate section.",
            "At least two limitations of the proposed system are identified, and specific future research directions are suggested.",
            "The response adheres to the specified format, including correct numbering and headings for each section, and stays within the given word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
