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
from datasketch import MinHash


class FingerprintGenerator(object):
    def __init__(self, min_t_delta=0, max_t_delta=100, fan_out=5):
        """

        :param min_t_delta:
        :param max_t_delta:
        :param fan_out:
        """
        # min_t_delta, max_t_delta and min_t_delta defines the size of the target zone
        self.min_t_delta = min_t_delta
        self.max_t_delta = max_t_delta
        self.fan_out = fan_out

    def generate_fingerprints(self, spectral_peaks, audio_fingerprints, audio_fingerprints_info):
        """

        :param spectral_peaks:
        :param audio_fingerprints:
        :param audio_fingerprints_info:
        """
        for i in range(len(spectral_peaks)):
            for j in range(1, self.fan_out):
                if (i + j) < len(spectral_peaks):
                    f1 = spectral_peaks[i][1]
                    f2 = spectral_peaks[i + j][1]
                    t1 = spectral_peaks[i][0]
                    t2 = spectral_peaks[i + j][0]
                    t_delta = t2 - t1
                    if self.min_t_delta <= t_delta <= self.max_t_delta:
                        peak_info = {str(f1), str(f2), str(t_delta)}
                        peak_digest = MinHash(num_perm=128)
                        for d in peak_info:
                            peak_digest.update(d.encode('utf8'))
                        audio_fingerprints.append(peak_digest)
                        audio_fingerprints_info.append(t1)
