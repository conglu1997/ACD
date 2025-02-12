class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "biological_process": "G protein-coupled receptor signaling",
                "application": "Environmental toxin detection"
            },
            "2": {
                "biological_process": "Bacterial quorum sensing",
                "application": "Distributed biocomputing network"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired information processing system based on {t['biological_process']}, then apply it to create a novel {t['application']} device. Your response should include the following sections:

1. Biological Basis (250-300 words):
   a) Explain the key mechanisms and components of {t['biological_process']}.
   b) Describe how this process handles and transmits information at the cellular level.
   c) Discuss any unique features or advantages of this biological information processing system.

2. Bio-inspired System Design (300-350 words):
   a) Outline the architecture of your bio-inspired information processing system.
   b) Explain how you translate biological components and mechanisms into artificial counterparts.
   c) Describe the information flow in your system, drawing parallels to the biological process.
   d) Discuss any novel algorithms or techniques used in your design.
   e) Include a diagram or flowchart illustrating your system's architecture (use ASCII art or a clear textual description).

3. Application to {t['application']} (250-300 words):
   a) Explain how your bio-inspired system can be applied to create a {t['application']} device.
   b) Describe the key features and capabilities of your device.
   c) Discuss potential advantages of your bio-inspired approach compared to traditional methods.
   d) Address any challenges in implementing your design and propose solutions.

4. Information Theory Analysis (200-250 words):
   a) Analyze your system from an information theory perspective.
   b) Discuss concepts such as information encoding, transmission, and processing efficiency.
   c) Compare the information handling capabilities of your system to both biological and traditional artificial systems.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of creating bio-inspired information processing systems.
   b) Address concerns related to synthetic biology and the creation of 'living' computational systems.
   c) Propose guidelines for responsible development and use of such technologies.

6. Future Directions (200-250 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how these developments could enhance performance or expand applications.
   c) Propose an experiment to further explore the potential of your bio-inspired approach.
   d) Speculate on the long-term implications of bio-inspired information processing systems for technology and society.

Ensure your response demonstrates a deep understanding of cellular biology, information theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified biological process and its information processing mechanisms.",
            "The bio-inspired system design effectively translates biological principles into an artificial system.",
            "The application to the specified device is innovative and plausible.",
            "The information theory analysis is thorough and insightful.",
            "Ethical considerations are thoughtfully addressed.",
            "Future directions are creative and well-reasoned.",
            "The overall response shows strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
