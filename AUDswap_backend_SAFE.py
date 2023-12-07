from timeit import default_timer as timer
from pydub import AudioSegment



def convert(src, dst, to_format):


	#list of allowed extensions
	supported_extensions = "wav, mp4, mp3, ogg, pcm"

	#exit if there is more than one or no extension
	if len(src.spit(".")) !=2:
		return "Error, file name must only have one extension"


	# get filename and extension
	filename, from_format=src.split('.')



	#check if file type is convertable
	
	
	n=supported_extensions.split(', ')
	i=1

	#check if all extensions are supported (compares through extension list)
	for str in n:

		#if from_format is not the same as selected extension
		if from_format != str:


			#increment i (counter)
			i+=1

			#check if all extensions have been searched through w/ counter
			if i == len(n):


				#error mesage if file is unsupported and terminates function
				return "Error, file extension unsupported"

			#run loop again if the counter has not reached the end of the supported extensions
			pass


		if from_format == str:
			#if file extension is a match, exit loop and continue the program
			continue


	#pydub conversion <to_format>
	raw_audio = AudioSegment.from_file(src, format=from_format)

	#pydub export to <dst>
	raw_audio.export(dst, format=to_format)



src = "transcript.mp3"
dst = "test.wav"
start = timer()
convert(src, dst, 'wav')
end = timer()
print ("required run time is " + str(end - start))
