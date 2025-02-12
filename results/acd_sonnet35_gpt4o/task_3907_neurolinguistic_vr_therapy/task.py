import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        disorders = [
            {
                "name": "Broca's aphasia",
                "description": "Difficulty in speech production and articulation",
                "example_patient": "65-year-old right-handed male, 3 months post-left hemispheric stroke"
            },
            {
                "name": "Wernicke's aphasia",
                "description": "Difficulty in language comprehension",
                "example_patient": "58-year-old right-handed female, 2 months post-left temporal lobe stroke"
            },
            {
                "name": "Global aphasia",
                "description": "Severe impairment in both speech production and comprehension",
                "example_patient": "72-year-old left-handed male, 1 month post-extensive left hemispheric stroke"
            }
        ]
        return {str(i+1): disorder for i, disorder in enumerate(random.sample(disorders, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality-based therapy system that uses neurolinguistic principles and AI to treat {t['name']} ({t['description']}). Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your VR therapy system, including hardware and software elements.
   b) Explain how neurolinguistic principles are incorporated into the system design.
   c) Detail the AI algorithms and techniques used to adapt the therapy to individual patients.
   d) Provide a high-level diagram of your system architecture (describe it textually).

2. Neurolinguistic Approach (250-300 words):
   a) Explain the specific neurolinguistic theories or models your system is based on.
   b) Describe how your approach targets the neural pathways affected by {t['name']}.
   c) Discuss how your system leverages neuroplasticity to promote language recovery.

3. Virtual Reality Environment (250-300 words):
   a) Describe the virtual environments and scenarios used in your therapy system.
   b) Explain how these environments are designed to address {t['name']}.
   c) Discuss how immersion and interactivity in VR contribute to the therapeutic process.
   d) Provide an example of a specific VR scenario designed for {t['name']}.

4. AI-Driven Personalization (250-300 words):
   a) Detail how AI is used to personalize the therapy experience for each patient.
   b) Explain the data collection and analysis processes used to inform treatment.
   c) Describe how the system adapts in real-time to patient progress and challenges.
   d) Discuss the use of natural language processing and computer vision in patient interaction.
   e) Explain how machine learning algorithms are used to predict patient outcomes and optimize treatment plans.

5. Treatment Protocol (250-300 words):
   a) Outline a sample treatment protocol using your system for a patient with {t['name']}.
   b) Describe specific exercises or tasks the patient would perform in the VR environment.
   c) Explain how progress is measured and how the protocol adjusts based on patient performance.
   d) Provide a detailed example of how your system would approach treatment for this patient: {t['example_patient']}.

6. Integration with Other Therapies (150-200 words):
   a) Discuss how your VR system could be integrated with traditional speech and language therapy approaches.
   b) Explain potential synergies with other rehabilitation techniques (e.g., physical therapy, occupational therapy).
   c) Propose a multidisciplinary treatment plan that incorporates your VR system.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues related to using VR and AI in language therapy.
   b) Address any limitations or potential side effects of your approach.
   c) Propose guidelines for responsible implementation and use of your system.

8. Future Developments (150-200 words):
   a) Suggest two potential enhancements or extensions to your system.
   b) Discuss how emerging technologies (e.g., brain-computer interfaces, augmented reality) might be incorporated into future versions.
   c) Propose a research study to validate the effectiveness of your approach.

Ensure your response demonstrates a deep understanding of neurolinguistics, virtual reality technologies, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and therapeutic plausibility.

Format your response with clear headings for each section. Your total response should be between 1750-2150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neurolinguistics, virtual reality technologies, and artificial intelligence.",
            f"The proposed system effectively addresses the treatment of {t['name']}.",
            "The virtual reality environments and scenarios are well-designed and appropriate for language therapy.",
            "The AI-driven personalization approach is sophisticated, well-explained, and includes specific algorithms and techniques.",
            "The treatment protocol is clear, detailed, and based on sound therapeutic principles.",
            f"A specific example of treatment for the given patient ({t['example_patient']}) is provided and well-explained.",
            "The integration with other therapies is thoroughly discussed and demonstrates interdisciplinary knowledge.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The future developments proposed are innovative and plausible.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
