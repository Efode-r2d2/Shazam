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
from Utilities import AudioManager
from Utilities import GraphManager
from Utilities import DirManager
from Core import Spectrogram
from Core import PeakExtractor
from Core import FingerprintGenerator
from FingerprintManager import FingerprintManager

# source directory
src_dir = "../../../Test_Data/Reference_Audios"
# path for fingerprints file
fingerprints_file_path = "../../../Hashes/Shazam/fingerprints_file"
# searching for all .mp3 files under a specified source dir
mp3_files = DirManager.find_mp3_files(src_dir=src_dir)
# spectrogram, peak extractor and fingerprint generator objects
stft = Spectrogram(hop_length=32)
peak_extractor = PeakExtractor()
fingerprint_generator = FingerprintGenerator()
fingerprint_file = FingerprintManager.load_fingerprints_file(fingerprints_file_path=fingerprints_file_path)
# fingerprinting five audios
for i in mp3_files:
    audio_fingerprints = list()
    audio_fingerprints_info = list()
    audio_id = i.split("/")[5].split(".")[0]
    audio_data = AudioManager.load_audio(audio_path=i)
    spectrogram = stft.compute_stft_magnitude_in_db(audio_data=audio_data)
    spectral_peaks = peak_extractor.extract_spectral_peaks_2(spectrogram=spectrogram)
    fingerprint_generator.generate_fingerprints(spectral_peaks=spectral_peaks[0],
                                                audio_fingerprints=audio_fingerprints,
                                                audio_fingerprints_info=audio_fingerprints_info)
    FingerprintManager.insert_fingerprints(fingerprint_file=fingerprint_file,
                                           audio_id=audio_id,
                                           audio_fingerprints=audio_fingerprints,
                                           audio_fingerprints_info=audio_fingerprints_info)
    print(audio_id, " Fingerprinted!")
FingerprintManager.dump_fingerprints_file(fingerprints_file=fingerprint_file,
                                          fingerprint_file_path=fingerprints_file_path)
