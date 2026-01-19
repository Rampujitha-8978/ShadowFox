class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Calling...")

    def receive_call(self):
        print("Receiving call...")

    def take_picture(self):
        print("Picture taken")

    def phone_details(self):
        print(f"Screen: {self.screen_type}")
        print(f"Network: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print("-" * 30)


class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", False,
                         front_camera, rear_camera, ram, storage)


class Samsung(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage, dual_sim):
        super().__init__("Touch Screen", "4G/5G", dual_sim,
                         front_camera, rear_camera, ram, storage)


# Apple objects
iphone1 = Apple("12MP", "48MP", "4GB", "64GB")
iphone2 = Apple("16MP", "32MP", "6GB", "128GB")

# Samsung objects
samsung1 = Samsung("8MP", "32MP", "4GB", "64GB", True)
samsung2 = Samsung("16MP", "48MP", "8GB", "128GB", True)

# Display details
iphone1.phone_details()
iphone2.phone_details()
samsung1.phone_details()
samsung2.phone_details()
