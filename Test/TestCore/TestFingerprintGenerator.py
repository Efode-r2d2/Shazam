"""
    < This program reproduced a work published in https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf>
    Copyright (C) <2019>  <Efriem Desalew Gebie>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from Utilities import DirManager
from Utilities import AudioManager
from Utilities import GraphManager
from Core import Spectrogram
from Core import PeakExtractor
from Core import FingerprintGenerator

# source directory
src_dir = "../../../Test_Data/Reference_Audios"
# spectrogram and peak extractor objects
stft = Spectrogram(hop_length=32)
peak_extractor = PeakExtractor()
fingerprint_generator = FingerprintGenerator()
# searching for all .mp3 file under specified source dir
mp3_files = DirManager.find_mp3_files(src_dir=src_dir)
# reading audio data re-sampled at 7KHz for
# audio portion defined by offset and duration parameters
audio_data = AudioManager.load_audio(audio_path=mp3_files[0], offset=10.0, duration=3.0)
# computing spectrogram
spectrogram = stft.compute_stft_magnitude_in_db(audio_data=audio_data)
# extract spectral peaks
spectral_peaks = peak_extractor.extract_spectral_peaks_1(spectrogram=spectrogram)
# generate fingerprints
audio_fingerprints = list()
audio_fingerprints_info = list()
fingerprint_generator.generate_fingerprints(spectral_peaks=spectral_peaks[0],
                                            audio_fingerprints=audio_fingerprints,
                                            audio_fingerprints_info=audio_fingerprints_info)
# audio fingerprints
print("Audio Fingerprints", len(audio_fingerprints))
print(audio_fingerprints)
# audio fingerprints info
print("Audio Fingerprints Raw Data", len(audio_fingerprints))
print(audio_fingerprints_info)
