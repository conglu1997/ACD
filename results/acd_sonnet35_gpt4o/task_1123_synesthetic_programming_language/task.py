import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synesthesia_types = [
            {
                'type': 'Grapheme-color synesthesia',
                'description': 'Association of letters or numbers with specific colors',
                'example': 'Seeing the letter A as red'
            },
            {
                'type': 'Chromesthesia',
                'description': 'Association of sounds with colors',
                'example': 'Perceiving musical notes as specific colors'
            },
            {
                'type': 'Lexical-gustatory synesthesia',
                'description': 'Association of words or phonemes with tastes',
                'example': 'The word "castle" tasting like vanilla'
            },
            {
                'type': 'Spatial-sequence synesthesia',
                'description': 'Perception of numerical sequences as points in space',
                'example': 'Visualizing numbers as a 3D map'
            }
        ]
        return {str(i+1): synesthesia for i, synesthesia in enumerate(random.sample(synesthesia_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on the principles of {t['type']}, incorporating elements of color, sound, or spatial relationships as appropriate. Your task is to:

1. Briefly explain the given type of synesthesia and its key characteristics (2-3 sentences).

2. Design an innovative programming language that incorporates this form of synesthesia as its fundamental principle. Describe its key components and functioning (5-6 sentences). Include at least one code snippet demonstrating a basic operation (e.g., variable declaration, function definition) in your language.

3. Explain how your language represents at least three common programming concepts (e.g., loops, conditionals, data structures) using synesthetic elements.

4. Analyze how this programming language could potentially impact coding education and cognitive processing for programmers (3-4 sentences).

5. Discuss possible challenges in implementing or using this programming language and how they might be addressed (2-3 sentences).

6. Explore the potential implications of this synesthesia-based programming language on accessibility in computer science, considering both advantages and potential drawbacks (3-4 sentences).

7. Propose a simple experiment or user study that could be conducted to test the effectiveness of your programming language in comparison to traditional text-based languages (2-3 sentences).

Format your response as follows:

Synesthesia Explanation:
[Your explanation of the synesthesia type]

Programming Language Design:
[Your description of the synesthesia-based programming language]

Code Representation:
1. [First programming concept]
2. [Second programming concept]
3. [Third programming concept]

Cognitive Impact Analysis:
[Your analysis of potential impacts on coding education and cognitive processing]

Challenges and Solutions:
[Your discussion of challenges and potential solutions]

Accessibility Implications:
[Your exploration of accessibility implications]

Proposed Experiment:
[Your proposal for an experiment or user study]

Ensure that your programming language design is logically consistent and takes into account the specific characteristics of the given synesthesia type. Use appropriate terminology from both computer science and cognitive psychology where applicable. Be creative in your approach while maintaining scientific and practical plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of {t['type']} and its key characteristics is accurate and clear.",
            "The programming language design creatively and logically incorporates the synesthesia principle.",
            "At least one code snippet demonstrating a basic operation is included.",
            "The representation of three common programming concepts using synesthetic elements is well-explained.",
            "The analysis of cognitive impacts on coding education and processing is thoughtful and well-reasoned.",
            "Challenges and potential solutions are realistic and well-considered.",
            "The exploration of accessibility implications is insightful and considers both advantages and drawbacks.",
            "The proposed experiment or user study is relevant and could feasibly test the language's effectiveness.",
            "The response is well-organized and follows the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
