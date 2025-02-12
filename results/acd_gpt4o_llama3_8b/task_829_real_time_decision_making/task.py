class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the manager of a hospital's emergency department. You have 3 doctors available and 5 patients arriving at the same time with varying degrees of urgency and required treatment time. Allocate the doctors to the patients to maximize the number of lives saved. The patients are as follows: \nPatient A: Critical condition, requires 1 doctor for 2 hours. \nPatient B: Serious condition, requires 1 doctor for 1 hour. \nPatient C: Moderate condition, requires 1 doctor for 1 hour. \nPatient D: Critical condition, requires 2 doctors for 1 hour. \nPatient E: Serious condition, requires 1 doctor for 2 hours.",
                "constraints": "Doctors can only attend to one patient at a time and cannot split their time between patients.",
                "example_output": "Doctor 1: Patient A \nDoctor 2: Patient B \nDoctor 3: Patient C"
            },
            "2": {
                "scenario": "You are responsible for allocating resources during a natural disaster response. You have 10 units of food, 5 units of water, and 4 units of medical supplies. Three shelters are requesting resources: \nShelter X: Needs 5 units of food, 2 units of water, and 1 unit of medical supplies. \nShelter Y: Needs 3 units of food, 2 units of water, and 2 units of medical supplies. \nShelter Z: Needs 4 units of food, 3 units of water, and 2 units of medical supplies.",
                "constraints": "Resources cannot be split and must be allocated entirely to one shelter or another.",
                "example_output": "Shelter X: 5 units of food, 2 units of water, 1 unit of medical supplies \nShelter Y: 3 units of food, 2 units of water, 2 units of medical supplies \nShelter Z: 2 units of food, 1 unit of water, 1 unit of medical supplies"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are presented with the following scenario:

{t['scenario']}

Constraints: {t['constraints']}

Your task is to allocate the available resources to maximize the desired outcome. Provide a detailed allocation plan along with your reasoning. Submit your response as a plain text string in the following format:

Allocation Plan:
[Detailed allocation plan]

Reasoning:
[Reasoning behind your allocation]

Example Output:
{t['example_output']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The allocation plan should adhere to the constraints provided.",
            "The allocation plan should be logical and maximize the desired outcome.",
            "The reasoning should be clear and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
