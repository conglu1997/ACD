import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        story_elements = [
            "A mysterious letter",
            "A hidden treasure map",
            "An ancient artifact",
            "A betrayal by a close friend",
            "A daring escape",
            "A surprising alliance",
            "A tragic loss",
            "A moment of triumph",
            "An unexpected revelation",
            "A difficult moral choice"
        ]
        
        locations = [
            "Grand library",
            "Abandoned lighthouse",
            "Bustling marketplace",
            "Secret underground tunnel",
            "Misty mountain peak",
            "Opulent palace ballroom",
            "Eerie graveyard at midnight",
            "Futuristic space station",
            "Tranquil Zen garden",
            "Chaotic battlefield"
        ]
        
        perspectives = [
            "The protagonist",
            "The antagonist",
            "A neutral bystander",
            "A future historian",
            "An omniscient narrator"
        ]
        
        tasks = {}
        for i in range(2):
            selected_elements = random.sample(story_elements, 5)
            selected_locations = random.sample(locations, 5)
            perspective = random.choice(perspectives)
            
            tasks[str(i+1)] = {
                "story_elements": selected_elements,
                "locations": selected_locations,
                "perspective": perspective
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a memory palace to structure and recall a complex narrative, then reconstruct the story from a specific perspective. Follow these steps:

1. Memory Palace Creation (200-250 words):
   Create a memory palace using the following locations: {', '.join(t['locations'])}.
   For each location, vividly describe its appearance and atmosphere.

2. Story Element Placement (200-250 words):
   Place the following story elements in your memory palace: {', '.join(t['story_elements'])}.
   Explain how each element is represented and connected to its location.

3. Narrative Construction (300-350 words):
   Using your memory palace, construct a coherent narrative that incorporates all the story elements.
   Ensure the story flows logically and creates meaningful connections between the elements.

4. Perspective Retelling (250-300 words):
   Retell the story from the perspective of {t['perspective']}.
   Adapt the narrative to reflect this perspective, highlighting how it changes the interpretation of events.

5. Memory Palace Reflection (150-200 words):
   Discuss how the memory palace technique influenced your narrative construction.
   Explain any challenges you faced and how you overcame them.

Ensure your response is creative, coherent, and demonstrates a clear understanding of the memory palace technique and its application to narrative construction."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of a memory palace using the provided locations",
            "All given story elements are incorporated into the memory palace and narrative",
            "The narrative is coherent and creates meaningful connections between the story elements",
            "The story is effectively retold from the specified perspective",
            "The reflection demonstrates understanding of the memory palace technique and its influence on narrative construction"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
