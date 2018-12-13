import os
import wave
import contextlib
import soundfile as sf
from pydub import AudioSegment
#Redirige a la carperta de ubicacion  del archivo python
UPLOAD_FOLDER=os.getcwd()

#file=  archivo ingresado
#paths = ruta de destino
def divisor_audio(file, paths):
	for file in os.listdir(UPLOAD_FOLDER):
			name_file=file.split('.')

			if(name_file[1]=='wav'): #Buscamos dentro de la carpeta donde está el archivo python, un archivo con extension ".wav"

				f=sf.SoundFile(file)
				time = 30000 
				j=1
				with contextlib.closing(wave.open(UPLOAD_FOLDER+ "/"+ file,'r')) as f:
		    			frames = f.getnframes()
		    			rate = f.getframerate()

		    			duration = int((frames / float(rate))*1000) #Duracion total del audio
					for i in range (0,duration,time): #rango de duracion del audio, tiempo que deseamos partir el audio (30seg) 
						newAudio = AudioSegment.from_wav(file)
						newAudio = newAudio[i:i+30000] #partimos el audio cada 30 segundos
						destino = paths+"/"+name_file[0]+'_'+str(j)
						newAudio.export(destino, format="wav")
						j=j+1 #repetimos la accion hasta terminar la duracion
