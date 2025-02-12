import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_variables = [
            "Temperature",
            "Precipitation",
            "Sea level",
            "Greenhouse gas concentrations"
        ]
        neuromorphic_components = [
            "Spiking neural networks",
            "Memristive devices",
            "Neuromorphic sensors",
            "Brain-inspired learning algorithms"
        ]
        symbolic_reasoning_methods = [
            "First-order logic",
            "Bayesian networks",
            "Decision trees",
            "Rule-based systems"
        ]
        
        tasks = {}
        for i in range(2):
            climate_var = random.choice(climate_variables)
            neuro_comp = random.choice(neuromorphic_components)
            symbolic_method = random.choice(symbolic_reasoning_methods)
            
            tasks[str(i+1)] = {
                "climate_variable": climate_var,
                "neuromorphic_component": neuro_comp,
                "symbolic_reasoning_method": symbolic_method
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neurosymbolic AI system that integrates neuromorphic computing and symbolic reasoning to model and predict climate change patterns, then propose interventions based on the model's insights. Focus on the climate variable of {t['climate_variable']}, using {t['neuromorphic_component']} as the primary neuromorphic component and {t['symbolic_reasoning_method']} for symbolic reasoning. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your neurosymbolic AI system for climate modeling.
   b) Explain how you integrate {t['neuromorphic_component']} with {t['symbolic_reasoning_method']}.
   c) Detail how your system processes and analyzes {t['climate_variable']} data.
   d) Discuss any novel features that distinguish your system from traditional climate models.

2. Data Processing and Learning (250-300 words):
   a) Explain how your system acquires and preprocesses {t['climate_variable']} data.
   b) Describe the learning mechanisms employed by the neuromorphic component.
   c) Outline how symbolic knowledge is incorporated and updated in your system.
   d) Discuss how your system handles uncertainty and incomplete data.

3. Prediction and Reasoning (250-300 words):
   a) Detail the process by which your system generates predictions about {t['climate_variable']} patterns.
   b) Explain how symbolic reasoning enhances or refines these predictions.
   c) Provide an example scenario demonstrating your system's predictive capabilities.
   d) Compare your system's approach to traditional statistical or pure deep learning methods.

4. Intervention Proposals (200-250 words):
   a) Describe how your system generates intervention proposals based on its predictions.
   b) Explain the role of symbolic reasoning in formulating these proposals.
   c) Provide an example of a specific intervention your system might propose for {t['climate_variable']}.
   d) Discuss how your system evaluates the potential impact of proposed interventions.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues in using AI to guide climate change interventions.
   b) Discuss the implications of potential biases in your system's neuromorphic or symbolic components.
   c) Propose guidelines for the responsible development and use of neurosymbolic AI in climate science.
   d) Consider the broader societal impacts of relying on AI-generated climate interventions.

6. Future Developments and Challenges (150-200 words):
   a) Propose two potential improvements or extensions to your neurosymbolic climate AI system.
   b) Discuss technical or conceptual challenges in scaling your approach to model multiple climate variables simultaneously.
   c) Speculate on how your neurosymbolic approach might influence future climate science research and policy-making.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuromorphic computing, particularly {t['neuromorphic_component']}, and how it can be applied to climate modeling",
            f"The integration of {t['symbolic_reasoning_method']} with neuromorphic components is well-explained and plausible",
            f"The system's approach to modeling and predicting {t['climate_variable']} patterns is innovative and scientifically grounded",
            "The proposed interventions are logical and based on the system's predictions",
            "The ethical considerations are thoughtfully analyzed and address potential issues specific to this application",
            "The response shows creativity and innovation while maintaining scientific and technological plausibility",
            "The response adheres to the specified word count for each section and the overall word limit",
            "All required sections and subsections are addressed comprehensively",
            "The example scenarios provided are detailed, relevant, and demonstrate a clear understanding of the system's capabilities"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
