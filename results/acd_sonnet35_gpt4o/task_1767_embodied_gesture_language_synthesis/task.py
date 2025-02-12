import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Time",
            "Justice",
            "Freedom",
            "Knowledge",
            "Chaos",
            "Balance",
            "Evolution",
            "Consciousness"
        ]
        
        tasks = {}
        for i in range(2):
            concept = random.choice(abstract_concepts)
            abstract_concepts.remove(concept)  # Ensure no repetition
            tasks[str(i+1)] = {"abstract_concept": concept}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interpret complex gestures and generate corresponding natural language descriptions, then use this system to create a gesture-based language for abstract concepts. Your task focuses on the abstract concept: {t['abstract_concept']}.

Embodied cognition is the theory that many features of cognition are shaped by aspects of the entire body of the organism. In this view, cognition and language are deeply rooted in our physical experiences and interactions with the world.

For the purpose of this task, a 'gesture' refers to a deliberate movement or series of movements of the body or its parts, especially the hands and arms, used to express an idea, emotion, or function.

For example, a simple gesture-based representation for the concept of 'growth' might be a gradual upward movement of the hand with fingers spread, mimicking a plant growing from the ground.

Provide your response in the following format:

1. Gesture Recognition System (250-300 words):
   a) Describe the architecture of your gesture recognition system, including sensors and data processing pipeline.
   b) Explain how your system distinguishes between intentional gestures and incidental movements.
   c) Discuss how your system handles variations in gesture performance across individuals.

2. Language Generation Module (200-250 words):
   a) Outline the components of your language generation module.
   b) Explain how this module translates recognized gestures into natural language descriptions.
   c) Discuss any novel techniques used to ensure coherent and contextually appropriate language output.

3. Gesture-Based Language for Abstract Concepts (250-300 words):
   a) Describe your approach to creating a gesture-based language for the given abstract concept.
   b) Provide 3-5 example gestures for expressing different aspects or nuances of this concept.
   c) Explain the rationale behind each gesture, linking it to embodied experiences or metaphors.
   d) Discuss how your system would generate language descriptions for these concept-specific gestures.
   e) Provide a detailed visual description or diagram of at least one of these gestures.

4. Embodied Cognition Integration (200-250 words):
   a) Explain how your system incorporates principles of embodied cognition.
   b) Discuss how this integration enhances the system's understanding and expression of abstract concepts.
   c) Analyze potential limitations of this approach for concept representation.

5. Cross-Modal Reasoning (150-200 words):
   a) Describe how your system performs cross-modal reasoning between gestural and linguistic representations.
   b) Provide an example of how this reasoning might lead to novel insights about the given abstract concept.

6. Evaluation and Implications (150-200 words):
   a) Propose metrics to evaluate the effectiveness of your gesture-based language for abstract concepts.
   b) Discuss potential applications of this system in fields such as human-computer interaction, cognitive science, or language education.
   c) Explore ethical considerations related to creating new modes of communication for abstract thought.

Ensure your response demonstrates a deep understanding of gesture recognition, natural language processing, embodied cognition, and abstract reasoning. Be creative in your approach while maintaining scientific plausibility. Strive for a balance between innovative gesture designs and their grounding in physical experiences or metaphors. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words.

Remember to address all parts of the task thoroughly, including the visual description or diagram of at least one gesture."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed gesture recognition system with clear explanation of its architecture and functioning",
            "The language generation module is thoroughly described, including its components and novel techniques",
            f"The gesture-based language for the concept of {t['abstract_concept']} is creative, well-explained, and includes 3-5 example gestures",
            "The integration of embodied cognition principles is clearly explained and justified, with analysis of potential limitations",
            "The cross-modal reasoning approach is logically sound and includes a specific example related to the given abstract concept",
            "The evaluation metrics and implications are thoughtful, comprehensive, and include ethical considerations",
            "The response includes a detailed visual description or diagram of at least one gesture",
            "The response demonstrates a deep understanding of gesture recognition, natural language processing, embodied cognition, and abstract reasoning",
            "The total response is between 1200-1500 words and formatted with clear headings for each section",
            "The proposed gestures balance creativity with plausibility and grounding in physical experiences or metaphors"
        ]
        score = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria]) / len(criteria)
        return score
