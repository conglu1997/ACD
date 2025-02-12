import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_model': 'Spreading Activation Theory',
                'nlp_technique': 'Word Embeddings',
                'programming_paradigm': 'Functional Programming'
            },
            {
                'cognitive_model': 'Construction Grammar',
                'nlp_technique': 'Dependency Parsing',
                'programming_paradigm': 'Logic Programming'
            },
            {
                'cognitive_model': 'Dual-Route Model of Reading',
                'nlp_technique': 'Named Entity Recognition',
                'programming_paradigm': 'Object-Oriented Programming'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel programming language based on natural language processing (NLP) principles and cognitive models of language understanding. Your language should incorporate the following elements:

1. Cognitive Model: {t['cognitive_model']}
2. NLP Technique: {t['nlp_technique']}
3. Programming Paradigm: {t['programming_paradigm']}

Your task is to create a detailed proposal for this programming language, including:

1. Language Overview (200-250 words):
   - Provide a high-level description of your programming language.
   - Explain how it incorporates the given cognitive model, NLP technique, and programming paradigm.
   - Discuss the main features and goals of your language.

2. Syntax and Structure (250-300 words):
   - Describe the basic syntax of your language, including how it differs from traditional programming languages.
   - Explain how the syntax reflects natural language structures and the given cognitive model.
   - Provide at least two code examples that demonstrate unique features of your language.

3. Semantic Processing (200-250 words):
   - Explain how your language processes and interprets code semantically.
   - Describe how the given NLP technique is used in this process.
   - Discuss any ambiguity resolution mechanisms in your language.

4. Cognitive Model Integration (200-250 words):
   - Describe in detail how the given cognitive model influences the design and execution of your language.
   - Explain any specific language features that directly reflect this cognitive model.

5. Use Cases and Advantages (150-200 words):
   - Propose at least two specific use cases where your language would be particularly effective.
   - Discuss the advantages of your language over traditional programming languages for these use cases.

6. Challenges and Limitations (100-150 words):
   - Identify potential challenges in implementing your language.
   - Discuss any limitations of your language and how they might be addressed in future versions.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and computer science. Use appropriate terminology from all relevant fields and provide explanations where necessary. Be creative in your language design while maintaining scientific and technical rigor.

Format your response using clear headings for each section. Your total response should be between 1100-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive model, NLP technique, and programming paradigm.",
            "The language overview clearly explains how all required elements are incorporated and presents innovative features.",
            "The syntax and structure description includes at least two code examples demonstrating unique features.",
            "The semantic processing explanation effectively integrates the given NLP technique.",
            "The cognitive model integration is well-explained and reflected in specific language features.",
            "At least two specific and plausible use cases are proposed with clear advantages over traditional programming languages.",
            "Potential challenges and limitations are identified and discussed thoughtfully.",
            "The response follows the specified format with clear headings for each section.",
            "The total word count is between 1100-1300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
