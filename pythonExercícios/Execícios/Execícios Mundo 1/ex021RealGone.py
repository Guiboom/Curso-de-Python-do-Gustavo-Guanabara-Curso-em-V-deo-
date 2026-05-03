import os
import time
import vlc

# pasta onde o ex021.py esta
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

# caminho mp3
caminho_mp3 = os.path.join(pasta_do_script, "realgone.mp3")

print(caminho_mp3)  #veja o caminho real

player = vlc.MediaPlayer(caminho_mp3)
player.audio_set_volume(150)
player.play()

time.sleep(999999)
player.stop()
