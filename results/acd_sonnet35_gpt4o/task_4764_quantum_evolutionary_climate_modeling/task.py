import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'climate_phenomenon': 'El Niño–Southern Oscillation (ENSO)',
                'quantum_principle': 'superposition',
                'evolutionary_mechanism': 'genetic drift',
                'time_scale': '6-18 months',
                'key_variable': 'sea surface temperature'
            },
            {
                'climate_phenomenon': 'Arctic sea ice decline',
                'quantum_principle': 'entanglement',
                'evolutionary_mechanism': 'natural selection',
                'time_scale': '10-30 years',
                'key_variable': 'ice extent'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired evolutionary algorithm to model and predict the complex climate system of {t['climate_phenomenon']}, integrating the quantum principle of {t['quantum_principle']} and the evolutionary mechanism of {t['evolutionary_mechanism']}. Your algorithm should focus on predicting changes in {t['key_variable']} over a {t['time_scale']} time scale. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain how {t['quantum_principle']} can be applied to modeling climate systems.
   b) Describe how {t['evolutionary_mechanism']} can be integrated into a quantum-inspired algorithm.
   c) Discuss the potential advantages of this approach for modeling {t['climate_phenomenon']}.

2. Algorithm Design (250-300 words):
   a) Outline the key components of your quantum-inspired evolutionary algorithm.
   b) Explain how your algorithm incorporates {t['quantum_principle']} and {t['evolutionary_mechanism']}.
   c) Describe the representation of climate data and model parameters in your quantum-inspired system.
   d) Discuss how your algorithm handles the complexity and non-linearity of {t['climate_phenomenon']}.
   e) Provide a simple pseudocode or flowchart of your algorithm (this can be described textually).

3. Implementation Strategy (200-250 words):
   a) Propose a high-level implementation plan for your algorithm.
   b) Discuss any technical challenges you anticipate and how you would address them.
   c) Explain how you would validate and benchmark your algorithm against classical climate models.
   d) Discuss potential trade-offs between computational complexity and prediction accuracy.
   e) Include a brief example of how your algorithm would process a simple climate dataset.

4. Predictive Capabilities (150-200 words):
   a) Describe how your algorithm predicts changes in {t['key_variable']} over the {t['time_scale']} time scale.
   b) Explain how the integration of quantum and evolutionary principles might improve predictive accuracy.
   c) Discuss any limitations or uncertainties in your model's predictive capabilities.

5. Ethical and Societal Implications (100-150 words):
   a) Identify potential ethical concerns or societal impacts of using quantum-inspired evolutionary algorithms for climate prediction.
   b) Discuss how these advanced predictive models might influence climate policy and decision-making.
   c) Propose guidelines for the responsible development and use of such algorithms in climate science.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your algorithm.
   b) Discuss how advancements in quantum computing or climate science might impact your approach.
   c) Propose a related research question that builds on your algorithm.

Ensure your response demonstrates a deep understanding of quantum computing principles, evolutionary algorithms, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed explanation of how {t['quantum_principle']} and {t['evolutionary_mechanism']} are integrated into the algorithm design for modeling {t['climate_phenomenon']}.",
            f"The algorithm design specifically addresses predicting changes in {t['key_variable']} over a {t['time_scale']} time scale.",
            "The response includes a simple pseudocode or flowchart (described textually) of the proposed algorithm.",
            "The implementation strategy discusses potential trade-offs between computational complexity and prediction accuracy.",
            "The implementation strategy includes a brief example of how the algorithm would process a simple climate dataset.",
            "The predictive capabilities, limitations, and uncertainties of the model are thoroughly discussed.",
            "Ethical and societal implications of the proposed algorithm are thoughtfully considered, including guidelines for responsible development and use.",
            "Future research directions are proposed that build on the presented algorithm, considering advancements in quantum computing and climate science.",
            "The response is well-formatted with clear headings for each section and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
