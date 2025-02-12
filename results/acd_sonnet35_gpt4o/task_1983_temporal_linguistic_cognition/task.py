import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        temporal_concepts = [
            "future tense",
            "aspect markers",
            "time metaphors",
            "temporal deixis"
        ]
        cognitive_processes = [
            "planning",
            "memory formation",
            "risk assessment",
            "delay discounting"
        ]
        cultural_contexts = [
            "Western",
            "East Asian",
            "African",
            "Indigenous American"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "temporal_concept": random.choice(temporal_concepts),
                "cognitive_process": random.choice(cognitive_processes),
                "cultural_context": random.choice(cultural_contexts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the relationship between language, temporal cognition, and decision-making, focusing on the following elements:

Temporal Concept: {t['temporal_concept']}
Cognitive Process: {t['cognitive_process']}
Cultural Context: {t['cultural_context']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling temporal linguistic cognition.
   b) Explain how your system incorporates the given temporal concept and its expression in language.
   c) Detail how the system models the specified cognitive process in relation to temporal perception.
   d) Discuss how your system accounts for the influence of the given cultural context.

2. Linguistic-Cognitive Interface (250-300 words):
   a) Explain how your system translates linguistic data into cognitive representations of time.
   b) Describe the mapping between the temporal concept and the cognitive process in your model.
   c) Provide an example of how a specific linguistic expression would be processed and its impact on cognition.

3. Cross-Cultural Analysis (200-250 words):
   a) Compare how your system would model the given temporal concept and cognitive process in the specified cultural context versus another culture of your choice.
   b) Discuss potential differences in decision-making outcomes based on these cultural-linguistic variations.
   c) Analyze the implications of these differences for cross-cultural communication and understanding.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test the predictions of your AI model regarding the influence of the temporal concept on the cognitive process.
   b) Describe the methodology, including participant selection, stimuli, and measurement techniques.
   c) Discuss how you would validate your AI model's predictions against human data.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential biases in your model and how they might be mitigated.
   b) Address ethical implications of using AI to model cultural-linguistic differences in cognition.
   c) Consider limitations of your approach and propose future research directions.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the temporal concept '{t['temporal_concept']}' and its linguistic expression.",
            f"The system effectively models the cognitive process of {t['cognitive_process']} in relation to temporal perception.",
            f"The cultural context of {t['cultural_context']} is thoughtfully incorporated into the model.",
            "The cross-cultural analysis is insightful and well-reasoned.",
            "The proposed experiment is well-designed and appropriate for validating the AI model.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
