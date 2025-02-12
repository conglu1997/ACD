import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'language_pair': ('Mandarin', 'English'),
                'linguistic_focus': 'Tonal to Non-tonal',
                'cognitive_aspect': 'Working Memory'
            },
            {
                'language_pair': ('Arabic', 'Spanish'),
                'linguistic_focus': 'Root-based to Conjugation-based',
                'cognitive_aspect': 'Attention Mechanisms'
            },
            {
                'language_pair': ('Japanese', 'Russian'),
                'linguistic_focus': 'Subject-Object-Verb to Subject-Verb-Object',
                'cognitive_aspect': 'Long-term Potentiation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human brain's language processing centers, focusing on multilingual capabilities and neuroplasticity. Your task is to create a detailed proposal for this system, considering the following language pair: {t['language_pair'][0]} and {t['language_pair'][1]}, with a focus on the linguistic aspect of {t['linguistic_focus']} and the cognitive process of {t['cognitive_aspect']}.

Your response should include the following sections:

1. Neurolinguistic Foundation (200-250 words):
   a) Describe the key brain regions involved in language processing, focusing on those relevant to multilingual abilities.
   b) Explain how these regions interact in multilingual individuals, particularly for the given language pair.
   c) Discuss the role of neuroplasticity in language acquisition and processing.

2. Neural Network Architecture (250-300 words):
   a) Propose a novel neural network architecture that mimics the identified brain regions and their interactions.
   b) Explain how your architecture incorporates the principle of neuroplasticity.
   c) Describe how your model accounts for the specific linguistic focus ({t['linguistic_focus']}) between the given language pair.
   d) Include a diagram or detailed description of your proposed architecture.

3. Cognitive Process Integration (200-250 words):
   a) Explain how your architecture models the specified cognitive aspect ({t['cognitive_aspect']}).
   b) Describe how this cognitive process contributes to language processing in your model.
   c) Discuss any novel approaches or algorithms used to implement this cognitive aspect.

4. Multilingual Capabilities (200-250 words):
   a) Describe how your architecture handles translation between the given language pair.
   b) Explain any specific features designed to address the challenges of the given linguistic focus.
   c) Discuss how your model could be extended to incorporate additional languages.

5. Training and Adaptation (150-200 words):
   a) Propose a method for training your neural network architecture.
   b) Explain how your model could adapt to new linguistic information, demonstrating neuroplasticity.
   c) Discuss any potential challenges in the training process and how they might be overcome.

6. Evaluation and Benchmarking (150-200 words):
   a) Suggest methods to evaluate the performance of your architecture, particularly in handling the specified language pair and linguistic focus.
   b) Propose benchmarks to compare your model's performance against existing language models and human performance.
   c) Discuss how you would measure the model's capability in terms of the specified cognitive aspect.

7. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical implications of developing AI systems that closely mimic human brain function.
   b) Address any limitations of your proposed architecture and suggest areas for future research.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1250-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence, particularly in relation to language processing and multilingual capabilities.",
            "The proposed neural network architecture is innovative, well-explained, and plausibly mimics the relevant brain regions and their interactions.",
            "The integration of neuroplasticity and the specified cognitive aspect is clearly explained and relevant to the task.",
            "The approach to handling the given language pair and linguistic focus is well-thought-out and demonstrates an understanding of the challenges involved.",
            "The training, adaptation, and evaluation methods are appropriate and well-justified.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
