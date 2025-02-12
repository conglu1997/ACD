import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_features = [
            "sentiment analysis",
            "named entity recognition",
            "text summarization",
            "machine translation",
            "question answering"
        ]
        programming_paradigms = [
            "object-oriented",
            "functional",
            "logic",
            "event-driven",
            "dataflow"
        ]
        return {
            "1": {
                "nlp_feature": random.choice(nlp_features),
                "paradigm": random.choice(programming_paradigms)
            },
            "2": {
                "nlp_feature": random.choice(nlp_features),
                "paradigm": random.choice(programming_paradigms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel programming language that seamlessly integrates natural language processing capabilities, focusing on {t['nlp_feature']} as a core feature. The language should follow the {t['paradigm']} programming paradigm. Your response should include:

1. Language Overview (200-250 words):
   a) Provide a name and brief description of your programming language.
   b) Explain how it integrates {t['nlp_feature']} as a core feature.
   c) Describe how it adheres to the {t['paradigm']} paradigm.
   d) Outline the key benefits and potential applications of your language.

2. Syntax and Semantics (250-300 words):
   a) Describe the basic syntax of your language, including any novel elements.
   b) Explain how {t['nlp_feature']} is represented and manipulated in the language.
   c) Provide at least two code snippets demonstrating unique features of your language.
   d) Discuss how the language's semantics support both NLP and traditional programming tasks.

3. Implementation Considerations (200-250 words):
   a) Outline the key components needed to implement your language.
   b) Discuss potential challenges in implementation and propose solutions.
   c) Explain how your language could be optimized for performance.

4. Comparison and Analysis (200-250 words):
   a) Compare your language to existing programming languages and NLP tools.
   b) Analyze the strengths and limitations of your approach.
   c) Discuss how your language could impact software development and NLP research.

5. Future Directions (100-150 words):
   a) Propose two potential extensions or improvements to your language.
   b) Discuss how your language could evolve to address future challenges in computing and NLP.

Ensure your response demonstrates a deep understanding of programming language design, natural language processing, and the specified programming paradigm. Be innovative in your approach while considering practical implementation aspects. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language successfully integrates {t['nlp_feature']} as a core feature.",
            f"The language adheres to the {t['paradigm']} programming paradigm.",
            "The syntax and semantics are clearly explained and demonstrated with code snippets.",
            "The response addresses implementation considerations and potential challenges.",
            "The language design is innovative and offers clear benefits over existing solutions.",
            "The analysis demonstrates a deep understanding of programming language design and NLP."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
