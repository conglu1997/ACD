import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "name": "Aquatic",
                "description": "A world entirely covered in water, where intelligent species live in underwater cities.",
                "cultural_aspect": "Highly communal society with emphasis on resource sharing."
            },
            {
                "name": "Volcanic",
                "description": "A planet with constant volcanic activity, where inhabitants live in heat-resistant structures.",
                "cultural_aspect": "Ritualistic practices centered around predicting and appeasing volcanic eruptions."
            },
            {
                "name": "Arboreal",
                "description": "A world covered in massive trees, where intelligent life evolved to live entirely in the canopy.",
                "cultural_aspect": "Strongly hierarchical society based on canopy levels."
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional language (conlang) for a species living in the following environment:

Environment: {t['name']} - {t['description']}
Cultural Aspect: {t['cultural_aspect']}

Your task has four parts:

1. Design the basic structure of the language (100-150 words):
   - Describe the phonetic inventory (sounds used)
   - Explain the morphological system (how words are formed)
   - Outline the syntactic structure (how sentences are constructed)
   - Justify how these linguistic features are adapted to the environment and culture

2. Provide a sample vocabulary (exactly 10 words) with English translations. For each word, briefly explain its relation to the environment or culture (1-2 sentences per word).

3. Translate the following sentence into your conlang, and explain the translation (50-75 words):
   "Our community must work together to overcome the challenges of our world."

4. Describe how speakers of this language would use it to solve a problem unique to their environment (100-150 words). Include at least one example sentence in your conlang (with translation) to demonstrate its practical usage in problem-solving.

Format your response as follows:

Language Structure:
[Your description here]

Vocabulary:
1. [Conlang word]: [English translation]
   Explanation: [Your explanation]
2. [Conlang word]: [English translation]
   Explanation: [Your explanation]
...

Translation:
[Your translated sentence]
Explanation: [Your explanation]

Problem-Solving Application:
[Your description here]
Example sentence: [Conlang sentence]
Translation: [English translation]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design should clearly reflect the {t['name']} environment and the given cultural aspect",
            "The vocabulary should include exactly 10 words with explanations relating to the environment and culture",
            "The translation should be consistent with the described language structure",
            "The problem-solving application should be logical, relevant to the given environment, and include an example sentence in the conlang"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
