from timeit import default_timer as timer
from pydub import AudioSegment


#start = timer()

# files
# convert to file selection 'browse as input
src = "transcript.mp3"
dst = "test.wav"




# sorce <src> is converted to wav (live audio may need to be convertes every 16 bits/sample/'data chunk')
def convert(src):
	supported_extensions = "wav, mp4, mp3, ogg, pcm"
	#set converted file to wav
	to_format='wav'
	from_format= "mp3"

	#exit if there is more than one or no extension
	if len(src) !=2:
		return "Error, file name must only have one extension"

	# get filename and extension
	filename, from_format=src.split('.')

	#check if file type is convertable 
	#needs extra function to return is all are 'err'
	n=supported_extensions.split(', ')
	i=1
	for str in n:
		if from_format != str:

			if i == len(n):
				return "Error, file extension unsupported"
			
			i+=1
			pass

		if from_format == str:
			#print("supported")
			continue

	#exit if input is already WAV
	if from_format == 'wav':
		return end

	#pydub conversion <to_format>
	raw_audio = AudioSegment.from_file(src, format=from_format)
	raw_audio.export("C:\\Users\\74lch\\Desktop\\programs\\M1.wav", format=to_format)


start = timer()
convert("C:\\Users\\74lch\\Desktop\\programs\\M1.mp4")
end = timer()
print ("required run time is " + str(end - start))