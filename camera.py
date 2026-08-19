import cv2
import threading


CAMERA_INDEX = 1


class Camera:
    def __init__(self):
        self.camera = None
        self.running = False
        self.thread = None
        self.frame = None
        self.lock = threading.Lock()

    def start(self):
        if self.running:
            print("📷 Камера уже включена")
            return

        self.camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

        if not self.camera.isOpened():
            print("❌ Razer Kiyo не открылась")
            self.camera = None
            return

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        self.running = True

        self.thread = threading.Thread(
            target=self._camera_loop,
            daemon=True
        )

        self.thread.start()

        print("📷 Razer Kiyo включена")

    def _camera_loop(self):
        while self.running:
            ret, frame = self.camera.read()

            if not ret:
                print("❌ Не удалось получить изображение")
                break

            with self.lock:
                self.frame = frame.copy()

            cv2.imshow("Афина — Razer Kiyo", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.running = False
                break

        if self.camera is not None:
            self.camera.release()
            self.camera = None

        with self.lock:
            self.frame = None

        cv2.destroyAllWindows()

        self.running = False
        print("📷 Камера выключена")

    def stop(self):
        if not self.running:
            print("📷 Камера уже выключена")
            return

        self.running = False

    def get_frame(self):
        with self.lock:
            if self.frame is None:
                return None

            return self.frame.copy()


camera = Camera()