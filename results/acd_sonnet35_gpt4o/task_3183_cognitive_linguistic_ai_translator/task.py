import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_linguistic_phenomena = [
            ('conceptual blending', 'the process by which elements from different mental spaces are combined to create new meaning'),
            ('embodied cognition', 'the theory that many features of cognition are shaped by aspects of the body'),
            ('linguistic relativity', 'the idea that the structure of a language affects its speakers\' worldview or cognition'),
            ('metaphorical mapping', 'the systematic set of correspondences between conceptual domains'),
            ('construction grammar', 'the theory that patterns of form and meaning are represented as constructions')
        ]
        nlp_tasks = [
            ('sentiment analysis', 'determining the emotional tone behind a series of words'),
            ('machine translation', 'automatically converting text from one language to another'),
            ('text summarization', 'creating a concise and coherent summary of a longer text'),
            ('named entity recognition', 'identifying and classifying named entities in text into predefined categories'),
            ('question answering', 'automatically answering questions posed in natural language')
        ]
        tasks = [
            {
                'cognitive_linguistic_phenomena': random.sample(cognitive_linguistic_phenomena, k=3),
                'nlp_task': random.choice(nlp_tasks)
            }
            for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        phenomena = ', '.join([f"{p[0]} ({p[1]})" for p in t['cognitive_linguistic_phenomena']])
        return f"""Design an AI system that integrates the following cognitive-linguistic phenomena: {phenomena} into a unified machine learning algorithm, and apply it to the natural language processing task of {t['nlp_task'][0]} ({t['nlp_task'][1]}). Your response should include the following sections:

1. Cognitive-Linguistic Analysis (300-350 words):
   a) Explain each chosen cognitive-linguistic phenomenon in depth.
   b) Discuss their relevance to language processing and cognition.
   c) Analyze how these phenomena might interact and manifest in the specified NLP task.
   d) Provide a concrete example demonstrating the interplay of these phenomena in the context of the NLP task.

2. Computational Model Design (350-400 words):
   a) Propose a novel machine learning architecture that captures the essence of the cognitive-linguistic phenomena.
   b) Explain how your model translates abstract cognitive concepts into concrete computational structures.
   c) Describe the key components of your model and their functions, including how they represent each phenomenon.
   d) Include a high-level pseudocode or diagram illustrating the main aspects of your algorithm.
   e) Provide a mathematical formulation of a key component of your model, explaining its significance.
   f) Justify your design choices with reference to both cognitive linguistics and machine learning principles.

3. Application to NLP Task (300-350 words):
   a) Detail how your cognitive-linguistic AI model would be applied to the specified NLP task.
   b) Explain the potential advantages of your approach compared to traditional methods.
   c) Discuss any challenges or limitations specific to this application.
   d) Propose a method for evaluating the performance of your model on this task.
   e) Provide a hypothetical case study demonstrating how your model would process a specific input.

4. Critical Evaluation (200-250 words):
   a) Identify potential weaknesses or limitations of your proposed model.
   b) Discuss alternative approaches that could address these limitations.
   c) Compare your model to existing state-of-the-art approaches for the given NLP task.
   d) Propose a strategy for empirically validating the cognitive-linguistic foundations of your model.

5. Training and Data Considerations (200-250 words):
   a) Describe the type of data required to train your model.
   b) Explain any novel data preprocessing or augmentation techniques needed.
   c) Discuss potential biases or ethical considerations in data collection and model training.
   d) Propose a strategy for handling out-of-distribution or edge cases.

6. Broader Implications (150-200 words):
   a) Discuss how your approach might advance our understanding of human cognition and language processing.
   b) Explore potential applications of your model to other areas of AI or cognitive science.
   c) Consider any philosophical implications of translating multiple cognitive phenomena into AI systems.
   d) Address potential societal impacts of your proposed system.

7. Future Research Directions (100-150 words):
   a) Propose two potential extensions or improvements to your model.
   b) Suggest a research question that could further the integration of cognitive linguistics and AI.
   c) Outline a potential experiment to validate your model's cognitive-linguistic foundations.

Ensure your response demonstrates a deep understanding of cognitive linguistics, machine learning, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and include the word count at the end of each section. Your total response should be between 1600-1950 words. Include a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the cognitive-linguistic phenomena ({', '.join([p[0] for p in t['cognitive_linguistic_phenomena']])}) and their relevance to the specified NLP task ({t['nlp_task'][0]}).",
            "The proposed AI system effectively integrates multiple cognitive-linguistic concepts into a unified computational model.",
            "The application of the model to the NLP task is well-explained and plausible, with a clear hypothetical case study provided.",
            "The response includes a mathematical formulation of a key component of the model, with a clear explanation of its significance.",
            "The critical evaluation section thoroughly addresses potential weaknesses and alternative approaches.",
            "The response addresses all required sections with appropriate depth and creativity, adhering to the specified word counts.",
            "The response includes innovative ideas while maintaining scientific and technological plausibility.",
            "The broader implications and future research directions are thoughtfully considered, including potential societal impacts.",
            "Concrete examples and use cases are provided to demonstrate understanding of both the cognitive-linguistic phenomena and the NLP task.",
            "The response includes appropriate technical terminology and clear explanations for complex concepts.",
            "The proposed evaluation method for the model's performance is well-reasoned and appropriate for the task.",
            "The response adheres to the specified format, including section headings and word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
