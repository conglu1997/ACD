import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation",
            "olfaction",
            "magnetoreception in birds"
        ]
        return {
            "1": {"process": random.choice(biological_processes)},
            "2": {"process": random.choice(biological_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based AI system to model and simulate the biological process of {t['process']} at the quantum level. While a 45-minute time constraint is mentioned to simulate real-world conditions, please note that this is not strictly enforced in this context. Your response should include:

1. Quantum Biology Framework (250-300 words):
   a) Explain at least three quantum phenomena relevant to {t['process']}.
   b) Describe how these quantum effects influence the biological process, providing specific examples.
   c) Discuss current scientific understanding, citing at least two recent (past 5 years) peer-reviewed studies.
   d) Identify one major controversy or unanswered question in this area.

2. AI System Design (300-350 words):
   a) Outline the architecture of your quantum-based AI system, including specific quantum algorithms or models used.
   b) Explain how it models both quantum and biological aspects of {t['process']}, detailing the integration approach.
   c) Describe at least two novel algorithms or approaches used in your system, justifying their selection.
   d) Discuss how your system handles the transition between quantum and classical scales, addressing any potential limitations.

3. Simulation Details (250-300 words):
   a) Describe at least five key parameters and variables in your simulation, explaining their significance.
   b) Explain how your system would visualize or represent the quantum biological process, proposing an innovative visualization technique.
   c) Discuss the computational resources required for your simulation, including quantum hardware specifications.
   d) Propose a method to validate the accuracy of your simulation against experimental data.

4. Predictive Capabilities (200-250 words):
   a) Explain how your system could be used to make at least three specific predictions about {t['process']}.
   b) Propose a detailed hypothesis that your system could test, including expected outcomes.
   c) Describe an experiment to validate your system's predictions, including methodology and potential challenges.

5. Novel Insights (250-300 words):
   a) Based on your simulation, propose a new biological mechanism or therapeutic approach related to {t['process']}.
   b) Explain the reasoning behind your proposal, citing relevant quantum biological principles.
   c) Discuss potential implications of your proposal on current scientific understanding or medical treatments.
   d) Address at least three ethical considerations related to your proposal and suggest mitigation strategies.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and computational modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary. Cite at least five relevant peer-reviewed sources throughout your response.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1250-1500 words. Include a word count at the end of your response.

IMPORTANT: Your response should be complete and coherent. Do not include any placeholder text or incomplete sections."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Explains at least three quantum phenomena relevant to the given biological process",
            "Cites at least two recent (past 5 years) peer-reviewed studies in the Quantum Biology Framework section",
            "Describes at least two novel algorithms or approaches in the AI System Design section",
            "Describes at least five key parameters and variables in the Simulation Details section",
            "Proposes at least three specific predictions in the Predictive Capabilities section",
            "Addresses at least three ethical considerations in the Novel Insights section",
            "Cites at least five relevant peer-reviewed sources throughout the response",
            "Demonstrates a deep understanding of quantum mechanics, biology, and computational modeling",
            "Presents innovative yet scientifically plausible ideas and approaches",
            "Uses appropriate scientific terminology and provides necessary explanations",
            "Maintains logical consistency and coherence throughout the response",
            "Adheres to the specified word count (1250-1500 words) and formatting requirements",
            "Does not contain any placeholder text or incomplete sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
