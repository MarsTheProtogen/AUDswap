from pydub import AudioSegment

#for aplications that are delay sensitive, the conversion appears to have a base rin time of ~.15s + 0.005405405405*<seconds of audio>

def convert(src, dst, to_format):


	#list of allowed extensions
<<<<<<< HEAD
	supported_extensions = "mp3, aac, pcm, ogg, flac, wav, aiff, dsd, pcm, avi, flv, mkv, mov, webm, avchd, mp4, wmv, mpeg4"
=======
	supported_extensions = "mp3, aac, ogg, flac, wav, aiff, dsd, pcm, avi, flv, mkv, mov, webm, avchd, mp4, wmv, mpeg4"
>>>>>>> 2cf8f1f1443ece57b2abc0335039c94e8dbd7ec5


	#exit if there is more than one or no extension
	if len(src.split(".")) !=2:
		return "Error, file name must only have one extension"


	# get filename and extension
	filename, from_format=src.split('.')


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
			break


	#pydub conversion <to_format>
	raw_audio = AudioSegment.from_file(src, format=from_format)

	#pydub export to <dst>
	raw_audio.export(dst, format=to_format)
