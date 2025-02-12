import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_constraints = [
            {
                "constraint": "Non-linear time perception",
                "description": "Design a language for a species that perceives time non-linearly, with the ability to experience past, present, and future simultaneously."
            },
            {
                "constraint": "Synesthesia-based communication",
                "description": "Create a language for beings who communicate primarily through synesthesia, where words evoke specific sensory experiences across multiple modalities."
            }
        ]
        return {str(i+1): task for i, task in enumerate(cognitive_constraints)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) based on the following cognitive constraint: {t['constraint']}. {t['description']}

Your response should include the following sections:

1. Language Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how these features reflect the given cognitive constraint.
   c) Provide examples of basic sentences or phrases in your conlang, with translations and explanations.
   d) Include at least one example of how your conlang expresses a concept that would be difficult or impossible in natural languages.

2. Cognitive Analysis (250-300 words):
   a) Analyze how using this language might affect thought processes and perception.
   b) Discuss potential cognitive advantages and limitations of your conlang compared to natural languages.
   c) Explain how the language's structure might influence memory, problem-solving, or other cognitive functions.

3. Comparative Linguistic Analysis (200-250 words):
   a) Compare your conlang to at least two natural languages, highlighting key similarities and differences.
   b) Discuss how these differences might lead to varied cognitive effects among speakers.
   c) Propose a hypothesis about how your conlang might influence the Sapir-Whorf hypothesis.

4. Learning and Acquisition (150-200 words):
   a) Describe the potential challenges in learning your conlang for speakers of natural languages.
   b) Propose methods to facilitate the learning process, considering the unique cognitive aspects of your language.
   c) Discuss how acquisition of your conlang might differ between children and adults.

5. Practical Applications (150-200 words):
   a) Suggest two potential real-world applications or experiments using your conlang.
   b) Explain how these applications could contribute to our understanding of language and cognition.
   c) Discuss any ethical considerations related to the use or study of your conlang.

6. Creative Writing Sample (100-150 words):
   Provide a short creative writing sample (poem, story excerpt, or dialogue) in your conlang, with translation and explanation of how it showcases the language's unique features.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and creative language design. Be innovative in your approach while maintaining scientific plausibility and logical consistency. Provide sufficient examples in your conlang to demonstrate its structure and usage.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design clearly reflects the given cognitive constraint and includes unique features that would be difficult or impossible in natural languages",
            "The response demonstrates a deep understanding of linguistics and cognitive science, with well-reasoned analyses",
            "The comparative linguistic analysis is thorough and demonstrates knowledge of natural languages",
            "The practical applications and creative writing sample are innovative and effectively showcase the language's unique features",
            "Sufficient examples of the conlang are provided throughout the response, demonstrating its structure and usage",
            "The response is well-structured, coherent, and meets the specified word count requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
