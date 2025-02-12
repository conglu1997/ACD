import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_problems = [
            {
                "name": "Metaphor Detection",
                "description": "Identify and interpret metaphors in natural language text."
            },
            {
                "name": "Sentiment Analysis",
                "description": "Determine the emotional tone and attitude expressed in a piece of text."
            },
            {
                "name": "Semantic Role Labeling",
                "description": "Identify the semantic relationships between predicates and their arguments in sentences."
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(nlp_problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on cognitive linguistics principles and use it to solve the following natural language processing problem: {t['name']} - {t['description']}

Your response should include the following sections:

1. Language Design (300-350 words):
   a) Explain the core principles of cognitive linguistics that inform your language design.
   b) Describe the key features and syntax of your programming language.
   c) Explain how your language mirrors human cognitive processes and linguistic structures.
   d) Provide a simple code example in your language with explanation.

2. Cognitive-Computational Mapping (200-250 words):
   a) Describe how specific cognitive linguistics concepts are mapped to computational constructs in your language.
   b) Explain how this mapping facilitates solving the given NLP problem.
   c) Discuss any novel features that distinguish your language from traditional programming languages.

3. Problem-Solving Approach (250-300 words):
   a) Outline an algorithm in your language to address the given NLP problem.
   b) Explain how your language's features are particularly suited to solving this problem.
   c) Discuss any potential advantages your approach might have over traditional NLP methods.

4. Implementation Challenges (150-200 words):
   a) Identify potential difficulties in implementing your language on current computer architectures.
   b) Propose solutions or workarounds for these challenges.
   c) Discuss any trade-offs between cognitive fidelity and computational efficiency in your design.

5. Implications and Future Directions (200-250 words):
   a) Discuss how your language might influence future NLP research and cognitive modeling.
   b) Explore potential applications of your language beyond the given NLP problem.
   c) Propose an experiment to evaluate the effectiveness of your language compared to traditional approaches.

Ensure your response demonstrates a deep understanding of cognitive linguistics, programming language theory, and natural language processing. Be creative in your approach while maintaining scientific and computational plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics principles and their application to programming language design.",
            "The proposed language design is innovative and clearly mirrors human cognitive processes and linguistic structures.",
            f"The approach to solving the {t['name']} problem is well-reasoned and leverages the unique features of the designed language.",
            "The response addresses implementation challenges and proposes plausible solutions or workarounds.",
            "The implications and future directions discussed are insightful and demonstrate a broad understanding of the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
