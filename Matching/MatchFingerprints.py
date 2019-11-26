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
from collections import defaultdict
from FingerprintManager import FingerprintManager


def match_fingerprints(fingerprint_file, audio_fingerprints, audio_fingerprints_info):
    """

    :param self:
    :param fingerprint_file:
    :param audio_fingerprints:
    :param audio_fingerprints_info:
    :return:
    """
    matches_in_bins = defaultdict(list)
    query_seq = 0
    for query in audio_fingerprints:
        matches = FingerprintManager.query_fingerprint(lsh=fingerprint_file, audio_fingerprint=query)
        for i in matches:
            fingerprint_info = i.split("_")
            # keep in mind the difference between hash_info and hashes_info
            matches_in_bins[fingerprint_info[0]].append(int(fingerprint_info[2]) - audio_fingerprints_info[query_seq])
        query_seq += 1
    return matches_in_bins
