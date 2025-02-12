class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "organism": "Bacteria",
                "environmental_factor": "Ocean acidification",
                "data_processing_task": "Distributed computing",
                "constraint": "Must operate in deep sea environments (>1000m depth)"
            },
            "2": {
                "organism": "Plants",
                "environmental_factor": "Air pollution",
                "data_processing_task": "Pattern recognition",
                "constraint": "Must be resistant to extreme temperature fluctuations (-20°C to 50°C)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical bio-information network using genetically modified {t['organism']} for environmental monitoring of {t['environmental_factor']} and {t['data_processing_task']}. Your design must adhere to the following constraint: {t['constraint']}.

Your response should include the following sections:

1. Biological System Design (250-300 words):
   a) Describe the genetic modifications you would make to the {t['organism']} to enable environmental sensing and information processing.
   b) Explain how these modifications allow the organisms to detect and respond to {t['environmental_factor']}.
   c) Discuss how your design addresses the given constraint: {t['constraint']}.
   d) Discuss any potential ecological impacts or safety considerations of releasing these modified organisms.

2. Information Encoding and Processing (200-250 words):
   a) Explain how environmental data about {t['environmental_factor']} is encoded in the biological system.
   b) Describe how the organisms perform {t['data_processing_task']} on this data.
   c) Provide a mathematical model or pseudocode representation of the information processing mechanism.
   d) Discuss the theoretical information capacity and processing speed of your bio-network.

3. Network Architecture (200-250 words):
   a) Outline the structure of your bio-information network, including how individual organisms communicate and share data.
   b) Explain how the network aggregates and transmits processed information to human researchers.
   c) Discuss the scalability and resilience of your network design.
   d) Provide a diagram or detailed description of the network topology.

4. Data Interpretation and Application (150-200 words):
   a) Describe how the processed data from your bio-network would be interpreted and used for environmental monitoring.
   b) Explain any advantages this system has over traditional sensing and computing methods for monitoring {t['environmental_factor']}.
   c) Propose a specific environmental management decision that could be informed by your bio-network.
   d) Discuss potential limitations or edge cases where your system might fail or provide inaccurate data.

5. Ethical and Regulatory Considerations (150-200 words):
   a) Discuss the ethical implications of using genetically modified organisms for environmental monitoring and computation.
   b) Propose guidelines for the responsible development and deployment of bio-information networks.
   c) Discuss potential regulatory challenges and how they might be addressed.
   d) Consider the long-term ecological impact of your system and propose mitigation strategies.

6. Future Developments and Challenges (100-150 words):
   a) Suggest potential improvements or extensions to your bio-information network.
   b) Discuss how this technology might evolve over the next decade.
   c) Identify key research challenges that need to be overcome for practical implementation.
   d) Propose a novel application of your bio-information network beyond environmental monitoring.

Ensure your response demonstrates a deep understanding of biotechnology, information theory, and environmental science. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1050-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biotechnology, information theory, and environmental science.",
            "The biological system design is creative, plausible, and addresses the specified environmental factor and constraint.",
            "The information encoding and processing approach is well-explained with a mathematical model or pseudocode representation.",
            "The network architecture is clearly described with a diagram or detailed description of the topology.",
            "The data interpretation and application section provides concrete examples, demonstrates the system's advantages, and discusses limitations.",
            "Ethical and regulatory considerations are thoroughly discussed with thoughtful guidelines and mitigation strategies proposed.",
            "Future developments and challenges are insightfully explored with a novel application proposed.",
            "The response is well-structured, within the specified word count, and uses appropriate terminology.",
            "The response includes all required sections and addresses all points within each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
