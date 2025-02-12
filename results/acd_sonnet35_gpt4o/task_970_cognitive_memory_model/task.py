import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_types = [
            "Episodic memory",
            "Semantic memory",
            "Procedural memory",
            "Working memory"
        ]
        cognitive_processes = [
            "Attention",
            "Pattern recognition",
            "Decision making",
            "Problem-solving"
        ]
        tasks = {}
        for i in range(2):
            memory = random.choice(memory_types)
            process = random.choice(cognitive_processes)
            tasks[str(i+1)] = {"memory_type": memory, "cognitive_process": process}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model of human {t['memory_type']} that incorporates the cognitive process of {t['cognitive_process']}. Your model should integrate principles from neuroscience, cognitive psychology, and computer science. Provide your response in the following format:

1. Model Architecture (250-300 words):
   a) Describe the key components of your computational memory model.
   b) Explain how these components interact to simulate {t['memory_type']}.
   c) Detail how your model incorporates the cognitive process of {t['cognitive_process']}.
   d) Include a high-level diagram or pseudocode to illustrate your model's architecture.

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your model.
   b) Describe how your model reflects current understanding of brain structure and function related to {t['memory_type']}.
   c) Discuss any novel features in your model that extend beyond current neuroscientific knowledge.

3. Information Processing (200-250 words):
   a) Detail how information is encoded, stored, and retrieved in your model.
   b) Explain how your model handles the integration of new information with existing memories.
   c) Describe how your model simulates the process of memory consolidation and reconsolidation.

4. Cognitive Process Integration (200-250 words):
   a) Explain in detail how your model incorporates the cognitive process of {t['cognitive_process']}.
   b) Discuss how this integration enhances the model's ability to simulate human-like memory function.
   c) Provide an example scenario demonstrating the interaction between {t['memory_type']} and {t['cognitive_process']} in your model.

5. Model Evaluation and Predictions (150-200 words):
   a) Propose a method to evaluate your model's performance in simulating human {t['memory_type']}.
   b) Describe a novel prediction your model makes about human memory or cognition.
   c) Suggest an experiment that could test this prediction in human subjects.

Ensure your response demonstrates a deep understanding of neuroscience, cognitive psychology, and computational modeling. Be creative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear description of a computational model for {t['memory_type']}",
            f"The model should incorporate the cognitive process of {t['cognitive_process']}",
            "The response should demonstrate integration of neuroscience, cognitive psychology, and computer science principles",
            "The model architecture, neuroscientific basis, information processing, and cognitive process integration should be thoroughly explained",
            "A method for model evaluation and a novel prediction should be proposed",
            "The response should be creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
