import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            "Bacteriophage",
            "White blood cell",
            "Mitochondria",
            "Flagellated bacteria",
            "Enzyme"
        ]
        medical_interventions = [
            "Targeted drug delivery",
            "Cancer cell destruction",
            "Blood clot removal",
            "Cellular repair",
            "Pathogen elimination"
        ]
        
        tasks = {}
        for i in range(2):
            inspiration = random.choice(biological_inspirations)
            intervention = random.choice(medical_interventions)
            tasks[str(i+1)] = {
                "biological_inspiration": inspiration,
                "medical_intervention": intervention
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic nanorobot system inspired by {t['biological_inspiration']}, capable of performing {t['medical_intervention']} at the cellular level. Your response should include the following sections:

1. Nanorobot Design (300-350 words):
   a) Describe the key components and structure of your nanorobot.
   b) Explain how your design mimics the biological inspiration.
   c) Discuss how your nanorobot will perform the specified medical intervention.
   d) Include a brief description of a diagram representing your nanorobot's structure.

2. Biomimetic Principles (200-250 words):
   a) Analyze the specific biological mechanisms or features you're mimicking.
   b) Explain how these natural principles are translated into your nanorobot design.
   c) Discuss any challenges in adapting biological processes to nanoscale engineering.

3. Operational Mechanism (200-250 words):
   a) Describe in detail how your nanorobot navigates within the body.
   b) Explain the mechanism by which it identifies its target.
   c) Detail the process of performing the medical intervention.

4. Materials and Fabrication (150-200 words):
   a) Specify the materials used in your nanorobot design.
   b) Propose a method for fabricating your nanorobot.
   c) Discuss any novel materials or fabrication techniques required.

5. Control and Communication (150-200 words):
   a) Explain how the nanorobot is controlled or programmed.
   b) Describe any communication mechanisms between the nanorobot and external systems.
   c) Discuss how multiple nanorobots might coordinate their actions.

6. Safety and Ethical Considerations (150-200 words):
   a) Analyze potential risks or side effects of your nanorobot system.
   b) Propose safety mechanisms to prevent unintended consequences.
   c) Discuss ethical implications of deploying such nanorobots in medical treatments.

7. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your nanorobot design.
   b) Discuss how this technology might evolve over the next decade.

Ensure your response demonstrates a deep understanding of nanotechnology, biology, and medical science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of both the biological inspiration and the medical intervention",
            "The nanorobot design effectively mimics the specified biological system and addresses the given medical intervention",
            "The explanation of biomimetic principles shows a deep understanding of how biological processes can be adapted to nanotechnology",
            "The operational mechanism is logically sound and aligns with current scientific understanding",
            "The materials and fabrication methods proposed are plausible and well-justified",
            "The control and communication systems are well-thought-out and appropriate for the nanorobot's function",
            "Safety and ethical considerations are thoroughly addressed",
            "The response shows creativity and innovation while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
