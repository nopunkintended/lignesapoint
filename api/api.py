import hug

from hartml import art_generate


@hug.get('/', output=hug.output_format.html)
def art():
    return art_generate()


@hug.cli()
def mgmt():
    pass
