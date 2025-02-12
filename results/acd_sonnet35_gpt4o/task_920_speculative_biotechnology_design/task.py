import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_principles = [
            {
                "principle": "Epigenetics",
                "description": "The study of heritable changes in gene expression that do not involve changes to the underlying DNA sequence."
            },
            {
                "principle": "Synthetic Biology",
                "description": "The design and construction of new biological parts, devices, and systems, or the re-design of existing natural biological systems for useful purposes."
            },
            {
                "principle": "Biomimicry",
                "description": "The imitation of models, systems, and elements of nature for the purpose of solving complex human problems."
            },
            {
                "principle": "Optogenetics",
                "description": "The use of light to control cells in living tissue, typically neurons, that have been genetically modified to express light-sensitive ion channels."
            }
        ]
        return {
            "1": random.choice(biological_principles),
            "2": random.choice(biological_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel biotechnology based on the biological principle of {t['principle']}. Your task is to create a detailed proposal for this speculative biotechnology, addressing the following points:

1. Technology Overview (200-250 words):
   - Describe your proposed biotechnology, explaining how it incorporates {t['principle']}.
   - Outline the key components or processes involved in your technology.
   - Explain how your technology builds upon or extends current understanding of {t['principle']}.

2. Potential Applications (200-250 words):
   - Propose at least three potential applications of your biotechnology in different fields (e.g., medicine, agriculture, environmental science).
   - For each application, explain how it could address a current challenge or create new opportunities.
   - Discuss any potential advantages your technology might have over existing solutions.

3. Technical Challenges (150-200 words):
   - Identify at least two major technical challenges in developing and implementing your biotechnology.
   - Propose potential solutions or research directions to address these challenges.
   - Discuss any limitations or constraints of your technology.

4. Ethical Implications (200-250 words):
   - Analyze at least three potential ethical issues raised by your proposed biotechnology.
   - Discuss how these ethical concerns might be addressed or mitigated.
   - Consider both short-term and long-term ethical implications of widespread adoption of your technology.

5. Regulatory Considerations (150-200 words):
   - Propose a framework for regulating the development and use of your biotechnology.
   - Discuss potential safety measures and testing protocols that should be implemented.
   - Consider how existing regulatory bodies and ethical guidelines might need to adapt to address your technology.

6. Societal Impact (150-200 words):
   - Speculate on how your biotechnology might impact society if widely adopted.
   - Discuss potential changes in human behavior, social structures, or cultural norms that might result from your technology.
   - Consider both positive and negative potential consequences of your biotechnology.

Ensure your response demonstrates a deep understanding of the biological principle, as well as its potential technological applications. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['principle']} and its potential technological applications.",
            "The proposed biotechnology is innovative and scientifically plausible.",
            "The potential applications are diverse and well-explained, addressing current challenges or creating new opportunities.",
            "Technical challenges are thoughtfully considered, with plausible solutions or research directions proposed.",
            "The ethical analysis is thorough, considering multiple perspectives and both short-term and long-term implications.",
            "The proposed regulatory framework and safety measures are appropriate and well-reasoned.",
            "The discussion of societal impact is insightful, considering both positive and negative potential consequences.",
            "The response maintains scientific rigor while showcasing creativity in technology design and problem-solving.",
            "The response is well-structured and addresses all required points comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
