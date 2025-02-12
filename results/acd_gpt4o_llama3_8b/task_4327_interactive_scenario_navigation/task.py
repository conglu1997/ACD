class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_state": "You are in a room with a door to the north and a window to the east. There is a bed, a wardrobe, and a desk.",
                "goal": "Find the key to unlock the door and exit the room.",
                "commands": [
                    {"command": "Look under the bed.", "response": "You find a box with a key inside."},
                    {"command": "Open the box.", "response": "The box is locked. You need a code to open it."},
                    {"command": "Search the wardrobe.", "response": "You find a note with the code 1234."},
                    {"command": "Enter the code 1234 to open the box.", "response": "The box is now open. You find the key inside."},
                    {"command": "Unlock the door.", "response": "The door is now unlocked."},
                    {"command": "Open the door.", "response": "You have successfully exited the room."}
                ]
            },
            "2": {
                "initial_state": "You are in a garden with a fountain in the center and a gate to the south. There is a shed to the west and a tree to the east.",
                "goal": "Find a way to open the gate and exit the garden.",
                "commands": [
                    {"command": "Inspect the fountain.", "response": "You find a lever hidden behind the fountain."},
                    {"command": "Pull the lever.", "response": "You hear a clicking sound from the gate."},
                    {"command": "Inspect the shed.", "response": "You find a key inside the shed."},
                    {"command": "Use the key on the gate.", "response": "The gate is still locked. You need to find another key."},
                    {"command": "Inspect the tree.", "response": "You find another key hidden in the branches."},
                    {"command": "Use the second key on the gate.", "response": "The gate swings open."},
                    {"command": "Open the gate.", "response": "You have successfully exited the garden."}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are in the following initial state: {t['initial_state']} Your goal is to: {t['goal']} You can interact with the environment by issuing natural language commands. Use the information provided in the responses to achieve your goal. Submit your response as a series of commands and their responses in the format: 'Command: [command] Response: [response]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must follow the precise sequence of commands provided to achieve the goal.",
            f"The final state must be consistent with successfully achieving the goal: {t['goal']}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
