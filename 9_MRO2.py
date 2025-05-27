class GPS:
    def navigate(self):
        print('GPS active')

class Radar:
    def navigate(self):
        print('Radar system in operation')

class AIEngine:
    def navigate(self):
        print('AI navigation active')

class AutoPilot(GPS, Radar, AIEngine):
    pass

Tesla = AutoPilot()
Tesla.navigate()

print(f'Method Resolution Order: {AutoPilot.__mro__}')
