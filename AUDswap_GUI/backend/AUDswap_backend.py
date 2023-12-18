from pydub import AudioSegment

def convert(src, dst, to_format):

	#supported_extensions = "mp3, aac, pcm, ogg, flac, wav, aiff, dsd, pcm, avi, flv, mkv, mov, webm, avchd, mp4, wmv, mpeg4"

	# get filename and extension
	filename, from_format=src.split('.')

	#pydub conversion <to_format>
	raw_audio = AudioSegment.from_file(src, format=from_format)

	#pydub export to <dst>
	raw_audio.export(dst, format=to_format)
