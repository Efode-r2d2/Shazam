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
from Utilities import DirManager
from Core import Spectrogram
from Core import PeakExtractor
from Core import FingerprintGenerator
from Matching import MatchFingerprints
from FingerprintManager import FingerprintManager
from Matching import VerifyMatches

# source dir for modified audios
src_dir = "../../../Test_Data/Modified_Audios/White_Noise"
# fingerprints_file_path
fingerprints_file_path = "../../../Hashes/Shazam/fingerprints_file"
# fingerprints file
fingerprints_file = FingerprintManager.load_fingerprints_file(fingerprints_file_path=fingerprints_file_path)
# spectrogram, peak extractor and fingerprint generator objects
stft = Spectrogram(hop_length=32)
peak_extractor = PeakExtractor()
fingerprint_generator = FingerprintGenerator()
# reading all .wav files under given source dir
wav_files = DirManager.find_wav_files(src_dir=src_dir)
# reading audio data re-sampled at 7KHz of a given audio portion specified by offset and duration parameters
audio_data = AudioManager.load_audio(audio_path=wav_files[1])
# computing spectrogram
spectrogram = stft.compute_stft_magnitude_in_db(audio_data=audio_data)
# extract spectral peaks
spectral_peaks = peak_extractor.extract_spectral_peaks_2(spectrogram=spectrogram)
# generate fingerprints
audio_fingerprints = list()
audio_fingerprints_info = list()
fingerprint_generator.generate_fingerprints(spectral_peaks=spectral_peaks[0],
                                            audio_fingerprints=audio_fingerprints,
                                            audio_fingerprints_info=audio_fingerprints_info)
matches_in_bins = MatchFingerprints.match_fingerprints(fingerprint_file=fingerprints_file,
                                                       audio_fingerprints=audio_fingerprints,
                                                       audio_fingerprints_info=audio_fingerprints_info)
match = VerifyMatches.verify_wang_matches(matches_in_bins=matches_in_bins)
print(match)
