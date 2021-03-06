# Copyright (c) 2016 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import Column
from sqlalchemy import MetaData, String, Table


def upgrade(migrate_engine):
    """Add cluster name to image cache entries."""
    meta = MetaData()
    meta.bind = migrate_engine

    image_cache = Table('image_volume_cache_entries', meta, autoload=True)
    cluster_name = Column('cluster_name', String(255), nullable=True)
    if not hasattr(image_cache.c, 'cluster_name'):
        image_cache.create_column(cluster_name)
