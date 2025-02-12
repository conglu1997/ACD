import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "Design a particle that could be used to create a stable wormhole",
                "constraints": ["Must obey the laws of thermodynamics", "Cannot violate causality"],
                "application": "Solve the problem of faster-than-light travel"
            },
            {
                "problem": "Create a particle that can manipulate the strength of gravity",
                "constraints": ["Must be consistent with general relativity", "Cannot create singularities"],
                "application": "Develop a method for controlled fusion reactions"
            },
            {
                "problem": "Invent a particle that can store and transfer quantum information",
                "constraints": ["Must preserve quantum coherence", "Cannot violate the no-cloning theorem"],
                "application": "Design a quantum internet protocol"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical particle with unique properties to solve the following physics problem:

{t['problem']}

Your response should include the following:

1. Particle Design (250-300 words):
   a) Describe the fundamental properties of your particle (e.g., mass, charge, spin).
   b) Explain any unique quantum properties or interactions it possesses.
   c) Discuss how it interacts with known particles and forces.
   d) Provide a name for your particle and explain the reasoning behind it.

2. Theoretical Framework (200-250 words):
   a) Outline the mathematical or physical theories that support your particle's existence.
   b) Provide at least one equation or formula that describes a key property or interaction of your particle.
   c) Explain how your particle fits within or extends the Standard Model of particle physics.
   d) Cite relevant theories or research where applicable.

3. Problem Solution (250-300 words):
   a) Describe in detail how your particle solves the given problem.
   b) Explain the mechanism by which it achieves the desired effect.
   c) Address how your solution satisfies the given constraints: {', '.join(t['constraints'])}
   d) Discuss any potential side effects or unintended consequences of using your particle.

4. Experimental Detection (150-200 words):
   a) Propose an experimental setup that could potentially detect or create your particle.
   b) Describe the expected results and how they would confirm your particle's existence.
   c) Discuss any technological limitations that might make detection challenging.

5. Broader Implications (150-200 words):
   a) Explore how your particle and its application ({t['application']}) could impact other areas of physics or technology.
   b) Discuss any philosophical or ethical implications of your particle's existence or use.
   c) Propose a potential future research direction based on your particle.

Ensure your response demonstrates a deep understanding of particle physics, creative problem-solving, and the ability to work within theoretical constraints. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Balance creativity with adherence to established physical laws and theories.

Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of particle physics and related concepts",
            "The designed particle is creative, well-described, and theoretically plausible",
            "The solution effectively addresses the given problem and satisfies the stated constraints",
            "The theoretical framework and equations are sound and properly explained",
            "The proposed experimental detection method is logical and well-reasoned",
            "The discussion of broader implications is insightful and thought-provoking",
            "The response is well-structured and adheres to the word count guidelines",
            "The response balances creativity with scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
