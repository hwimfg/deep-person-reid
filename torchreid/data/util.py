try:
    from scipy.io import loadmat
except ImportError:
    # Hack implementation to work around not having scipy.
    def loadmat(file_name, mdict=None, appendmat=True, **kwargs):
        return {}
