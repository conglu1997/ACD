import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "synesthesia_type": "Grapheme-color synesthesia",
                "application": "Text sentiment analysis",
                "target_language": "English",
                "example_input": "The sky was a brilliant azure, reflecting her joyous mood."
            },
            {
                "synesthesia_type": "Lexical-gustatory synesthesia",
                "application": "Recipe generation",
                "target_language": "French",
                "example_input": "Le parfum délicat des fraises fraîches"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models {t['synesthesia_type']} and apply it to enhance {t['application']} in {t['target_language']}. Your response should include:

1. Synesthesia Model Design (250-300 words):
   a) Explain the key components of your AI model for {t['synesthesia_type']}.
   b) Describe how your model captures the relationship between linguistic elements and sensory experiences.
   c) Detail any novel algorithms or neural network architectures you've incorporated.
   d) Explain how your model accounts for individual variations in synesthetic experiences.

2. Data and Training Process (200-250 words):
   a) Describe the dataset you would use to train your model, including its composition and sources.
   b) Explain any data preprocessing or augmentation techniques specific to modeling synesthesia.
   c) Outline your training process, including any specialized techniques or considerations.
   d) Discuss potential challenges in training and how you would address them.

3. Application to {t['application']} (250-300 words):
   a) Explain how your synesthesia model enhances {t['application']} in {t['target_language']}.
   b) Provide a specific example of how your model would process and analyze this input: "{t['example_input']}"
   c) Describe any unique insights or capabilities your model offers compared to traditional approaches.
   d) Discuss potential limitations or biases in applying your model to this task.

4. Evaluation and Validation (200-250 words):
   a) Propose at least three quantitative metrics to evaluate your model's performance.
   b) Describe a qualitative evaluation method involving human subjects with and without synesthesia.
   c) Explain how you would validate that your model accurately represents synesthetic experiences.
   d) Discuss how you would ensure your model's outputs are reliable and consistent.

5. Ethical Considerations and Broader Impacts (150-200 words):
   a) Discuss potential ethical issues in modeling and applying synesthetic experiences in AI.
   b) Consider the implications of your model for understanding human cognition and perception.
   c) Explore potential applications of your model in fields beyond {t['application']}.
   d) Reflect on how this technology might impact individuals with synesthesia.

Ensure your response demonstrates a deep understanding of linguistic synesthesia, cognitive science principles, and AI technologies. Be creative in your approach while maintaining scientific plausibility. Use clear examples and explanations throughout your response.

Format your response with clear headings for each section and subsection (e.g., '1. Synesthesia Model Design', 'a) Key components'). Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately covers all five required sections, addressing {t['synesthesia_type']}, {t['application']}, and {t['target_language']}.",
            "The AI system design demonstrates a clear understanding of linguistic synesthesia and its potential applications in AI.",
            "The response shows creativity and innovation in the proposed model and its application.",
            f"The submission includes a specific analysis of the example input: \"{t['example_input']}\"",
            "The response addresses potential challenges, limitations, and ethical considerations of the proposed system.",
            "The submission follows the required formatting with clear headings for each section and subsection.",
            "The response maintains scientific plausibility while exploring novel ideas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
