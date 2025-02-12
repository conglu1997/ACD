import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_periods = [
            "Renaissance",
            "Impressionism",
            "Cubism",
            "Surrealism",
            "Abstract Expressionism",
            "Pop Art"
        ]
        brain_regions = [
            "Visual cortex",
            "Prefrontal cortex",
            "Temporal lobe",
            "Parietal lobe",
            "Amygdala",
            "Hippocampus"
        ]
        cognitive_processes = [
            "Pattern recognition",
            "Emotional processing",
            "Spatial reasoning",
            "Memory formation",
            "Attention allocation",
            "Semantic processing"
        ]
        ai_techniques = [
            "Convolutional Neural Networks",
            "Generative Adversarial Networks",
            "Recurrent Neural Networks",
            "Transformer models",
            "Reinforcement Learning",
            "Neuroevolution"
        ]
        tasks = [
            {
                "source_period": sp,
                "target_period": tp,
                "brain_region": br,
                "cognitive_process": cp,
                "ai_technique": ai
            }
            for sp in art_periods
            for tp in art_periods if tp != sp
            for br in brain_regions
            for cp in cognitive_processes
            for ai in ai_techniques
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that combines principles of neuroscience and art history to perform style transfer from {t['source_period']} to {t['target_period']}, focusing on the {t['brain_region']} and the cognitive process of {t['cognitive_process']}. Your system should incorporate {t['ai_technique']} as a key component. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your neuroaesthetic style transfer system.
   b) Explain how it incorporates knowledge of the {t['brain_region']} and {t['cognitive_process']}.
   c) Detail how {t['ai_technique']} is integrated into the system.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Neuroscience-Art Integration (250-300 words):
   a) Explain how your system models the neural processes involved in aesthetic perception.
   b) Discuss how the system accounts for differences in cognitive processing between {t['source_period']} and {t['target_period']}.
   c) Describe how the focus on {t['brain_region']} and {t['cognitive_process']} influences the style transfer process.

3. Art Historical Analysis (200-250 words):
   a) Compare and contrast the key artistic features of {t['source_period']} and {t['target_period']}.
   b) Explain how your system identifies and translates these features during style transfer.
   c) Discuss any challenges in maintaining artistic integrity while transforming between these periods.

4. AI Technique Implementation (250-300 words):
   a) Describe in detail how {t['ai_technique']} is used in your system.
   b) Explain any novel adaptations or modifications you've made to this technique for neuroaesthetic style transfer.
   c) Discuss potential limitations of this AI approach and how you address them.

5. Ethical and Cultural Considerations (200-250 words):
   a) Analyze potential biases in your system's approach to art and aesthetics.
   b) Discuss how your system accounts for cultural differences in artistic perception.
   c) Propose guidelines for the responsible use of AI in art creation and modification.

6. Future Research Directions (150-200 words):
   a) Suggest two potential advancements or extensions of your neuroaesthetic style transfer system.
   b) Discuss how these developments might impact our understanding of creativity and artistic cognition.

Ensure your response demonstrates a deep understanding of neuroscience, art history, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains how the {t['brain_region']} and {t['cognitive_process']} are incorporated into the neuroaesthetic style transfer system",
            f"The system design effectively uses {t['ai_technique']} as a key component",
            f"The art historical analysis thoroughly compares and contrasts {t['source_period']} and {t['target_period']}",
            "The response demonstrates a deep understanding of neuroscience, art history, and artificial intelligence",
            "The proposed system and analysis are innovative while maintaining scientific plausibility",
            "The response addresses all required sections and is within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
