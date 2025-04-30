
class LightSensorAgent:
    def __init__(self, light_threshold):
        self.light_threshold = light_threshold

    def perceive_environment(self, light_intensity):
        self.light_intensity = light_intensity

    def decide_action(self):
        if self.light_intensity > self.light_threshold:
            return "Turn Light OFF"
        else:
            return "Turn Light ON"

    def act(self):
        action = self.d ecide_action()
        print(f"Action: {action}")


sensor = LightSensorAgent(light_threshold=50)
sensor.perceive_environment(light_intensity=30)  
sensor.act()

sensor.perceive_environment(light_intensity=70) 
sensor.act()
