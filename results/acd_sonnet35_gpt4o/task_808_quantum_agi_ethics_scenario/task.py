class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_advantage": "error correction",
                "agi_capability": "self-improvement",
                "ethical_focus": "privacy and surveillance"
            },
            "2": {
                "quantum_advantage": "optimization",
                "agi_capability": "creative problem-solving",
                "ethical_focus": "economic disruption"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical scenario involving the development of artificial general intelligence (AGI) powered by quantum computing. AGI refers to highly autonomous systems that outperform humans at most economically valuable work.

Your scenario should focus on the following aspects:

Quantum computing advantage: {t['quantum_advantage']}
AGI capability: {t['agi_capability']}
Ethical focus: {t['ethical_focus']}

Your response should include:

1. Scenario Description (200-250 words):
   Describe a plausible scenario where quantum-powered AGI with the specified capability is developed. Explain how the quantum advantage is leveraged and how it enhances the AGI's capabilities. Include a specific example or use case to illustrate your scenario.

2. Technical Analysis (200-250 words):
   Provide a technical explanation of how the quantum computing advantage works in this context and how it specifically enables or enhances the AGI capability. Include at least one relevant quantum computing concept or principle in your explanation.

3. Ethical Implications (200-250 words):
   Analyze the ethical implications of this technology, focusing on the specified ethical concern. Discuss potential positive and negative consequences, and explain how the quantum-AGI combination specifically affects these ethical considerations.

4. Societal Impact (150-200 words):
   Discuss the broader societal impacts of this technology. Consider effects on economics, politics, social structures, or other relevant domains.

5. Risk Assessment and Mitigation (150-200 words):
   Identify key risks associated with the development and deployment of this quantum-powered AGI. Propose at least two specific measures to mitigate these risks.

6. Regulatory Framework (100-150 words):
   Outline a potential regulatory approach for governing the development and use of quantum-powered AGI, addressing the specific ethical focus of your scenario.

7. Future Projections (100-150 words):
   Based on your scenario, make two specific predictions about how quantum-powered AGI might evolve or impact society in the next 50 years.

Ensure your response demonstrates a deep understanding of both quantum computing and artificial general intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and rigorous ethical reasoning.

Format your response using clear headings for each section, numbered exactly as above. Your total response should be between 1100-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and artificial general intelligence.",
            f"The scenario effectively incorporates the specified quantum advantage ({t['quantum_advantage']}) and AGI capability ({t['agi_capability']}).",
            f"The ethical analysis thoroughly addresses the given ethical focus ({t['ethical_focus']}).",
            "The technical explanation includes at least one relevant quantum computing concept or principle.",
            "The response provides creative yet plausible predictions and risk mitigation strategies.",
            "The regulatory framework proposed is relevant to the specific ethical focus and technological scenario.",
            "The scenario description includes a specific example or use case to illustrate the concept.",
            "The overall response is well-structured, coherent, and adheres to the word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
