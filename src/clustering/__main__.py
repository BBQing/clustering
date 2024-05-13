from dependency_injector.wiring import Provide, inject

from clustering.cli import parser
from clustering.config import parse_config
from clustering.containers import Container
from clustering.readers import Reader
from clustering.writers import Writer


@inject
def main(
    reader: Reader = Provide[Container.reader],
    model=Provide[Container.model],
    writer: Writer = Provide[Container.writer],
    config=Provide[Container.config],
):

    model_kwargs = config["clustering"]["model_kwargs"]
    data = reader.read()
    model.set_params(**model_kwargs)
    print(model)
    writer.write("haha")


if __name__ == "__main__":
    args = parser.parse_args()

    container = Container()

    container.config.from_dict(parse_config(args.config))
    container.wire(modules=[__name__])

    main()
