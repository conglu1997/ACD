import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "quantum computing operations",
            "multi-dimensional time",
            "non-Euclidean geometry",
            "emotion-based arithmetic"
        ]
        
        tasks = {
            "1": {"domain": random.choice(domains)},
            "2": {"domain": random.choice(domains)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel mathematical notation system for {t['domain']}, then use it to solve related problems. Your task has the following parts:

1. Notation System Design (250-300 words):
   a) Describe your notation system, explaining its basic symbols and rules.
   b) Explain how it represents key concepts in the given domain.
   c) Provide a legend or key for your notation system, including at least 10 symbols or operators.
   d) Provide examples of how basic operations or relationships are expressed.
   e) Discuss any advantages your system has over traditional mathematical notation for this domain.

2. Notation System Justification (150-200 words):
   a) Explain how your notation system reflects or respects the underlying principles of the domain.
   b) Discuss any novel features that make it particularly suited for representing concepts in this area.
   c) Compare your notation system to an existing one in the field, highlighting key differences and improvements.

3. Problem Formulation (100-150 words):
   a) Create two problems in the given domain that can be solved using your notation system:
      - One problem demonstrating a basic concept or operation
      - One problem demonstrating a more complex relationship or process
   b) State these problems first in natural language, then translate them into your notation system.

4. Problem Solving (200-250 words):
   a) Solve the two problems you formulated using your notation system.
   b) Show your work step-by-step, explaining the meaning of each step in natural language.
   c) Translate your final answers back into natural language.

5. System Evaluation (150-200 words):
   a) Reflect on the strengths and limitations of your notation system as revealed by the problem-solving process.
   b) Suggest one way your system could be expanded or improved for broader application.

6. Interdisciplinary Application (100-150 words):
   Propose how your notation system could be applied in a different field or domain, explaining its potential benefits.

Ensure your response demonstrates a deep understanding of mathematical principles and the specific domain. Be creative in your system design while maintaining logical consistency and practical applicability.

Format your response with clear headings for each section and use examples to illustrate your points where appropriate. Use ASCII characters or Unicode symbols for your notation system.

Your total response should be between 950-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a novel and coherent mathematical notation system for the given domain, with a clear legend of at least 10 symbols or operators.",
            "The notation system is logically consistent, clearly explained, and compared to an existing system in the field.",
            "Two problems (one basic, one complex) are correctly formulated and translated into the new notation system.",
            "The problems are solved step-by-step using the new notation, with clear explanations and correct final answers.",
            "The evaluation of the system is thoughtful, identifying genuine strengths and limitations based on the problem-solving experience.",
            "The proposed interdisciplinary application is plausible and demonstrates creative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
