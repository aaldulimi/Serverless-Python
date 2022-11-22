import os

class Container():
    def __init__(self, id, filename, name, cpu, ram, image, pip):
        self.id = id
        self.filename = filename
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.image = image
        self.pip = pip

        self.docker_commands = []
    
    def _create_image(self):
        return "FROM " + self.image

    def _create_pip_commands(self, packages: list):
        for package_name in packages:
            self.docker_commands.append(f"RUN pip install {package_name}")

    def _collect_all_commands(self):
        self.docker_commands.append(self._create_image())
        self.docker_commands.append("WORKDIR /app")
        self._create_pip_commands(self.pip)
        self.docker_commands.append("COPY . /app")
        self.docker_commands.append(f'CMD ["python", "{self.filename}"]')

       
    def _write_dockerfile(self):
        with open(f"{self.id}/Dockerfile", "w") as f:
            for command in self.docker_commands:
                f.write(f"{command}\n\n")

    def create_dockerfile(self):
        self._collect_all_commands()
        self._write_dockerfile()

   