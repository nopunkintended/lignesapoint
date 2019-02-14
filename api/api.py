import hug


@hug.cli()
@hug.local()
@hug.get()
def ping():
	return 'pong'
