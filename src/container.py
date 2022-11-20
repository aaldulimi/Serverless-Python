
class Container():
    def __init__(self,
            name: str,
            cpu: int = 1,
            ram: int = 2,
            image: str = None,
            commands: list = None,
            pip: list = None,
            schedule = None
            ):

        self.name = name
        self.cpu = cpu 
        self.ram = ram
        self.image = image
        self.commands = commands
        self.pip = pip
        self.schedule = schedule
        