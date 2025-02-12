import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_problems = [
            "ocean plastic pollution",
            "urban air pollution",
            "soil degradation in agriculture",
            "freshwater scarcity",
            "deforestation"
        ]
        return {
            "1": {"problem": random.choice(environmental_problems)},
            "2": {"problem": random.choice(environmental_problems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel biomimetic solution to address the environmental problem of {t['problem']}. Your response should demonstrate interdisciplinary knowledge and creative problem-solving. Complete the following five parts, adhering to the specified word limits:

1. Problem Analysis (150-200 words):
   a) Describe the environmental problem and its key challenges.
   b) Identify the main factors contributing to this problem.
   c) Explain why current solutions are inadequate or insufficient.

2. Biological Inspiration (200-250 words):
   a) Identify at least two natural systems or organisms that have evolved solutions relevant to this problem.
   b) Describe how these biological models address similar challenges in nature.
   c) Explain the key principles or mechanisms that make these natural solutions effective.

3. Biomimetic Solution Design (250-300 words):
   a) Propose a novel solution that mimics or draws inspiration from your chosen biological models.
   b) Describe how your solution works, including its key components and mechanisms.
   c) Explain how your design incorporates the principles observed in nature.
   d) Discuss how your solution addresses the specific challenges of the environmental problem.
   e) Provide a detailed illustration or diagram of your solution (describe it textually).

4. Feasibility and Implementation (200-250 words):
   a) Assess the technical feasibility of your proposed solution.
   b) Identify potential challenges in implementing your solution at scale.
   c) Propose strategies to overcome these challenges.
   d) Discuss any ethical considerations or potential unintended consequences of your solution.

5. Impact Analysis (150-200 words):
   a) Predict the potential environmental impact of your solution if successfully implemented.
   b) Discuss any additional benefits your solution might offer beyond addressing the primary problem.
   c) Compare the potential effectiveness of your biomimetic solution to existing approaches.
   d) Provide a quantitative estimate of the solution's potential impact (e.g., percentage reduction in pollution, increase in resource efficiency).

Ensure your response demonstrates a deep understanding of biological systems, environmental science, and engineering principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from relevant fields and provide clear explanations for your design choices.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The solution specifically addresses the environmental problem of {t['problem']} with a clear understanding of its challenges and contributing factors.",
            "The biological inspiration is thoroughly explained, with at least two relevant natural systems or organisms identified and their principles clearly linked to the problem.",
            "The biomimetic solution demonstrates creative application of natural principles, with a detailed description of its mechanisms and a clear illustration or diagram.",
            "The feasibility analysis is comprehensive, addressing technical challenges, scalability issues, and ethical considerations.",
            "The impact analysis provides well-reasoned predictions, including a quantitative estimate of the solution's potential effects.",
            "The response demonstrates interdisciplinary knowledge, effectively integrating concepts from biology, environmental science, and engineering.",
            "The submission adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
