import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_processes = [
            "Hebbian learning",
            "Predictive coding",
            "Attractor dynamics",
            "Sparse coding"
        ]
        environmental_problems = [
            "Ecosystem restoration",
            "Climate change mitigation",
            "Biodiversity conservation",
            "Pollution reduction"
        ]
        tasks = [
            {
                "neural_process": process,
                "environmental_problem": problem
            } for process in neural_processes for problem in environmental_problems
        ]
        selected_tasks = random.sample(tasks, 2)
        return {"1": selected_tasks[0], "2": selected_tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the neural process of {t['neural_process']} to address the environmental problem of {t['environmental_problem']}. Then, apply your system to a specific challenging scenario within this problem domain. Your response should include:

1. Neuro-Environmental AI System Design (300-350 words):
   a) Explain how you adapt {t['neural_process']} to model environmental processes.
   b) Describe the key components of your AI system and their neuro-inspired functionalities.
   c) Discuss how your system integrates environmental data and knowledge.
   d) Provide a high-level diagram or detailed description of your system's architecture.

2. Neural Process Implementation (250-300 words):
   a) Describe in detail how you implement {t['neural_process']} in your AI system.
   b) Explain how this neural process enhances the system's ability to address {t['environmental_problem']}.
   c) Discuss any novel algorithms or techniques used in your implementation.
   d) Provide a mathematical formulation or pseudo-code snippet that illustrates your approach.

3. Application to Environmental Problem (250-300 words):
   a) Outline how your neuro-environmental AI system addresses {t['environmental_problem']}.
   b) Explain how the implemented neural process provides new insights or approaches to this problem.
   c) Discuss potential advantages and limitations of your neuro-inspired approach compared to traditional methods.
   d) Provide a specific example of how your system would process and analyze relevant environmental data.

4. Challenging Scenario Analysis (200-250 words):
   a) Present a specific, complex scenario within the domain of {t['environmental_problem']}.
   b) Describe how your AI system would approach and analyze this scenario.
   c) Explain the outputs or recommendations your system would provide.
   d) Discuss how the neural process influences the system's performance in this scenario.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns in applying neuro-inspired AI to environmental problems.
   b) Discuss the broader societal implications of using your system for {t['environmental_problem']}.
   c) Propose guidelines for responsible development and use of neuro-environmental AI systems.
   d) Address potential issues of data privacy, bias, or unintended consequences.

6. Future Developments and Interdisciplinary Implications (150-200 words):
   a) Propose two potential extensions or improvements to your neuro-environmental AI system.
   b) Discuss how your approach might be applied to other areas of environmental science or related fields.
   c) Explore potential collaborations between neuroscientists, AI researchers, and environmental scientists that could arise from this work.
   d) Speculate on how this interdisciplinary approach might influence future environmental policy and decision-making.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and environmental science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly address the neural process of {t['neural_process']} and apply it to the environmental problem of {t['environmental_problem']}",
            "The AI system design should demonstrate a strong understanding of both neuroscience and environmental science principles",
            "The neural process implementation should be well-explained and scientifically plausible",
            "The application to the environmental problem should be detailed and demonstrate potential real-world impact",
            "The challenging scenario analysis should be complex and showcase the system's capabilities",
            "Ethical considerations and societal impact should be thoughtfully addressed",
            "Future developments and interdisciplinary implications should be innovative and well-reasoned",
            "The response should demonstrate interdisciplinary thinking by effectively connecting concepts from neuroscience, AI, and environmental science"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
