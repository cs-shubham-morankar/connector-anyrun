""" Copyright start
  Copyright (C) 2008 - 2021 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import Connector, ConnectorError, get_logger

from .operations import operations, _check_health

logger = get_logger('anyrun')


class anyrun(Connector):
    def execute(self, config, operation_name, params, **kwargs):
        try:
            logger.info("Action name: {}".format(operation_name))
            op = operations.get(operation_name)
            result = op(config, params)
            return result
        except Exception as e:
            logger.exception("An exception occurred {}".format(e))
            raise ConnectorError(e)

    def check_health(self, config):
        try:
            return _check_health(config)
        except Exception as e:
            logger.error('{}'.format(e))
            raise ConnectorError(e)
