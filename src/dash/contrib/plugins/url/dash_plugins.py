__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseURLPlugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory
from dash.contrib.plugins.url.forms import URLForm, BookmarkForm

# ********************************************************************************
# ********************************* URL plugin ***********************************
# ********************************************************************************

class BaseURLPlugin(BaseDashboardPlugin):
    """
    Base URL plugin.
    """
    name = _("URL")
    group = _("URLs")
    form = URLForm

    @property
    def html_class(self):
        """
        If plugin has an image, we add a class `iconic` to it.
        """
        html_class = super(BaseURLPlugin, self).html_class
        if self.data.image:
            html_class += ' iconic-url'
        return html_class

# ********************************************************************************
# ********** Generating and registering the URL plugins using factory ************
# ********************************************************************************

sizes = (
    (1, 1),
    (2, 2)
)

plugin_factory(BaseURLPlugin, 'url', sizes)


# ********************************************************************************
# ********************************* Bookmark plugin ******************************
# ********************************************************************************

class BaseBookmarkPlugin(BaseDashboardPlugin):
    """
    Base URL plugin.
    """
    name = _("Bookmark")
    group = _("URLs")
    form = BookmarkForm

    @property
    def html_class(self):
        """
        If plugin has an image, we add a class `iconic` to it.
        """
        html_class = super(BaseBookmarkPlugin, self).html_class
        if self.data.image:
            html_class += ' iconic-url'
        return html_class

    def update_plugin_data(self, dashboard_entry):
        """
        Updates the plugin entry data.
        """
        # TODO

# ********************************************************************************
# ******* Generating and registering the Bookmark plugins using factory **********
# ********************************************************************************

sizes = (
    (1, 1),
    #(2, 2)
)

plugin_factory(BaseBookmarkPlugin, 'bookmark', sizes)
