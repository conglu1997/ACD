import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_aspects = [
            {
                "aspect": "Phonological development",
                "description": "The acquisition of speech sounds and phonological rules"
            },
            {
                "aspect": "Syntactic development",
                "description": "The acquisition of grammatical structures and rules"
            },
            {
                "aspect": "Semantic development",
                "description": "The acquisition of word meanings and conceptual knowledge"
            },
            {
                "aspect": "Pragmatic development",
                "description": "The acquisition of social language use and communication skills"
            }
        ]
        return {str(i+1): aspect for i, aspect in enumerate(random.sample(language_aspects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and analyzes the stages of human language acquisition, with a focus on the critical period hypothesis and its implications for AI language models. Your system should specifically address the language aspect of {t['aspect']} - {t['description']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling language acquisition.
   b) Explain how your system incorporates principles from linguistics, cognitive science, and developmental psychology.
   c) Detail how your system models the critical period hypothesis in relation to {t['aspect']}.
   d) Discuss any novel AI techniques or algorithms used in your model.
   e) Provide a high-level diagram of your system architecture (describe it textually).

2. Language Acquisition Modeling (250-300 words):
   a) Outline the stages of language acquisition your system models, focusing on {t['aspect']}.
   b) Explain how your system simulates the learning process for this aspect of language.
   c) Describe how your model accounts for individual differences in language acquisition.
   d) Discuss how your system handles the interaction between innate language capabilities and environmental input.

3. Critical Period Integration (200-250 words):
   a) Explain how your system models the critical period hypothesis for {t['aspect']}.
   b) Describe the mechanisms your system uses to simulate age-related changes in language learning ability.
   c) Discuss how your model accounts for potential exceptions or variations to the critical period hypothesis.

4. Data Sources and Processing (200-250 words):
   a) Describe the types of data your system uses to model language acquisition (e.g., child language corpora, experimental data).
   b) Explain how your system processes and integrates different data sources.
   c) Discuss any challenges in data collection or processing for modeling {t['aspect']}.

5. Model Validation and Testing (200-250 words):
   a) Propose methods to validate your model against empirical data on child language acquisition.
   b) Describe experiments you would conduct to test your model's predictions about {t['aspect']}.
   c) Discuss how you would evaluate your model's performance in simulating the critical period hypothesis.

6. Implications for AI Language Models (250-300 words):
   a) Discuss how insights from your language acquisition model could inform the development of AI language models.
   b) Propose specific ways to apply the critical period hypothesis to improve AI language learning algorithms.
   c) Analyze potential limitations in applying human language acquisition principles to AI systems.
   d) Suggest novel approaches for creating more human-like language learning in AI based on your model.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical issues related to modeling child language acquisition in AI systems.
   b) Discuss the implications of your model for understanding and potentially enhancing human language learning.
   c) Propose future research directions that could extend or refine your model of language acquisition.

8. Concrete Example (200-250 words):
   Provide a detailed, concrete example of how your AI system would model a specific language acquisition phenomenon within {t['aspect']}. This example should demonstrate the practical application of your system's capabilities and illustrate how it integrates various components of your model.

Ensure your response demonstrates a deep understanding of language acquisition theories, cognitive science, and AI capabilities. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings a), b), c) etc. as appropriate. Adhere to the word count specified for each section. Your total response should be between 1750-2150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for an AI system modeling language acquisition, focusing on {t['aspect']}",
            "The system architecture is well-described and incorporates principles from linguistics, cognitive science, and developmental psychology",
            "The model adequately addresses the critical period hypothesis and its implications for AI language models",
            "The response demonstrates a deep understanding of language acquisition theories and their application to AI",
            "The proposed model validation and testing methods are appropriate and well-reasoned",
            "The implications for AI language models are thoughtfully explored and innovative",
            "Ethical considerations are adequately addressed",
            "A concrete example of modeling a specific language acquisition phenomenon is provided and well-explained",
            "The response is well-structured, using clear headings for each section, and adheres to the specified word count guidelines for each section",
            "The total response falls within the 1750-2150 word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
