import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "relativistic_principle": "Time dilation",
                "cognitive_process": "Decision making",
                "problem_domain": "Stock market prediction"
            },
            {
                "relativistic_principle": "Length contraction",
                "cognitive_process": "Spatial reasoning",
                "problem_domain": "Autonomous vehicle navigation"
            },
            {
                "relativistic_principle": "Relativity of simultaneity",
                "cognitive_process": "Causal reasoning",
                "problem_domain": "Distributed systems optimization"
            },
            {
                "relativistic_principle": "Mass-energy equivalence",
                "cognitive_process": "Resource allocation",
                "problem_domain": "Energy grid management"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that incorporates the principle of {t['relativistic_principle']} from special relativity into its {t['cognitive_process']} process, then analyze how this might affect its problem-solving abilities in the domain of {t['problem_domain']}. Your response should include:

1. Relativistic Principle Overview (150-200 words):
   a) Explain the chosen principle of special relativity.
   b) Discuss its implications in physics and potential analogies in cognition.

2. AI System Design (300-350 words):
   a) Describe the architecture of your AI system that incorporates the relativistic principle.
   b) Explain how the principle is implemented in the system's cognitive processes.
   c) Discuss any novel algorithms or data structures required.
   d) Include a simple diagram or schematic representation of your proposed system (describe it textually).

3. Cognitive Process Analysis (250-300 words):
   a) Analyze how the relativistic principle affects the specified cognitive process.
   b) Compare this to traditional, non-relativistic approaches to the same cognitive task.
   c) Discuss potential advantages and challenges of this relativistic approach.

4. Problem-Solving Application (250-300 words):
   a) Describe how your AI system would approach a specific problem in the given domain.
   b) Explain how the relativistic cognitive process influences problem-solving strategies.
   c) Provide a hypothetical example of the AI's problem-solving process, including sample 'thoughts'.

5. Implications and Limitations (200-250 words):
   a) Discuss the broader implications of incorporating relativistic principles into AI cognition.
   b) Address potential limitations or paradoxes that might arise.
   c) Suggest how this approach might inform our understanding of human cognition or AI development.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI systems with relativistic cognition.
   b) Propose guidelines for responsible development and use of such systems.

7. Future Research Directions (100-150 words):
   a) Suggest areas for future research or expansion of this concept.
   b) Propose one novel research question that arises from your design.

Ensure your response demonstrates a deep understanding of special relativity, cognitive science, and AI systems. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified relativistic principle and its potential applications to AI cognition.",
            "The AI system design is innovative, coherent, and plausibly incorporates the relativistic principle into cognitive processes.",
            "The analysis of how relativistic principles affect cognition and problem-solving is insightful and well-reasoned.",
            "The problem-solving application is creative and clearly illustrates how relativistic cognition might be applied in practice.",
            "The response addresses implications, limitations, and ethical considerations thoughtfully.",
            "The proposed future research directions are novel and thought-provoking.",
            "The overall response is well-structured, coherent, and demonstrates strong interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
