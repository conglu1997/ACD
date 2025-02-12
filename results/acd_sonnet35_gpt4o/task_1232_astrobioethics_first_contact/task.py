import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Europa's subsurface ocean",
            "Martian underground caves",
            "Titan's hydrocarbon lakes",
            "Enceladus' geysers",
            "Venus' upper atmosphere"
        ]
        organism_types = [
            "chemosynthetic",
            "radiation-resistant",
            "silicon-based",
            "ammonia-based",
            "methane-metabolizing"
        ]
        return {
            "1": {"environment": random.choice(environments), "organism_type": random.choice(organism_types)},
            "2": {"environment": random.choice(environments), "organism_type": random.choice(organism_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a comprehensive protocol for first contact with a newly discovered alien microorganism in {t['environment']}. The organism is believed to be {t['organism_type']}. Your protocol should address the following aspects:

1. Scientific Approach (250-300 words):
   a) Describe the methods and technologies you would use to safely detect and study the microorganism.
   b) Explain how you would analyze its biochemistry and potential metabolic processes.
   c) Propose experiments to determine if it meets the criteria for life as we understand it.
   d) Discuss how you would assess potential risks to Earth's biosphere.

2. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of studying and potentially removing samples of the microorganism from its environment.
   b) Discuss the moral status of the microorganism and our ethical obligations towards it.
   c) Address the potential conflicts between scientific curiosity and the preservation of alien ecosystems.
   d) Consider the ethical implications of potential contamination (in both directions).

3. Quarantine and Containment (150-200 words):
   a) Design a quarantine protocol to prevent contamination of Earth or the alien environment.
   b) Describe the containment facilities and procedures necessary for studying the organism.
   c) Explain how you would balance safety concerns with the need for scientific study.

4. Communication and Decision Making (200-250 words):
   a) Propose a framework for making decisions about further interaction with the microorganism.
   b) Describe how you would communicate findings to the scientific community and the public.
   c) Discuss the potential geopolitical implications of the discovery and how to address them.
   d) Explain how you would involve diverse stakeholders in the decision-making process.

5. Long-term Implications (150-200 words):
   a) Analyze the potential long-term effects of this discovery on human society and scientific understanding.
   b) Discuss how this finding might influence our search for life elsewhere in the universe.
   c) Consider the implications for our understanding of the origin and evolution of life.

6. Innovative Proposal (200-250 words):
   a) Propose an innovative method or technology specifically designed for studying this type of microorganism in its environment.
   b) Explain how your proposal addresses the unique challenges presented by the organism and its habitat.
   c) Discuss potential broader applications of your proposed method or technology.

Ensure your response demonstrates a deep understanding of astrobiology, microbiology, and ethical principles. Use appropriate scientific terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section and use numbered or bulleted lists where appropriate. Your total response should be between 1150-1450 words.

IMPORTANT: Do not provide any direct answers or hints that would make the task trivial. Your response should be a well-reasoned, original protocol based on the given scenario and your knowledge of astrobiology and ethics.

Please structure your response as follows:

[Scientific Approach]
(Your content here)

[Ethical Considerations]
(Your content here)

[Quarantine and Containment]
(Your content here)

[Communication and Decision Making]
(Your content here)

[Long-term Implications]
(Your content here)

[Innovative Proposal]
(Your content here)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of astrobiological principles and their application to the given scenario.",
            "The ethical analysis is thorough, considering multiple perspectives and potential consequences.",
            "The proposed scientific methods and experiments are well-reasoned and appropriate for the given environment and organism type.",
            "The quarantine and containment protocols are detailed and address both safety and scientific needs.",
            "The communication and decision-making framework is inclusive and considers various stakeholders.",
            "The analysis of long-term implications shows depth of thought and considers multiple aspects of the discovery's impact.",
            "The innovative proposal is creative, scientifically plausible, and addresses the unique challenges of the scenario.",
            "The response is well-structured, follows the specified format, and falls within the given word count range.",
            "The response specifically addresses the given environment and organism type, demonstrating an understanding of their unique characteristics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
