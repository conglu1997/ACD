import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            ("Coral reef", "Great Barrier Reef"),
            ("Tropical rainforest", "Amazon Rainforest"),
            ("Arctic tundra", "Siberian Tundra"),
            ("Temperate grassland", "North American Prairie")
        ]
        degradation_factors = [
            ("Climate change", "ocean acidification"),
            ("Pollution", "microplastic contamination"),
            ("Invasive species", "lionfish invasion"),
            ("Habitat fragmentation", "deforestation")
        ]
        constraints = [
            "Limited budget of $10 million over 5 years",
            "Strict regulations on species introduction",
            "Conflicting interests between local communities and conservation groups",
            "Rapid urbanization in surrounding areas"
        ]
        return {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "degradation_factor": random.choice(degradation_factors),
                "constraint": random.choice(constraints)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "degradation_factor": random.choice(degradation_factors),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models complex ecosystem interactions and generates strategies for restoring degraded environments. Then, apply your system to develop a restoration plan for the {t['ecosystem'][1]} ({t['ecosystem'][0]}) affected by {t['degradation_factor'][0]} (specifically, {t['degradation_factor'][1]}), while considering the constraint: {t['constraint']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for ecosystem modeling and restoration planning.
   b) Explain how your system integrates machine learning techniques with ecological principles.
   c) Detail any novel algorithms or data structures used in your design.
   d) Discuss how your system handles uncertainty and adapts to new information.
   e) Provide a high-level pseudocode or flow diagram of your system's main algorithm.
   f) Explain how your system balances multiple, potentially conflicting restoration goals.

2. Ecosystem Modeling Approach (300-350 words):
   a) Explain how your AI system models complex ecosystem interactions, including at least three specific examples relevant to the {t['ecosystem'][0]}.
   b) Describe the types of data your system would use, including at least five specific data sources or types.
   c) Discuss how your model accounts for both biotic and abiotic factors in the ecosystem.
   d) Explain how your system predicts long-term ecosystem changes and tipping points, providing at least one mathematical or statistical technique used.
   e) Detail your approach to error analysis and uncertainty quantification in the ecosystem model.
   f) Describe how your system incorporates future climate projections and their potential impacts on the ecosystem.

3. Restoration Strategy Generation (300-350 words):
   a) Detail how your AI system generates and evaluates potential restoration strategies, including at least three specific strategies for addressing {t['degradation_factor'][1]}.
   b) Explain how the system balances multiple objectives (e.g., biodiversity, ecosystem services, cost-effectiveness), using a multi-criteria decision-making approach.
   c) Describe how your system incorporates stakeholder input and local knowledge, providing at least two specific mechanisms.
   d) Discuss how the system adapts strategies based on monitoring and feedback, including a specific example of an adaptive management approach.
   e) Explain how your system accounts for the given constraint: {t['constraint']}.
   f) Describe how your system prioritizes interventions given limited resources and time.

4. Application to Specific Scenario (350-400 words):
   a) Apply your AI system to develop a restoration plan for the {t['ecosystem'][1]} affected by {t['degradation_factor'][1]}, considering the constraint: {t['constraint']}.
   b) Provide a detailed overview of the generated restoration strategy, including at least five specific interventions.
   c) Explain how your system addresses the specific challenges posed by {t['degradation_factor'][1]}, including potential cascading effects on the ecosystem.
   d) Discuss potential risks and uncertainties in the proposed restoration plan, and how your AI system accounts for them.
   e) Present a timeline for the restoration project, including key milestones and decision points.
   f) Describe how your plan adapts to three potential future scenarios (optimistic, neutral, and pessimistic) based on climate projections and socio-economic factors.

5. Ethical Considerations and Limitations (250-300 words):
   a) Discuss at least three ethical implications of using AI for ecosystem management decisions.
   b) Address potential biases in data or algorithms and how they might affect restoration outcomes, providing at least two specific examples.
   c) Explain how your system ensures transparency and interpretability in its decision-making process, including any visualization techniques used.
   d) Discuss at least three limitations of your approach and areas for future improvement.
   e) Analyze potential unintended consequences of the restoration plan and how they might be mitigated.

6. Comparative Analysis (250-300 words):
   a) Compare your AI-driven approach to at least two traditional ecological restoration methods used for {t['ecosystem'][0]} ecosystems.
   b) Discuss at least three potential advantages and three disadvantages of your system.
   c) Propose a detailed method for empirically evaluating the performance of your system against existing approaches, including specific metrics and a timeline for assessment.
   d) Discuss how your approach might be generalized to other ecosystem types or restoration scenarios.

Ensure your response demonstrates a deep understanding of ecology, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use numbered lists for subsections. Your total response should be between 1750-2050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['ecosystem'][0]} ecosystems and the specific impact of {t['degradation_factor'][1]}, while addressing the constraint: {t['constraint']}.",
            "The AI system design integrates ecological principles with advanced machine learning techniques, including a clear pseudocode or flow diagram and a method for balancing conflicting goals.",
            "The ecosystem modeling approach includes at least three specific examples, five data sources, and a detailed error analysis and uncertainty quantification method.",
            "The restoration strategy generation section includes at least three specific strategies, a multi-criteria decision-making approach, and a method for prioritizing interventions given limited resources.",
            "The application to the specific scenario provides at least five detailed interventions, addresses cascading effects, and includes adaptations for three future scenarios.",
            "The response addresses at least three ethical considerations, three limitations of the AI-driven approach, and potential unintended consequences.",
            "The comparative analysis compares the AI approach to at least two traditional methods, proposes a detailed evaluation method, and discusses generalization to other ecosystems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
