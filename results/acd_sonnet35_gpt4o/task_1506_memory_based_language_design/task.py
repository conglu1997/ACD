import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_processes = [
            'episodic memory',
            'semantic memory',
            'working memory',
            'procedural memory'
        ]
        applications = [
            'AI language models',
            'human-computer interfaces',
            'cognitive enhancement technologies',
            'educational systems'
        ]
        constraints = [
            'must not use traditional grammar structures',
            'must incorporate non-linear time perception',
            'must represent emotions as complex memory patterns',
            'must use a non-alphabetic symbol system'
        ]
        tasks = [
            {
                'memory_process': random.choice(memory_processes),
                'application': random.choice(applications),
                'constraint': random.choice(constraints)
            },
            {
                'memory_process': random.choice(memory_processes),
                'application': random.choice(applications),
                'constraint': random.choice(constraints)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language system based on the human memory process of {t['memory_process']}, analyze its cognitive implications, and explore its potential applications in {t['application']}. Your language system must adhere to the following constraint: {t['constraint']}. Your response should include:

1. Language System Design (250-300 words):
   a) Describe the key features and structure of your memory-based language system.
   b) Explain how it incorporates principles of {t['memory_process']}.
   c) Provide at least two concrete examples of how this language would represent and communicate ideas differently from traditional languages. Format each example as follows:
      Traditional language: [example]
      Your memory-based language: [corresponding representation]

2. Cognitive Implications (200-250 words):
   a) Analyze how using this language might affect thought processes and cognitive abilities.
   b) Discuss at least two potential benefits and two potential drawbacks for memory, learning, and problem-solving.
   c) Explain how this language might influence perception and conceptualization of time, space, or causality.

3. Linguistic Analysis (200-250 words):
   a) Compare your memory-based language to existing natural languages in terms of syntax, semantics, and pragmatics.
   b) Discuss how this language handles abstract concepts, emotions, or complex ideas. Provide a specific example for each.
   c) Propose a unique linguistic feature that emerges from basing the language on {t['memory_process']}. Describe its structure and function in detail.

4. Application in {t['application']} (200-250 words):
   a) Explain how your memory-based language could be integrated into {t['application']}.
   b) Describe two potential benefits and two potential challenges of using this language in this context.
   c) Propose an innovative use case that showcases the unique advantages of your language system. Provide a step-by-step explanation of how it would work.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss at least two potential ethical implications of implementing this memory-based language system.
   b) Analyze how it might affect social interactions, cultural transmission, or individual identity.
   c) Propose three specific safeguards or guidelines for responsible development and use of this language system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and the specified application domain. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response and number your examples, benefits, challenges, and safeguards as instructed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system design is creative, coherent, and plausibly based on {t['memory_process']}, while adhering to the constraint: {t['constraint']}.",
            "At least two concrete examples of language representation are provided in the specified format.",
            "The cognitive implications section includes at least two potential benefits and two potential drawbacks.",
            "The linguistic analysis includes specific examples for handling abstract concepts, emotions, and complex ideas.",
            "A unique linguistic feature is proposed and described in detail.",
            f"The application in {t['application']} includes two benefits, two challenges, and a step-by-step explanation of an innovative use case.",
            "At least two ethical implications are discussed, and three specific safeguards or guidelines are proposed.",
            "The response is well-structured, following the outlined format with clear headings for each section and numbered lists where required."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
