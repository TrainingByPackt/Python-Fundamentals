class MobilePhone:
    def __init__(self, memory):
        self.memory = memory


class Camera:
    def take_picture(self):
        print("Say cheese!")


class CameraPhone(MobilePhone, Camera):
    pass


cameraphone = CameraPhone("200KB")
cameraphone.take_picture()
print(cameraphone.memory)
