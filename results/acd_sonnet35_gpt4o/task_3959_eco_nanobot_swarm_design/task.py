import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "pollutant": "Microplastics",
                "ocean_zone": "Surface waters",
                "additional_challenge": "High salinity and UV radiation"
            },
            {
                "pollutant": "Nurdles (plastic pellets)",
                "ocean_zone": "Coastal areas",
                "additional_challenge": "Strong currents and tidal forces"
            }
        ]
        
        tasks = {}
        for i, scenario in enumerate(scenarios, 1):
            tasks[str(i)] = scenario
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-controlled swarm of nanobots for cleaning up {t['pollutant']} in {t['ocean_zone']}, while addressing the additional challenge of {t['additional_challenge']}. Your response should include:

1. Nanobot Design (250-300 words):
   a) Describe the physical structure and key components of your nanobots.
   b) Explain how the nanobots will interact with and remove the specified pollutant.
   c) Discuss how the nanobots are adapted to function in the given ocean zone.
   d) Address how the design mitigates the additional challenge.

2. Swarm Intelligence (200-250 words):
   a) Explain the AI algorithms governing the swarm behavior.
   b) Describe how individual nanobots communicate and coordinate within the swarm.
   c) Discuss how the swarm adapts to changing environmental conditions.

3. Environmental Impact Assessment (200-250 words):
   a) Analyze potential effects of the nanobot swarm on marine ecosystems.
   b) Propose safeguards to minimize unintended ecological consequences.
   c) Discuss the long-term environmental implications of your solution.

4. Scalability and Efficiency (150-200 words):
   a) Estimate the number of nanobots required for effective cleanup.
   b) Propose a method for measuring and optimizing the swarm's efficiency.
   c) Discuss potential challenges in scaling up the solution and how to address them.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to deploying AI-controlled nanobot swarms in the ocean.
   b) Propose guidelines for responsible development and use of this technology.
   c) Discuss the implications of using artificial systems for environmental remediation.

Ensure your response demonstrates a deep understanding of nanotechnology, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The nanobot design is innovative and tailored to the specific pollutant and ocean zone",
            "The swarm intelligence approach is well-explained and suitable for the task",
            "Environmental impacts and ethical considerations are thoroughly analyzed",
            "The solution demonstrates a deep understanding of nanotechnology, environmental science, and AI",
            "The response is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
