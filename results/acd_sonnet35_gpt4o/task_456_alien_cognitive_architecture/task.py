import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        perception_modes = [
            {
                'mode': 'quantum_state_detection',
                'information_processing': 'probabilistic_wave_function_collapse',
                'problem': 'interstellar_navigation'
            },
            {
                'mode': 'electromagnetic_field_sensing',
                'information_processing': 'distributed_parallel_processing',
                'problem': 'ecosystem_balance_prediction'
            }
        ]
        return {str(i+1): mode for i, mode in enumerate(random.sample(perception_modes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture for a hypothetical alien species with a fundamentally different way of perceiving and processing information, then use this architecture to solve a complex problem. The alien species has the following characteristics:

- Primary perception mode: {t['mode']}
- Information processing paradigm: {t['information_processing']}
- Complex problem to solve: {t['problem']}

Your response should include:

1. Cognitive Architecture Design (250-300 words):
   a) Describe the key components of the alien cognitive architecture.
   b) Explain how the perception mode and information processing paradigm are integrated into the architecture.
   c) Compare and contrast this architecture with human cognition, highlighting key differences.

2. Information Representation (150-200 words):
   a) Propose a novel way this species might represent and store information.
   b) Explain how this representation system leverages their unique perception and processing capabilities.

3. Decision-Making and Reasoning (200-250 words):
   a) Describe the decision-making and reasoning processes in this cognitive architecture.
   b) Explain how these processes differ from traditional AI approaches.
   c) Provide an example of how a simple decision might be made using this system.

4. Problem-Solving Approach (250-300 words):
   a) Apply the designed cognitive architecture to solve the given complex problem.
   b) Describe the step-by-step approach the alien intelligence would take.
   c) Explain how their unique cognitive architecture provides advantages in solving this problem.

5. Limitations and Adaptations (150-200 words):
   a) Discuss potential limitations of this cognitive architecture.
   b) Propose how the species might compensate for these limitations.
   c) Suggest how the architecture might adapt or evolve over time.

6. Implications for AI and Cognitive Science (150-200 words):
   a) Discuss how studying this hypothetical cognitive architecture could advance our understanding of intelligence and cognition.
   b) Propose two novel AI approaches inspired by this alien cognitive architecture.

Ensure your response is creative yet grounded in principles of cognitive science and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['mode']} and {t['information_processing']} in the context of cognitive architectures.",
            "The proposed cognitive architecture is novel, coherent, and fundamentally different from human cognition.",
            f"The problem-solving approach for {t['problem']} leverages the unique aspects of the designed cognitive architecture.",
            "The response shows critical thinking about the limitations and potential adaptations of the proposed system.",
            "The discussion of implications for AI and cognitive science is insightful and proposes novel ideas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
