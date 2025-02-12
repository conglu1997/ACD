import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_states = [
            "Stress",
            "Flow",
            "Fatigue",
            "Curiosity"
        ]
        language_aspects = [
            "Vocabulary acquisition",
            "Grammar comprehension",
            "Idiomatic expressions",
            "Phonological awareness"
        ]
        applications = [
            "Second language learning",
            "Aphasia rehabilitation",
            "Cultural immersion training",
            "Cognitive flexibility enhancement"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "cognitive_state": random.choice(cognitive_states),
                "language_aspect": random.choice(language_aspects),
                "application": random.choice(applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality linguistic landscape that adapts to users' cognitive state of {t['cognitive_state']} and focuses on the language aspect of {t['language_aspect']}. Then, analyze its potential application in {t['application']}. Your response should include:

1. VR Landscape Design (250-300 words):
   a) Describe the key features of your VR linguistic landscape.
   b) Explain how it adapts to the specified cognitive state.
   c) Detail how it addresses the chosen language aspect.
   d) Provide a brief sensory description of the user's experience in this VR environment.

2. Cognitive-Linguistic Integration (200-250 words):
   a) Analyze how your design leverages principles from cognitive science and linguistics.
   b) Explain the theoretical basis for the adaptation mechanisms in your VR environment.
   c) Discuss any potential cognitive or linguistic challenges users might face and how your design addresses them.

3. Technology Specifications (150-200 words):
   a) Describe the key technologies required to implement your VR linguistic landscape.
   b) Explain any novel or speculative technologies you've incorporated.
   c) Discuss potential technical challenges and how they might be overcome.

4. Application Analysis (200-250 words):
   a) Explain how your VR linguistic landscape could be applied to {t['application']}.
   b) Provide a specific scenario or use case for this application.
   c) Discuss potential benefits and limitations of using your VR environment in this context.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to your VR linguistic landscape.
   b) Discuss privacy concerns, particularly regarding cognitive state monitoring.
   c) Propose guidelines for responsible development and use of such technology.

6. Future Research Directions (100-150 words):
   a) Suggest two potential research projects that could further explore or validate your VR linguistic landscape.
   b) Briefly describe the methodology and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and virtual reality technology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1000-1300 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a VR linguistic landscape that adapts to the cognitive state of {t['cognitive_state']} and focuses on {t['language_aspect']}",
            f"The design should be creative and plausible, integrating principles from cognitive science and linguistics",
            "The response should thoroughly analyze the application of the VR environment to the specified area",
            "The technology specifications should be detailed and include novel or speculative elements",
            "Ethical considerations should be thoughtfully addressed",
            "The proposed future research directions should be relevant and well-described",
            "The overall response should demonstrate interdisciplinary thinking and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
