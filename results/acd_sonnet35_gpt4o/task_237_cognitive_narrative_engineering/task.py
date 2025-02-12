import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "Working Memory Limitations",
                "narrative_element": "Flashbacks",
                "philosophical_concept": "Free Will"
            },
            {
                "cognitive_principle": "Cognitive Dissonance",
                "narrative_element": "Unreliable Narrator",
                "philosophical_concept": "Personal Identity"
            },
            {
                "cognitive_principle": "Dual Process Theory",
                "narrative_element": "Stream of Consciousness",
                "philosophical_concept": "Nature of Reality"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a narrative structure based on the cognitive science principle of {t['cognitive_principle']}, incorporating the narrative element of {t['narrative_element']}. Then, use this structure to generate a short story that explores the philosophical concept of {t['philosophical_concept']}.

Your response should include:

1. Cognitive Principle Analysis (100-150 words):
   Explain the chosen cognitive principle and its relevance to narrative comprehension.
   Example: If the principle is Working Memory Limitations, discuss how the capacity of working memory affects story processing.

2. Narrative Structure Design (200-250 words):
   Describe your narrative structure, explaining how it incorporates the cognitive principle.
   Detail how the specified narrative element is integrated into this structure.
   Provide a visual representation or diagram of your narrative structure using ASCII art or a clear textual description.
   Example: For Working Memory Limitations and Flashbacks, you might design a structure with short, interconnected scenes that challenge the reader's memory.

3. Short Story (300-400 words):
   Write a short story using your designed narrative structure.
   The story should explore the given philosophical concept.
   Clearly indicate how your narrative structure and the cognitive principle are reflected in the story.
   Use [COGNITIVE PRINCIPLE] and [NARRATIVE ELEMENT] tags to highlight relevant parts of your story.

4. Meta-Cognitive Analysis (150-200 words):
   Analyze how your narrative structure might influence the reader's cognitive processes.
   Discuss how this structure potentially enhances or challenges the reader's understanding of the philosophical concept.
   Provide at least two specific examples from your story to support your analysis.

5. Cognitive-Narrative Evaluation (100-150 words):
   Propose a method to empirically test the effectiveness of your cognitive-based narrative structure.
   Suggest a specific experiment or study that could validate your approach, including:
   a) Hypothesis
   b) Experimental design (briefly)
   c) Measurable outcomes

Ensure your response demonstrates a deep understanding of cognitive science, narrative theory, and philosophy. Be creative in your approach while maintaining scientific rigor. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response using clear headings for each section. Your total response should be between 850-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the cognitive principle of {t['cognitive_principle']} and its relevance to narrative comprehension, with a concrete example",
            f"The narrative structure incorporates the cognitive principle of {t['cognitive_principle']} and the narrative element of {t['narrative_element']}, with a clear visual representation or description",
            f"The short story (300-400 words) effectively uses the designed narrative structure and explores the philosophical concept of {t['philosophical_concept']}, with appropriate use of [COGNITIVE PRINCIPLE] and [NARRATIVE ELEMENT] tags",
            "The meta-cognitive analysis provides at least two specific examples from the story to illustrate how the narrative structure influences cognitive processes",
            "The proposed evaluation method includes a clear hypothesis, experimental design, and measurable outcomes",
            "The response demonstrates a clear understanding of cognitive science, narrative theory, and philosophy, using appropriate terminology",
            "The response follows the specified format and word count guidelines for each section",
            "The response balances creativity with scientific rigor throughout all sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
