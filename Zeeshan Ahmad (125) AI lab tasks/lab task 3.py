class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.memory = {}

    def perceive(self, current_temperature):
        return current_temperature

    def update_memory(self, room, current_temperature):
        self.memory[room] = current_temperature

    def act(self, room, current_temperature):
        self.update_memory(room, current_temperature)
        
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        
        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(room, temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}. Memory: {agent.memory}.")
