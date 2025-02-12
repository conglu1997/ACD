import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_aspects = ['Phonology', 'Morphology', 'Syntax', 'Semantics', 'Pragmatics']
        brain_regions = ['Broca\'s area', 'Wernicke\'s area', 'Angular gyrus', 'Arcuate fasciculus', 'Inferior frontal gyrus']
        learning_scenarios = ['First language acquisition in infants', 'Second language learning in adults', 'Language recovery after brain injury', 'Artificial language learning in AI models']
        
        tasks = {
            "1": {
                "language_aspect": random.choice(language_aspects),
                "brain_region": random.choice(brain_regions),
                "learning_scenario": random.choice(learning_scenarios)
            },
            "2": {
                "language_aspect": random.choice(language_aspects),
                "brain_region": random.choice(brain_regions),
                "learning_scenario": random.choice(learning_scenarios)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neurolinguistically-inspired AI model for language acquisition and processing, focusing on the language aspect of {t['language_aspect']}, the brain region {t['brain_region']}, and the learning scenario of {t['learning_scenario']}. Your response should include the following sections:

1. Theoretical Foundation (250-300 words):
   a) Explain the role of {t['brain_region']} in language processing, particularly in relation to {t['language_aspect']}.
   b) Discuss current neurolinguistic theories relevant to {t['learning_scenario']}.
   c) Analyze how these theories could inform AI language model development.

2. Model Architecture (300-350 words):
   a) Design a novel AI architecture that incorporates neurolinguistic principles for language acquisition and processing.
   b) Explain how your model simulates the function of {t['brain_region']} in processing {t['language_aspect']}.
   c) Describe how your model adapts to the specific challenges of {t['learning_scenario']}.
   d) Include a diagram or pseudocode representing your model's key components and their interactions.

3. Learning Mechanisms (200-250 words):
   a) Detail the learning algorithms and processes used in your model.
   b) Explain how these mechanisms reflect current understanding of neural language acquisition.
   c) Discuss how your model balances innate linguistic knowledge and learned patterns.

4. Comparative Analysis (200-250 words):
   a) Compare your neurolinguistic AI model to traditional language models.
   b) Analyze potential advantages and limitations of your approach.
   c) Discuss how your model might perform differently on specific language tasks.

5. Experimental Validation (150-200 words):
   a) Propose an experiment to test your model's performance in the given learning scenario.
   b) Describe how you would measure the model's acquisition of {t['language_aspect']}.
   c) Discuss potential challenges in validating your model against human language acquisition.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of developing AI systems that closely mimic human language acquisition.
   b) Propose guidelines for responsible development and use of neurolinguistic AI models.
   c) Suggest two potential extensions or applications of your model in language technology or cognitive science.

Ensure your response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the role of {t['brain_region']} in language processing, particularly in relation to {t['language_aspect']}",
            f"The model architecture effectively incorporates neurolinguistic principles for language acquisition and processing, focusing on {t['language_aspect']}",
            f"The learning mechanisms reflect current understanding of neural language acquisition and are appropriate for {t['learning_scenario']}",
            "The comparative analysis provides insightful comparisons between the proposed model and traditional language models",
            "The experimental validation proposal is well-designed and appropriate for testing the model's performance",
            "The response addresses ethical implications and future directions for neurolinguistic AI models",
            "The response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence",
            "The ideas presented are innovative while maintaining scientific plausibility",
            "The response is well-structured with clear headings for each section",
            "The total response falls within the specified word count range of 1250-1550 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
