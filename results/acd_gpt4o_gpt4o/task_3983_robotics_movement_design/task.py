class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"robot_description": "A simple wheeled robot with two motors for movement and an ultrasonic sensor for obstacle detection. The robot can move forward, backward, turn left, and turn right.", "objective": "Program the robot to navigate a maze and reach the endpoint without hitting any obstacles.", "constraints": "The robot must start at the maze entrance and follow a path to the endpoint. It must avoid obstacles using the ultrasonic sensor and can only move in steps of 10 cm."},
            "2": {"robot_description": "A simple robotic arm with three joints and a gripper. The arm can rotate at each joint and open/close the gripper.", "objective": "Program the robotic arm to pick up an object from a specified location and place it at a target location.", "constraints": "The arm must start at a home position, pick up the object from the pick-up location, and place it at the target location. The movement should be smooth and avoid any collisions with surrounding objects."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design and program the movement of a simple robot based on the following description, objective, and constraints:\n\n{t["robot_description"]}\n\nObjective: {t["objective"]}\n\nConstraints: {t["constraints"]}\n\nProvide your program in plain text format, along with a brief explanation of your reasoning. Format your response as follows:\n\nProgram: [Your program]\nExplanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a plausible program that meets the objective and constraints.",
            "The response should provide a detailed explanation of the reasoning behind the program.",
            "The program should be logically sound and feasible based on the robot's capabilities."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
