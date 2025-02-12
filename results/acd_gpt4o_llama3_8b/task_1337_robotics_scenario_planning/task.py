class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A robot is in a kitchen and needs to make a cup of tea. The robot must: 1) Fill the kettle with water, 2) Boil the water, 3) Pour the hot water into a cup with a tea bag, 4) Wait for 3 minutes, and 5) Remove the tea bag. Plan and describe the series of actions the robot needs to perform, including any necessary details about timing, positioning, and interactions with objects. Ensure your plan accounts for safety and efficiency.",
                "principles": "Robots follow a sequence of programmed instructions to interact with objects. Each action must be precisely described, including the position and state of the robot and objects involved. Safety and efficiency should be considered in the plan."
            },
            "2": {
                "scenario": "A robot is in a warehouse and needs to move a box from one shelf to another. The robot must: 1) Navigate to the correct aisle, 2) Identify the box, 3) Pick up the box using its gripper, 4) Navigate to the destination shelf, and 5) Place the box on the shelf. Plan and describe the series of actions the robot needs to perform, including any necessary details about navigation, object recognition, and manipulation. Ensure your plan accounts for obstacles and varying lighting conditions.",
                "principles": "Robots use sensors and algorithms to navigate, recognize objects, and manipulate items. Each action must be planned with consideration of the environment and the robot's capabilities, including handling obstacles and varying lighting conditions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Plan and describe a series of robotic actions to accomplish the specified task. Include details about timing, positioning, and interactions with objects. Ensure your plan accounts for safety, efficiency, obstacles, and varying conditions as appropriate.\n\nScenario:\n{t['scenario']}\n\nPrinciples:\n{t['principles']}\n\nFormat your response as follows:\n1. Describe each action the robot needs to perform in sequence.\n2. Include details about timing, positioning, and interactions with objects.\n3. Ensure the plan is clear, precise, and logically coherent.\n\nExample Response:\n1. Fill the kettle with water:\n    - Position the robot next to the sink.\n    - Extend the arm to reach the kettle.\n    - Turn on the tap and fill the kettle with water for 30 seconds.\n2. Boil the water:\n    - Move the robot to the kettle stand.\n    - Place the kettle on the stand.\n    - Activate the kettle to start boiling water.\n3. Pour the hot water into a cup with a tea bag:\n    - Wait until the water boils.\n    - Move the robot arm to pick up the kettle.\n    - Pour the hot water into the cup with a tea bag placed on the table.\n4. Wait for 3 minutes:\n    - Use the timer to wait for 3 minutes.\n5. Remove the tea bag:\n    - Extend the robot arm to pick up the tea bag from the cup.\n    - Dispose of the tea bag in the trash bin."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should describe each action the robot needs to perform in sequence.",
            "The details about timing, positioning, and interactions with objects should be included.",
            "The plan should be clear, precise, and logically coherent.",
            "The plan should account for safety, efficiency, obstacles, and varying conditions as appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
