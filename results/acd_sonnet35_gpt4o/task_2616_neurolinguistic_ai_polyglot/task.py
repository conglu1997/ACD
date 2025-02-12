import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = [
            "Indo-European",
            "Sino-Tibetan",
            "Afroasiatic",
            "Austronesian",
            "Niger-Congo"
        ]
        
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Supramarginal gyrus",
            "Inferior frontal gyrus"
        ]
        
        linguistic_features = [
            "Syntax",
            "Semantics",
            "Phonology",
            "Pragmatics",
            "Morphology"
        ]
        
        ai_techniques = [
            "Transformer architecture",
            "Recurrent Neural Networks",
            "Attention mechanisms",
            "Convolutional Neural Networks",
            "Reinforcement Learning"
        ]
        
        return {
            "1": {
                "language_family": random.choice(language_families),
                "brain_region": random.choice(brain_regions),
                "linguistic_feature": random.choice(linguistic_features),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "language_family": random.choice(language_families),
                "brain_region": random.choice(brain_regions),
                "linguistic_feature": random.choice(linguistic_features),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuroscience-inspired AI language model that mimics human brain processes for multilingual language understanding and generation. Your model should focus on the {t['language_family']} language family, incorporate insights from the {t['brain_region']}, emphasize the linguistic feature of {t['linguistic_feature']}, and utilize the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. Model Architecture (300-350 words):
   a) Describe the key components of your AI language model and how they interact.
   b) Explain how your model incorporates neuroscientific insights, particularly from the specified brain region.
   c) Detail how the model handles multilingual processing within the given language family.
   d) Discuss how the specified AI technique is integrated into your model's design.

2. Linguistic Feature Integration (250-300 words):
   a) Explain how your model specifically addresses the given linguistic feature.
   b) Describe any novel approaches or mechanisms used to process this feature across multiple languages.
   c) Discuss how this integration enhances the model's language understanding and generation capabilities.

3. Neuroscience-AI Synergy (250-300 words):
   a) Analyze how your model's design bridges neuroscience and artificial intelligence.
   b) Explain any novel concepts or mechanisms inspired by the specified brain region.
   c) Discuss potential insights your model could provide for both neurolinguistics and AI research.

4. Multilingual Capabilities (200-250 words):
   a) Describe how your model handles translation and cross-lingual understanding within the language family.
   b) Explain any unique features that allow for effective processing of multiple related languages.
   c) Discuss potential challenges and solutions for extending the model to other language families.

5. Training and Data Considerations (200-250 words):
   a) Propose a training methodology for your neurolinguistic AI model.
   b) Describe the types of data needed and any special preprocessing requirements.
   c) Discuss potential biases and how you would mitigate them in a multilingual context.

6. Evaluation and Benchmarking (150-200 words):
   a) Suggest methods to evaluate your model's performance in language understanding and generation.
   b) Propose novel benchmarks that specifically test the model's neurolinguistic and multilingual capabilities.
   c) Discuss how you would validate the model's alignment with actual brain processes.

7. Ethical Considerations and Potential Applications (150-200 words):
   a) Identify potential ethical issues related to the development and use of your model.
   b) Discuss the implications of such a model for language preservation and linguistic diversity.
   c) Propose two novel applications of your model beyond natural language processing.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, linguistics, and artificial intelligence.",
            "The model design effectively incorporates insights from the specified brain region and linguistic feature.",
            "The approach to multilingual processing within the given language family is innovative and well-reasoned.",
            "The integration of the specified AI technique is clearly explained and justified.",
            "The discussion of neuroscience-AI synergy provides novel insights or approaches.",
            "The proposed training methodology and data considerations are appropriate and address potential biases.",
            "The evaluation methods and benchmarks are suitable for testing the model's unique capabilities.",
            "Ethical considerations and potential applications are thoughtfully discussed.",
            "The overall response is well-structured, innovative, and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
