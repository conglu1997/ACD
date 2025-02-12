import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'semantic_phenomenon': 'Quantifier scope ambiguity',
                'example_sentence': 'Every student read two books.',
                'additional_context': 'Consider how different scope readings affect the truth conditions.'
            },
            {
                'semantic_phenomenon': 'Presupposition projection',
                'example_sentence': 'If the king of France is bald, then the king of France exists.',
                'additional_context': 'Analyze how the presupposition behaves in complex sentences.'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a system that bridges formal semantics theory with practical natural language processing applications, focusing on compositional semantics and inference. Your task will revolve around the semantic phenomenon of {t['semantic_phenomenon']}, using the example sentence: "{t['example_sentence']}"

Additional context: {t['additional_context']}

Your response should include the following components:

1. Theoretical Foundation (200-250 words):
   a) Explain the chosen semantic phenomenon and its significance in natural language understanding.
   b) Describe the relevant formal semantic theories or frameworks that address this phenomenon.
   c) Discuss how this phenomenon challenges traditional NLP approaches.

2. Formal Representation (200-250 words):
   a) Provide a formal semantic representation of the example sentence using an appropriate logical formalism (e.g., first-order logic, lambda calculus, or a more specialized framework).
   b) Explain your choice of formalism and how it captures the semantic nuances of the phenomenon.
   c) Demonstrate how your representation handles the complexities or ambiguities present in the example.

3. Computational Implementation (250-300 words):
   a) Describe an algorithm or computational process to derive your formal semantic representation from the natural language input.
   b) Explain how your system would handle compositionality and build complex meanings from simpler parts.
   c) Discuss any optimizations or approximations necessary for practical implementation.
   d) Provide pseudocode for a key component of your system.

4. Inference Mechanism (200-250 words):
   a) Design an inference mechanism that can reason over your semantic representations.
   b) Explain how this mechanism would derive implicit information or resolve ambiguities.
   c) Provide an example of an inference your system could make based on the example sentence.

5. NLP Integration (200-250 words):
   a) Propose how your system could be integrated into a larger NLP pipeline or application.
   b) Discuss potential benefits and challenges of using formal semantics in practical NLP tasks.
   c) Suggest a specific NLP task that could significantly benefit from your approach.

6. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system.
   b) Discuss limitations of your approach and potential areas for future improvement.
   c) Consider scalability issues and how they might be addressed.

Ensure your response demonstrates a deep understanding of formal semantics, natural language processing, and the interface between theoretical linguistics and computational applications. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific rigor and practical feasibility.

Format your response with clear headings for each section. The total word count for your response should be between 1200-1500 words. Begin each section with the heading (e.g., '1. Theoretical Foundation:') on a new line, followed by your response for that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of formal semantics and the specified semantic phenomenon, including the additional context provided.",
            "The formal representation accurately captures the semantic nuances of the example sentence, addressing any ambiguities or complexities.",
            "The computational implementation is well-described, addresses compositionality, and includes relevant pseudocode.",
            "The inference mechanism is logically sound, relevant to the semantic phenomenon, and provides a concrete example based on the given sentence.",
            "The proposed NLP integration is practical, potentially impactful, and clearly explains benefits and challenges.",
            "The evaluation methods and limitations discussion show critical thinking and awareness of challenges, including scalability issues.",
            "The overall response effectively bridges theoretical linguistics with practical NLP applications, maintaining scientific rigor and practical feasibility.",
            "The submission is well-structured, clear, uses appropriate technical terminology, and adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
