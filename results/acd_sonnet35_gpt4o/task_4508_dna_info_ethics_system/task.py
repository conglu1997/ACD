import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'info_type': 'Cultural heritage',
                'ethical_concern': 'Privacy and consent',
                'storage_duration': 'Millennia'
            },
            {
                'info_type': 'Scientific knowledge',
                'ethical_concern': 'Equitable access',
                'storage_duration': 'Centuries'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a DNA-based information storage system for preserving human knowledge, focusing on {t['info_type']}. Your system should address the ethical concern of {t['ethical_concern']} and be capable of storing information for {t['storage_duration']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your DNA-based information storage system.
   b) Explain the encoding method for converting {t['info_type']} into DNA sequences.
   c) Detail the storage and retrieval mechanisms, including error correction.
   d) Discuss how your system ensures long-term stability for {t['storage_duration']}.

2. Molecular Biology Principles (250-300 words):
   a) Explain the key molecular biology principles underlying your system.
   b) Discuss any novel DNA manipulation techniques you've incorporated.
   c) Address potential biological challenges and your solutions.

3. Information Theory Application (200-250 words):
   a) Describe how information theory is applied in your encoding scheme.
   b) Analyze the information density and error rates of your system.
   c) Compare your system's efficiency to current digital storage methods.

4. Ethical Analysis (250-300 words):
   a) Thoroughly examine the ethical implications of your system, focusing on {t['ethical_concern']}.
   b) Discuss potential misuse scenarios and proposed safeguards.
   c) Analyze the long-term societal impacts of preserving {t['info_type']} in DNA.

5. Implementation and Accessibility (200-250 words):
   a) Propose a method for implementing your system on a global scale.
   b) Discuss how to ensure equitable access and prevent monopolization.
   c) Address challenges in reading and interpreting the stored information in the distant future.

6. Future Directions and Challenges (150-200 words):
   a) Identify potential advancements that could enhance your system.
   b) Discuss unresolved challenges in DNA-based information storage.
   c) Propose a research agenda to address these challenges.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of molecular biology, information theory, and ethics.",
            "The proposed DNA-based information storage system is innovative, scientifically plausible, and well-justified.",
            "The system architecture effectively addresses the given information type and storage duration.",
            "The ethical analysis thoroughly examines the specified concern and potential societal impacts.",
            "The implementation and accessibility plan is comprehensive and considers global implications.",
            "The response shows strong integration of knowledge from multiple scientific disciplines.",
            "The proposed system addresses potential challenges and includes error correction mechanisms.",
            "The response includes creative solutions while maintaining scientific rigor.",
            "The future directions and challenges section identifies relevant areas for further research.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
