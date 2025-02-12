import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Detect and respond to environmental pollutants",
            "Produce a specific protein on demand",
            "Create a biological oscillator",
            "Design a cellular memory system",
            "Implement a biological logic gate"
        ]
        cellular_contexts = ["E. coli", "S. cerevisiae", "Mammalian cells", "Plant cells"]
        constraints = [
            "Minimize metabolic burden on the host cell",
            "Ensure orthogonality with host systems",
            "Maximize stability and robustness",
            "Optimize for rapid response time",
            "Design for scalability and modularity"
        ]
        genetic_components = [
            "LacI repressor",
            "TetR repressor",
            "Green Fluorescent Protein (GFP)",
            "Luciferase",
            "CRISPRi system"
        ]
        
        return {
            "1": {
                "problem": random.choice(problems),
                "context": random.choice(cellular_contexts),
                "constraint": random.choice(constraints),
                "component": random.choice(genetic_components)
            },
            "2": {
                "problem": random.choice(problems),
                "context": random.choice(cellular_contexts),
                "constraint": random.choice(constraints),
                "component": random.choice(genetic_components)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a synthetic biological circuit to {t['problem']} in {t['context']}, while addressing the constraint: {t['constraint']}. Your circuit must incorporate the genetic component: {t['component']}. Your task has the following parts:\n\n1. Circuit Design (200-250 words):\n   a) Describe the overall architecture of your synthetic biological circuit.\n   b) Explain the key genetic components used in your design, including how you've incorporated {t['component']}.\n   c) Provide a simple diagram or schematic representation of your circuit.\n\n2. Functional Analysis (150-200 words):\n   a) Explain how your circuit achieves the desired function.\n   b) Discuss potential interactions between your circuit and the host cell's systems.\n   c) Address how your design meets the given constraint.\n\n3. Performance Prediction (150-200 words):\n   a) Predict the behavior of your circuit under different conditions (e.g., high/low input signal, varying cellular resources).\n   b) Describe potential failure modes and how they might be mitigated.\n   c) Suggest specific experiments to validate the circuit's performance.\n\n4. Ethical and Safety Considerations (100-150 words):\n   a) Discuss potential biosafety concerns related to your circuit.\n   b) Address any ethical implications of implementing your design.\n   c) Propose containment or control measures to ensure responsible use.\n\n5. Future Improvements and Applications (100-150 words):\n   a) Suggest ways to optimize or expand your circuit's functionality.\n   b) Discuss potential applications of your circuit beyond the initial problem.\n   c) Propose how your design could be integrated with other synthetic biology tools or systems.\n\nEnsure your response demonstrates a deep understanding of molecular biology, genetic engineering principles, and systems biology. Use appropriate scientific terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining biological plausibility and addressing real-world constraints.\n\nFormat your response with clear headings for each section, and include a brief summary (50-75 words) at the beginning of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The circuit design effectively addresses the problem: {t['problem']}",
            f"The design is appropriate for the given cellular context: {t['context']}",
            f"The solution adequately addresses the constraint: {t['constraint']}",
            f"The genetic component {t['component']} is effectively incorporated and its role is clearly explained",
            "The circuit design is clearly explained and includes all required components",
            "The functional analysis demonstrates a deep understanding of synthetic biology principles",
            "The performance prediction includes specific conditions and potential failure modes",
            "Proposed experiments for validation are specific and appropriate",
            "Ethical and safety considerations are thoroughly addressed with specific containment measures",
            "Future improvements and applications are innovative, plausible, and well-explained",
            "The response demonstrates interdisciplinary knowledge application",
            "The overall design is creative while maintaining biological feasibility",
            "The response follows the required format, including a brief summary and clear section headings"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
