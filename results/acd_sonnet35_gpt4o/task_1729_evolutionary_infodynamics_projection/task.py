import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Post-antibiotic world",
            "Extreme climate change scenario",
            "Interplanetary colonization",
            "Technological singularity aftermath"
        ]
        info_dynamics = [
            "Epigenetic information transfer",
            "Quantum coherence in biological systems",
            "Horizontal gene transfer networks",
            "Symbiotic information processing"
        ]
        tasks = {
            "1": {
                "environment": random.choice(environments),
                "info_dynamic": random.choice(info_dynamics),
                "timeframe": f"{random.randint(100, 1000)} years"
            },
            "2": {
                "environment": random.choice(environments),
                "info_dynamic": random.choice(info_dynamics),
                "timeframe": f"{random.randint(100, 1000)} years"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model of information dynamics in biological evolution, focusing on {t['info_dynamic']} in a {t['environment']} scenario. Then, use this model to project evolutionary trajectories over the next {t['timeframe']}. Your response should include:

1. Model Design (250-300 words):
   a) Describe the key components and mechanisms of your evolutionary infodynamics model.
   b) Explain how it incorporates {t['info_dynamic']} and adapts to the {t['environment']} scenario.
   c) Discuss any novel mathematical or computational approaches used in your model.

2. Information Theory Analysis (200-250 words):
   a) Analyze the information flows and transformations in your model using concepts from information theory.
   b) Discuss how these information dynamics might differ from traditional evolutionary models.
   c) Propose a novel metric for quantifying evolutionary information complexity in your model.

3. Evolutionary Trajectory Projection (250-300 words):
   a) Describe the projected evolutionary trajectories for at least three different species or biological systems over the {t['timeframe']} timeframe.
   b) Explain key adaptations or evolutionary innovations that might emerge, given the {t['environment']} scenario.
   c) Discuss any potential evolutionary dead-ends or extinction events predicted by your model.

4. Broader Implications (200-250 words):
   a) Analyze how your model and projections might influence our understanding of evolution and information processing in biological systems.
   b) Discuss potential applications of your model in fields such as synthetic biology, artificial life, or astrobiology.
   c) Address any ethical considerations or potential societal impacts of your evolutionary projections.

5. Model Limitations and Future Research (100-150 words):
   a) Discuss the limitations of your model and evolutionary projections.
   b) Propose two specific areas for future research that could address these limitations or extend your model.

Ensure your response demonstrates a deep understanding of evolutionary biology, information theory, and complex systems modeling. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, information theory, and complex systems modeling",
            "The model design is creative, scientifically plausible, and effectively incorporates the specified information dynamic and environmental scenario",
            "The information theory analysis is insightful and applies relevant concepts to the evolutionary model",
            "The evolutionary trajectory projections are detailed, creative, and logically consistent with the model and scenario",
            "The discussion of broader implications shows thoughtful consideration of the model's potential impact and applications",
            "The response addresses model limitations and proposes relevant future research directions",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The response stays within the specified word limit and follows the required format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
