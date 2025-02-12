import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_load_principles = [
            "Split attention principle",
            "Modality principle",
            "Redundancy principle",
            "Segmenting principle",
            "Pre-training principle",
            "Coherence principle"
        ]
        communication_contexts = [
            "Academic learning",
            "Emergency response",
            "Technical documentation",
            "Cross-cultural dialogue"
        ]
        return {
            "1": {
                "principle": random.choice(cognitive_load_principles),
                "context": random.choice(communication_contexts)
            },
            "2": {
                "principle": random.choice(cognitive_load_principles),
                "context": random.choice(communication_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language optimized for minimal cognitive load based on the {t['principle']} from cognitive load theory, specifically for use in {t['context']}. Your task has five parts:

1. Language Design (250-300 words):
   a) Explain how your language incorporates the {t['principle']} to minimize cognitive load.
   b) Describe the key features of your language, including its phonology, morphology, and syntax.
   c) Provide examples of how these features reduce cognitive load in the context of {t['context']}.
   d) Explain any trade-offs made in your design and justify your decisions.

2. Vocabulary and Concept Representation (200-250 words):
   a) Describe how your language represents and organizes vocabulary.
   b) Explain how complex concepts are formed or expressed.
   c) Provide three example words or phrases in your language, along with their meanings and an explanation of how they embody the {t['principle']}.

3. Learning and Acquisition (200-250 words):
   a) Propose a method for teaching this language that aligns with its cognitive load optimization.
   b) Discuss potential challenges in learning this language and how they might be overcome.
   c) Speculate on how acquisition of this language might differ from natural language acquisition.

4. Practical Application (150-200 words):
   a) Describe a specific scenario in {t['context']} where your language would be particularly effective.
   b) Explain how the language's features would enhance communication or learning in this scenario.
   c) Discuss any potential limitations or drawbacks of using your language in this context.

5. Cognitive Science Implications (200-250 words):
   a) Analyze how your language design might influence cognitive processes related to language use.
   b) Discuss potential implications for memory, attention, and information processing.
   c) Propose an experiment to test the effectiveness of your language in reducing cognitive load.

Ensure your response demonstrates a deep understanding of cognitive load theory, linguistics, and the specific communication context. Be creative in your language design while maintaining scientific plausibility and internal consistency. Use appropriate terminology and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and application of the specified cognitive load principle.",
            "The language design is creative, well-explained, and plausibly optimized for the given communication context.",
            "The analysis of learning, acquisition, and cognitive implications is thorough and scientifically grounded.",
            "The response addresses all five parts of the task comprehensively.",
            "The explanation demonstrates interdisciplinary knowledge of cognitive science, linguistics, and the specific communication context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
