# Copyright 2008 Paul Swartz
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
import os
import shutil


def class_template(name):
    name = name.replace(' ', '')
    return '%s_app' % name.lower(), '%sActivity' % name


def activity_info_template(name):
    bundle_id = 'org.laptop.%s' % name.replace(' ', '')
    return """[Activity]
name = %s
bundle_id = %s
icon = activity-default
exec = sugar-activity %s.%s -s
activity_version = 1
show_launcher = yes
""" % ((name, bundle_id) + class_template(name))


def base_file_template(name):
    __filen, classn = class_template(name)
    return """import gtk
from sugar.activity import activity
from sugar.activity.widgets import ActivityToolbarButton
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import StopButton

class %s(activity.Activity):
    '''
    The base class for the %s activity.
    '''

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        toolbarbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbarbox.toolbar.insert(activity_button, 0)

        separator = gtk.SeparatorToolItem()
        separator.set_draw(False)
        separator.set_expand(True)
        toolbarbox.toolbar.insert(separator, -1)

        toolbarbox.toolbar.insert(StopButton(self), -1)
        toolbarbox.show_all()
        self.set_toolbar_box(toolbarbox)


    def write_file(self, file_path):
        '''
        Implement this method to save your activity's state.
        '''
        raise NotImplementedError

    def read_file(self, file_path):
        '''
        Implement this method to resume state saved in write_file().
        '''
        raise NotImplementedError
""" % (classn, name)


def new_activity(name, base_path):
    path = os.path.expanduser(os.path.join(base_path,
                        '%s.activity' % name.replace(' ', '')))
    os.makedirs(path)
    activityPath = os.path.join(path, 'activity')
    os.mkdir(activityPath)
    filen, __classn = class_template(name)
    _file = file(os.path.join(path, filen + '.py'), 'w')
    _file.write(base_file_template(name))
    _file.close()

    _file = file(os.path.join(activityPath, 'activity.info'), 'w')
    _file.write(activity_info_template(name))
    _file.close()

    _file = file(os.path.join(path, 'NEWS'), 'w')
    _file.close()

    icon_path = os.path.join(os.path.dirname(__file__), 'activity',
        'activity-default.svg')
    shutil.copy(icon_path, activityPath)

    return path
