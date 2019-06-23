import logging


class Task:

    def run(self, action, config):
        logging.info('Running action "{}"...'.format(action))
        getattr(self, '_process_' + action)(config)
        logging.info('Well done.')

    def _process_training(self, config):
        pass

    def _process_application(self, config):
        pass
