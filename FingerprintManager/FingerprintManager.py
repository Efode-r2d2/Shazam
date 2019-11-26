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
from datasketch import MinHashLSH
import pickle


def create_fingerprint_file(fingerprint_file_path, threshold=0.75, num_perm=128):
    """

    :param fingerprint_file_path:
    :param threshold:
    :param num_perm:
    """
    lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
    pickle.dump(lsh, open(fingerprint_file_path, "wb"))
    print(fingerprint_file_path, " Created!")


def insert_fingerprint(fingerprint_file, audio_id, audio_fingerprint):
    """

    :param fingerprint_file:
    :param audio_id:
    :param audio_fingerprint:
    """
    fingerprint_file.insert(audio_id, audio_fingerprint, check_duplication=False)


def query_fingerprint(fingerprint_file, audio_fingerprint):
    """

    :param fingerprint_file:
    :param audio_fingerprint:
    :return:
    """
    return fingerprint_file.query(audio_fingerprint)


def insert_fingerprints(fingerprint_file, audio_id, audio_fingerprints, audio_fingerprints_info):
    """

    :param fingerprint_file:
    :param audio_id:
    :param audio_fingerprints:
    :param audio_fingerprints_info:
    """
    fingerprint_seq = 0
    for i in audio_fingerprints:
        fingerprint_id = audio_id + "_" + str(fingerprint_seq) + "_" + str(audio_fingerprints_info[fingerprint_seq])
        insert_fingerprint(fingerprint_file, fingerprint_id, i)
        fingerprint_seq += 1
