from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from frodokem import FrodoKEM

class SampleApp(App):
    def build(self):
        frodokem = FrodoKEM()
        (pk, sk) = frodokem.kem_keygen()
        (ct, ss) = frodokem.kem_encaps(pk)
        print(ss)
        return Label(text = str(ss)) 

if __name__ == "__main__":
    SampleApp().run()