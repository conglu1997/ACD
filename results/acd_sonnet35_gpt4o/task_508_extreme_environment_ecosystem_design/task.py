import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                'name': 'Methane Ocean World',
                'conditions': 'Liquid methane oceans, -180°C surface temperature, 1.5 Earth gravity, dense nitrogen atmosphere'
            },
            {
                'name': 'Hypergravity Rocky Planet',
                'conditions': 'Rocky surface, 4.5 Earth gravity, 50°C average temperature, thin carbon dioxide atmosphere, intense UV radiation'
            },
            {
                'name': 'Supercritical CO2 Planet',
                'conditions': 'Supercritical CO2 atmosphere, 100 Earth atmospheres pressure, 40°C surface temperature, constant electrical storms'
            },
            {
                'name': 'Tidally Locked Ice World',
                'conditions': 'Permanent twilight zone between frozen and molten hemispheres, extreme temperature gradients, thin xenon atmosphere'
            }
        ]
        
        tasks = random.sample(environments, 2)
        return {str(i+1): {'environment': env} for i, env in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical ecosystem for the following extreme alien environment:

{t['environment']['name']}
Environmental conditions: {t['environment']['conditions']}

Your task is to create a coherent ecosystem with at least three distinct life forms. Provide your response in the following format:

1. Environmental Analysis (200-250 words):
   a) Describe the key challenges that life would face in this environment.
   b) Identify potential energy sources and chemical processes that could support life.

2. Life Form Descriptions (300-350 words, 100-120 words per life form):
   For each of the three life forms, provide:
   a) A name and brief physical description.
   b) Its role in the ecosystem (producer, consumer, decomposer, etc.).
   c) Key adaptations that allow it to survive in the extreme environment.
   d) Its primary mode of energy acquisition and metabolism.

3. Ecosystem Interactions (200-250 words):
   a) Describe how the three life forms interact with each other.
   b) Explain any symbiotic relationships or food chains.
   c) Discuss how the ecosystem as a whole maintains stability.

4. Evolutionary History (150-200 words):
   Propose a brief evolutionary history explaining how these life forms might have developed their unique adaptations.

5. Comparative Analysis (150-200 words):
   Compare and contrast your proposed ecosystem with extreme environments on Earth (e.g., deep-sea hydrothermal vents, Antarctic dry valleys). Discuss similarities and differences in adaptation strategies.

Ensure your response is grounded in scientific principles while demonstrating creative problem-solving. Use appropriate scientific terminology and provide clear explanations for your proposed adaptations and ecosystem dynamics.

Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the challenges posed by the extreme environment.",
            "The proposed life forms have scientifically plausible adaptations for the given conditions.",
            "The ecosystem interactions and evolutionary history are coherent and well-reasoned.",
            "The comparative analysis shows insightful connections to real extreme environments on Earth.",
            "The response balances scientific accuracy with creative, speculative thinking.",
            "The response adheres to the specified word count (1000-1250 words) and section structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
