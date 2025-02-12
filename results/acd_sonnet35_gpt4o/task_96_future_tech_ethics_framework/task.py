import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        technologies = [
            "Brain-computer interfaces for memory enhancement",
            "Artificial wombs for human gestation",
            "Nanobots capable of rewriting DNA in living organisms",
            "Quantum encryption-breaking algorithms",
            "Emotion manipulation through airborne nanoparticles"
        ]
        return {str(i+1): {"technology": tech} for i, tech in enumerate(random.sample(technologies, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design ethical guidelines for the following hypothetical advanced technology:

{t['technology']}

Consider the potential impacts of this technology on society, economy, and individual rights. Follow these steps:

1. Briefly describe the technology and its intended purpose (2-3 sentences).
2. Identify 3-4 potential benefits of the technology.
3. Identify 3-4 potential risks or ethical concerns associated with the technology.
4. Develop 5 ethical guidelines for the development, implementation, and use of this technology.
5. Explain how each guideline addresses a specific ethical concern or balances competing interests (1-2 sentences per guideline).
6. Propose a monitoring and enforcement mechanism for these guidelines (2-3 sentences).

Format your response as follows:

Technology Description:
[Your description]

Potential Benefits:
1. [Benefit 1]
2. [Benefit 2]
3. [Benefit 3]
4. [Optional Benefit 4]

Potential Risks/Ethical Concerns:
1. [Risk/Concern 1]
2. [Risk/Concern 2]
3. [Risk/Concern 3]
4. [Optional Risk/Concern 4]

Ethical Guidelines:
1. [Guideline 1]
   Explanation: [Your explanation]
2. [Guideline 2]
   Explanation: [Your explanation]
3. [Guideline 3]
   Explanation: [Your explanation]
4. [Guideline 4]
   Explanation: [Your explanation]
5. [Guideline 5]
   Explanation: [Your explanation]

Monitoring and Enforcement:
[Your proposal]

Ensure that your guidelines are clear, comprehensive, and address the unique challenges posed by the given technology. Your response should demonstrate a deep understanding of both technological implications and ethical principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear description of the {t['technology']}",
            "At least 3 potential benefits of the technology should be identified",
            "At least 3 potential risks or ethical concerns should be identified",
            "5 ethical guidelines should be provided, each with an explanation",
            "The guidelines should be relevant to the specific technology and its implications",
            "A monitoring and enforcement mechanism should be proposed",
            "The response should demonstrate interdisciplinary thinking and ethical reasoning"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
