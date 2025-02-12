import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conlangs = [
            {
                'name': 'Zxylophian',
                'features': 'Uses musical tones to convey meaning. Has no concept of past or future, only present.',
                'culture': 'Highly collaborative society where individual achievements are discouraged.',
                'problem': 'Negotiate a peace treaty between warring factions.'
            },
            {
                'name': 'Quantumspeak',
                'features': 'Every sentence must contain a paradox. Verbs change meaning based on the observer.',
                'culture': 'Values uncertainty and multiple truths. Decisions are made by embracing all possibilities simultaneously.',
                'problem': 'Design a fair voting system for electing a leader.'
            },
            {
                'name': 'Empathosyntax',
                'features': 'Sentence structure changes based on the emotional state of the speaker and listener.',
                'culture': 'Prioritizes emotional harmony above all else. Conflicts are seen as emotional imbalances.',
                'problem': 'Create a system for allocating limited resources among community members.'
            },
            {
                'name': 'Fractalis',
                'features': 'Words have different meanings at different scales. Sentences are valid only if they form a geometric pattern.',
                'culture': 'Obsessed with patterns and recursion. Believes the universe is a giant fractal.',
                'problem': 'Develop an educational curriculum for young learners.'
            }
        ]
        
        tasks = random.sample(conlangs, 2)
        return {str(i+1): {'conlang': conlang} for i, conlang in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve a complex problem within the constraints of a fictional constructed language (conlang) and its associated imaginary culture. Your task involves the following conlang and problem:

Conlang Name: {t['conlang']['name']}
Language Features: {t['conlang']['features']}
Cultural Context: {t['conlang']['culture']}
Problem to Solve: {t['conlang']['problem']}

Provide your solution in the following format:

1. Language Analysis (200-250 words):
   a) Explain how the unique features of the conlang might affect problem-solving and communication.
   b) Describe potential challenges in expressing complex ideas in this language.
   c) Propose at least three example phrases or sentences in the conlang, with explanations of their structure and meaning.

2. Cultural Interpretation (200-250 words):
   a) Analyze how the given cultural context would influence approaches to the problem.
   b) Discuss potential cultural taboos or preferences that might affect the solution.
   c) Explain how the culture's values and beliefs might shape the desired outcome.

3. Problem Solution (300-350 words):
   a) Present a detailed solution to the problem that adheres to both linguistic and cultural constraints.
   b) Explain your reasoning for each part of the solution, referencing specific language features and cultural aspects.
   c) Describe how you would communicate this solution using the conlang, including any unique linguistic structures or cultural references.
   d) Address potential misunderstandings or conflicts that might arise due to the language and culture, and how you would mitigate them.

4. Comparative Analysis (200-250 words):
   a) Compare your approach to how this problem might be solved in a real-world language and culture.
   b) Discuss the advantages and disadvantages of the conlang and its culture in addressing this specific problem.
   c) Propose how insights from this fictional scenario might be applied to real-world problem-solving or cross-cultural communication.

Ensure your response demonstrates creativity, cultural sensitivity, and logical problem-solving while adhering to the unique constraints of the conlang and its associated culture. Use appropriate examples and explanations to illustrate your points.

Your total response should be between 900-1100 words. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the conlang's features and their implications for communication and problem-solving.",
            "The cultural interpretation shows insight into how the imaginary culture would approach the problem.",
            "The problem solution is creative, detailed, and adheres to both linguistic and cultural constraints.",
            "The comparative analysis offers thoughtful insights on the differences between the fictional scenario and real-world approaches.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
