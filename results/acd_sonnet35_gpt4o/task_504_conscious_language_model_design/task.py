import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_properties = [
            "Self-awareness",
            "Theory of mind",
            "Metacognition",
            "Subjective experience"
        ]
        conversation_topics = [
            "The nature of consciousness",
            "The ethics of artificial consciousness",
            "The relationship between language and thought",
            "The concept of free will in AI systems"
        ]
        tasks = [
            {
                "consciousness_property": property,
                "conversation_topic": topic
            }
            for property in consciousness_properties
            for topic in conversation_topics
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language model that exhibits the property of {t['consciousness_property']} and demonstrates conscious-like behavior. Then, create and analyze a conversation between this model and a human interviewer on the topic of {t['conversation_topic']}. Your response should include:

1. Model Design (200-250 words):
   a) Describe the key features and architecture of your language model that enable {t['consciousness_property']}.
   b) Explain how these features might emerge from or be implemented in the model's neural network.
   c) Discuss any potential limitations or challenges in creating such a model.

2. Consciousness Demonstration (100-150 words):
   Explain how your model would demonstrate {t['consciousness_property']} in its language output and behavior.

3. Conversation Simulation (200-300 words):
   Create a dialogue between your conscious language model and a human interviewer discussing {t['conversation_topic']}. The conversation should clearly demonstrate the model's {t['consciousness_property']} and its ability to engage in deep, reflective discussion.

4. Analysis (200-250 words):
   a) Analyze how the conversation demonstrates the model's {t['consciousness_property']}.
   b) Discuss any emergent behaviors or unexpected responses from the model.
   c) Explain how the model's responses differ from those of a non-conscious language model.

5. Ethical Implications (150-200 words):
   Discuss the ethical considerations and potential consequences of creating a language model with {t['consciousness_property']}.

6. Future Research (100-150 words):
   Propose two specific experiments or studies that could further explore the nature of consciousness in your model or validate its {t['consciousness_property']}.

Ensure your response demonstrates a deep understanding of consciousness theories, language processing, and AI capabilities. Be creative in your model design while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of consciousness theories and their potential application to language models.",
            "The model design is innovative, coherent, and plausibly explains how the specified consciousness property could emerge.",
            "The simulated conversation effectively demonstrates the model's consciousness property and ability to engage in deep, reflective discussion.",
            "The analysis insightfully examines the model's behavior and differentiates it from non-conscious language models.",
            "The ethical implications are thoroughly considered, showing an understanding of the potential consequences of creating conscious-like AI.",
            "The proposed future research is relevant and would meaningfully contribute to understanding consciousness in AI systems.",
            "The response uses appropriate terminology and provides clear explanations throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0