import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        adaptive_problems = [
            "dynamic resource allocation in a changing environment",
            "real-time language translation in a multilingual context",
            "adaptive traffic management in a smart city",
            "personalized learning in an AI-driven education system"
        ]
        neuroplasticity_mechanisms = [
            "synaptic pruning",
            "long-term potentiation",
            "neurogenesis",
            "axon guidance"
        ]
        return {
            "1": {
                "adaptive_problem": random.choice(adaptive_problems),
                "neuroplasticity_mechanism": random.choice(neuroplasticity_mechanisms)
            },
            "2": {
                "adaptive_problem": random.choice(adaptive_problems),
                "neuroplasticity_mechanism": random.choice(neuroplasticity_mechanisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic computing architecture inspired by neuroplasticity, then use it to solve the complex adaptive problem of {t['adaptive_problem']}. Your architecture should specifically incorporate the neuroplasticity mechanism of {t['neuroplasticity_mechanism']}. Your response should include the following sections:

1. Architecture Design (300-350 words):
   a) Describe the key components and structure of your neuroplastic computing architecture.
   b) Explain how your architecture incorporates the specified neuroplasticity mechanism.
   c) Detail how your system mimics the brain's ability to rewire itself and adapt to new information.
   d) Include a diagram or pseudocode (10-15 lines) to illustrate your architecture's structure and function. If using a diagram, describe it in words as well.

2. Neuroplasticity Integration (200-250 words):
   a) Analyze how the chosen neuroplasticity mechanism is implemented in your computing architecture.
   b) Explain the advantages this mechanism provides in terms of adaptability and learning.
   c) Discuss any challenges in translating this biological process into a computational model.

3. Problem Solution (250-300 words):
   a) Apply your neuroplastic computing architecture to solve the given adaptive problem.
   b) Explain how your architecture's adaptive capabilities are particularly suited to this problem.
   c) Provide a step-by-step description of how your system would approach and adapt to the problem.
   d) Discuss any potential advantages your approach might have over traditional computing methods.

4. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate the performance and adaptability of your architecture.
   b) Hypothesize about the expected performance of your system compared to traditional approaches.
   c) Discuss potential limitations or challenges in implementing and scaling your architecture.

5. Broader Implications (150-200 words):
   a) Explore how your neuroplastic computing architecture might impact the field of artificial intelligence.
   b) Discuss potential applications of your architecture in other domains or industries.
   c) Speculate on how this approach might influence our understanding of cognition and learning.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical issues in developing and deploying neuroplastic computing systems.
   b) Propose guidelines for responsible development and use of these technologies.
   c) Suggest future research directions to further advance neuroplastic computing.

7. Conclusion (50-100 words):
   Summarize the key points of your neuroplastic computing architecture design and its potential impact on solving adaptive problems and advancing the field of biomimetic computing.

Ensure your response demonstrates a deep understanding of both neuroscience and computer science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed neuroplastic computing architecture that clearly incorporates the specified neuroplasticity mechanism, with a detailed diagram or pseudocode.",
            "The neuroplasticity integration section provides a thorough analysis of how the chosen mechanism is implemented and its advantages.",
            "The problem solution demonstrates a coherent and logical application of the neuroplastic architecture to address the given adaptive problem, with a clear step-by-step description.",
            "The performance analysis section proposes specific metrics and provides a thoughtful discussion of the architecture's potential performance and limitations.",
            "The broader implications and ethical considerations sections demonstrate critical thinking about the potential impact and responsible development of neuroplastic computing systems.",
            "The conclusion effectively summarizes the key points of the design and its potential impact.",
            "The overall response is well-structured, coherent, and adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
