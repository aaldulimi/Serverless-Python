import os
class Dockerfile():
    def __init__(self, id, name, filename, image, pip):
        self.id = id
        self.name = name
        self.filename = filename
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

    def create(self):
        self._collect_all_commands()
        self._write_dockerfile()

   
class Image():
    def __init__(self, id, container_name):
        self.id = id 
        self.container_name = container_name
        self.name = f"{id}_{container_name}"
    
    def build(self):
        os.system(f"docker build -t {self.name} {self.id}/")

    def compress(self):
        compressed_name = f"{self.id}/{self.name}_compressed.tar.gz"
        os.system(f"docker save {self.name}:latest | gzip > {compressed_name}")

        return compressed_name
