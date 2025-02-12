import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            {
                "name": "Ergative-Absolutive",
                "features": ["subject of intransitive verb and object of transitive verb marked the same", "agent of transitive verb marked differently"]
            },
            {
                "name": "Topic-Comment",
                "features": ["sentence structure organized around topic and comment", "topic is what the sentence is about, comment provides information about the topic"]
            }
        ]
        reasoning_tasks = [
            "Solve a complex logical puzzle",
            "Analyze and interpret abstract poetry"
        ]
        return {
            "1": {"structure": random.choice(linguistic_structures), "task": random.choice(reasoning_tasks)},
            "2": {"structure": random.choice(linguistic_structures), "task": random.choice(reasoning_tasks)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial cognitive architecture based on the {t['structure']['name']} linguistic structure, and use it to {t['task']}. Your response should include the following sections:

1. Cognitive Architecture Design (300-350 words):
   a) Describe the key components of your cognitive architecture.
   b) Explain how the {t['structure']['name']} structure is incorporated into the architecture.
   c) Discuss how this architecture models key cognitive processes (e.g., memory, attention, reasoning).
   d) Provide a diagram or detailed description of the architecture's structure.

2. Linguistic Integration (250-300 words):
   a) Explain how the following features of the {t['structure']['name']} structure are implemented in your architecture:
      {', '.join(t['structure']['features'])}
   b) Discuss how this linguistic structure influences information processing in your model.
   c) Provide an example of how a simple piece of information would be represented and processed in this architecture.

3. Task Application (250-300 words):
   a) Describe how your cognitive architecture would approach the task: {t['task']}
   b) Explain the step-by-step process the architecture would follow to solve the task.
   c) Discuss any unique advantages or challenges your architecture might face in this task.

4. Comparative Analysis (200-250 words):
   a) Compare your architecture to a traditional cognitive architecture (e.g., ACT-R, SOAR).
   b) Discuss potential advantages and limitations of your linguistically-inspired approach.
   c) Propose an experiment to test the effectiveness of your architecture compared to traditional models.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical implications of creating AI systems based on specific linguistic structures.
   b) Explore the philosophical questions raised by your architecture regarding the relationship between language and cognition.

6. Future Developments (150-200 words):
   a) Propose potential improvements or extensions to your cognitive architecture.
   b) Discuss how this approach could be applied to other areas of AI or cognitive science research.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cognitive architecture effectively incorporates the {t['structure']['name']} linguistic structure",
            "The design demonstrates a deep understanding of cognitive processes and linguistic principles",
            f"The architecture is applied to the task of {t['task']} in a logical and innovative manner",
            "The response includes a comparative analysis with traditional cognitive architectures",
            "Ethical and philosophical implications are thoughtfully discussed",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
