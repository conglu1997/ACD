import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "temporal_feature": "Non-linear time expression",
                "cognitive_aspect": "Memory formation and recall",
                "ai_application": "Predictive modeling"
            },
            {
                "temporal_feature": "Quantum superposition of tenses",
                "cognitive_aspect": "Decision-making under uncertainty",
                "ai_application": "Quantum computing in AI"
            },
            {
                "temporal_feature": "Emotional time dilation grammar",
                "cognitive_aspect": "Affective processing of experiences",
                "ai_application": "Emotion-aware AI systems"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language with a unique temporal grammar system based on the concept of {t['temporal_feature']}. Then, analyze its cognitive implications and explore its potential applications in AI development. Your response should include:

1. Language Design (250-300 words):
   - Explain the core principles of your temporal grammar system.
   - Provide 3-5 example sentences in your language with English translations.
   - Describe how your language handles past, present, and future tenses.

2. Cognitive Implications (200-250 words):
   - Analyze how your language might influence speakers' perception of time.
   - Discuss potential effects on {t['cognitive_aspect']}.
   - Explore how this language might shape other cognitive processes.

3. AI Applications (200-250 words):
   - Propose how your language design could be applied to {t['ai_application']}.
   - Explain the potential benefits and challenges of this application.
   - Discuss how it might advance current AI capabilities in this area.

4. Comparative Analysis (150-200 words):
   - Compare your language's approach to time with that of existing human languages.
   - Discuss any similarities or differences with other constructed languages or formal logic systems.

5. Experimental Design (100-150 words):
   - Propose an experiment to test the cognitive effects of your language on human subjects.
   - Outline the methodology and expected outcomes.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence principles. Be creative in your language design while maintaining scientific plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design must incorporate the temporal feature: {t['temporal_feature']}",
            f"The cognitive implications analysis should address: {t['cognitive_aspect']}",
            f"The AI application section must discuss: {t['ai_application']}",
            "The response should demonstrate interdisciplinary knowledge in linguistics, cognitive science, and AI",
            "The language design should be innovative yet logically consistent",
            "The analysis should show depth of thought and consideration of multiple perspectives",
            "The response should be well-structured with clear headings for each section",
            "The total response should be comprehensive, between 900-1150 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
