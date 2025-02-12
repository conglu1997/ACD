class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "Design a small urban park for a neighborhood with a high population density. The park should include green spaces, recreational areas, and pathways. Provide a detailed description of each component and the overall layout, explaining the reasoning behind your design choices. The park must be able to accommodate at least 200 people at a time, and should include at least one children's play area, a seating area for adults, and a jogging track."
            },
            "2": {
                "task": "Propose a redesign of a congested traffic intersection in a city to improve traffic flow and pedestrian safety. Describe the new layout, including traffic signals, pedestrian crossings, and any other relevant features. Explain how your design will achieve the intended improvements. The redesign should ensure that the average waiting time at the intersection is reduced by at least 30%, and should include measures to ensure the safety of pedestrians, particularly those with disabilities."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the following task:

{t['task']}

Ensure that your design includes:
1. A clear and detailed description of each component.
2. An overall layout that is logical and practical.
3. Creative and innovative solutions to the given problem.
4. Explanations for the reasoning behind your design choices.
5. Specific elements as mentioned in the task (e.g., children's play area, seating area, jogging track for Task 1; reduced waiting time, pedestrian safety measures for Task 2).

Submit your design as a plain text string in the following format:

Component Descriptions:
[Detailed descriptions of each component]

Overall Layout:
[Logical and practical layout]

Innovative Solutions:
[Creative solutions to the problem]

Design Reasoning:
[Explanations for your design choices]

Example response format:

Component Descriptions:
- Children's Play Area: A designated space with playground equipment for children aged 3-12, including swings, slides, and climbing structures.
- Seating Area: Benches and shaded seating arrangements for adults to relax and supervise children.
- Jogging Track: A 400-meter track around the perimeter of the park for jogging and walking.

Overall Layout:
The children's play area is located in the center of the park, surrounded by green spaces and flower beds. The seating area is adjacent to the play area, providing a clear view for supervision. The jogging track encircles the entire park, with pathways connecting all areas.

Innovative Solutions:
The park includes solar-powered lighting and water fountains, promoting sustainability and convenience for visitors.

Design Reasoning:
The central placement of the play area ensures safety and accessibility, while the surrounding green spaces provide a pleasant environment. The jogging track encourages physical activity, and the solar-powered amenities reflect a commitment to eco-friendly design."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design should include a clear and detailed description of each component.",
            "The overall layout should be logical and practical.",
            "The design should include creative and innovative solutions.",
            "The reasoning behind the design choices should be explained.",
            "For Task 1, the park should accommodate at least 200 people, include a children's play area, a seating area, and a jogging track.",
            "For Task 2, the redesign should reduce the average waiting time by at least 30% and include measures for pedestrian safety, particularly for those with disabilities."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
