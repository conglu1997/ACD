import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_process": "Horizontal gene transfer in bacteria",
                "optimization_problem": "Protein folding prediction"
            },
            {
                "biological_process": "Epigenetic inheritance in plants",
                "optimization_problem": "Neural network architecture search"
            },
            {
                "biological_process": "Symbiogenesis in eukaryotic cell evolution",
                "optimization_problem": "Multi-agent path finding"
            },
            {
                "biological_process": "Quorum sensing in bacterial colonies",
                "optimization_problem": "Distributed task scheduling"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel evolutionary algorithm inspired by the biological process of {t['biological_process']}, then apply it to solve the optimization problem of {t['optimization_problem']}. Your response should include:

1. Biological Process Analysis (200-250 words):
   a) Explain the key mechanisms and characteristics of {t['biological_process']}.
   b) Discuss how this process differs from traditional evolutionary mechanisms.
   c) Identify aspects of this process that could be beneficial for optimization algorithms.

2. Evolutionary Algorithm Design (250-300 words):
   a) Describe the structure and components of your novel evolutionary algorithm.
   b) Explain how your algorithm incorporates key aspects of {t['biological_process']}.
   c) Discuss any novel operators or mechanisms in your algorithm.
   d) Provide pseudocode for a key component of your algorithm.

3. Application to Optimization Problem (200-250 words):
   a) Briefly describe the {t['optimization_problem']} and its challenges.
   b) Explain how your algorithm is particularly suited to address this problem.
   c) Discuss potential advantages of your approach over traditional evolutionary algorithms.

4. Algorithm Analysis (200-250 words):
   a) Analyze the computational complexity of your algorithm.
   b) Discuss potential limitations or drawbacks of your approach.
   c) Propose methods to evaluate the performance of your algorithm.

5. Comparative Evaluation (150-200 words):
   a) Compare your algorithm to a traditional evolutionary algorithm.
   b) Discuss how your algorithm might perform on other optimization problems.
   c) Propose an experiment to test the efficacy of your algorithm against existing methods.

6. Broader Implications (150-200 words):
   a) Discuss how your algorithm contributes to our understanding of biological processes.
   b) Explore potential applications of your algorithm in other fields.
   c) Propose a future research direction building on your algorithm.

Ensure your response demonstrates a deep understanding of evolutionary computation and biology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the biological process of {t['biological_process']}",
            "The proposed evolutionary algorithm clearly incorporates aspects of the specified biological process",
            f"The algorithm is appropriately applied to the {t['optimization_problem']} problem",
            "The response includes a thorough analysis of the algorithm's complexity and limitations",
            "The comparative evaluation and broader implications sections demonstrate deep understanding and creativity"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
