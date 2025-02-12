import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_theories = [
            "Plutchik's Wheel of Emotions",
            "Dimensional Theory of Emotion",
            "Cognitive Appraisal Theory"
        ]
        linguistic_frameworks = [
            "Cognitive Linguistics",
            "Systemic Functional Linguistics",
            "Construction Grammar"
        ]
        scenarios = [
            "A person receiving unexpected news",
            "An individual facing a moral dilemma",
            "Someone experiencing a bittersweet moment"
        ]
        
        return {
            "1": {
                "emotional_theory": random.choice(emotional_theories),
                "linguistic_framework": random.choice(linguistic_frameworks),
                "scenario": random.choice(scenarios)
            },
            "2": {
                "emotional_theory": random.choice(emotional_theories),
                "linguistic_framework": random.choice(linguistic_frameworks),
                "scenario": random.choice(scenarios)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze language expressing complex emotional states, based on the following specifications:

Emotional Theory: {t['emotional_theory']}
Linguistic Framework: {t['linguistic_framework']}
Scenario: {t['scenario']}

Your task has the following parts:

1. Theoretical Foundation (200-250 words):
   a) Briefly explain the key concepts of the given emotional theory and linguistic framework.
   b) Discuss how these two approaches can be integrated to understand and generate emotional language.
   c) Explain how this integration could be particularly relevant for the given scenario.

2. AI System Design (250-300 words):
   a) Outline the main components of your AI system, including data input, processing, and output generation.
   b) Explain how your system would incorporate the emotional theory and linguistic framework.
   c) Describe the system's approach to generating emotionally nuanced language for the given scenario.
   d) Discuss how the system would analyze and interpret emotional language input by users.

3. Example Output (150-200 words):
   Provide a sample dialogue or monologue (5-7 sentences) that your AI system might generate for the given scenario. Explain how this output demonstrates the integration of the emotional theory and linguistic framework.

4. Evaluation Metrics (150-200 words):
   a) Propose 3-4 specific metrics to evaluate the performance of your AI system.
   b) Explain how each metric relates to the emotional theory, linguistic framework, or the system's overall goals.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of an AI system that generates and analyzes emotional language.
   b) Address concerns about privacy, manipulation, or misuse of emotional data.
   c) Propose safeguards or guidelines for responsible use of your system.

6. Future Developments (100-150 words):
   Suggest two potential improvements or expansions for your system, explaining how they would enhance its capabilities in emotional language processing or generation.

Ensure your response demonstrates a deep understanding of the specified emotional theory, linguistic framework, and AI capabilities. Be creative in your approach while grounding your ideas in established theories and ethical considerations.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the given emotional theory and linguistic framework.",
            "The AI system design effectively integrates the emotional theory and linguistic framework.",
            "The example output clearly illustrates the application of the emotional theory and linguistic framework in the given scenario.",
            "The proposed evaluation metrics are relevant and well-justified.",
            "The ethical considerations are thoughtfully addressed with appropriate safeguards suggested.",
            "The suggested future developments are innovative and relevant to the system's goals."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
