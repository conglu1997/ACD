import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "physical_concept": "AdS/CFT correspondence",
                "computational_aspect": "quantum error correction",
                "application_domain": "cryptography"
            },
            "2": {
                "physical_concept": "black hole information paradox",
                "computational_aspect": "reversible computing",
                "application_domain": "quantum simulation"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a speculative computational paradigm based on the holographic principle from theoretical physics, focusing on the concept of {t['physical_concept']}. Your paradigm should incorporate aspects of {t['computational_aspect']} and explore potential applications in {t['application_domain']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the key aspects of the holographic principle and {t['physical_concept']} relevant to your computational paradigm.
   b) Describe how your paradigm translates these physical concepts into a computational model.
   c) Discuss any novel mathematical or physical formulations required for your paradigm.

2. Computational Architecture (250-300 words):
   a) Outline the basic structure and components of your holographic computation system.
   b) Explain how information is encoded, processed, and retrieved in your paradigm.
   c) Describe how your system incorporates {t['computational_aspect']} and how it differs from conventional computing architectures.

3. Information Processing Capabilities (200-250 words):
   a) Analyze the theoretical advantages and limitations of your holographic computation paradigm.
   b) Compare its potential capabilities to those of classical and quantum computing systems.
   c) Discuss any unique computational problems your paradigm might be particularly suited to solve.

4. Application in {t['application_domain']} (200-250 words):
   a) Propose a specific application of your holographic computation paradigm in {t['application_domain']}.
   b) Explain how this application leverages the unique features of your paradigm.
   c) Discuss potential advantages and challenges of implementing this application.

5. Philosophical and Scientific Implications (200-250 words):
   a) Explore how your holographic computation paradigm might influence our understanding of information, computation, and physical reality.
   b) Discuss any implications for the nature of space, time, and causality.
   c) Consider how this paradigm might impact other scientific fields or technological domains.

6. Technical Challenges and Future Research (150-200 words):
   a) Identify key technical challenges in realizing your holographic computation paradigm.
   b) Propose potential research directions or experiments to address these challenges.
   c) Speculate on how this technology might evolve over the next few decades.

Ensure your response demonstrates a deep understanding of theoretical physics, information theory, and computer science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility and logical consistency.

Your total response should be between 1300-1600 words. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the holographic principle and {t['physical_concept']}",
            f"The computational paradigm effectively incorporates aspects of {t['computational_aspect']}",
            f"The proposed application in {t['application_domain']} is innovative and well-explained",
            "The answer shows creative problem-solving and interdisciplinary knowledge synthesis",
            "The response explores philosophical and scientific implications of the paradigm",
            "Technical challenges and future research directions are identified and discussed",
            "The answer is well-structured, coherent, and adheres to the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
