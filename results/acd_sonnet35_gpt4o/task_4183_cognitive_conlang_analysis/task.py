import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                'process': 'Metacognition',
                'description': 'Awareness and understanding of one\'s own thought processes',
                'related_concept': 'Theory of Mind'
            },
            {
                'process': 'Counterfactual Thinking',
                'description': 'Imagining alternative scenarios to past events',
                'related_concept': 'Causal Reasoning'
            }
        ]
        return {str(i+1): process for i, process in enumerate(cognitive_processes)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language (conlang) that encodes the cognitive process of {t['process']} and use it to explore complex mental phenomena. A conlang is a constructed language, created for a specific purpose rather than having evolved naturally.

Your response should include the following sections:

1. Language Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how these features specifically encode {t['process']}.
   c) Provide at least three examples of basic sentences or expressions in your conlang that represent cognitive states or operations, including both the conlang text and its English translation.
   d) Discuss how your language incorporates or relates to the concept of {t['related_concept']}.

2. Cognitive Process Analysis (250-300 words):
   a) Analyze how your conlang's structure reflects current theories about {t['process']}.
   b) Discuss any novel insights about {t['process']} that emerge from your language design.
   c) Explain how your conlang might be used to study or model {t['process']} in cognitive science research.

3. Mental Phenomena Exploration (250-300 words):
   a) Choose a complex mental phenomenon (e.g., decision-making under uncertainty, emotional regulation, or creative problem-solving).
   b) Demonstrate how your conlang could be used to describe or analyze this phenomenon.
   c) Provide at least two specific examples of expressions or constructions in your conlang that capture key aspects of the chosen phenomenon, including both the conlang text and its English translation.

4. Linguistic Relativity Hypothesis (200-250 words):
   a) Discuss how your conlang might influence thought processes related to {t['process']} if it were used as a primary language.
   b) Propose an experiment to test the potential cognitive effects of using your conlang.
   c) Analyze the implications of your conlang for the linguistic relativity hypothesis.

5. AI and Cognitive Modeling (200-250 words):
   a) Explain how your conlang could be used to enhance AI systems' understanding or modeling of {t['process']}.
   b) Propose a specific AI application that could benefit from incorporating your conlang.
   c) Discuss any challenges in implementing your conlang in AI systems and potential solutions.

6. Ethical and Philosophical Implications (150-200 words):
   a) Analyze the ethical considerations of designing languages that encode cognitive processes.
   b) Discuss the philosophical implications of your conlang for our understanding of mind and language.
   c) Consider potential societal impacts if such cognitive conlangs were widely adopted.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology, but provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section with the word count in parentheses. Your total response should be between 1350-1650 words, not including the headings and word counts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The conlang design is creative, well-explained, and plausibly encodes the given cognitive process.",
            "The analysis of the cognitive process and mental phenomena is insightful and scientifically grounded.",
            "The discussion of linguistic relativity and AI applications is thoughtful and well-reasoned.",
            "The ethical and philosophical implications are carefully considered.",
            "The response is well-structured, clear, and uses appropriate technical terminology.",
            "The response adheres to the specified word limit and format guidelines.",
            "Concrete examples of the conlang, including translations, are provided as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
