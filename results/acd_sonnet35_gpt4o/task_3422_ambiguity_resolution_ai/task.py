import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "type": "semantic",
                "context": "A news headline",
                "example": "Visiting relatives can be boring."
            },
            {
                "type": "syntactic",
                "context": "A legal document",
                "example": "The defendant examined by the lawyer shocked the jury."
            },
            {
                "type": "lexical",
                "context": "A restaurant menu",
                "example": "We serve fresh fish and chips."
            },
            {
                "type": "scope",
                "context": "A financial report",
                "example": "Every investor hasn't read the report."
            }
        ]
        return {
            "1": random.choice(scenarios[:2]),
            "2": random.choice(scenarios[2:])
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting ambiguous sentences, then apply it to the following linguistic scenario:

Ambiguity type: {t['type']}
Context: {t['context']}
Example ambiguous sentence: "{t['example']}"

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and interpreting ambiguous sentences.
   b) Explain how your system incorporates linguistic knowledge and contextual information.
   c) Discuss any novel approaches or algorithms used in your design to handle ambiguity.

2. Ambiguity Analysis (250-300 words):
   a) Analyze the example ambiguous sentence, explaining its possible interpretations.
   b) Describe how your AI system would process and represent these different interpretations.
   c) Explain how your system determines the most likely interpretation based on the given context.

3. Ambiguity Generation (200-250 words):
   a) Explain how your system would generate a new ambiguous sentence similar to the example, but with a different meaning.
   b) Provide the generated ambiguous sentence and analyze its possible interpretations.
   c) Discuss how your system ensures the generated ambiguity is appropriate for the given context.

4. Cognitive Modeling (200-250 words):
   a) Describe how your AI system models the cognitive processes involved in human ambiguity resolution.
   b) Compare your system's approach to ambiguity resolution with current theories in cognitive linguistics.
   c) Discuss any insights your model might provide about human language processing.

5. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate the effectiveness of your system in generating and interpreting ambiguous sentences.
   b) Describe metrics you would use to assess both linguistic accuracy and cognitive plausibility.
   c) Suggest how you might compare your system's performance to human performance on similar tasks.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of an AI system capable of generating and interpreting ambiguous language.
   b) Address any limitations of your approach and areas for future improvement.
   c) Propose guidelines for the responsible development and use of such systems in real-world applications.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section, numbered as above (e.g., '1. System Architecture', '2. Ambiguity Analysis', etc.). Adhere strictly to the word count limits for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six required sections with appropriate headings",
            "Each section adheres to the specified word count range",
            "The system architecture is well-described and incorporates novel approaches to handling ambiguity",
            "The ambiguity analysis demonstrates a deep understanding of the specific type of ambiguity ({t['type']}) in the given context",
            "The ambiguity generation process produces a valid ambiguous sentence appropriate for the given context",
            "The cognitive modeling section shows a strong grasp of current theories in cognitive linguistics",
            "The evaluation methodology includes specific, measurable metrics for assessing the system's performance",
            "Ethical considerations and limitations are thoroughly discussed with concrete examples",
            "The response demonstrates creativity while maintaining scientific plausibility",
            "Technical terminology is used appropriately and explained when necessary"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
