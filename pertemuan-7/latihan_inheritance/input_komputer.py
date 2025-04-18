class PerangkatInput:
    def input_data(self):
        pass

class Keyboard(PerangkatInput):
    def input_data(self):
        print("Keyboard: Mengetik huruf dan angka...")

class Mouse(PerangkatInput):
    def input_data(self):
        print("Mouse: Menggerakkan kursor dan klik...")

# Contoh penggunaan
keyboard = Keyboard()
mouse = Mouse()

keyboard.input_data()  # Output: Keyboard: Mengetik huruf dan angka...
mouse.input_data()     # Output: Mouse: Menggerakkan kursor dan klik...