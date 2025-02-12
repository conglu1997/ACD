import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domain_pairs = [
            ("Quantum Mechanics", "Social Networks"),
            ("Ecosystem Dynamics", "Financial Markets"),
            ("Neurobiology", "Urban Planning"),
            ("Plate Tectonics", "Cybersecurity"),
            ("Immunology", "Information Technology")
        ]
        return {
            "1": {"domains": random.choice(domain_pairs)},
            "2": {"domains": random.choice(domain_pairs)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create and analyze a conceptual blend between two complex systems from different domains: {t['domains'][0]} and {t['domains'][1]}.

1. Conceptual Blend (150-200 words):
   a) Identify key concepts, principles, or mechanisms from each domain.
   b) Create a novel conceptual blend that integrates elements from both domains.
   c) Describe the resulting blended system, explaining how components from each domain interact and function together.

2. Analogical Mapping (100-150 words):
   a) Explain the analogical relationships between specific elements of the two domains in your blend.
   b) Discuss how these analogies contribute to the coherence and functionality of the blended system.

3. Potential Applications (100-150 words):
   a) Propose two potential real-world applications or innovations inspired by your conceptual blend.
   b) Explain how each application leverages the unique properties of the blended system.

4. Implications and Limitations (100-150 words):
   a) Discuss potential implications (positive or negative) of implementing your blended system or its applications.
   b) Identify at least two limitations or challenges that might arise from this conceptual integration.

5. Interdisciplinary Insights (100-150 words):
   a) Explain how this conceptual blend might lead to new insights or research directions in either or both of the original domains.
   b) Propose a specific research question or hypothesis that emerges from your conceptual blend.

Ensure your response demonstrates creativity, logical coherence, and a deep understanding of both domains. Use appropriate terminology and provide clear explanations throughout your analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conceptual blend integrates elements from both domains in a novel and coherent manner.",
            "The analogical mapping clearly explains relationships between elements of the two domains.",
            "The proposed applications are innovative and leverage the unique properties of the blended system.",
            "The implications and limitations are thoughtfully considered and relevant to the blend.",
            "The interdisciplinary insights and proposed research question demonstrate a deep understanding of both domains.",
            "The overall response shows creativity, logical coherence, and appropriate use of domain-specific terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
