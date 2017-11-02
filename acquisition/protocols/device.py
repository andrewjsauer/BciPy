from __future__ import absolute_import, division, print_function


class Device(object):
    """Base class for device-specific behavior.

    Parameters
    ----------
        connection_params : dict
            Parameters needed to connect with the given device
        fs : int
            Sample frequency in Hz.
        channels : list
            List of channel names.
    """

    def __init__(self, connection_params, fs, channels):
        self._connection_params = connection_params
        self.fs = fs
        self.channels = channels

    @property
    def name(self):
        raise NotImplementedError('Subclass must define a name property')

    def connect(self):
        """Connect to the data source."""
        pass

    def acquisition_init(self):
        """Initialization step. Depending on the protocol, this may involve
        reading header information and setting the appropriate instance
        properties or writing to the server to set params (ex. sampling freq).
        """
        pass

    def read_data(self):
        """Read the next sensor data record from the data source.

        Returns
        -------
            list with a float for each channel.
        """
        raise NotImplementedError(
            'Subclass must define the read_sensor_data method')

    def disconnect(self):
        pass