from dependency_injector import containers, providers
from sklearn.cluster import Birch, BisectingKMeans, KMeans  # type: ignore

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
        kmeans=providers.Factory(KMeans, config.clustering.model_kwargs),
        birch=providers.Factory(Birch, config.clustering.model_kwargs),
        bisecting_kmeans=providers.Factory(
            BisectingKMeans, **config.clustering.model_kwargs
        ),
    )

    writer = providers.Selector(
        config.writer.format,
        json=providers.Factory(JSONWriter, path=config.writer.path),
        numpy=providers.Factory(NumpyWriter, path=config.writer.path),
    )
