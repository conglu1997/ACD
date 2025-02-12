class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "focus": "metaphor interpretation",
                "target_metaphor": "Time is a river"
            },
            "2": {
                "focus": "metaphor generation",
                "source_domain": "technology",
                "target_domain": "nature"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = """Design a semantic network-based natural language processing system for metaphor interpretation and generation, then analyze its cognitive implications. Your task has four parts:

1. System Design (250-300 words):
   a) Describe the architecture of your semantic network-based NLP system.
   b) Explain how it represents concepts, relationships, and contextual information.
   c) Detail the algorithms or methods used for metaphor processing.
   d) Discuss how your system integrates principles from cognitive science and linguistics.

2. Metaphor Processing (200-250 words):
   a) {task_specific_instruction}
   b) Provide a step-by-step explanation of how your system processes the metaphor.
   c) Illustrate the resulting semantic network (describe it textually).

3. Cognitive Implications (200-250 words):
   a) Analyze how your system's approach to metaphor processing relates to theories of human cognition.
   b) Discuss potential insights your system might offer into human metaphor comprehension or creation.
   c) Explore any limitations of your system compared to human cognitive capabilities.

4. Evaluation and Expansion (150-200 words):
   a) Propose a method to evaluate the effectiveness of your system.
   b) Suggest how your system could be expanded to handle more complex linguistic phenomena.
   c) Discuss potential applications of your system in AI and cognitive science research.

Ensure your response demonstrates a deep understanding of semantic networks, natural language processing, cognitive science, and linguistics. Be innovative in your approach while maintaining scientific plausibility.
"""

        if t["focus"] == "metaphor interpretation":
            task_specific_instruction = f"Demonstrate how your system would interpret the metaphor: '{t['target_metaphor']}'"
        else:
            task_specific_instruction = f"Show how your system would generate a novel metaphor relating {t['source_domain']} to {t['target_domain']}"

        return base_instructions.format(task_specific_instruction=task_specific_instruction)

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of semantic networks, NLP, cognitive science, and linguistics.",
            "The system design is innovative, well-explained, and scientifically plausible.",
            "The metaphor processing demonstration is clear, detailed, and aligns with the proposed system design.",
            "The analysis of cognitive implications is insightful and well-reasoned.",
            "The evaluation method and expansion ideas are practical and show a good grasp of the field's challenges and potential."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
