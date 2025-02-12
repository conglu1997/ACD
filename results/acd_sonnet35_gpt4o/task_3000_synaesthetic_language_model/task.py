import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synaesthesia_types = [
            {
                'type': 'Grapheme-color',
                'description': 'Association of letters or numbers with specific colors',
                'example': {'A': 'red', 'B': 'blue', 'C': 'yellow', '1': 'white', '2': 'black'}
            },
            {
                'type': 'Lexical-gustatory',
                'description': 'Association of words with specific tastes',
                'example': {'hello': 'sweet', 'goodbye': 'bitter', 'love': 'spicy', 'hate': 'sour'}
            },
            {
                'type': 'Spatial-sequence',
                'description': 'Perception of numerical sequences as having specific spatial arrangements',
                'example': {'1-10': 'circular', '11-20': 'linear', '21-30': 'zigzag'}
            },
            {
                'type': 'Chromesthesia',
                'description': 'Association of sounds with colors',
                'example': {'C': 'red', 'D': 'blue', 'E': 'green', 'F': 'yellow', 'G': 'orange'}
            }
        ]
        return {str(i+1): type for i, type in enumerate(random.sample(synaesthesia_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI language model that incorporates principles of {t['type']} synaesthesia ({t['description']}) to generate and process multi-sensory linguistic representations. Use the following example associations as a starting point: {t['example']}. Your response should include the following sections:

1. Model Architecture (300-350 words):
   a) Describe the key components of your synaesthetic language model.
   b) Explain how your model incorporates the principles of {t['type']} synaesthesia.
   c) Detail how your model processes and generates multi-sensory linguistic representations.
   d) Include a simple diagram or flowchart illustrating your model's architecture (describe it textually).

2. Synaesthetic Representation (250-300 words):
   a) Explain how your model represents the synaesthetic associations between linguistic elements and sensory experiences.
   b) Describe the data structures or mathematical formulations used to encode these associations.
   c) Discuss how your model handles individual variations in synaesthetic experiences.

3. Training and Learning (200-250 words):
   a) Describe the training process for your synaesthetic language model.
   b) Explain how your model learns to generate coherent multi-sensory representations.
   c) Discuss any novel machine learning techniques specific to synaesthetic modeling.

4. Applications and Use Cases (200-250 words):
   a) Propose three innovative applications of your synaesthetic language model.
   b) Explain how each application leverages the multi-sensory aspects of your model.
   c) Discuss potential benefits and challenges of using synaesthetic AI in these contexts.

5. Cognitive Science Implications (150-200 words):
   a) Analyze how your model might contribute to our understanding of human synaesthesia and cross-modal perception.
   b) Propose an experiment to test a key prediction of your model about synaesthetic language processing.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to the development and use of synaesthetic AI.
   b) Discuss privacy concerns, particularly regarding the collection and use of personal synaesthetic data.
   c) Propose guidelines for the responsible development and application of synaesthetic language models.

7. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your synaesthetic language model.
   b) Propose a novel research question that could be explored using your model.

8. Code Implementation (100-150 words):
   Provide a Python function that demonstrates a key aspect of your synaesthetic language model. For example, you could implement a function that takes a word or sentence as input and returns its synaesthetic representation based on the {t['type']} synaesthesia type. Include comments explaining your code.

Ensure your response demonstrates a deep understanding of synaesthesia, cognitive neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1450-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['type']} synaesthesia and its potential applications in AI language models.",
            "The model architecture is well-explained and incorporates the specified type of synaesthesia.",
            "The synaesthetic representation and training process are clearly described and scientifically plausible.",
            "The proposed applications are innovative and leverage the multi-sensory aspects of the model.",
            "The response addresses cognitive science implications, ethical considerations, and future research directions.",
            "The provided Python function correctly implements a key aspect of the synaesthetic language model.",
            "The writing is clear, well-structured, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
