#  Copyright 2022 Pavel Suprunov
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from fastapi import FastAPI
from loguru import logger

from app.core.settings.app import AppSettings
from app.manager.connection_manager import ConnectionManager


def create_connection_manager(app: FastAPI, settings: AppSettings):
    logger.info("Create connection manager")

    manager = ConnectionManager()

    app.state.manager = manager

    logger.info("Connection manager created")
