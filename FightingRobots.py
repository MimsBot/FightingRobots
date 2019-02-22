class Robot:
    all_robots = []

    @classmethod
    def one_thousand_years(cls):
        for current_robot in cls.all_robots:
            current_robot.take_dmg(1)

    def __init__(self, new_name, attack=2):
        self.name = new_name
        self.life = 10
        self.attack_power = attack
        Robot.all_robots.append(self)

    def talk(self, message):
        print("Hello! My name is {}. {}".format(self.name, message))

    def fight(self, opponent):
        print("{} is fighting {}.".format(self.name, opponent.name))
        # opponent.life -= 1
        opponent.take_dmg(self.attack_power)
        self.status()
        opponent.status()

    def take_dmg(self, amount):  # optional parameter ie (amount=3)
        self.life -= amount

    def status(self):
        print("{}: {}".format(self.name, self.life))


robot1 = Robot('Darius')
print(robot1)

print(robot1.name)
print(robot1.life)

robot2 = Robot('Lucius', 3)
print(robot2.name)
print(robot2.life)

robot1.talk("I think you're really great.")

robot1.fight(robot2)
robot2.fight(robot1)

print(Robot.all_robots)

Robot.one_thousand_years()

robot1.status()
robot2.status()

Robot.one_thousand_years()

robot1.status()
robot2.status()

Robot.one_thousand_years()

robot1.status()
robot2.status()

print('---')


class BattleBot(Robot):

    def __init__(self, name):
        print("I AM A BATTLEBOT")
        super().__init__(name, 6)

    def talk(self):
        print("NO TALK. BATTLEBOT.")
        # super.talk("")




robot3 = BattleBot('BattleMeister')
robot3.talk()
# robot3.talk("I'm here to battle!")
robot3.fight(robot1)
