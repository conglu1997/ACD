import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "environment": "underwater",
                "abstract_concept": "time",
                "reasoning_task": "temporal sequencing"
            },
            {
                "environment": "zero-gravity",
                "abstract_concept": "balance",
                "reasoning_task": "ethical decision-making"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a robotic system that learns and generates novel metaphors based on its physical interactions in a {t['environment']} environment, then use it to solve abstract reasoning tasks related to {t['abstract_concept']}. Your response should include the following sections:

1. Robotic System Design (250-300 words):
   a) Describe the physical components and sensors of your robot, explaining how they allow it to interact with and perceive the {t['environment']} environment.
   b) Explain the robot's learning mechanism for generating metaphors from its physical experiences.
   c) Discuss how the robot's embodied experiences in the {t['environment']} environment might lead to unique metaphors for {t['abstract_concept']}.

2. Metaphor Generation Process (200-250 words):
   a) Provide a step-by-step explanation of how your robot generates metaphors.
   b) Give two examples of novel metaphors your robot might create for {t['abstract_concept']} based on its {t['environment']} experiences.
   c) Explain how these metaphors differ from common human-generated metaphors for {t['abstract_concept']}.

3. Abstract Reasoning Application (200-250 words):
   a) Describe how your robot applies its embodied metaphors to the {t['reasoning_task']} task.
   b) Provide an example of how a generated metaphor could lead to a novel approach or solution in this task.
   c) Discuss potential advantages and limitations of using embodied, robotically-generated metaphors for abstract reasoning.

4. Cognitive Science Implications (150-200 words):
   a) Explain how your robotic system might provide insights into the relationship between physical experiences, language, and abstract thought.
   b) Propose an experiment to test whether your robot's metaphor generation process mirrors human cognitive processes.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using robotically-generated metaphors in human-like reasoning tasks.
   b) Propose two future research directions that could extend or improve your embodied metaphor robotics system.

Ensure your response demonstrates a deep understanding of robotics, embodied cognition, linguistics, and abstract reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Robotic System Design section must clearly explain how the robot interacts with and perceives the {t['environment']} environment.",
            f"The Metaphor Generation Process section should provide plausible examples of novel metaphors for {t['abstract_concept']} based on {t['environment']} experiences.",
            f"The Abstract Reasoning Application section must demonstrate how the generated metaphors are applied to the {t['reasoning_task']} task.",
            "The Cognitive Science Implications section should provide insightful connections between the robotic system and human cognition.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, and critical thinking in robotics, linguistics, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
