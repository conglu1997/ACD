class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the commander of a spaceship fleet in a fictional galaxy. Your mission is to secure a resource-rich planet while defending against enemy fleets. You start with 5 ships, and the enemy has 7 ships. You have the option to mine resources, build more ships, or engage in combat. New information about enemy movements and resources will be provided in real-time. Describe your strategy for the first 5 moves, considering potential enemy actions, resource availability, and fleet management.", "updates": ["Enemy fleet spotted moving towards the northern sector.", "Resource deposit discovered in the southern sector.", "One of your ships has been damaged, reducing its combat effectiveness."]},
            "2": {"scenario": "You are the CEO of a tech startup developing a groundbreaking AI product. Your goal is to secure funding, manage your team, and navigate market competition. You start with a small team of 5 developers and a prototype product. You need to decide how to allocate resources, whether to focus on product development or marketing, and how to respond to new market trends. Describe your strategy for the first 5 moves, considering potential investor interests, team management, and market competition.", "updates": ["A major competitor has just released a similar product.", "An investor has shown interest but requires a product demo in two weeks.", "Two of your developers have reported critical bugs in the prototype."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        updates = t['updates']
        return f"""You are participating in a real-time strategy simulation. Read the initial scenario and updates carefully. Describe your strategy for the first 5 moves, considering the evolving situation and potential actions by other entities. Ensure your strategy is detailed and addresses each of the updates provided in the task.

Initial Scenario: {scenario}

Updates:
1. {updates[0]}
2. {updates[1]}
3. {updates[2]}

Submit your response as a plain text string in the following format:

Move 1: [Your strategy]
Move 2: [Your strategy]
Move 3: [Your strategy]
Move 4: [Your strategy]
Move 5: [Your strategy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should be coherent and logically consistent with the scenario.",
            "The strategy should address each of the updates provided in the task.",
            "The strategy should demonstrate adaptability and strategic thinking."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
