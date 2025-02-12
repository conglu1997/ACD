import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "aphasia_type": "Broca's aphasia",
                "brain_region": "left frontal lobe",
                "primary_symptom": "difficulty in speech production"
            },
            {
                "aphasia_type": "Wernicke's aphasia",
                "brain_region": "left temporal lobe",
                "primary_symptom": "impaired language comprehension"
            },
            {
                "aphasia_type": "Global aphasia",
                "brain_region": "extensive damage to language areas",
                "primary_symptom": "severe impairment in both production and comprehension"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that simulates the experience of {t['aphasia_type']}, a type of aphasia affecting the {t['brain_region']} and primarily causing {t['primary_symptom']}. This system should be used for educational and therapeutic purposes. Your response should include the following sections:

1. Neurological Basis (200-250 words):
   a) Explain the neurological mechanisms underlying {t['aphasia_type']}.
   b) Describe how damage to the {t['brain_region']} leads to {t['primary_symptom']}.
   c) Discuss any secondary symptoms or effects associated with this type of aphasia.

2. VR System Design (300-350 words):
   a) Propose a detailed design for the VR system, including hardware and software components.
   b) Explain how the system will simulate the primary symptom of {t['primary_symptom']}.
   c) Describe how the VR environment will represent the user's subjective experience of aphasia.
   d) Include at least one novel feature that leverages VR technology to enhance the simulation's effectiveness.

3. User Experience (200-250 words):
   a) Detail the user's journey through the VR experience, from setup to completion.
   b) Explain how the system will adapt to different user profiles (e.g., medical students, patients' families, speech therapists).
   c) Describe any interactive elements or tasks within the VR environment.

4. Educational and Therapeutic Applications (250-300 words):
   a) Propose specific ways this VR system could be used in medical education.
   b) Suggest how the system might be employed in therapy for aphasia patients.
   c) Discuss potential benefits and limitations of using VR to simulate aphasia.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in simulating a neurological condition.
   b) Propose guidelines for responsible use of the VR aphasia simulator.
   c) Discuss how to ensure the simulation is respectful to individuals with aphasia.

6. Technical Challenges and Solutions (200-250 words):
   a) Identify key technical challenges in implementing this VR system.
   b) Propose innovative solutions to these challenges.
   c) Suggest a method for validating the accuracy of the aphasia simulation.

Ensure your response demonstrates a deep understanding of neurolinguistics, virtual reality technology, and the ethical implications of simulating neurological conditions. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of {t['aphasia_type']} and its neurological basis",
            "The VR system design should be innovative, detailed, and technologically plausible",
            "The user experience should be well-thought-out and adaptable to different user profiles",
            "The educational and therapeutic applications should be specific and well-reasoned",
            "Ethical considerations should be thoroughly addressed",
            "Technical challenges and solutions should be identified and addressed creatively",
            "The response should show interdisciplinary integration of neuroscience, linguistics, and VR technology",
            "The proposed system should be innovative while maintaining scientific accuracy",
            "The response should include all required sections with appropriate word counts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
