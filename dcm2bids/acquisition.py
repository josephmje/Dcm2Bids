# -*- coding: utf-8 -*-


import os


class Acquisition(object):
    """
    """

    def __init__(self, description, dicomsDir, participant, session):
        self._description = description
        self._dicomsDir = dicomsDir
        self._participant = participant
        self._session = session


    @property
    def dataType(self):
        return self._description['data_type']


    @property
    def suffix(self):
        result = ''
        if not self._session.isSingle():
            result += '{}_'.format(self._session.name)
        if self._description.has_key('custom_labels'):
            for key, value in self._description['custom_labels'].iteritems():
                result += '{}-{}_'.format(key, value)
        result += self._description['suffix']
        return result


    @property
    def outputDir(self):
        return os.path.join(self._session.directory, self.dataType)


    @property
    def filename(self):
        return '{}_{}'.format(self._participant.name, self.suffix)


    @property
    def dicomsDir(self):
        return os.path.join(self._dicomsDir, self._description['directory'])