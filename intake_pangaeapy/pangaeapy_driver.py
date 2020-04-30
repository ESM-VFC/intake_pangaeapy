import intake
import pangaeapy


class PangaeapySource(intake.source.base.DataSource):
    container = "dataframe"
    name = "pangaeapy"
    version = "0.1.0"
    partition_access = False

    def __init__(self, pangaea_doi, metadata=None):
        self.pangaea_doi = pangaea_doi
        super(PangaeapySource, self).__init__(metadata=metadata)

    def _maybe_load_data(self):
        """Load data only once."""
        if not hasattr(self, "pandataset"):
            self.pandataset = pangaeapy.PanDataSet(self.pangaea_doi)

    def _get_schema(self):
        return intake.source.base.Schema(
            datashape=None,
            dtype=None,
            shape=(None,),
            npartitions=1,
            extra_metadata=dict(),
        )

    def _get_partition(self, i):
        raise NotImplementedError("Partitioned read is not implemented")

    def read(self):
        self._maybe_load_data()
        self._load_metadata()
        return self.pandataset.data

    def _close(self):
        # close any files, sockets, etc
        pass
