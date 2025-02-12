import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_parameters = [
            "working memory capacity",
            "spatial reasoning ability",
            "temporal perception",
            "emotional processing"
        ]
        cultural_contexts = [
            "nomadic desert society",
            "advanced space-faring civilization",
            "underwater civilization",
            "hivemind collective"
        ]
        language_aspects = [
            "phonology",
            "morphology",
            "syntax",
            "semantics"
        ]
        return {
            "1": {
                "cognitive_parameter": random.choice(cognitive_parameters),
                "cultural_context": random.choice(cultural_contexts),
                "language_aspect": random.choice(language_aspects)
            },
            "2": {
                "cognitive_parameter": random.choice(cognitive_parameters),
                "cultural_context": random.choice(cultural_contexts),
                "language_aspect": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing constructed languages (conlangs) based on specific cognitive and cultural parameters. Then, apply your system to create a language for a society with the following characteristics:

Cognitive Parameter: {t['cognitive_parameter']}
Cultural Context: {t['cultural_context']}

Focus on the language aspect of {t['language_aspect']} in your response.

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and analyzing conlangs.
   b) Explain how your system incorporates cognitive science and cultural anthropology principles.
   c) Discuss any novel elements in your design that enable the creation of cognitively and culturally appropriate languages.

2. Cognitive-Linguistic Mapping (200-250 words):
   a) Explain how your system maps the given cognitive parameter to specific linguistic features.
   b) Provide concrete examples of how {t['cognitive_parameter']} might influence language structure or use.
   c) Discuss potential challenges in modeling this cognitive-linguistic relationship.

3. Cultural-Linguistic Adaptation (200-250 words):
   a) Describe how your AI adapts language features to suit the given cultural context.
   b) Explain the cultural considerations taken into account for a {t['cultural_context']}.
   c) Provide examples of how these cultural factors might influence language development.

4. Language Generation Process (200-250 words):
   a) Detail the step-by-step process your AI uses to generate a conlang, from parameter input to final language output.
   b) Focus on how it develops the {t['language_aspect']} of the language.
   c) Explain how your system ensures consistency and naturalism in the generated language.

5. Sample Language Output (150-200 words):
   a) Provide a brief sample of the generated language, focusing on its {t['language_aspect']}.
   b) Explain how this sample reflects both the cognitive parameter and cultural context.
   c) Analyze the unique features of your generated language.

6. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate the cognitive and cultural appropriateness of your AI-generated language.
   b) Describe metrics you would use to assess both linguistic creativity and adherence to the given parameters.
   c) Discuss potential challenges in evaluating artificial languages.

7. Ethical Considerations and Implications (150-200 words):
   a) Discuss potential ethical implications of using AI for language creation and analysis.
   b) Consider the impact of such technology on linguistic diversity and cultural representation.
   c) Propose guidelines for the responsible use of AI in linguistics and cognitive science research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and AI systems.",
            "The AI system design is innovative, plausible, and incorporates principles from multiple disciplines.",
            f"The cognitive-linguistic mapping for {t['cognitive_parameter']} is well-explained and plausible.",
            f"The cultural-linguistic adaptation for a {t['cultural_context']} is thoughtful and well-reasoned.",
            f"The language generation process, focusing on {t['language_aspect']}, is clearly explained and logical.",
            "The sample language output is creative and reflects both the cognitive parameter and cultural context.",
            "The evaluation methodology is well-designed and addresses potential challenges.",
            "Ethical considerations are thoroughly discussed with appropriate guidelines proposed.",
            "The response is well-structured, within the specified word count, and uses technical terminology appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
