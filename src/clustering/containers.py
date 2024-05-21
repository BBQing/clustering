from dependency_injector import containers, providers
from sklearn.cluster import Birch, BisectingKMeans, KMeans

from clustering.readers import JSONReader, NumpyReader
from clustering.writers import JSONWriter, NumpyWriter


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    reader = providers.Selector(
        config.reader.format,
        json=providers.Factory(JSONReader, path=config.reader.path),
        numpy=providers.Factory(NumpyReader, path=config.reader.path),
    )

    model = providers.Selector(
        config.clustering.model,
        kmeans=providers.Factory(KMeans),
        birch=providers.Factory(Birch),
        bisecting_kmeans=providers.Factory(BisectingKMeans),
    )

    writer = providers.Selector(
        config.writer.format,
        json=providers.Factory(JSONWriter, path=config.writer.path),
        numpy=providers.Factory(NumpyWriter, path=config.writer.path),
    )
