# Copyright (c) 2019 Cloudbase Solutions Srl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Command-line interface sub-commands related to diagnostics.
"""
from cliff import lister

from coriolisclient.cli import formatter


class DiagnosticsFormatter(formatter.EntityFormatter):

    columns = ("Application", "Hostname", "IP addresses", "Packages",
               "OS info")

    def _get_sorted_list(self, obj_list):
        return sorted(obj_list, key=lambda o: o.application)

    def _get_formatted_data(self, obj):
        data = (obj.application, obj.hostname, obj.ip_addresses, obj.packages,
                obj.os_info)
        return data


class GetCoriolisDiagnostics(lister.Lister):
    """Get diagnostics"""

    def get_parser(self, prog_name):
        parser = super(GetCoriolisDiagnostics, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        diag_details = self.app.client_manager.coriolis.diagnostics.get()
        return DiagnosticsFormatter().list_objects(diag_details)
