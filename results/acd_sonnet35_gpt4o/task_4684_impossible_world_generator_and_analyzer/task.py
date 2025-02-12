import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'altered_law': 'Time flows backwards and at variable rates depending on spatial location and the observer\'s velocity',
                'domains': ['physics', 'biology', 'sociology']
            },
            {
                'altered_law': 'Causality is reversed (effects precede causes) and operates probabilistically, with probability distributions affected by conscious observation',
                'domains': ['philosophy', 'psychology', 'economics']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an 'impossible' world where the following fundamental law of reality is altered:

Altered Law: {t['altered_law']}

Your task is to:

1. World Design (300-350 words):
   a) Describe the key features and mechanics of this impossible world.
   b) Explain how the altered law fundamentally changes the nature of reality.
   c) Provide 3-4 specific examples of how everyday phenomena would be affected.
   d) Discuss any paradoxes or logical inconsistencies that arise and how they might be resolved.
   e) Propose a novel physical or logical principle that could help maintain consistency in this world.

2. Implications Analysis (350-400 words):
   Analyze the implications of this impossible world across the following domains: {', '.join(t['domains'])}.
   For each domain:
   a) Describe how fundamental principles or theories in this field would need to be revised.
   b) Provide a specific example of how a key process or phenomenon in this domain would function differently.
   c) Discuss potential new discoveries or insights that might emerge from studying this impossible world.
   d) Propose a novel research question that would be unique to this impossible world.

3. Cognitive and Experiential Impact (250-300 words):
   a) Describe how human cognition and perception would need to adapt to this impossible world.
   b) Explain how the subjective experience of consciousness might be altered.
   c) Discuss potential changes to language, memory, or other cognitive processes.
   d) Propose a new cognitive ability that might evolve in response to this world's unique challenges.

4. Narrative Scenario (200-250 words):
   Write a brief narrative scenario set in this impossible world, highlighting its unique features and challenges.
   Focus on how characters perceive and interact with this altered reality.

5. Meta-Analysis and Self-Assessment (200-250 words):
   a) Reflect on the process of designing and analyzing this impossible world.
   b) Discuss what this exercise reveals about the nature of reality, logic, and human understanding.
   c) Propose a novel question or area of inquiry that arises from contemplating this impossible world.
   d) Speculate on how an AI system might be designed to operate effectively in this impossible world.
   e) Assess the logical consistency of your own response, identifying any potential contradictions or areas where further clarification might be needed.

6. Experimental Design (150-200 words):
   Propose an experiment or simulation that could test some aspect of your impossible world design.
   a) Describe the setup and methodology of the experiment.
   b) Explain what results you would expect and how they would validate or challenge your world design.
   c) Discuss any ethical considerations or practical limitations of conducting such an experiment.

Ensure your analysis is creative yet logically consistent within the constraints of the altered law. Use specific examples and avoid broad generalizations. Your response should demonstrate deep, interdisciplinary thinking and an ability to reason about abstract concepts.

Format your response with clear headings for each section, and include the word count for each section in parentheses at the end. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the required format, including word counts for each section, and adheres to the overall word count guidelines.",
            "The world design is creative, logically consistent (within the constraints of the altered law), and thoroughly explores the implications of the change.",
            "The implications analysis demonstrates deep, interdisciplinary thinking and provides specific, well-reasoned examples for each domain.",
            "The cognitive and experiential impact section shows a strong understanding of human cognition and consciousness, with insightful speculation on how they would be affected.",
            "The narrative scenario effectively illustrates the unique features of the impossible world and engages the reader.",
            "The meta-analysis demonstrates reflective thinking and proposes a novel, thought-provoking question or area of inquiry.",
            "The self-assessment shows critical thinking and accurately identifies potential inconsistencies or areas needing clarification.",
            "The experimental design is well-thought-out, relevant to the world design, and considers ethical and practical implications.",
            "The overall response shows creativity, logical consistency, and an ability to reason about highly abstract concepts across multiple disciplines.",
            "The response maintains internal consistency throughout all sections, with ideas and concepts coherently linked across the analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
