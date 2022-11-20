import inspect, os

class Container:
    def __init__(
        self,
        name: str,
        cpu: int = 1,
        ram: int = 2,
        image: str = None,
        pip: list = None,
    ):

        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.image = image
        self.pip = pip

        self.docker_commands = []
        self._collect_all_commands()
        self._write_dockerfile()

        # build docker image
        # send container details to server 
        # push docker image to server 
        # run docker image on server
        
    def _create_image(self):
        return "FROM " + self.image

    def _create_pip_commands(self, packages: list):
        for package_name in packages:
            self.docker_commands.append(f"RUN pip install {package_name}")

    def _get_filename(self):
        caller_frame = inspect.stack()[1]
        caller_filename_full = caller_frame.filename
        caller_dir_filename = caller_filename_full.split("/")[-2::]
        caller_dir_filename = '/'.join(caller_dir_filename)
        self.docker_commands.append(f'CMD ["python", "{caller_dir_filename}"]')

    def _collect_all_commands(self):
        self.docker_commands.append(self._create_image())
        self.docker_commands.append("WORKDIR /app")
        self._create_pip_commands(self.pip)
        self.docker_commands.append("COPY . /app")
        self._get_filename()
       
    def _write_dockerfile(self):
        with open("Dockerfile", "w") as f:
            for command in self.docker_commands:
                f.write(command)
                f.write("\n")

    
    def _build_images(self):
        os.system(f"docker build -t {self.name} .")

    def _compress_image_to_tar(self):
        os.system(f"docker save {self.name}:latest | gzip > {self.name}_compressed.tar.gz")
    
    def _push_to_backend(self):
        pass