import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'scenario': 'Global Resource Allocation',
                'quantum_principle': 'Superposition',
                'geopolitical_context': 'Post-scarcity economy'
            },
            {
                'scenario': 'Diplomatic Negotiations',
                'quantum_principle': 'Entanglement',
                'geopolitical_context': 'Multi-polar world order'
            },
            {
                'scenario': 'Cybersecurity Arms Race',
                'quantum_principle': 'Quantum Key Distribution',
                'geopolitical_context': 'Emerging AI superpowers'
            },
            {
                'scenario': 'Space Colonization',
                'quantum_principle': 'Quantum Tunneling',
                'geopolitical_context': 'Interplanetary relations'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a geopolitical strategy game that incorporates quantum computing principles, then analyze optimal strategies for the following scenario: {t['scenario']}. Your response should include:

1. Game Design (300-350 words):
   a) Describe the core mechanics of your geopolitical strategy game.
   b) Explain how you've incorporated the quantum principle of {t['quantum_principle']} into the game mechanics.
   c) Detail how the game reflects the geopolitical context of {t['geopolitical_context']}.
   d) Provide an example of a typical turn or round in the game.

2. Quantum Mechanics Integration (250-300 words):
   a) Explain the relevant aspects of {t['quantum_principle']} for non-experts.
   b) Describe how this quantum principle is mathematically or conceptually represented in your game.
   c) Discuss any challenges in translating quantum concepts into game mechanics and how you addressed them.

3. Scenario Analysis (250-300 words):
   a) Analyze the {t['scenario']} scenario in the context of your game.
   b) Identify key factors and variables that players must consider.
   c) Discuss how the quantum elements of the game influence strategic decisions in this scenario.

4. Optimal Strategy (250-300 words):
   a) Propose an optimal strategy for a player in the {t['scenario']} scenario.
   b) Explain how this strategy leverages both geopolitical and quantum aspects of the game.
   c) Discuss potential counter-strategies and how to adapt to them.

5. Implications and Ethical Considerations (200-250 words):
   a) Discuss the potential real-world implications of applying quantum principles to geopolitical strategy.
   b) Address any ethical concerns raised by your game or the proposed strategies.
   c) Explore how this game might contribute to our understanding of complex global issues.

Ensure your response demonstrates a deep understanding of both quantum mechanics and geopolitical strategy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your game design while maintaining scientific and strategic plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle {t['quantum_principle']} and how it can be applied to game mechanics.",
            f"The game design effectively incorporates the geopolitical context of {t['geopolitical_context']}.",
            "The scenario analysis and optimal strategy discussion show depth of strategic thinking and consideration of multiple factors.",
            "The response addresses ethical implications and real-world relevance of the game and strategies.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
