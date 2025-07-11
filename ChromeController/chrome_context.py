
import logging
import contextlib

from .manager import ChromeRemoteDebugInterface

@contextlib.contextmanager
def ChromeContext(*args, **kwargs):
	'''
	Context manager for conveniently handling the lifetime of the underlying chromium instance.

	In general, this should be the preferred way to use an instance of `ChromeRemoteDebugInterface`.

	All parameters are forwarded through to the underlying ChromeRemoteDebugInterface() constructor.
	'''
	log = logging.getLogger("Main.ChromeController.ChromeContext")
	chrome_created = False
	try:
		chrome_instance = ChromeRemoteDebugInterface(*args, **kwargs)
		chrome_created = True
		log.info("Entering chrome context")
		yield chrome_instance
	except Exception as e:
		log.exception("Exception in chrome context!")
		raise e

	finally:
		log.info("Exiting chrome context")
		if chrome_created:
			chrome_instance.close()

